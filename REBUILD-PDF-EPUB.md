# Reconstruire la cinquième livraison française d’OpenLogic

Cette livraison comprend six chapitres, 45 sections et 51 unités sur les 722
prévues. Le fichier **fr/reader-cumulative.tex** contient tout le texte publié.
Les fichiers modulaires d’origine sont conservés dans **fr/**. Le dossier
**upstream/** fournit les figures, styles, classes, macros et bibliographies
du projet à la révision 9620cc73f9c8e0ad003c514a5d3748f29611c4c0.

## Environnement

La reconstruction a été vérifiée sous Windows avec Python 3, MiKTeX,
XeLaTeX, BibTeX et les polices TeX Gyre Pagella, Heros et Cursor.
L’EPUB emploie aussi les versions de TeX4ht, make4ht et tex4ebook fournies
dans **tools/epub/dependencies/**, avec leurs notices de licence.
Les exécutables TeX doivent être accessibles dans le PATH.
Le script de réparation EPUB utilise la bibliothèque Python lxml.

Les scripts prennent le verrou Global\InterlanguageTeXSlotV1 pendant
toute la compilation. Ils attendent le verrou au plus 45 secondes et
limitent à 180 secondes l’ensemble de leurs processus descendants.
Un reçu d’exécution distingue un verrou occupé d’une compilation réussie.
Si le verrou est occupé, aucun moteur n’est lancé.

Décompresser le paquet dans un répertoire neuf avant chaque reconstruction
complète. Les copies de travail restent dans tools/epub/.

## PDF

Depuis la racine du paquet :

~~~powershell
python tools/epub/prepare_inputs.py pdf
python tools/epub/guard_tex4ebook.py pdf-build pdf-compare
~~~

Le résultat est **tools/epub/direct-tex-check/source/locale/fr/reader.pdf**.
La copie préparée emploie le LaTeX cumulatif. Trois passes de XeLaTeX
et une passe de BibTeX produisent les références et la bibliographie.
La date de construction est fixée par SOURCE_DATE_EPOCH=1788739200.
Dans l’environnement vérifié, le PDF comprend 79 pages et son SHA-256 est :

06031d3d8449269c57216306b3a04ff098d3f122eb72c1e601af05df57174816.

## EPUB 3

~~~powershell
python tools/epub/prepare_inputs.py epub
python tools/epub/guard_tex4ebook.py epub-build convert
python tools/epub/repair_epub.py
python tools/epub/inspect_epub.py tools/epub/openlogic-fr-ensembles-fonctions-construction-des-nombres.epub
~~~

Le fichier final porte ce dernier nom dans tools/epub/. La préparation
remplace les raccourcis de jetons par un alias équivalent dans une copie,
et groupe explicitement un exposant pour le lecteur de TeX4ht.
Le traitement final corrige les défauts d’export constatés : espaces de noms
MathML, fractions, flèche d’application partielle, ancres de notes, identifiants
dupliqués, tabulations sérialisées et dimensions des figures.
Les expressions mathématiques restent en MathML et les figures en SVG.
Les formules trop larges défilent dans leur propre bloc sur un écran étroit.

Le résultat livré a passé EPUBCheck 5.3.0 sans erreur ni avertissement.
Il contient 3 245 expressions MathML, 13 figures, 73 exercices et 76 notes.
Les preuves de contrôle sont dans provenance/QA.json.

## Droits et portée

Texte original et traduction : Creative Commons Attribution 4.0 International.
Les licences particulières des composants sont conservées. Les documents
de référence consultés pour le français ne sont pas redistribués ; leurs
identités bibliographiques et les passages de repérage figurent dans
provenance/. Cette édition assistée par IA ne revendique pas de validation
humaine indépendante et ne constitue pas encore l’édition intégrale.
