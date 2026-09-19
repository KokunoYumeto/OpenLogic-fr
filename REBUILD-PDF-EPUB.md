# Reconstruire la septième livraison française d’OpenLogic

Cette livraison comprend neuf chapitres, 65 sections et 74 unités sur les 722 prévues. **fr/reader-cumulative.tex** contient tout le texte du lecteur. Les sources modulaires sont conservées dans **fr/**. Six unités déjà rédigées restent hors du lecteur : le pilote de partie OLP-0055 et les cinq sections du premier ordre OLP-0072, OLP-0076, OLP-0080, OLP-0082 et OLP-0083. Elles rejoindront les chapitres communs lorsque les prérequis seront disponibles. Les imports inactifs de ces cinq sections sont retirés du fichier cumulatif, tandis que le pilote modulaire reste complet.

Le dossier **upstream/** fournit les figures, styles, classes, macros et bibliographies de la révision 9620cc73f9c8e0ad003c514a5d3748f29611c4c0.

## Environnement

Windows, Python 3, MiKTeX, XeLaTeX, BibTeX et les polices TeX Gyre Pagella, Heros et Cursor. L’EPUB utilise les copies de TeX4ht, make4ht et tex4ebook fournies dans **tools/epub/dependencies/**, avec leurs licences. Les exécutables TeX doivent être dans le PATH. Le traitement EPUB nécessite la bibliothèque Python lxml.

Les scripts réservent Global\InterlanguageTeXSlotV1 pendant toute la vie de leurs processus descendants : attente maximale de 45 secondes, durée maximale de 180 secondes, supervision par Windows Job Object. Le reçu distingue une compilation réussie d’un créneau occupé, qui ne lance aucun moteur. Utiliser un répertoire neuf pour chaque reconstruction complète ; conserver et reprendre une opération déjà lancée jusqu’à son état terminal.

## PDF

Depuis la racine du paquet :

~~~powershell
python tools/epub/prepare_inputs.py pdf
python tools/epub/guard_tex4ebook.py pdf-build pdf-compare
~~~

Le résultat est **tools/epub/direct-tex-check/source/locale/fr/reader.pdf**. Quatre passes de XeLaTeX et une passe de BibTeX stabilisent les références et la bibliographie. La date est fixée par SOURCE_DATE_EPOCH=1788739200. Dans l’environnement vérifié, le PDF compte 110 pages. Le PDF modulaire et celui obtenu depuis le fichier cumulatif sont identiques octet pour octet ; leurs empreintes figurent dans **provenance/QA.json**.

## EPUB 3

~~~powershell
python tools/epub/prepare_inputs.py epub
python tools/epub/guard_tex4ebook.py epub-build convert
python tools/epub/repair_epub.py
python tools/epub/inspect_epub.py tools/epub/openlogic-fr-ensembles-calcul-des-sequents.epub
~~~

La préparation remplace les raccourcis de jetons par des appels équivalents dans une copie, développe sept jetons à majuscule selon leurs formes grammaticales et groupe un exposant pour TeX4ht. Quatre passes de conversion et BibTeX produisent le livre. La dépendance bussproofs.4ht inclut une correction documentée du nombre d’arguments de DisplayProof ; les arbres de preuve et les groupes de règles sont capturés intégralement en SVG.

Le traitement final corrige les défauts d’export constatés : espaces de noms MathML, fractions, flèche d’application partielle, ancres de notes, identifiants dupliqués, tabulations sérialisées, bordures des tables et présentation des figures. Il retire une rubrique d’exercices vide générée par le convertisseur. Les grands diagrammes conservent une taille lisible et disposent d’un défilement horizontal local. Leurs descriptions textuelles préservent les prémisses, les conclusions, les règles, les branches incomplètes et les signes de fin de démonstration.

Les contrôles et leur portée sont détaillés dans **provenance/QA.json**. L’EPUB conserve 89 exercices, 87 notes, 4 358 expressions MathML et 70 images SVG décrites, dont 54 nouveaux schémas de séquents. Les textes des huit chapitres antérieurs et leurs seize images sont identiques aux fichiers EPUB déjà publiés.

## Droits et portée

Texte original et traduction : CC BY 4.0. Les licences particulières sont conservées. Les ouvrages universitaires consultés ne sont pas redistribués ; leurs identités et les passages de repérage figurent dans **provenance/**. Cette édition assistée par IA ne revendique pas de validation humaine indépendante et ne constitue pas encore l’édition intégrale.
