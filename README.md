# OpenLogic : édition française

Traduction française, en cours, du manuel de logique mathématique *Open Logic Text* (The Open Logic Project). La onzième
livraison (v0.11.0) réunit treize chapitres, des ensembles à la logique du premier ordre : ensembles, relations,
fonctions, dénombrabilité, nombres, ensembles infinis, logique propositionnelle, introduction à la logique du premier
ordre, systèmes de dérivation, calcul des séquents, déduction naturelle, tableaux analytiques signés et déduction
axiomatique. Le volume compte 159 pages, 98 sections et 106 exercices.

[Lire le PDF](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.11.0-first-order-introduction/00-00-00-00-01-openlogic-fr-ensembles-logique-premier-ordre.pdf) ·
[EPUB](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.11.0-first-order-introduction/00-00-00-00-04-openlogic-fr-ensembles-logique-premier-ordre.epub) ·
[Toutes les livraisons](https://github.com/KokunoYumeto/OpenLogic-fr/releases)

## Réalisation

La traduction est réalisée par IA ; les contrôles éditoriaux et techniques ne constituent pas une validation humaine
indépendante. Les démonstrations, exemples et exercices du projet original sont conservés ; quatre défauts locaux de la
source sont corrigés et signalés. Un réaudit ciblé de trois chapitres (neuf pages, 3 916 mots comparés aux sources
anglaises) n’a relevé aucun défaut majeur, mathématique, logique, d’omission ou de rendu ; cinq corrections mineures
ont été intégrées. L’EPUB contient 5 935 expressions MathML natives, 146 figures SVG décrites, 106 exercices et 88
notes ; EPUBCheck 5.3.0 ne signale aucune erreur ni aucun avertissement. Les références françaises consultées et les
décisions de traduction sont dans `provenance/`, les questions de révision dans `review/`.

## État

Le volume intègre 111 des 722 unités TeX de la révision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0` d’OpenLogic.
132 unités sont rédigées ; vingt et une restent hors du volume, dont vingt sections de systèmes de preuve qui attendent
leurs dépendances de syntaxe et de sémantique du premier ordre. Il reste 590 unités à traduire et 611 à intégrer au
lecteur.

## Contenu

Livraison [v0.11.0-first-order-introduction](https://github.com/KokunoYumeto/OpenLogic-fr/releases/tag/v0.11.0-first-order-introduction) :
[PDF](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.11.0-first-order-introduction/00-00-00-00-01-openlogic-fr-ensembles-logique-premier-ordre.pdf),
[LaTeX cumulatif complet](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.11.0-first-order-introduction/00-00-00-00-02-openlogic-fr-ensembles-logique-premier-ordre.tex),
[sources et reconstruction PDF/EPUB](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.11.0-first-order-introduction/00-00-00-00-03-openlogic-fr-ensembles-logique-premier-ordre-sources.zip),
[EPUB](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.11.0-first-order-introduction/00-00-00-00-04-openlogic-fr-ensembles-logique-premier-ordre.epub).

Les éditions historiques disposent chacune de leur PDF, de leur LaTeX cumulatif complet et de leur ZIP de sources :

| Édition | PDF | LaTeX complet | Sources |
| --- | --- | --- | --- |
| Ensembles, 7 unités | [PDF](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.1.0-ensembles/07-01-openlogic-fr-ensembles.pdf) | [LaTeX](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.1.0-ensembles/07-02-openlogic-fr-ensembles.tex) | [ZIP](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.1.0-ensembles/07-03-openlogic-fr-ensembles-sources.zip) |
| Ensembles et relations, 16 unités | [PDF](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.2.0-ensembles-relations/06-01-openlogic-fr-ensembles-relations.pdf) | [LaTeX](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.2.0-ensembles-relations/06-02-openlogic-fr-ensembles-relations.tex) | [ZIP](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.2.0-ensembles-relations/06-03-openlogic-fr-ensembles-relations-sources.zip) |
| Ensembles, relations et fonctions, 23 unités | [PDF](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.3.0-ensembles-relations-fonctions/05-01-openlogic-fr-ensembles-relations-fonctions.pdf) | [LaTeX](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.3.0-ensembles-relations-fonctions/05-02-openlogic-fr-ensembles-relations-fonctions.tex) | [ZIP](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v0.3.0-ensembles-relations-fonctions/05-03-openlogic-fr-ensembles-relations-fonctions-sources.zip) |

Chaque LaTeX cumulatif contient tout le texte de sa livraison et reproduit exactement le PDF correspondant, avec les dépendances de son ZIP. Les fichiers et liens historiques restent publics.

Le dossier `fr/` contient le texte français modulaire et le LaTeX cumulatif ; `upstream/` conserve la source anglaise
figée et les composants du projet (sa présence ne compte pas comme traduction).

### Recompiler

Voir [les instructions de reconstruction](REBUILD-PDF-EPUB.md). Le ZIP complet comprend également les dépendances de conversion EPUB. La compilation PDF depuis ce dépôt utilise le même garde de processus et le même fichier cumulatif.

~~~powershell
.\tools\Build-Reader.ps1 -ScratchRoot C:\chemin\vers\un-nouveau-dossier
~~~

Le PDF résultant se trouve dans tools/epub/direct-tex-check/source/locale/fr/reader.pdf sous ce nouveau dossier. Les versions antérieures restent disponibles avec leurs sources dans la lignée de publication.

## Sources et crédits

- [The Open Logic Project](https://openlogicproject.org/), révision
  [`9620cc73`](https://github.com/OpenLogicProject/OpenLogic/tree/9620cc73f9c8e0ad003c514a5d3748f29611c4c0).
- [Collection des traductions OpenLogic](https://kokunoyumeto.github.io/OpenLogic-translations/).

## Licence

Texte original et traduction : CC BY 4.0. Les [notices originales](upstream/LICENSE.md) et les licences particulières des
composants sont conservées. Les PDF universitaires consultés ne sont pas redistribués.
