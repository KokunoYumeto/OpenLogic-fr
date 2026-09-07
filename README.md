# OpenLogic — édition française

Une édition française du manuel ouvert de logique mathématique de l’[Open Logic Project](https://openlogicproject.org/), avec ses démonstrations, exemples, figures et exercices.

**Première livraison : le chapitre « Ensembles » est complet.** Ses six sections et son fichier de chapitre représentent **7 des 722 unités** prévues pour l’édition intégrale. Les 715 autres unités restent à traduire et à intégrer. Cette livraison n’est donc pas présentée comme le manuel complet.

[Lire le chapitre en PDF](reader/openlogic-fr-ensembles.pdf) · [Sources françaises](fr/content/sets-functions-relations/sets) · [Choix éditoriaux](review/CHOICES.md) · [Catalogue des traductions d’OpenLogic](https://kokunoyumeto.github.io/OpenLogic-translations/)

Le chapitre traite de l’extensionnalité, des sous-ensembles et de l’ensemble des parties, des principaux ensembles de nombres, des mots et des suites, des réunions et intersections, des produits cartésiens et du paradoxe de Russell. Les dix exercices sont réunis en fin de chapitre.

La traduction s’appuie sur des passages précisément repérés de cours universitaires français. Les références documentent la terminologie, certaines formulations et les conventions ; le texte anglais reste l’autorité pour les énoncés traduits. Les alternatives, leurs motifs et les incertitudes sont consignées dans le dossier de révision. La traduction et sa révision ont été assistées par IA. Aucune validation humaine indépendante du chapitre entier n’est revendiquée.

Les précisions apportées aux exemples et aux conditions d’existence sont signalées dans le lecteur. Le dossier de provenance distingue ces corrections de la traduction. Les PDF de référence externes ne sont pas redistribués.

## Contenu du dépôt

- `fr/` : texte français éditable et fichier maître du lecteur.
- `reader/` : lecteur PDF vérifié.
- `upstream/` : source anglaise figée, conservée sans modification, ainsi que les macros, figures et notices de droits nécessaires.
- `provenance/` : identités des sources, alignement, références consultées et résultats de vérification.
- `review/` : décisions terminologiques et syntaxiques, précisions éditoriales et échantillons de paraphrase inverse.
- `tools/` : compilation reproductible du lecteur.

Les fichiers anglais dans `upstream/` servent à la provenance et à la compilation ; leur présence ne compte pas comme traduction française.

## Recompiler

Sous Windows, avec PowerShell, MiKTeX ou une distribution compatible fournissant XeLaTeX, les paquets utilisés par OpenLogic et les polices TeX Gyre :

```powershell
.\tools\Build-Reader.ps1 -ScratchRoot C:\chemin\vers\un-nouveau-dossier
```

Le dossier doit être nouveau. Le script y assemble une copie des sources et effectue trois passes de XeLaTeX. Le PDF se trouve ensuite dans `source/locale/fr/reader.pdf`. Le script fixe la date de compilation et utilise le mutex `Global\InterlanguageTeXSlotV1` pendant toutes les passes. Si le créneau est occupé, aucun moteur TeX n’est lancé.

Deux compilations dans des dossiers distincts ont produit un PDF identique octet pour octet. Les versions et empreintes pertinentes figurent dans `provenance/QA.json`.

## Licence et attribution

Texte original : Open Logic Project. La traduction et les modifications éditoriales sont identifiées comme telles. Le texte original et la traduction sont diffusés sous [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). La [licence originale](upstream/LICENSE.md) et les éventuelles notices propres aux composants sont conservées. Les références universitaires externes conservent leurs droits propres et ne sont pas couvertes par cette licence du dépôt.
