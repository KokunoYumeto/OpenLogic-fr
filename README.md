# OpenLogic — édition française

Une édition française du manuel ouvert de logique mathématique de l’[Open Logic Project](https://openlogicproject.org/), avec ses démonstrations, exemples, figures et exercices.

**Deuxième livraison : les chapitres « Ensembles » et « Relations » sont complets.** Leurs quatorze sections et deux fichiers de chapitre représentent **16 des 722 unités** prévues pour l’édition intégrale. Les 706 autres unités restent à achever et à intégrer.

[Lire les deux chapitres en PDF](reader/openlogic-fr-ensembles-relations.pdf) · [Sources françaises](fr/content/sets-functions-relations) · [Choix éditoriaux](review/CHOICES.md) · [Catalogue des traductions d’OpenLogic](https://kokunoyumeto.github.io/OpenLogic-translations/)

Livraisons archivées : [versions Zenodo](https://zenodo.org/records/22650158).

Le lecteur de 22 pages traite des ensembles et de leurs opérations, du paradoxe de Russell, des relations binaires, de leurs interprétations philosophiques, des relations d’équivalence, des ordres, des graphes, des arbres et des opérations sur les relations. Les seize exercices sont réunis à la fin des chapitres. Les figures et les démonstrations sont conservées.

La traduction s’appuie sur des passages précisément repérés de cours universitaires français. Les références documentent la terminologie, certaines formulations et les conventions ; le texte anglais reste l’autorité pour les énoncés traduits. Cinquante choix avec leurs alternatives, motifs et incertitudes sont consignés dans le dossier de révision. La traduction et sa révision ont été assistées par IA. Aucune validation humaine indépendante des chapitres entiers n’est revendiquée.

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

Le dossier doit être nouveau. Le script y assemble une copie des sources et effectue trois passes de XeLaTeX avec BibTeX après la première. Le PDF se trouve ensuite dans `source/locale/fr/reader.pdf`. Le script fixe la date de compilation et utilise le mutex `Global\InterlanguageTeXSlotV1` pendant toutes les passes et la bibliographie. Si le créneau est occupé, aucun moteur TeX n’est lancé.

Deux compilations dans des dossiers distincts ont produit un PDF identique octet pour octet. Les versions et empreintes pertinentes figurent dans `provenance/QA.json`.

## Licence et attribution

Texte original : Open Logic Project. La traduction et les modifications éditoriales sont identifiées comme telles. Le texte original et la traduction sont diffusés sous [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). La [licence originale](upstream/LICENSE.md) et les éventuelles notices propres aux composants sont conservées. Les références universitaires externes conservent leurs droits propres et ne sont pas couvertes par cette licence du dépôt.
