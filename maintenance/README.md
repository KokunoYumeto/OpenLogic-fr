# Retrouver les passages de l’édition française

L’index met en correspondance les 722 unités anglaises et françaises de la version 1.0.0. Chacune des 2 182 entrées de segment situe un passage dans les deux fichiers. Selon l’unité, le découpage porte sur plusieurs paragraphes, une partie de ligne ou le fichier entier. Les empreintes permettent de retrouver le texte exact auquel se rapporte un choix de traduction. L’appréciation de ce choix demande de lire les deux passages et les références citées. [Index des passages](alignement-v1.0.0.jsonl) · [Sources de l’édition française](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v1.0.0/openlogic-fr-sources.zip)

Depuis la racine du dépôt, avec Python 3.11 ou une version ultérieure et l’archive téléchargée dans ce répertoire :

```sh
python maintenance/verifier_alignement.py openlogic-fr-sources.zip
```

Chaque ligne de l’index décrit une unité. Dans l’archive, le chemin `path` se trouve sous `OpenLogic-fr/upstream/` pour l’anglais et `OpenLogic-fr/fr/` pour le français. Les indices de lignes commencent à 1, dernière ligne comprise. Le mode `lines-original` conserve les retours chariot des fichiers d’origine. Le mode `lines-lf` ramène les fins de ligne CRLF à LF. Dans ces deux modes, on joint les lignes retenues par LF. Le mode `characters-lf` utilise le texte UTF-8 décodé avec fins de ligne normalisées et deux positions de caractères comptées à partir de zéro, borne supérieure exclue. L’empreinte du fichier entier porte toujours sur ses octets d’origine.

Indexation et vérification produites par OpenAI Codex, GPT-6 Astra, effort de raisonnement Ultra. Les auteurs du texte et la provenance de la traduction figurent dans [la présentation de l’édition](../README.md).

## Consulter les sources d’un passage

Pour retrouver les sources associées au théorème de Rice, saisir depuis la racine du dépôt :

```sh
python maintenance/consulter.py OLP-0248-R00
```

La commande donne les références, les repères de lecture et les liens vers les documents. Dans les notes de cours d’Arnaud Durand et Paul Rozière, le théorème 2.3.13, page 43, porte sur les propriétés extensionnelles des fonctions partielles calculables. Le corollaire 2.3.14, page 44, en déduit des problèmes de décision concernant les machines. Les exemples et la démonstration du volume français se comparent avec ceux du texte anglais d’Open Logic. [Notes de cours, pages 43–44](https://www.irif.fr/~roziere/m2cf2/calculabilite93.pdf#page=43)

Les [104 notices bibliographiques](sources-du-canon.jsonl) identifient les documents par leur URL, leur taille et leur empreinte SHA-256. Les [389 repères](reperes-du-canon.jsonl) en situent les passages. L’[index des consultations](consultations-par-segment.jsonl) conserve les associations entre ces repères et les segments, ainsi que les réexamens rétrospectifs. Un repère peut justifier un terme ou un renvoi précis. La liste seule ne dit pas quels autres choix de la phrase il justifie. Lorsqu’un réexamen porte sur une rédaction antérieure, la commande le signale si son empreinte permet de le déterminer. Une liste vide ou un contrôle en attente reste visible.

Les [cinq renvois structurels](renvois-structurels.jsonl) situent une commande LaTeX dans les fichiers du volume. Ils ne constituent pas des attestations linguistiques.
