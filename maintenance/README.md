# Retrouver les passages de l’édition française

L’index met en correspondance les 722 unités anglaises et françaises de la version 1.0.0. Chacune des 2 182 entrées de segment situe un passage dans les deux fichiers. Selon l’unité, le découpage porte sur plusieurs paragraphes, une partie de ligne ou le fichier entier. Les empreintes permettent de retrouver le texte exact auquel se rapporte un choix de traduction. L’appréciation de ce choix demande de lire les deux passages et les références citées. [Index des passages](alignement-v1.0.0.jsonl) · [Sources de l’édition française](https://github.com/KokunoYumeto/OpenLogic-fr/releases/download/v1.0.0/openlogic-fr-sources.zip)

Depuis la racine du dépôt, avec Python 3.11 ou une version ultérieure et l’archive téléchargée dans ce répertoire :

```sh
python maintenance/verifier_alignement.py openlogic-fr-sources.zip
```

Chaque ligne de l’index décrit une unité. Dans l’archive, le chemin `path` se trouve sous `OpenLogic-fr/upstream/` pour l’anglais et `OpenLogic-fr/fr/` pour le français. Les indices de lignes commencent à 1, dernière ligne comprise. Le mode `lines-original` conserve les retours chariot des fichiers d’origine. Le mode `lines-lf` ramène les fins de ligne CRLF à LF. Dans ces deux modes, on joint les lignes retenues par LF. Le mode `characters-lf` utilise le texte UTF-8 décodé avec fins de ligne normalisées et deux positions de caractères comptées à partir de zéro, borne supérieure exclue. L’empreinte du fichier entier porte toujours sur ses octets d’origine.

Indexation et vérification produites par OpenAI Codex, GPT-6 Astra, effort de raisonnement Ultra. Les auteurs du texte et la provenance de la traduction figurent dans [la présentation de l’édition](../README.md).
