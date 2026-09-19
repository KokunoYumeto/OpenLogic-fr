"""Read-only validation of a converted EPUB; semantic acceptance remains separate."""
from pathlib import Path, PurePosixPath
import hashlib,json,zipfile,sys,collections,posixpath,re
from urllib.parse import urlsplit,unquote
from lxml import etree
E=Path(__file__).resolve().parent
epub=Path(sys.argv[1])
sha=lambda b:hashlib.sha256(b).hexdigest()
errors=[];documents={};ids={};maths=0;figures=0;links=0;external=[];missing_math=[];spine=[]
with zipfile.ZipFile(epub) as z:
 names=set(z.namelist());entries=z.infolist()
 assert entries[0].filename=="mimetype" and entries[0].compress_type==zipfile.ZIP_STORED
 assert z.read("mimetype")==b"application/epub+zip"
 parser=etree.XMLParser(resolve_entities=False,no_network=True,huge_tree=True)
 container=etree.fromstring(z.read("META-INF/container.xml"),parser)
 package_path=container.xpath("//*[local-name()='rootfile']/@full-path")[0]
 package=etree.fromstring(z.read(package_path),parser)
 base=posixpath.dirname(package_path)
 language=package.xpath("//*[local-name()='language']/text()")
 if language!=["fr"]:errors.append(["language",language])
 if package.get("version")!="3.0":errors.append(["version",package.get("version")])
 items={x.get("id"):x for x in package.xpath("//*[local-name()='manifest']/*")}
 for item in items.values():
  p=posixpath.normpath(posixpath.join(base,unquote(item.get("href"))))
  if p not in names:errors.append(["manifest_missing",p])
  if item.get("media-type")=="application/xhtml+xml" and p in names:
   try:root=etree.fromstring(z.read(p),parser)
   except Exception as ex:errors.append(["xhtml",p,str(ex)]);continue
   documents[p]=root
   arr=root.xpath("//@id");ids[p]=set(arr)
   if len(arr)!=len(set(arr)):errors.append(["duplicate_ids",p])
   if root.xpath("//*[local-name()='script']"):errors.append(["script",p])
   if root.get("{http://www.w3.org/XML/1998/namespace}lang") not in ["fr",None]:errors.append(["document_language",p])
   mm=root.xpath("//*[local-name()='math']")
   maths+=len(mm)
   if mm and "mathml" not in item.get("properties","").split():errors.append(["mathml_manifest_property",p])
   for n,m in enumerate(mm):
    if not list(m):missing_math.append([p,n,"empty"])
    if etree.QName(m).namespace!="http://www.w3.org/1998/Math/MathML":errors.append(["mathml_namespace",p,n])
    if any(etree.QName(e).namespace!="http://www.w3.org/1998/Math/MathML" for e in m.iter() if isinstance(e.tag,str) and etree.QName(e).localname!="img"):errors.append(["mathml_child_namespace",p,n])
   figures+=len(root.xpath("//*[local-name()='img' or local-name()='svg']"))
   if not "".join(root.itertext()).strip():errors.append(["empty_document",p])
 for itemref in package.xpath("//*[local-name()='spine']/*"):
  item=items.get(itemref.get("idref"))
  if item is None:errors.append(["spine_missing",itemref.get("idref")])
  else:spine.append(posixpath.normpath(posixpath.join(base,item.get("href"))))
 for p,root in documents.items():
  for attr in root.xpath("//@href | //@src"):
   u=urlsplit(attr)
   if u.scheme or u.netloc:external.append(attr);continue
   dest=posixpath.normpath(posixpath.join(posixpath.dirname(p),unquote(u.path))) if u.path else p
   links+=1
   if dest not in names:errors.append(["local_link_missing",p,attr])
   elif u.fragment and dest in ids and unquote(u.fragment) not in ids[dest]:errors.append(["fragment_missing",p,attr])
 if maths==0:errors.append(["no_native_mathml"])
 nav=[x for x in items.values() if "nav" in x.get("properties","").split()]
 if len(nav)!=1:errors.append(["nav_count",len(nav)])
 report=dict(epub=epub.name,bytes=epub.stat().st_size,sha256=sha(epub.read_bytes()),documents=len(documents),spine=spine,native_mathml_roots=maths,figures=figures,internal_links=links,external_links=sorted(set(external)),missing_math=missing_math,errors=errors,status="PASS_STRUCTURE_ONLY" if not errors and not missing_math else "FAIL",semantic_source_coverage_inferred=False,source_scope_units=64,total_edition_units=722,full_edition_complete=False)
 print(json.dumps(report,ensure_ascii=True,indent=2))
sys.exit(bool(errors or missing_math))

