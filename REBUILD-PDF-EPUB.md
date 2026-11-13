# Reconstruire l’édition française d’OpenLogic

Le fichier `fr/reader-full.tex` assemble le lecteur. Les 722 unités françaises éditables se trouvent dans `fr/content/`. Cinq pilotes de compilation alternatifs sont conservés dans les sources. Le lecteur charge les 717 autres unités. Les fichiers `provenance/SOURCE_MANIFEST.jsonl` et `provenance/FULL_READER_INPUTS.json` donnent la révision d’origine, les chemins et les empreintes utilisés pour vérifier les entrées.

## Environnement

Sous Windows, utiliser Python 3.10 ou une version ultérieure avec `lxml`, ainsi que MiKTeX, XeLaTeX, BibTeX, dvisvgm et les polices TeX Gyre. Les exécutables doivent être accessibles dans `PATH`. Les versions de make4ht, TeX4ht et tex4ebook utilisées par les scripts sont fournies sous `tools/epub/dependencies/` avec leurs notices.

## PDF et EPUB

Extraire l’archive dans un nouveau dossier, puis exécuter les commandes suivantes depuis le dossier `OpenLogic-fr`.

```powershell
python -B -X utf8 tools/epub/build_full_reader.py pdf pdf-build
python -B -X utf8 tools/epub/build_full_reader.py epub epub-build
```

Le PDF se trouve dans `tools/epub/direct-full/source/locale/fr/reader.pdf`. L’EPUB se trouve dans `tools/epub/openlogic-fr.epub`. Les scripts vérifient les empreintes des sources et les fichiers lus par TeX. La conversion EPUB conserve les formules en MathML et les diagrammes vectoriels en SVG. Elle vérifie aussi la structure et les liens du livre numérique.

Les deux commandes utilisent le même verrou TeX sous Windows. Un code de sortie `2` signifie que le verrou est occupé et qu’aucun moteur TeX n’a démarré. Pour réessayer, donner un nouveau nom à la tentative. Pour reconstruire une seconde fois après une compilation terminée, repartir d’une extraction propre.

Les [références consultées pour l’édition française](provenance/REFERENCES-CONSULTEES.md) sont accompagnées de leurs repères de lecture.

Les polices et la version de la distribution TeX peuvent influer sur l’empreinte des fichiers produits. La révision anglaise et les notices de licence sont conservées sous `upstream/`.
