# Reconstruire cette édition française

Cette livraison comprend douze chapitres, 89 sections, 106 exercices et 101 unités du projet OpenLogic figé à la révision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. Le PDF compte 150 pages. Les 122 unités françaises rédigées figurent dans `fr/content/` ; la présence des sources anglaises dans `upstream/` ne les transforme pas en traductions.

Le fichier `fr/reader-cumulative.tex` contient le texte complet des 101 unités du volume. Il utilise les classes, styles, macros, bibliographie et figures fournis dans cette archive. Le fichier `fr/reader.tex` conserve l’organisation modulaire. Le registre `provenance/EDITION.json` indique les unités intégrées et les vingt et un brouillons exclus : OLP-0055, OLP-0072, OLP-0076, OLP-0080, OLP-0082, OLP-0083, OLP-0087, OLP-0090, OLP-0094, OLP-0096, OLP-0097, OLP-0101, OLP-0104, OLP-0108, OLP-0110, OLP-0111, OLP-0115, OLP-0117, OLP-0120, OLP-0123 et OLP-0125. Les sections propres au premier ordre attendent les chapitres de syntaxe et de sémantique correspondants.

## Environnement

Utiliser Windows, Python 3 avec `lxml`, MiKTeX avec XeLaTeX, BibTeX et les polices TeX Gyre. Les exécutables doivent être dans `PATH`. Les dépendances TeX4ht, make4ht et tex4ebook sont incluses sous `tools/epub/dependencies/`, avec leurs licences. Ne pas lancer les commandes TeX directement : le garde acquiert `Global\InterlanguageTeXSlotV1`, démarre le processus suspendu dans un Job Object sans échappement et conserve le verrou jusqu’à la fin de tous les descendants et des contrôles de journal. L’acquisition est bornée à 45 secondes ; le PDF est borné à 420 secondes et l’EPUB à 600 secondes. Un reçu `slot_occupied` signifie qu’aucun moteur n’a démarré. Une tentative suivante doit porter un nouveau nom et ne doit jamais dupliquer un processus encore actif.

Extraire le ZIP dans un nouveau dossier. Depuis le dossier `OpenLogic-fr`, exécuter :

```powershell
python tools/epub/prepare_inputs.py pdf
python tools/epub/guard_tex4ebook.py pdf-build pdf-compare
python tools/epub/prepare_inputs.py epub
python tools/epub/guard_tex4ebook.py epub-build convert
python tools/epub/repair_epub.py
python tools/epub/inspect_epub.py tools/epub/openlogic-fr-ensembles-derivations-axiomatiques.epub
```

Le PDF reconstruit se trouve dans `tools/epub/direct-tex-check/source/locale/fr/reader.pdf` ; le livre numérique dans `tools/epub/openlogic-fr-ensembles-derivations-axiomatiques.epub`. Le garde fixe `SOURCE_DATE_EPOCH=1788739200`. Les reçus de chaque tentative restent dans leur dossier.

La préparation EPUB vérifie les empreintes des 101 sources chargées, remplace 1 313 occurrences du raccourci de tokens et développe explicitement vingt-six tokens à initiale majuscule selon les macros OpenLogic. Cette adaptation ne modifie pas le texte du PDF. Les cadres de règles et arbres de preuve sont conservés comme SVG avec descriptions françaises : 146 diagrammes au total. Les grandes figures et les tables de dérivation gardent une taille lisible et se parcourent horizontalement. Les 5 594 autres formules sont du MathML natif. Les 87 notes ont leurs liens aller et retour ; les 106 exercices restent numérotés.

La réparation post-conversion corrige les espaces de noms MathML, les identifiants et liens de notes, les titres accentués et les métadonnées de livraison ; elle vérifie la conservation du texte des paragraphes. Les descriptions des figures sont fournies par `SEQUENT_IMAGE_ALTS.json`, `NATURAL_IMAGE_ALTS.json` et `TABLEAUX_IMAGE_ALTS.json`, ainsi que par les descriptions héritées dans le script. Les PDF des références universitaires consultées ne sont pas redistribués.

Les empreintes des livrables sont publiées avec la livraison. Les scripts de reconstruction sont fournis pour permettre leur comparaison octet par octet dans cet environnement. Une installation de TeX ou de polices différente peut produire un PDF graphiquement équivalent mais d’empreinte différente.
