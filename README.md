# OpenLogic — édition française

Cette huitième livraison de l’édition française d’OpenLogic réunit dix chapitres, des ensembles à la déduction naturelle : ensembles, relations, fonctions, dénombrabilité, nombres, ensembles infinis, logique propositionnelle, systèmes de dérivation, calcul des séquents et déduction naturelle. Elle conserve les démonstrations, exemples et exercices du projet original et signale les corrections apportées aux erreurs locales de la source.

Le volume comprend 126 pages, 73 sections et 95 exercices. Il intègre 83 des 722 unités TeX de la révision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0` d’OpenLogic. Au total, 94 unités sont rédigées; onze restent hors de ce volume, notamment les sections propres au premier ordre dont les prérequis ne sont pas encore intégrés. Il reste 628 unités à traduire et 639 à intégrer au lecteur. L’édition complète est en cours.

Le PDF est accompagné du LaTeX cumulatif directement téléchargeable, d’une archive des sources modulaires et des dépendances de reconstruction, ainsi que d’un EPUB à texte redistribuable avec formules MathML et descriptions des diagrammes. Les références françaises effectivement consultées, les décisions de traduction et les questions de révision sont documentées dans l’archive. La traduction est assistée par IA; les contrôles éditoriaux et techniques ne constituent pas une validation humaine indépendante.

[Projet OpenLogic](https://openlogicproject.org/) · [Collection des traductions](https://kokunoyumeto.github.io/OpenLogic-translations/).


## Lire et télécharger

1. [Lire les dix chapitres en PDF](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.8.0-deduction-naturelle/00-00-00-00-01-openlogic-fr-ensembles-deduction-naturelle.pdf)
2. [LaTeX cumulatif complet](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.8.0-deduction-naturelle/00-00-00-00-02-openlogic-fr-ensembles-deduction-naturelle.tex)
3. [Sources et reconstruction PDF/EPUB](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.8.0-deduction-naturelle/00-00-00-00-03-openlogic-fr-ensembles-deduction-naturelle-sources.zip)
4. [Télécharger l’EPUB](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.8.0-deduction-naturelle/00-00-00-00-04-openlogic-fr-ensembles-deduction-naturelle.epub)

[Livraison sur Zenodo](https://zenodo.org/records/22851625) · [DOI de cette version](https://doi.org/10.5281/zenodo.22851625).

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
