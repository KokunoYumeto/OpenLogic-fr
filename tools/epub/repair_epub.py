"""Repair evidenced TeX4ht export defects; preserve body text and mathematical trees."""
from pathlib import Path
from lxml import etree
import collections,copy,hashlib,json,re,zipfile
E=Path(__file__).resolve().parent
SOURCE=E/'conversion/source/locale/fr/reader.epub'
OUTPUT=E/'openlogic-fr-ensembles-fonctions-construction-des-nombres.epub'
HTML='http://www.w3.org/1999/xhtml'
MATH='http://www.w3.org/1998/Math/MathML'
sha=lambda b:hashlib.sha256(b).hexdigest()
local=lambda e:etree.QName(e).localname
def bodytext(r):
 return ''.join(r.find('{'+HTML+'}body').itertext())
def mathshape(e):
 return [local(e),sorted(e.attrib.items()),e.text,e.tail,[mathshape(c) for c in e if isinstance(c.tag,str)]]
def prose(r):
 c=copy.deepcopy(r)
 for m in c.xpath('//*[local-name()="math"]'):
  tail=m.tail;m.clear();m.tail=tail
 return bodytext(c)
def clone_math(e,root=False):
 if not isinstance(e.tag,str):return copy.deepcopy(e)
 namespace=HTML if local(e)=='img' else MATH
 n=etree.Element('{'+namespace+'}'+local(e),nsmap={None:namespace} if root or namespace==HTML else None)
 n.attrib.update(e.attrib);n.text=e.text;n.tail=e.tail
 for c in e:n.append(clone_math(c))
 return n
ALT={
 'reader27x.svg':'Deux carrés de côté n, décalés dans un carré de côté m, se recouvrent en un carré orange. Deux carrés blancs occupent les coins opposés. Le dessin illustre la réduction géométrique utilisée pour démontrer l’irrationalité de la racine carrée de 2.',
 'reader28x.svg':'L’hôtel de Hilbert : pour chaque entier k supérieur ou égal à 1, une flèche envoie le client de la chambre k vers la chambre k + 1. La chambre 1, entourée, devient libre.',
 'reader2x.svg':'Réunion de deux ensembles A et B : toute la région appartenant à A ou à B, y compris leur intersection, est colorée.',
 'reader5x.svg':'Intersection de deux ensembles A et B : seule leur région commune est colorée.',
 'reader8x.svg':'Différence A privé de B : seule la région appartenant à A et extérieure à B est colorée.',
 'reader9x.svg':'Graphe orienté de sommets 1, 2, 3 et 4. Arêtes : 1 vers 1, 1 vers 2, 1 vers 3 et 2 vers 3. Le sommet 4 est isolé.',
 'reader10x.svg':'Graphe orienté de sommets 1, 2 et 3, avec les mêmes arêtes : 1 vers 1, 1 vers 2, 1 vers 3 et 2 vers 3. Il ne contient pas le sommet isolé 4.',
 'reader11x.svg':'Arbre de racine r, dessinée en bas. Les enfants de r sont a et b ; les enfants de a sont c, d et e.',
 'reader14x.svg':'Fonction entre deux ensembles : de chaque point du domaine part une unique flèche vers sa valeur dans l’ensemble d’arrivée.',
 'reader17x.svg':'Fonction surjective : chaque point de l’ensemble d’arrivée est atteint par au moins une flèche.',
 'reader20x.svg':'Fonction injective : deux points distincts du domaine ont des images distinctes.',
 'reader23x.svg':'Fonction bijective : chaque point de l’ensemble d’arrivée est atteint par exactement une flèche.',
 'reader26x.svg':'Composition : x dans A est envoyé par f sur y dans B, puis par g sur z dans C. La flèche composée de A vers C représente g après f.'
}
report={'input_sha256':sha(SOURCE.read_bytes()),'repairs':[],'documents':[]}
with zipfile.ZipFile(SOURCE) as z:
 data={n:z.read(n) for n in z.namelist() if not n.endswith('/')}
for name,raw in list(data.items()):
 if not name.endswith('.xhtml'):continue
 r=etree.fromstring(raw)
 before=bodytext(r)
 before_prose=prose(r)
 # A tab in a deferred exercise was serialized literally by TeX as ^^I.
 tab_count=before_prose.count("^^I")
 if tab_count:
  assert tab_count=={"OEBPS/readerch1.xhtml":7,"OEBPS/readerch5.xhtml":1}.get(name)
  for node in r.iter():
   if node.text:node.text=node.text.replace("^^I"," ")
   if node.tail:node.tail=node.tail.replace("^^I"," ")
  report["repairs"].append({"document":name,"serialized_tab_replaced_by_space":tab_count})
  before_prose=before_prose.replace("^^I"," ")
 mm=r.xpath('//*[local-name()="math"]')
 oldmath=[mathshape(m) for m in mm]
 changed=[]
 for index,m in enumerate(mm):
  # A fresh root with its own default namespace survives epub.js HTML insertion.
  fresh=clone_math(m,True);m.getparent().replace(m,fresh);mm[index]=fresh
  m=fresh
  for mi in m.xpath('.//*[@mathvariant="double-struck"]//*[local-name()="mi"]'):
   mapping={'N':'ℕ','Z':'ℤ','Q':'ℚ','R':'ℝ','𝔹':'𝔹'}
   assert mi.text in mapping,mi.text
   mi.text=mapping[mi.text]
   changed.append({'math_index':index,'repair':'explicit Unicode double-struck character from source mathbb style'})
  for table in m.xpath('.//*[local-name()="mtable" and @rowlines=""]'):
   del table.attrib['rowlines']
  for sup in m.xpath('.//*[local-name()="sup" and @class="nicefrac"]'):
   slash=sup.getnext();sub=slash.getnext()
   assert local(slash)=='mo' and slash.text=='/' and local(sub)=='sub' and sub.get('class')=='nicefrac'
   old=etree.tostring(sup.getparent(),encoding='unicode')
   frac=etree.Element('{'+MATH+'}mfrac',bevelled='true')
   num=etree.SubElement(frac,'{'+MATH+'}mrow');den=etree.SubElement(frac,'{'+MATH+'}mrow')
   num.text=sup.text;den.text=sub.text
   for c in list(sup):num.append(c)
   for c in list(sub):den.append(c)
   frac.tail=sub.tail
   parent=sup.getparent();parent.replace(sup,frac);parent.remove(slash);parent.remove(sub)
   changed.append({'math_index':index,'repair':'nicefrac numerator/slash/denominator -> bevelled mfrac','before':old})
  for mo in m.xpath('.//*[local-name()="mo" and ./*[@class="oalign"]]'):
   assert ''.join(mo.itertext()).split()==['↦','→']
   old=etree.tostring(mo,encoding='unicode')
   tail=mo.tail;attrs=dict(mo.attrib);mo.clear();mo.attrib.update(attrs);mo.tail=tail
   mo.text='⇸'
   changed.append({'math_index':index,'repair':'source pto: centred vertical stroke over right arrow -> U+21F8','before':old})
  for sem in m.xpath('.//*[local-name()="semantics" and *[1][local-name()="annotation-xml"]]'):
   ann=sem[0];assert len(sem)==1 and len(ann)==1 and local(ann[0])=='img'
   sem.tag='{'+MATH+'}mtext';img=ann[0];ann.remove(img);sem.remove(ann);sem.append(img)
   changed.append({'math_index':index,'repair':'graph image in mtext HTML integration point instead of empty semantics'})
  if mathshape(m)!=oldmath[index]:
   # Namespace changes are excluded; remaining differences are the explicit
   # rendering repairs above or empty rowlines removal.
   report['repairs'].append({'document':name,'math_index':index,'before_shape':oldmath[index],'after_shape':mathshape(m)})
 report['repairs'].append({'document':name,'math_namespace_roots':len(mm)})
 # TeX4ht emits a valid noteref inside a redundant hyperref footnote link.
 nested=r.xpath('//*[local-name()="a" and .//*[local-name()="a"]]')
 for outer in nested:
  assert outer.get('href','').startswith('#Hfootnote.')
  assert len(outer)==1 and local(outer[0])=='a' and outer[0].get('role')=='doc-noteref'
  outer.tag='{'+HTML+'}span'
  report['repairs'].append({'document':name,'redundant_outer_link':outer.attrib.pop('href')})
 # One delayed footnotetext inherited an earlier footnote ID. Its printed
 # number32 and actual noteref#fn32x4 unambiguously identify the correct target.
 if name.endswith('readerch4.xhtml'):
  a=r.xpath('//*[@id="fn28x4"]')
  assert len(a)==2 and re.match(r'\s*32\.', ''.join(a[1].itertext()))
  a[1].set('id','fn32x4')
  report['repairs'].append({'document':name,'footnote_32_target':'fn28x4 -> fn32x4'})
 # Heading IDs collided between an example/proposition21 and exercise2.
 # No inbound links use these auto-generated duplicate IDs (checked globally).
 counts=collections.Counter(r.xpath('//@id'))
 for key,count in counts.items():
  if count<2:continue
  assert key in {'x121','x221','x421','x511','framed-1'},key
  for other in data.values():
   assert not re.search(rb'href\s*=\s*["\'][^"\']*#'+re.escape(key.encode())+rb'["\']',other),key
  for i,e in enumerate(r.xpath('//*[@id=$key]',key=key),1):
   if i>1:e.set('id',key+'-'+str(i))
  report['repairs'].append({'document':name,'unreferenced_duplicate_id':key,'occurrences':count})
 title=r.find('{'+HTML+'}head/{'+HTML+'}title')
 if title is not None and not (title.text or '').strip():
  title.text='OpenLogic : édition française — Ensembles, fonctions et construction des nombres'
 r.set('{http://www.w3.org/XML/1998/namespace}lang','fr')
 assert before_prose==prose(r),name
 for img in r.xpath('//*[local-name()="img"]'):
  assert img.get('src') in ALT
  img.set('alt',ALT[img.get('src')])
 data[name]=etree.tostring(r,encoding='utf-8',xml_declaration=True,doctype='<!DOCTYPE html>')
 report['documents'].append({'path':name,'prose_sha256_before_and_after':sha(before_prose.encode()),'body_text_before_sha256':sha(before.encode()),'body_text_after_sha256':sha(bodytext(r).encode()),'math_roots':len(mm),'explicit_math_repairs':changed})
# epub.js rewrites image URLs to blob URLs, defeating the generated src-prefix
# dark-mode filter. Give diagrams a stable white canvas in both themes.
data['OEBPS/reader.css']+=b'\n/* Preserve diagram contrast in readers that replace asset URLs. */\nimg { background-color: white; filter: none !important; max-width: 100% !important; height: auto; }\nfigure.figure { margin-left: 0; margin-right: 0; max-width: 100%; }\n'
data['OEBPS/reader.css']+=b'\n/* Wide equations and tables scroll locally on narrow reading screens. */\nmath { max-width: 100%; overflow-x: auto; overflow-y: hidden; }\nmath[display="block"] { display: block; }\ntable.equation-star { display: block; max-width: 100%; overflow-x: auto; }\ntable.equation-star tbody { display: table; width: 100%; }\ndiv.tabular, div.longtable { max-width: 100%; overflow-x: auto; }\n'
data['OEBPS/reader.css']+=b'\n/* Scale the Hilbert diagram inside its narrower quotation. */\nblockquote .center img { width: 100%; object-fit: contain; }\n.center p.indent { text-indent: 0; }\n'
# TeX4ht carried mathml onto a bibliography document without mathematics.
opf=etree.fromstring(data["OEBPS/content.opf"])
for item in opf.xpath('//*[local-name()="manifest"]/*'):
 if item.get("media-type")!="application/xhtml+xml":continue
 document="OEBPS/"+item.get("href")
 has_math=bool(etree.fromstring(data[document]).xpath('//*[local-name()="math"]'))
 properties=item.get("properties","").split()
 if ("mathml" in properties)!=has_math:
  properties=[p for p in properties if p!="mathml"]+(["mathml"] if has_math else [])
  if properties:item.set("properties"," ".join(properties))
  elif "properties" in item.attrib:del item.attrib["properties"]
  report["repairs"].append({"document":document,"mathml_manifest_property":has_math})
data["OEBPS/content.opf"]=etree.tostring(opf,encoding="utf-8",xml_declaration=True)
with zipfile.ZipFile(OUTPUT,'w') as z:
 for name in ['mimetype']+sorted(set(data)-{'mimetype'}):
  i=zipfile.ZipInfo(name,(2026,9,6,0,0,0))
  i.compress_type=zipfile.ZIP_STORED if name=='mimetype' else zipfile.ZIP_DEFLATED
  i.create_system=3;i.external_attr=0o100644<<16
  z.writestr(i,data[name],compresslevel=9)
report.update(output=OUTPUT.name,bytes=OUTPUT.stat().st_size,sha256=sha(OUTPUT.read_bytes()),status='STRUCTURALLY_REPAIRED_REQUIRES_QA')
(E/'STRUCTURAL_REPAIR_RECEIPT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ('repairs','documents')}))
