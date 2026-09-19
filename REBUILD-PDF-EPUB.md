# Reconstruire la sixième livraison française d’OpenLogic

Cette livraison comprend huit chapitres, 56 sections et 64 unités sur les 722 prévues. Le fichier **fr/reader-cumulative.tex** contient tout le texte du lecteur. Les sources modulaires sont conservées dans **fr/**. Le pilote de partie OLP-0055 est traduit mais n'est pas chargé, car ses autres chapitres ne sont pas encore disponibles ; il n'entre pas dans le compte des 64 unités. Le dossier **upstream/** fournit les figures, styles, classes, macros et bibliographies de la révision 9620cc73f9c8e0ad003c514a5d3748f29611c4c0.

## Environnement

La reconstruction a été vérifiée sous Windows avec Python 3, MiKTeX, XeLaTeX, BibTeX et les polices TeX Gyre Pagella, Heros et Cursor. L'EPUB utilise les copies de TeX4ht, make4ht et tex4ebook fournies dans **tools/epub/dependencies/**, avec leurs licences. Les exécutables TeX doivent être dans le PATH. Le traitement EPUB nécessite la bibliothèque Python lxml.

Les scripts réservent Global\InterlanguageTeXSlotV1 pendant toute la vie de leurs processus descendants : attente maximale de 45 secondes, durée maximale de 180 secondes, supervision par Windows Job Object. Le reçu distingue une compilation réussie d'un créneau occupé, qui ne lance aucun moteur. Utiliser un répertoire neuf pour chaque reconstruction complète.

## PDF

Depuis la racine du paquet :

~~~powershell
python tools/epub/prepare_inputs.py pdf
python tools/epub/guard_tex4ebook.py pdf-build pdf-compare
~~~

Le résultat est **tools/epub/direct-tex-check/source/locale/fr/reader.pdf**. La copie préparée utilise le LaTeX cumulatif complet. Quatre passes de XeLaTeX et une passe de BibTeX stabilisent les références et la bibliographie. La date est fixée par SOURCE_DATE_EPOCH=1788739200. Dans l'environnement vérifié, le PDF compte 94 pages. Le PDF modulaire et le PDF obtenu à partir du fichier cumulatif sont identiques octet pour octet ; leurs empreintes figurent dans **provenance/QA.json**.

## EPUB 3

~~~powershell
python tools/epub/prepare_inputs.py epub
python tools/epub/guard_tex4ebook.py epub-build convert
python tools/epub/repair_epub.py
python tools/epub/inspect_epub.py tools/epub/openlogic-fr-ensembles-logique-propositionnelle.epub
~~~

La préparation remplace les raccourcis de jetons par des appels équivalents dans une copie, explicite deux titres à jetons majuscules et groupe un exposant pour TeX4ht. Quatre passes de conversion et BibTeX produisent le livre. La dépendance bussproofs.4ht inclut une correction documentée du nombre d'arguments de DisplayProof ; les arbres de preuve sont capturés intégralement en SVG. Le tableau emploie l'abréviation française « Hyp. », développée dans son texte de remplacement.

Le traitement final corrige les défauts d'export constatés : espaces de noms MathML, fractions, flèche d'application partielle, ancres de notes, identifiants dupliqués, tabulations sérialisées, bordures des tables et présentation des figures. Il retire une rubrique d'exercices vide générée par le convertisseur. Les formules trop larges disposent d'un défilement local sur écran étroit.

Les contrôles du fichier livré et leur portée sont détaillés dans **provenance/QA.json**. Le lecteur EPUB conserve les 83 exercices, les 76 notes, les formules en MathML et les figures en SVG, avec leurs descriptions.

## Droits et portée

Texte original et traduction : CC BY 4.0. Les licences particulières sont conservées. Les ouvrages universitaires consultés ne sont pas redistribués ; leurs identités et les passages de repérage figurent dans **provenance/**. Cette édition assistée par IA ne revendique pas de validation humaine indépendante et ne constitue pas encore l'édition intégrale.
