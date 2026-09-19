# OpenLogic — édition française

Cette cinquième livraison française d’OpenLogic réunit six chapitres :
ensembles, relations, fonctions, dénombrabilité, construction des systèmes
de nombres et ensembles infinis. Elle comprend 45 sections, leurs
démonstrations et exemples, 73 exercices et 13 figures, soit 51 des
722 unités prévues pour l’édition intégrale.

Les nouveaux chapitres construisent les entiers, les rationnels et les réels
par les coupures de Dedekind et les suites de Cauchy, puis présentent
l’hôtel de Hilbert, les algèbres de Dedekind, la récurrence et une autre
démonstration de Schröder–Bernstein. Les corrections de la source et les
précisions éditoriales sont signalées dans le texte.

Les fichiers principaux sont proposés dans cet ordre : PDF de 79 pages,
LaTeX cumulatif complet, ZIP de toutes les sources et dépendances du projet,
puis EPUB 3 redistribuable. Le LaTeX cumulatif reproduit exactement le PDF
livré. L’EPUB conserve les mathématiques en MathML et les figures en SVG ;
il passe EPUBCheck 5.3.0 sans erreur ni avertissement.

Traduction et révision éditoriale assistées par IA, appuyées sur un corpus
mathématique français documenté. Aucune validation humaine indépendante
n’est revendiquée. L’édition intégrale reste en cours.

Texte original : [Open Logic Project](https://openlogicproject.org/),
révision 9620cc73f9c8e0ad003c514a5d3748f29611c4c0.
Texte et traduction sous licence CC BY 4.0 ; les notices propres aux
composants sont conservées.

[Catalogue des traductions d’OpenLogic](https://kokunoyumeto.github.io/OpenLogic-translations/).


## Lire et télécharger

1. [Lire les six chapitres en PDF](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.5.0-construction-des-nombres/00-01-openlogic-fr-ensembles-fonctions-construction-des-nombres.pdf)
2. [LaTeX cumulatif complet](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.5.0-construction-des-nombres/00-02-openlogic-fr-ensembles-fonctions-construction-des-nombres.tex)
3. [Sources et reconstruction PDF/EPUB](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.5.0-construction-des-nombres/00-03-openlogic-fr-ensembles-fonctions-construction-des-nombres-sources.zip)
4. [Télécharger l’EPUB](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.5.0-construction-des-nombres/00-04-openlogic-fr-ensembles-fonctions-construction-des-nombres.epub)

Version archivée avec DOI : [10.5281/zenodo.22849740](https://doi.org/10.5281/zenodo.22849740). Cette révision conserve le lecteur de 51 unités et ajoute les LaTeX cumulatifs directement téléchargeables des trois premières livraisons. [Lignée Zenodo](https://doi.org/10.5281/zenodo.22650157) · [Toutes les livraisons GitHub](https://github.com/KokunoYumeto/OpenLogic-fr/releases).

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
