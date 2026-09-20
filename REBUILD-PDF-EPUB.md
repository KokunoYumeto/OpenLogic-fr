# Reconstruire cette édition française

Cette livraison comprend dix chapitres, 73 sections, 95 exercices et 83 unités du projet OpenLogic figé à la révision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. Le PDF compte 126 pages. Les 94 unités françaises rédigées figurent dans `fr/content/`; la présence des sources anglaises dans `upstream/` ne les transforme pas en traductions.

Le fichier `fr/reader-cumulative.tex` contient le texte complet des 83 unités du volume. Il utilise les classes, styles, macros, bibliographie et figures fournis dans cette archive. Le fichier `fr/reader.tex` conserve l’organisation modulaire. Le registre `provenance/EDITION.json` indique les unités intégrées et les onze brouillons exclus : OLP-0055, OLP-0072, OLP-0076, OLP-0080, OLP-0082, OLP-0083, OLP-0087, OLP-0090, OLP-0094, OLP-0096 et OLP-0097. Les sections de premier ordre ne sont pas dupliquées dans le chapitre propositionnel.

## Environnement

Utiliser Windows, Python 3 avec `lxml`, MiKTeX avec XeLaTeX, BibTeX et les polices TeX Gyre. Les exécutables doivent être dans `PATH`. Les dépendances TeX4ht, make4ht et tex4ebook sont incluses sous `tools/epub/dependencies/`, avec leurs licences. Ne pas lancer les commandes TeX directement : le garde acquiert `Global\InterlanguageTeXSlotV1`, démarre le processus suspendu dans un Job Object sans échappement et conserve le verrou jusqu’à la fin de tous les descendants et des contrôles de journal. L’acquisition est bornée à 45 secondes; l’exécution complète est bornée à 180 secondes. Un reçu `slot_occupied` signifie qu’aucun moteur n’a démarré. Une tentative suivante doit porter un nouveau nom et ne doit jamais dupliquer un processus encore actif.

Extraire le ZIP dans un nouveau dossier. Depuis le dossier `OpenLogic-fr`, exécuter :

```powershell
python tools/epub/prepare_inputs.py pdf
python tools/epub/guard_tex4ebook.py pdf-build pdf-compare
python tools/epub/prepare_inputs.py epub
python tools/epub/guard_tex4ebook.py epub-build convert
python tools/epub/repair_epub.py
python tools/epub/inspect_epub.py tools/epub/openlogic-fr-ensembles-deduction-naturelle.epub
```

Le PDF reconstruit se trouve dans `tools/epub/direct-tex-check/source/locale/fr/reader.pdf`; le livre numérique dans `tools/epub/openlogic-fr-ensembles-deduction-naturelle.epub`. Le garde fixe `SOURCE_DATE_EPOCH=1788739200`. Les reçus de chaque tentative restent dans son dossier.

La préparation EPUB vérifie les empreintes des 83 sources chargées, remplace 999 occurrences du raccourci de tokens et développe explicitement onze tokens à initiale majuscule selon les macros OpenLogic. Cette adaptation ne modifie pas le texte du PDF. Les cadres de règles et arbres de preuve sont conservés comme SVG avec descriptions françaises : 114 diagrammes au total, dont 44 dans le nouveau chapitre. Les grandes figures gardent une taille lisible et se parcourent horizontalement. Les 4 826 autres formules sont du MathML natif. Les 87 notes ont leurs liens aller et retour; les 95 exercices restent numérotés.

La réparation post-conversion corrige les espaces de noms MathML, les identifiants et liens de notes et les titres accentués; elle vérifie la conservation du texte des paragraphes. Les descriptions des figures sont fournies par `SEQUENT_IMAGE_ALTS.json` et `NATURAL_IMAGE_ALTS.json`, ainsi que les descriptions héritées dans le script. Les PDF des références universitaires consultées ne sont pas redistribués.

Les empreintes des livrables sont publiées avec la livraison. Les scripts de reconstruction sont fournis pour permettre leur comparaison octet par octet dans cet environnement. Une installation de TeX ou de polices différente peut produire un PDF graphiquement équivalent mais d’empreinte différente.
