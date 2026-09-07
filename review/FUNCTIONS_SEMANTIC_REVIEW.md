# Fonctions : relecture sémantique et mathématique

Périmètre : les sept unités OLP-0020–0026, leurs six sections, 125 blocs alignés dont 87 blocs de prose. Révision bornée du chapitre entier par le même assistant ; aucune validation humaine indépendante ni justification exhaustive de chaque mot n’est revendiquée. Les 34 décisions nouvelles C216–C249 sont une relecture actuelle des premiers brouillons, et non une reconstruction de leur rédaction initiale. Les 53 autres décisions C163–C215 ont été consignées lors de la rédaction. Les anciennes décisions C51–C58 restent historiques.

Le texte distingue fonction totale, fonction partielle, domaine, ensemble d’arrivée et image. La convention du manuel est conservée malgré celle, différente, de Habermehl : une fonction non qualifiée est totale sur son domaine annoncé. La définition de l’injectivité autorise les fibres vides ; la surjectivité ne requiert pas l’unicité des antécédents. Les exemples constante, identité, successeur et arrondi supérieur de x/2 ont été recalculés, zéro compris. Pour ce dernier exemple, 2k atteint k, et 1 et 2 ont la même image.

La définition par cas pair/impair conserve exactement les deux expressions. L’exclusivité n’est cependant qu’une méthode suffisante : des branches qui se recoupent et donnent la même valeur conviennent aussi. Cette correction de portée est visible en note. L’extensionnalité compare des fonctions de mêmes domaine et ensemble d’arrivée ; le changement d’arrivée dans f′:A→ran(f) ne se réduit donc pas à un changement de nom.

Dans la section sur les graphes, les deux conditions existence/unicité sont distinguées dans la preuve. Le graphe est inclus dans A×B. La restriction fonctionnelle ne sélectionne que la première coordonnée ; une note conserve et distingue la restriction relationnelle antérieure à C². Les graphes coïncident lorsque f[C]⊆C. Le contre-exemple successeur sur N, C={0}, vérifie la différence. L’identification de la fonction à son graphe est présentée comme une représentation commode, sans nouvelle affirmation métaphysique.

Pour l’inverse à gauche, A non vide est ajouté et signalé. Un seul a∈A est fixé pour tous les points hors image : aucun choix simultané sur une famille n’est nécessaire. La fonction vide ∅→{0} réfute l’énoncé sans cette hypothèse ; le cas ∅→∅ reste explicitement valide. Pour l’inverse à droite, la note originale sur l’axiome du choix est conservée, y compris les exceptions A=N, A fini et f bijective. Les exercices ne deviennent pas des preuves fournies : les mentions de démonstration laissée en exercice sont du contenu original, pas des espaces réservés à compléter.

La composition applique f puis g et donne g∘f ; le produit relatif R_f | R_g conserve ce même ordre. Les exercices d’injectivité, surjectivité et graphe sont inchangés. Le domaine d’une fonction partielle est la partie où la valeur est définie. Son inverse partiel est défini sur les fibres à un seul élément ; les identités de l’exercice ne sont affirmées que sur dom(f) et ran(f). Le dernier énoncé sériel conserve exactement ∀x∈A ∃y∈B Rxy. Le terme « sérielle » reste un choix lexical éditorial provisoire : les témoins consultés pour ce chapitre ne l’attestent pas expressément.

Les branches conditionnelles ont été lues avec et sans les chapitres référencés. « Cela permet notamment d’envisager / On peut ainsi envisager » s’enchaîne dans les deux cas à « sur les fonctions… ». Le renvoi sur l’axiome du choix donne soit « reprendrons dans le chapitre… », soit « laisserons ici de côté ». La composition donne soit l’introduction sur l’inverse suivie de « on peut définir », soit « On peut définir ». Les références locales restantes seront également contrôlées dans le PDF compilé.

Les cinq figures sont les assets vectoriels d’origine. Leur fichier n’expose pas de texte ordinaire à traduire ; la lisibilité, les flèches et les légendes doivent être vérifiées sur leur rendu. Les contrôles des environnements, labels, références, citations, UTF-8/NFC, identités et ancres passent. La compilation et la relecture visuelle sont des contrôles distincts, consignés dans le reçu de livraison une fois exécutés.

# Échantillons de rétroparaphrase

Le relevé mécanique des segments mathématiques est dans FUNCTIONS_MATH_COMPARISON.json. Ses différences ont été examinées : les occurrences isolées de f, A, C et y sont des répétitions remplacées par des pronoms ou déplacées avec la phrase ; x₁ et x₂∈A sont réunis en x₁,x₂∈A. La preuve du graphe remplace une répétition conditionnelle par l’appel explicite à l’existence pour chaque x∈A. La preuve de l’inverse à gauche distingue les deux branches au lieu de ne réexpliquer que y∈ran(f), et ajoute la valeur a de la seconde branche. Les autres ajouts sont exactement les corrections signalées (n/x, domaine non vide et contre-exemple de restriction). Aucune expression de calcul, équation, négation ou domaine d’un résultat n’est supprimé sans cette justification. Le relevé normalise le texte contenu dans les formules ; la traduction de ce texte a donc aussi été lue directement.

- « Pour tout y∈B, il existe au moins un x∈A » revient à « every codomain member is hit by at least one input » ; cela n’ajoute ni unicité ni entrée commune à tous les y.
- « À condition que f et g aient le même domaine et le même ensemble d’arrivée » revient à « extensional equality is asserted only at a fixed domain and codomain » ; la qualification originale subsiste.
- « Fixons donc a∈A » revient à « choose one fixed domain element for every point outside the range » ; la preuve utilise exactement l’hypothèse ajoutée.
- « Pour tout x∈dom(f) … pour tout y∈ran(f) » revient à « the inverse identities are restricted to the defined inputs and attained outputs » ; elles ne s’étendent pas abusivement à tout A et B.

# Incertitudes conservées

« Biunivoque » et « sérielle » sont des choix éditoriaux réversibles ; la définition mathématique les accompagne. Les références natives éclairent les constructions et conventions explicitement indiquées, sans certifier tout le vocabulaire ou l’ensemble du raisonnement du manuel. Les questions précises et alternatives se trouvent dans l’audit de construction.

Le lecteur cumulatif a maintenant été compilé et reproduit à l’identique ; la relecture visuelle est terminée. Voir provenance/QA.json.
