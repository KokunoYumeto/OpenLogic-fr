# Revue sémantique et structurelle OLP-0098–OLP-0102

## Résultat

Les cinq unités sont intégralement traduites et comparées à leurs sources figées. Les imports du pilote, les quatorze schémas de règle, le schéma de substitution, les quatre tableaux arborescents, les signes de vérité, les numéros de lignes et les conditions sur les eigenvariables sont conservés. Les macros de concepts apparaissent avec les mêmes identités et multiplicités que dans les sources. La seule différence à l'intérieur d'un affichage mathématique est la traduction de `or` par `ou` dans la définition d'une formule signée.

## Comparaison par unité

- OLP-0098 : le pilote importe les treize sections dans le même ordre et sous les mêmes conditions FOL. Le chapitre est décrit comme un système de tableaux analytiques signés. La mention source de la déduction naturelle devant `prfTab` est corrigée et la correction est déclarée.
- OLP-0099 : la valeur de vérité et l'énoncé qui composent une formule signée, la croissance de l'arbre vers le bas, les hypothèses, l'application non locale des règles, la fermeture d'une branche et le tableau fermé de racine fausse sont tous conservés. « Possibilité conjointe » est reformulé par l'incompatibilité des deux signes, sans transformer l'explication intuitive en définition sémantique supplémentaire.
- OLP-0100 : les huit règles propositionnelles et la coupure sont identiques à la source. La coupure reste facultative et son rôle de combinaison des tableaux est conservé.
- OLP-0101 : les quatre règles de quantificateurs, l'affichage équivalent par substitution et l'exemple invalide sont identiques à la source. Les deux conditions distinctes sont conservées : fermeture de `t`, fraîcheur de la constante `a` sur toute la branche antérieure. La contradiction source entre « terme clos » et « aucune restriction » est résolue par « aucune restriction supplémentaire » et signalée dans une note éditoriale.
- OLP-0102 : la définition inductive par arbre fini, l'ordre des hypothèses, l'application des règles, les définitions ouverte et fermée et les trois états successifs de l'exemple sont conservés. La prose précise que `A` est la formule sous-jacente à la formule signée, ce que la source exprimait par une juxtaposition ambiguë.

## Rétro-paraphrases de contrôle

- OLP-0099 : a tableau systematically records possible truth and falsity in a structure by arranging signed sentences in a downward tree. A branch containing both signs for the same formula is closed; a closed tableau rooted at false A excludes every way A could be false.
- OLP-0101 : universal-true and existential-false instantiate with a closed term. Universal-false and existential-true introduce a constant absent from the preceding branch. Dropping that freshness condition would yield a closed tableau for a formula that is not valid.
- OLP-0102 : tableaux are finite trees built from one or more assumptions by rule applications. A branch is closed exactly when it contains opposite signs for one formula; otherwise it is open. The worked example expands true A-and-not-A and then closes with false A.

Ces rétro-paraphrases restituent les dépendances, les portées et les conclusions des sources. Aucun écart sémantique non déclaré ne subsiste dans le lot. Le rendu reste à effectuer lors de l'intégration du chapitre complet.


# Revue sémantique OLP-0103–OLP-0105

## Portée et résultat

Les trois sources et leurs traductions ont été relues intégralement, puis comparées après retrait uniquement des trente environnements `oltableau`. Ces trente blocs sont identiques à la source. Les séquences d'environnements hors notes éditoriales, les items, les labels, les balises FOL/notFOL et les commandes logiques contrôlées concordent. OLP-0103 contient 162 occurrences source de formule signée et 163 occurrences cible : l'unique différence est la séparation déclarée de l'hypothèse mal formée en deux formules signées. OLP-0104 conserve ses 100 occurrences; OLP-0105 conserve ses 35 occurrences. Les trois cibles sont en UTF-8 NFC et le balayage du texte ne relève aucun résidu de prose anglaise.

## OLP-0103 — exemples propositionnels

La traduction garde la progression pédagogique complète : inscrire les hypothèses, appliquer l'unique règle correspondant au signe et au connecteur principal, ne cocher une formule qu'après traitement sur toutes les branches ouvertes, choisir librement l'ordre lorsque plusieurs règles sont disponibles, et répéter les conclusions au bout de chaque branche concernée. Les trois constructions, les fermetures de branches, les justifications et les numéros de ligne sont inchangés. Les trois listes d'exercices sont complètes.

Rétro-paraphrase contrôlée : « L'ordre choisi est indifférent, pourvu que la règle correspondant à chaque formule signée soit appliquée sur toutes les branches » redonne « the order does not matter provided every signed formula receives its rule on every branch ». « Nous ne plaçons une coche qu'après application sur toutes les branches ouvertes » redonne exactement la convention source, sans transformer la coche en élément de la syntaxe formelle.

La réparation du neuvième item du deuxième groupe est justifiée par les exercices parallèles : les prémisses sont (A\lor B) et (\lnot B), toutes deux vraies, et la conclusion (A), supposée fausse pour construire le tableau. La cible ne modifie aucun autre exercice.

## OLP-0104 — quantificateurs

Les trois exemples conservent la condition de fraîcheur de l'eigenvariable et les choix de constantes (a,b,c). Les impératifs anglais sur l'ordre ont été rendus comme une méthode de recherche, puisqu'ils règlent l'efficacité de la construction et non la correction d'une inférence particulière. La distinction formelle demeure nette : les règles avec eigenvariable exigent une constante fraîche; les règles \(\mathrm T\forall\) et \(\mathrm F\exists\) peuvent être réappliquées avec tout terme clos utile.

Rétro-paraphrase contrôlée : « choisir tout terme clos » redonne l'intention de « pick any term » une fois la condition formelle de OLP-0101 rétablie. Le passage précise toujours que plusieurs applications avec des termes différents peuvent être nécessaires et qu'un terme déjà présent dans le tableau est souvent un bon choix. « Différer les règles de quantificateurs sans condition sur l'eigenvariable jusqu'à ce qu'elles soient nécessaires » conserve le conseil de stratégie, ainsi que le conseil séparé de différer les ramifications.

Les quinze tableaux, dont les lignes où (a), (b) et (c) sont introduits ou réutilisés, sont identiques à la source. Tous les exercices et toutes les portées de quantificateurs sont inchangés.

## OLP-0105 — notions de théorie de la démonstration

Les trois notions sont distinctes et complètes. Un théorème exige un tableau fermé pour \(\mathrm F A\). La relation \(\Gamma\vdash A\) exige un témoin fini \(\{B_1,\ldots,B_n\}\subseteq\Gamma\) et un tableau fermé contenant \(\mathrm F A\) avec chaque \(\mathrm T B_i\). L'incohérence exige un témoin fini dont toutes les formules sont prises avec le signe vrai. Le paragraphe introductif conserve la distinction entre notions sémantiques et notions de théorie de la démonstration, ainsi que la coïncidence donnée par correction et complétude.

Rétro-paraphrase contrôlée : la preuve de transitivité choisit un témoin fini dans \(\Delta\), un témoin fini dans \(\Gamma\), applique la coupure à (A), puis greffe sur les deux branches les tableaux fermés disponibles. Cela redonne exactement le mécanisme source. La proposition de compacité conserve ses deux directions opérationnelles : toute dérivabilité a un témoin fini, et toute incohérence a un témoin fini incohérent.

La réparation \(\{D_1,\ldots,D_m\}\subseteq\Gamma\) ne renforce pas l'argument : elle rend correctement la partie finie déjà requise par la définition. L'adaptation conditionnelle structures/valuations évite d'attribuer des structures de premier ordre à la présentation propositionnelle et reproduit la convention des chapitres déjà relus.

## Limite actuelle

La comparaison source-cible et la revue sémantique sont achevées pour ces trois unités. Leur composition dans le lecteur, le rendu visuel et la publication restent volontairement en attente de l'achèvement du chapitre entier.


# Revue sémantique OLP-0106–OLP-0111

## Portée et résultat

Les six sources et leurs traductions ont été relues intégralement. La séquence des environnements hors notes éditoriales, les items, les labels, les renvois, les balises FOL/notFOL et les commandes logiques contrôlées concordent. Dix-sept blocs formels sont présents : neuf `oltableau` dans OLP-0107, deux `tableau` et deux `oltableau` dans OLP-0108, un `defish` et trois `oltableau` dans OLP-0110. Tous sont identiques à la source, après la seule normalisation déclarée des huit appels mal formés à `sFmla` dans OLP-0107. Les six cibles sont en UTF-8 NFC; leurs accolades sont équilibrées; aucun résidu de prose anglaise n'a été relevé.

## OLP-0106 — dérivabilité et cohérence

Les quatre arguments emploient uniquement des témoins finis de dérivabilité ou d'incohérence, puis la règle de coupure et la greffe de tableaux déjà fermés. La première preuve réunit les témoins `Gamma_0` et `Gamma_1`. La deuxième remplace `F A` par `T non-A`, et sa réciproque traite séparément les deux façons dont une branche ancienne pouvait se fermer. La troisième conserve l'ordre exact des `n+1` hypothèses avant d'insérer `F A`. La dernière construit les deux branches de coupure et explique pourquoi les deux greffes restent correctes.

Rétro-paraphrase contrôlée : « après les `n+1` hypothèses » redonne une insertion à la position `n+2`, sans changer le tableau donné; « la règle vraie de la négation appliquée à `T non-A` » redonne exactement la prémisse et la conclusion `F A` du schéma formel. Les trois réparations portent sur l'index, la prémisse de règle et le numéro de ligne, non sur les résultats métalogiques.

## OLP-0107 — connecteurs propositionnels

Les énoncés et les neuf témoins formels établissent les deux éliminations et l'introduction de la conjonction, l'incohérence de `A ou B, non-A, non-B`, les deux introductions de la disjonction, le modus ponens et les deux voies d'introduction de l'implication. Les signes et les formules de chaque hypothèse correspondent aux relations de dérivabilité annoncées.

Rétro-paraphrase contrôlée : chaque tableau part de la négation signée de la conclusion et des prémisses signées vraies, puis se ferme par une paire `T/F` de la même formule. La réparation de notation ne déplace aucun nœud, ne change aucun signe et ne modifie aucune justification; elle restitue seulement les deux arguments syntaxiques requis par la commande.

## OLP-0108 — quantificateurs

La généralisation forte conserve les trois conditions nécessaires : `c` ne figure ni dans `Gamma` ni dans `A(x)`, `Gamma` dérive `A(c)`, et la ligne ajoutée est obtenue par la règle universelle fausse avec une constante fraîche au-dessus d'elle. Les deux propriétés suivantes portent sur un terme clos `t`; leurs tableaux appliquent respectivement la règle existentielle fausse et la règle universelle vraie.

Rétro-paraphrase contrôlée : le remplacement de la première hypothèse, suivi de l'insertion de `F A(c)`, redonne le tableau source sans prétendre que `c` est fraîche partout dans l'ancien arbre; la preuve contrôle exactement sa fraîcheur dans les hypothèses placées au-dessus de la nouvelle ligne. L'ajout « terme clos » rend visible une condition déjà imposée par les règles et ne restreint pas davantage le calcul.

## OLP-0109 — correction

La définition distingue `T A`, satisfaite quand `A` l'est, et `F A`, satisfaite quand `A` ne l'est pas. La preuve maintient l'invariant suivant : toute application de règle à un tableau possédant une branche satisfaisable laisse au moins une branche satisfaisable. Les cas sans ramification conservent la même structure ou valuation, sauf le cas universel faux qui modifie l'interprétation d'une constante fraîche. Les cas avec ramification choisissent la branche correspondant à la valeur sémantique du connecteur; la coupure choisit `T B` ou `F B` selon que `B` est satisfaite ou non.

Rétro-paraphrase contrôlée : dans le cas `F forall`, la structure `M'` ne diffère de `M` que par la valeur de la constante fraîche `a`, de sorte que toutes les formules signées de `Gamma` gardent leur valeur et que `F A(a)` devient satisfaite. Les deux prémisses universelles emploient maintenant `A(x)` de bout en bout, ce qui rétablit la formule sur laquelle portent déjà les calculs source. Les corollaires redonnent successivement validité ou tautologicité, conséquence sémantique et contraposée de la cohérence.

## OLP-0110–OLP-0111 — identité et correction

Les règles exigent des termes clos. La règle réflexive ajoute `T(t=t)`; les deux règles de remplacement combinent `T(t_1=t_2)` avec une formule signée de signe fixé portant sur `t_1`, puis transportent ce même signe vers `t_2`. Les trois tableaux donnent la substituabilité de Leibniz, la symétrie et la transitivité. Les explications corrigées identifient exactement les lignes et les substitutions utilisées.

Rétro-paraphrase contrôlée : pour la symétrie, prendre `A(x)` égal à `x=s_1` transforme la ligne 3 en `A(s_1)` et la conclusion en `A(s_2)`; pour la transitivité, prendre `A(x)` égal à `s_1=x` identifie `A(s_2)` à la ligne 2. Dans la preuve de correction, l'égalité des valeurs de `t_1` et `t_2`, avec l'extensionalité, transporte la satisfaction de `A(t_1)` vers `A(t_2)`. Le signe vrai de cette conclusion est donc imposé, tandis que le signe faux relève du cas analogue annoncé séparément.

## Limite actuelle

La comparaison source-cible et la revue sémantique sont achevées pour les six unités. Leur composition dans le lecteur, le rendu visuel et la publication doivent encore être validés au niveau du chapitre complet.
