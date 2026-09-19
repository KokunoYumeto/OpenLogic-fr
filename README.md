# OpenLogic — édition française

Cette sixième livraison française d’OpenLogic réunit huit chapitres, 56 sections et 83 exercices, soit 64 des 722 unités prévues pour l’édition intégrale.

Après les ensembles, les relations, les fonctions, la dénombrabilité, la construction des nombres et les ensembles infinis, deux nouveaux chapitres présentent la syntaxe et la sémantique propositionnelles et les systèmes de preuve : calcul des séquents, déduction naturelle, tableaux et dérivations axiomatiques. Les démonstrations, les formules et les exercices sont conservés ; les corrections de la source sont signalées dans le texte.

Le lecteur est proposé en PDF de 94 pages, en LaTeX cumulatif complet directement téléchargeable et en EPUB 3 avec MathML natif et figures décrites. Le ZIP contient les sources modulaires, les styles, les figures, les bibliographies et les outils nécessaires à leur reconstruction.

Traduction et révision éditoriale assistées par IA, avec références françaises consultées et décisions documentées. Aucune validation humaine indépendante n’est revendiquée. L’édition intégrale reste en cours. Les livraisons antérieures et leurs sources demeurent publiques.

[Catalogue des traductions d’OpenLogic](https://kokunoyumeto.github.io/OpenLogic-translations/) · [Lignée Zenodo](https://doi.org/10.5281/zenodo.22650157).


## Lire et télécharger

1. [Lire les huit chapitres en PDF](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.6.0-logique-propositionnelle/00-00-01-openlogic-fr-ensembles-logique-propositionnelle.pdf)
2. [LaTeX cumulatif complet](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.6.0-logique-propositionnelle/00-00-02-openlogic-fr-ensembles-logique-propositionnelle.tex)
3. [Sources et reconstruction PDF/EPUB](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.6.0-logique-propositionnelle/00-00-03-openlogic-fr-ensembles-logique-propositionnelle-sources.zip)
4. [Télécharger l’EPUB](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.6.0-logique-propositionnelle/00-00-04-openlogic-fr-ensembles-logique-propositionnelle.epub)

[Lignée Zenodo](https://doi.org/10.5281/zenodo.22650157) · [Toutes les livraisons GitHub](https://github.com/KokunoYumeto/OpenLogic-fr/releases).

Les éditions historiques disposent chacune de leur PDF, de leur LaTeX cumulatif complet et de leur ZIP de sources :

| Édition | PDF | LaTeX complet | Sources |
| --- | --- | --- | --- |
| Ensembles, 7 unités | [PDF](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.1.0-ensembles/07-01-openlogic-fr-ensembles.pdf) | [LaTeX](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.1.0-ensembles/07-02-openlogic-fr-ensembles.tex) | [ZIP](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.1.0-ensembles/07-03-openlogic-fr-ensembles-sources.zip) |
| Ensembles et relations, 16 unités | [PDF](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.2.0-ensembles-relations/06-01-openlogic-fr-ensembles-relations.pdf) | [LaTeX](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.2.0-ensembles-relations/06-02-openlogic-fr-ensembles-relations.tex) | [ZIP](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.2.0-ensembles-relations/06-03-openlogic-fr-ensembles-relations-sources.zip) |
| Ensembles, relations et fonctions, 23 unités | [PDF](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.3.0-ensembles-relations-fonctions/05-01-openlogic-fr-ensembles-relations-fonctions.pdf) | [LaTeX](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.3.0-ensembles-relations-fonctions/05-02-openlogic-fr-ensembles-relations-fonctions.tex) | [ZIP](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.3.0-ensembles-relations-fonctions/05-03-openlogic-fr-ensembles-relations-fonctions-sources.zip) |

Chaque LaTeX cumulatif contient tout le texte de sa livraison et reproduit exactement le PDF correspondant, avec les dépendances de son ZIP. Les fichiers et liens historiques restent publics.

## Sources et révision

Le dossier fr/ contient le texte français modulaire et le LaTeX cumulatif. Le dossier upstream/ conserve la source anglaise figée et les composants du projet ; sa présence ne compte pas comme traduction française. Les identités, passages consultés et décisions figurent dans provenance/, et les questions de révision dans review/CHOICES.md. Les choix historiques marqués non vérifiés ne servent pas à justifier cette livraison.

## Recompiler

Voir [les instructions de reconstruction](REBUILD-PDF-EPUB.md). Le ZIP complet comprend également les dépendances de conversion EPUB. La compilation PDF depuis ce dépôt utilise le même garde de processus et le même fichier cumulatif.

~~~powershell
.\tools\Build-Reader.ps1 -ScratchRoot C:\chemin\vers\un-nouveau-dossier
~~~

Le PDF résultant se trouve dans tools/epub/direct-tex-check/source/locale/fr/reader.pdf sous ce nouveau dossier. Les versions antérieures restent disponibles avec leurs sources dans la lignée de publication.

## Licence

Texte original et traduction : CC BY 4.0. Les [notices originales](upstream/LICENSE.md) et les licences particulières des composants sont conservées. Les PDF universitaires consultés ne sont pas redistribués.
