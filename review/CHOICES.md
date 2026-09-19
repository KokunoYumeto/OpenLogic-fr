# Décisions et questions de révision

Ces choix documentent la traduction assistée par IA ; ils ne constituent pas une validation humaine indépendante. Les anciens choix explicitement non vérifiés sont conservés uniquement dans le registre historique JSONL.

## C01 — OLP-0005-B04, OLP-0005-B05, OLP-0005-B06

**Choix :** élément, avec membre comme synonyme à la définition

**Autre formulation envisagée :** membre partout

**Motif :** Élément est directement utilisé dans l’axiome de la référence ; membre reste présent pour conserver les deux désignations de la source.

**Confiance et limites :** Même objet mathématique et usage visible dans le canon.

**Question de révision :** Le maintien du synonyme membre dans la définition suffit-il aux renvois ultérieurs ?

Passages de référence : L01.

## C02 — OLP-0005-B06, OLP-0006-B09, OLP-0009-B05, OLP-0010-B09

**Choix :** si et seulement si

**Autre formulation envisagée :** ssi

**Motif :** La forme développée rend les deux directions visibles dans les définitions et les preuves, sans exiger la maîtrise préalable de l’abréviation.

**Confiance et limites :** Le canon emploie ssi ; le développement garde exactement la biconditionnelle.

**Question de révision :** Conserver la forme développée dans les longues preuves ultérieures ou abréger après introduction ?

Passages de référence : H03.

## C03 — OLP-0005-B07, OLP-0010-B04

**Choix :** article défini expliqué, unicité conditionnée à l’existence

**Autre formulation envisagée :** traduire littéralement the par le et affirmer existence et unicité

**Motif :** Le français emploie l’ devant ensemble ; expliquer l’article défini restitue l’accent pédagogique. Le principe ne prouve que l’unicité conditionnelle, comme le précise ensuite Russell dans OLP.

**Confiance et limites :** Confirmation explicite dans l’axiome et sa remarque, ainsi que dans OLP-0010.

**Question de révision :** La note éditoriale distingue-t-elle assez clairement la correction de la traduction ?

Passages de référence : L07.

## C04 — OLP-0005-B08, OLP-0005-B10

**Choix :** frères et sœurs ; un frère ou une sœur

**Autre formulation envisagée :** fratrie ; membre de la fratrie

**Motif :** Le premier groupe décrit la collection ; la seconde expression teste l’appartenance d’une personne. Fratrie serait plus compact mais moins transparent pour ce premier exemple.

**Confiance et limites :** Le lien familial est celui du texte anglais ; le canon soutient seulement la forme collection/propriété.

**Question de révision :** Frères et sœurs est-il suffisamment naturel pour désigner ici la collection à un seul membre ?

Passages de référence : L01, L09.

## C05 — OLP-0005-B11

**Choix :** entier strictement positif et diviseurs propres positifs

**Autre formulation envisagée :** nombre et nombres qui le divisent sans lui être égaux

**Motif :** La source omet le domaine positif ; une lecture incluant zéro ou les diviseurs négatifs ne soutiendrait plus l’exemple de 6. Une note signale la clarification, sans changer la formule.

**Confiance et limites :** La somme 1+2+3 démontre le domaine positif attendu ; pas de prétendue définition canonique du nombre parfait.

**Question de révision :** La précision serait-elle mieux intégrée dans une convention générale sur les diviseurs ?

Passages de référence : L04, L07.

## C06 — OLP-0006-B03, OLP-0006-B05, OLP-0006-B14

**Choix :** sous-ensemble, synonyme partie ; ensemble des parties

**Autre formulation envisagée :** partie partout ; ensemble puissance

**Motif :** Les deux noms du sous-ensemble sont attestés conjointement par Habermehl. Sous-ensemble rend visible l’inclusion au début ; ensemble des parties est la désignation du power set utilisée à Lyon.

**Confiance et limites :** Les définitions canoniques portent exactement sur les mêmes relations et construction.

**Question de révision :** À quel moment passer à partie dans les chapitres plus avancés sans créer une rupture terminologique ?

Passages de référence : H01, L05.

## C07 — OLP-0006-B05

**Choix :** sous-ensemble strict

**Autre formulation envisagée :** sous-ensemble propre

**Motif :** Strict exprime immédiatement inclusion et inégalité ; propre est possible mais rencontre plus tard classe propre avec un autre contraste.

**Confiance et limites :** Choix éditorial motivé par la formule OLP ; H01 atteste seulement sous-ensemble, pas strict.

**Question de révision :** Le terme strict convient-il aussi aux emplois adjectivaux ultérieurs ?

Passages de référence : H01.

## C08 — OLP-0006-B06

**Choix :** rendre e distinct de a, b, c explicite

**Autre formulation envisagée :** laisser la distinction des lettres tacite

**Motif :** L’exemple négatif devient faux si e=a. L’hypothèse minimale ajoutée protège le sens sans supposer inutilement que a, b, c sont eux-mêmes distincts.

**Confiance et limites :** Contre-exemple immédiat e=a.

**Question de révision :** Adopter une convention locale de lettres distinctes pour les autres exemples analogues ?

Passages de référence : H01.

## C09 — OLP-0006-B11, OLP-0006-B12

**Choix :** abrège ; implication sous le quantificateur universel, conjonction sous l’existentiel

**Autre formulation envisagée :** exprime ; reformuler les deux restrictions de manière identique

**Motif :** La différence entre implication et conjonction constitue précisément le contenu de la définition ; les formules sont conservées sans modification.

**Confiance et limites :** Les deux formules OLP et leurs portées sont contrôlées directement.

**Question de révision :** Faut-il une future note sur le cas vide lorsque ces abréviations seront utilisées dans des preuves ?

Passages de référence : L07, L09.

## C10 — OLP-0007-B04, OLP-0007-B05, OLP-0007-B06

**Choix :** entiers naturels à partir de zéro ; entiers relatifs ; entiers strictement positifs

**Autre formulation envisagée :** nombres naturels ; entiers ; entiers positifs

**Motif :** La source inclut zéro dans Nat et l’exclut de PosInt. Strictement positifs évite l’ambiguïté française de positif ; relatifs distingue Int de Nat.

**Confiance et limites :** La construction des entiers naturels et relatifs est visible dans L04 ; PosInt est lu directement dans OLP.

**Question de révision :** Garder relatifs à chaque occurrence ou autoriser entiers quand le domaine est clair ?

Passages de référence : L04.

## C11 — OLP-0007-B07, OLP-0009-B18

**Choix :** mot fini ; mot vide ; longueur

**Autre formulation envisagée :** chaîne finie de symboles ; chaîne vide

**Motif :** Le cours d’informatique construit les mots à partir du mot vide et des lettres. Ce choix relie les strings de la première section aux words de la seconde, qui ont ici le même sens.

**Confiance et limites :** Définition inductive et emploi sur un alphabet effectivement consultés.

**Question de révision :** Les futurs usages informatiques de string nécessiteront-ils chaîne lorsqu’il s’agit de données textuelles plutôt que de langages formels ?

Passages de référence : H02.

## C12 — OLP-0007-B08

**Choix :** suite infinie qui se prolonge dans une seule direction

**Autre formulation envisagée :** suite bi-infinie ou liste infinie sans qualification

**Motif :** La précision une seule direction conserve le domaine indexé à partir de 1 et exclut une indexation par tous les entiers relatifs.

**Confiance et limites :** La qualification est explicite dans OLP ; le canon n’est consulté que pour le registre des suites.

**Question de révision :** La distinction avec suite bi-infinie devra-t-elle être rappelée dans les chapitres de calculabilité ?

Passages de référence : L11.

## C13 — OLP-0008-B03, OLP-0008-B07, OLP-0008-B20

**Choix :** réunion ; de A, de B, ou des deux

**Autre formulation envisagée :** union ; soit A soit B

**Motif :** Réunion est le choix de Lyon ; Habermehl emploie union. La mention ou des deux interdit la lecture exclusive du ou et conserve la disjonction de la formule.

**Confiance et limites :** Deux usages concurrents réellement observés, et portée disjonctive vérifiée.

**Question de révision :** Faut-il ajouter union comme synonyme lors de la première définition pour le lectorat informatique ?

Passages de référence : L08, H01.

## C14 — OLP-0008-B12, OLP-0008-B13, OLP-0008-B27

**Choix :** à la fois ; qui ne sont pas

**Autre formulation envisagée :** et ; sauf ceux de B

**Motif :** À la fois souligne la conjonction de l’intersection. La relative négative porte sur l’appartenance à B dans la différence, sans exclure tout B de l’univers.

**Confiance et limites :** Les prédicats et leur négation correspondent à la diapositive 8.

**Question de révision :** Le syntagme différence ensembliste apporte-t-il encore une information utile après la définition ?

Passages de référence : H01.

## C15 — OLP-0008-B19, OLP-0008-B21, OLP-0008-B24

**Choix :** famille non vide pour l’intersection sans univers fixé ; exception explicitée

**Autre formulation envisagée :** accepter une intersection vide comme ensemble de tous les objets

**Motif :** La condition universelle sur la famille vide est vraie de tout objet. Sans univers fixé elle ne définit pas un ensemble ; dans U, l’intersection vide peut être U. La restriction est signalée comme éditoriale.

**Confiance et limites :** Conséquence directe de la quantification vide ; H01 fournit explicitement le cadre ambiant alternatif.

**Question de révision :** La note suffit-elle à préparer les futures intersections de familles éventuellement vides ?

Passages de référence : L07, L09, H01.

## C16 — OLP-0009-B03, OLP-0009-B04, OLP-0009-B06

**Choix :** couple, avec paire ordonnée comme synonyme

**Autre formulation envisagée :** paire ordonnée partout

**Motif :** Paire ordonnée est le terme exact de Lyon ; couple est plus léger dans les preuves françaises. Le synonyme conserve le lien vers la source canonique.

**Confiance et limites :** Le sens est fixé par l’égalité coordonnée par coordonnée ; le choix couple n’est pas attribué au passage consulté.

**Question de révision :** Préférer paire ordonnée dans le titre pour renforcer la continuité avec le canon ?

Passages de référence : L02.

## C17 — OLP-0009-B05, OLP-0009-B08

**Choix :** composante ; n-uplet ordonné ; emboîtement à gauche

**Autre formulation envisagée :** élément ; n-tuple ; emboîtement à droite

**Motif :** Composante distingue les coordonnées des membres de l’ensemble qui code le couple. L’emboîtement à gauche est celui d’OLP et ne doit pas être remplacé par une autre convention.

**Confiance et limites :** Définition anglaise et toutes les expressions emboîtées contrôlées ; n-uplet est un jugement éditorial.

**Question de révision :** La distinction composante/membre devra-t-elle être rappelée au traitement formel des fonctions ?

Passages de référence : L02.

## C18 — OLP-0009-B12, OLP-0009-B17

**Choix :** définition par récurrence ; montrer par récurrence

**Autre formulation envisagée :** définition récursive ; montrer par induction

**Motif :** Dans ces occurrences, l’indice est un entier naturel k. Récurrence est l’usage visible dans Lyon ; les chapitres sur induction bien fondée pourront demander une autre distinction.

**Confiance et limites :** Application limitée ici à k naturel ; aucune généralisation à toute induction.

**Question de révision :** Maintenir définition récursive ailleurs pour distinguer construction et démonstration ?

Passages de référence : L11.

## C19 — OLP-0010-B07, OLP-0010-B10, OLP-0010-B11

**Choix :** ne pas s’appartenir à soi-même ; supposition et contradiction dans les deux cas

**Autre formulation envisagée :** non-auto-membre ; raccourcir à R appartient ssi R n’appartient pas

**Motif :** Le groupe verbal évite un adjectif artificiel. Le développement conserve séparément les hypothèses R dans R et R hors de R pour les lecteurs débutants.

**Confiance et limites :** Les deux sens ont été comparés à la preuve source et au paradoxe dans le canon.

**Question de révision :** La répétition finale de être/ne pas être est-elle la plus lisible sans perdre les deux polarités ?

Passages de référence : L06.

## C20 — OLP-0010-B12, OLP-0010-B13

**Choix :** affirmation contradictoire ; théorie naïve

**Autre formulation envisagée :** affirmation inconsistante ; théorie vraiment naïve

**Motif :** Ici inconsistent qualifie l’affirmation d’existence menant à une contradiction, pas encore une propriété formelle d’un calcul. Contradictoire suit l’explication canonique et évite de trancher prématurément tout le lexique de consistency.

**Confiance et limites :** Usage du canon et rôle local du mot concordent ; décision explicitement locale.

**Question de révision :** Quel terme général retenir après consultation des chapitres consacrés aux théories cohérentes ?

Passages de référence : L06, L09.

## C21 — 

**Choix :** préférence provisoire : au plus dénombrable pour la propriété incluant fini et vide

**Autre formulation envisagée :** dénombrable avec convention inclusive annoncée

**Motif :** Lyon atteste les deux conventions dans la même définition. La forme explicite évite de demander au lectorat francophone de deviner laquelle s’applique. Elle ne sera appliquée qu’après lecture des définitions OLP du chapitre concerné.

**Confiance et limites :** Convention inclusive attestée ; adjudication finale OLP encore à faire.

**Question de révision :** Les macroformes adjectivales exigent-elles un usage abrégé de dénombrable après convention explicite ?

Passages de référence : L10.

## C22 — OLP-0008-B15, OLP-0008-B22

**Choix :** hypothèses locales c≠d et b≠d, signalées en notes

**Autre formulation envisagée :** supposer toutes les lettres distinctes dans tout le chapitre

**Motif :** Les deux hypothèses suffisent aux intersections annoncées. Elles répondent exactement aux contre-exemples relevés par le manager, sans ajouter de restriction globale aux autres énoncés.

**Confiance et limites :** Vérification directe des appartenances et contre-exemples c=d ou b=d hors des éléments affichés.

**Question de révision :** Ces précisions locales sont-elles plus lisibles qu’une convention limitée aux exemples ?

Passages de référence : H01.

## C23 — OLP-0008-B14

**Choix :** a, b et c distincts de 0 et de 1 dans cet exemple

**Autre formulation envisagée :** traiter tacitement les lettres comme différentes des chiffres

**Motif :** L’intersection affichée n’est vide que si les deux ensembles sont disjoints ; la formulation explicite uniquement la condition déjà annoncée dans le texte.

**Confiance et limites :** Prendre a=0 donne immédiatement un contre-exemple à l’égalité sans hypothèse.

**Question de révision :** Une convention d’exemples pourrait-elle alléger ces notes dans une révision future ?

Passages de référence : H01.

## C24 — OLP-0009-B18

**Choix :** distinguer les mots abstraits de leurs représentations non munies de longueur

**Autre formulation envisagée :** identifier sans restriction les symboles et les couples de tout alphabet

**Motif :** Si l’alphabet contient le symbole ensemble vide, le codage original confond déjà le mot vide et un mot de longueur un. Le code de chaque longueur positive reste injectif ; associer la longueur à la représentation distingue les mots. La formule originale est préservée et son statut de représentation est explicité.

**Confiance et limites :** Contre-exemple direct A contenant l’ensemble vide ; différence entre mot inductif dans H02 et couple codé dans L02.

**Question de révision :** Faut-il adopter une définition par fonctions à domaine initial fini dans le futur chapitre formel sur les suites ?

Passages de référence : H02, L02.

## C25 — OLP-0007-B05, OLP-0008-B04, OLP-0008-B12, OLP-0009-B07

**Choix :** articles français devant les renvois ; renvoi conditionnel entre parenthèses

**Autre formulation envisagée :** calquer in/using par dans/à l’aide de sans article

**Motif :** Le PDF révélait Dans Section et À l’aide de Définition. Ajouter la et régler les noms automatiques en minuscules produit dans la section et à l’aide de la définition. Le renvoi futur à une étiquette de type encore variable est parenthétique.

**Confiance et limites :** Constat du lecteur compilé et accord syntaxique français ; la référence garde exactement son identifiant.

**Question de révision :** Les futurs renvois multiples exigent-ils une macro qui choisisse aussi le pluriel et l’article ?

Passages de référence : L06.

## C26 — OLP-0005-B04, OLP-0005-B08, OLP-0005-B10, OLP-0010-B05, OLP-0010-B11

**Choix :** police Unicode ; guillemets français ; groupe vide après le point d’exclamation actif

**Autre formulation envisagée :** accents et ligatures saisis par commandes TeX ; guillemets droits

**Motif :** Le passage au moteur XeTeX avait exposé un défaut de police huit bits : sœur perdait sa ligature et les guillemets étaient mal affichés. Une police Unicode conserve l’orthographe écrite. Le groupe vide empêche le mécanisme OLP des points d’exclamation de supprimer l’espace suivant.

**Confiance et limites :** Défauts constatés dans le PDF et le journal de compilation ; orthographe et espacement inspectés à nouveau après réparation.

**Question de révision :** Vérifier les autres langues et macros de ponctuation lors des chapitres suivants, sans extrapoler cette correction à des opérateurs mathématiques.

Passages de référence : L06.

## C27 — OLP-0012-B04, OLP-0012-B09

**Choix :** relation d’identité ; strictement inférieur/supérieur

**Autre formulation envisagée :** relation d’égalité ; inférieur/supérieur sans précision

**Motif :** Identité conserve la relation que chaque objet entretient avec lui-même ; strictement distingue les relations hors diagonale des relations comprenant la diagonale.

**Confiance et limites :** Définitions et exemples de H07 ainsi que les formules OLP concordent.

**Question de révision :** Employer identité systématiquement lorsqu’il s’agit d’une relation ensembliste, même si le prédicat est nommé égalité ?

Passages de référence : H07.

## C28 — OLP-0012-B09

**Choix :** définir localement I=Id_Nat avec une note éditoriale

**Autre formulation envisagée :** laisser I implicite ou remplacer I dans toutes les formules

**Motif :** La notation Id_A était définie, mais I apparaissait ensuite sans définition. L’ajout minimal permet de conserver K=L∪I et H=G∪I à l’identique.

**Confiance et limites :** Lecture directe du fichier et définition de la diagonale ; aucune autre signification de I n’est introduite.

**Question de révision :** Faut-il étendre cette notation I aux seules lignes de l’exemple ? La traduction la limite déjà par ici.

Passages de référence : H05, H07.

## C29 — OLP-0012-B08, OLP-0012-B10

**Choix :** relation sur un ensemble fixé ; aucun couple ou tout couple

**Autre formulation envisagée :** relation quelconque entre tous les objets sans domaine

**Motif :** Le domaine A fait partie de la définition et explique la relation vide et universelle ; il ne crée pas d’ensemble de toutes les relations ou de tous les ensembles.

**Confiance et limites :** Restriction au produit A² explicitement présente dans H04 et OLP.

**Question de révision :** Le mot universelle appelle-t-il un rappel du domaine dans les chapitres ultérieurs ?

Passages de référence : H04.

## C30 — OLP-0013-B03, OLP-0013-B07

**Choix :** identité métaphysique ; traiter certaines relations comme des ensembles

**Autre formulation envisagée :** égalité ontologique ; affirmer qu’elles sont littéralement ces ensembles

**Motif :** La prudence philosophique de l’original porte sur l’identification, sans remettre en cause l’usage mathématique de la représentation. Les modalisations et certaines sont conservées.

**Confiance et limites :** Sens contrôlé sur l’anglais ; le canon apporte un contraste relation/ensemble, pas une doctrine métaphysique indépendante.

**Question de révision :** Identité métaphysique est-il le meilleur choix pour identity fact dans ce passage précis ?

Passages de référence : L13.

## C31 — OLP-0013-B04, OLP-0013-B05

**Choix :** réductionnisme ensembliste ; exclure l’existence

**Autre formulation envisagée :** réduction aux ensembles ; nier comme simple opinion

**Motif :** Le premier choix conserve le nom de la position philosophique. Le second indique que l’axiomatique entraîne la non-existence, tout en gardant les deux branches du renvoi conditionnel.

**Confiance et limites :** Les deux codages et l’argument par l’ensemble universel sont conservés ; la référence Benacerraf1965 est celle de la source OLP.

**Question de révision :** Vérifier ultérieurement le lexique philosophique auprès d’un texte francophone spécialisé sans attribuer cette validation aux cours mathématiques actuels.

Passages de référence : L02, L06, L13.

## C32 — OLP-0013-B06

**Choix :** prédicat ; termes singuliers ; proposition

**Autre formulation envisagée :** relation-objet ; mots ; phrase

**Motif :** L’argument distingue ce qui sert à prédiquer de trois expressions qui désignent des objets. Termes singuliers conserve le niveau conceptuel de l’anglais, et proposition garde la question de ce qui est exprimé.

**Confiance et limites :** Fidélité au passage anglais certaine ; attestation française spécialisée de toute la série encore limitée.

**Question de révision :** Le contexte français préfère-t-il énoncé à proposition ici, sans confondre phrase et contenu ?

Passages de référence : L13.

## C33 — OLP-0013-B06

**Choix :** la tasse le pot à crayons la table

**Autre formulation envisagée :** la tasse pot à crayons la table

**Motif :** La suite doit rester volontairement dépourvue de prédication ; les trois groupes nominaux ne doivent pas devenir une phrase française assertive. Ajouter l’article au groupe central rend les trois désignations identifiables.

**Confiance et limites :** Structure de liste de noms conservée ; ce choix ne prétend pas être une citation française canonique.

**Question de révision :** La suite conserve-t-elle assez nettement le caractère volontairement absurde de l’original ?

Passages de référence : L13.

## C34 — OLP-0014-B05, OLP-0014-B08, OLP-0014-B09, OLP-0014-B12, OLP-0014-B13

**Choix :** réflexive, irréflexive, antisymétrique et asymétrique ; chaque fois que ; aucun couple

**Autre formulation envisagée :** non réflexive pour irréflexive ; non symétrique pour antisymétrique ; anti-symétrique avec trait d’union

**Motif :** Irréflexive nie chaque boucle, alors que non réflexive nie la propriété universelle. L’antisymétrie autorise la diagonale, l’asymétrie l’exclut. La graphie soudée est adoptée comme choix orthographique ; le cours consulté emploie un trait d’union.

**Confiance et limites :** Les quantificateurs sont contrôlés sur H06 et les définitions anglaises. La graphie est un choix éditorial distinct de la preuve.

**Question de révision :** La graphie soudée est-elle préférable pour assurer la cohérence avec asymétrique dans cette édition ?

Passages de référence : H06, H07.

## C35 — OLP-0014-B10, OLP-0016-B07, OLP-0016-B14, OLP-0016-B22, OLP-0016-B28

**Choix :** relation connexe ; connexité

**Autre formulation envisagée :** relation totale ; comparabilité des éléments distincts

**Motif :** Connexe conserve une propriété applicable aussi aux ordres stricts, où la diagonale est exclue. La condition x différent de y reste explicite. Employer totale avant de définir ordre total risquerait de confondre deux usages.

**Confiance et limites :** La définition OLP est préservée exactement ; le mot connexe n’est pas attesté par les passages primaires actuellement indexés. Le canon fournit ici le registre des définitions seulement.

**Question de révision :** Un lecteur francophone préférerait-il comparabilité à connexité pour éviter l’association avec la connexité des graphes ?

Passages de référence : H06, H13, H14.

## C36 — OLP-0014-B14

**Choix :** existence de relations ni réflexives ni irréflexives sous au moins deux éléments

**Autre formulation envisagée :** existence sur tout ensemble non vide

**Motif :** Sur un singleton, la relation vide est irréflexive et la diagonale est réflexive : il n’y a pas de troisième relation. La précision est donnée dans le texte avec une note explicite.

**Confiance et limites :** Contre-exemple exhaustif sur singleton et construction avec une seule boucle sur un domaine de deux éléments.

**Question de révision :** La note présente-t-elle suffisamment clairement le statut de correction de la source ?

Passages de référence : H06.

## C37 — OLP-0015-B07, OLP-0015-B08, OLP-0015-B09, OLP-0015-B11, OLP-0015-B12

**Choix :** blocs d’une partition ; ensemble quotient ; sens direct et réciproque

**Autre formulation envisagée :** plusieurs partitions ; quotient sans nom ensemble ; direction de gauche à droite

**Motif :** Les classes sont les blocs, non chacune une partition du domaine. Ensemble quotient nomme explicitement l’ensemble de classes. Les deux sens de la preuve restent séparés avec les usages de symétrie, transitivité et réflexivité.

**Confiance et limites :** Définition de classe et égalité ensembliste contrôlées ; la preuve couvre les mêmes dépendances que l’anglais.

**Question de révision :** Faut-il ajouter ultérieurement une preuve autonome de disjonction et recouvrement, plutôt que laisser leur déduction au lecteur comme ici ?

Passages de référence : H09, L01, L07.

## C38 — OLP-0015-B13, OLP-0015-B14

**Choix :** a et b naturels, n strictement positif ; reste de la division

**Autre formulation envisagée :** a, b et n tous strictement positifs comme dans la phrase source

**Motif :** Le quotient porte sur les naturels et comprend la classe de zéro ; la relation doit être définie pour zéro. Le module reste strictement positif, et le témoin multiplicateur reste un entier relatif.

**Confiance et limites :** Le domaine du quotient, la classe de zéro et la formule a-b=kn concordent après cette correction locale déclarée.

**Question de révision :** La précision sur le domaine est-elle assez proche de la première définition de la congruence ?

Passages de référence : H08, L04.

## C39 — OLP-0016-B05, OLP-0016-B06, OLP-0016-B07, OLP-0016-B08, OLP-0016-B13

**Choix :** préordre ; ordre partiel comprenant le cas total ; ordre strict avec asymétrie explicite

**Autre formulation envisagée :** ordre partiel signifiant non total ; supprimer asymétrique comme redondant

**Motif :** L’inclusion des ordres totaux dans les ordres partiels correspond à OLP et H13. L’asymétrie découle des deux autres propriétés mais reste énoncée comme dans la source.

**Confiance et limites :** Définitions primaires concordantes et absence de changement de convention.

**Question de révision :** Le maintien de la condition redondante aide-t-il la progression pédagogique avant la comparaison avec d’autres manuels ?

Passages de référence : H13, H14.

## C40 — OLP-0016-B09, OLP-0016-B11

**Choix :** de longueur inférieure ou égale à ; divisibilité

**Autre formulation envisagée :** pas plus long que ; division entière

**Motif :** La longueur est comparée sans identifier les mots. Divisibilité désigne l’existence d’un multiplicateur, pas l’opération de division euclidienne. La distinction entre domaines naturel et relatif reste décisive.

**Confiance et limites :** Les deux contre-exemples à l’antisymétrie et à la totalité sont conservés avec leurs domaines.

**Question de révision :** La locution longue sur la longueur reste-t-elle naturelle dans le cours sans un symbole lexical supplémentaire ?

Passages de référence : H13, H07.

## C41 — OLP-0016-B12, OLP-0018-B17

**Choix :** prolongement ; segment initial ; suites avec longueur ; non-linéarité si deux symboles distincts

**Autre formulation envisagée :** extension ; ordre non linéaire sur tout alphabet ; codage sans longueur

**Motif :** Prolongement rend le sens préfixe sans suggérer un surensemble. Un alphabet vide ou singleton donne un ordre linéaire. La longueur distingue les suites, comme la note de codage du premier chapitre le prévoit.

**Confiance et limites :** Contre-exemples aux petits alphabets explicites ; convention de suites compatible avec les arbres de mots.

**Question de révision :** Préfixe serait-il plus immédiat que segment initial pour les exemples informatiques, tout en conservant le terme ensembliste ?

Passages de référence : L14, H02.

## C42 — OLP-0016-B16, OLP-0016-B17, OLP-0019-B15, OLP-0019-B16, OLP-0019-B17

**Choix :** clôture réflexive ; clôture transitive ; note sur deux sens locaux de R+

**Autre formulation envisagée :** fermeture ; renommer uniformément R+ dans la source

**Motif :** Clôture suit le cours de logique consulté. OLP utilise R+ pour deux opérations différentes ; une note rend cette surcharge visible en gardant chaque formule originale.

**Confiance et limites :** Les deux définitions et leur domaine de validité sont comparées directement.

**Question de révision :** Une édition ultérieure devrait-elle harmoniser ce symbole à l’échelle du corpus plutôt que garder la surcharge signalée ?

Passages de référence : H11, H14.

## C43 — OLP-0017-B04, OLP-0017-B05, OLP-0017-B06, OLP-0017-B07

**Choix :** graphe orienté ; nœuds ou sommets ; arêtes ; se représente par un diagramme

**Autre formulation envisagée :** graphe dirigé ; vertices ; arcs exclusivement ; identifier le graphe au dessin

**Motif :** Le canon atteste les termes retenus, même arête pour le cas orienté. Se représente distingue l’objet de son dessin conformément à la définition par couple. La flèche va du premier sommet au second ; le sommet isolé demeure essentiel.

**Confiance et limites :** Texte et schémas français consultés ; deux diagrammes OLP inchangés.

**Question de révision :** Ajouter arcs comme synonyme des arêtes orientées apporterait-il une aide utile sans surcharger l’introduction ?

Passages de référence : G01, G02, G03.

## C44 — OLP-0018-B04, OLP-0018-B07, OLP-0018-B08, OLP-0018-B09

**Choix :** racine en bas ; arbre enraciné non vide ; bien ordonné ; plus petit élément

**Autre formulation envisagée :** arbre binaire récursif pouvant être vide ; élément minimal

**Motif :** Le vocabulaire du cours informatique est utile, mais sa convention d’arbre n’est pas celle d’OLP. Plus petit exige d’être inférieur à tous les éléments ; minimal serait trop faible pour un ordre partiel.

**Confiance et limites :** Sens du bon ordre vérifié dans Lyon ; représentation OLP et condition de racine préservées.

**Question de révision :** La transition du dessin fini à l’arbre ensembliste plus général mérite-t-elle un exemple transﬁni dans une future révision ?

Passages de référence : T01, T02, L14.

## C45 — OLP-0018-B10, OLP-0018-B11, OLP-0018-B12, OLP-0018-B13, OLP-0018-B14

**Choix :** successeur au sens immédiat ; enfant ; parent ; au plus un prédécesseur ; à branchement fini

**Autre formulation envisagée :** successeur quelconque ; descendant ; exactement un prédécesseur

**Motif :** La définition exclut tout nœud intermédiaire. Au plus un est indispensable pour les arbres infinis où un nœud limite peut ne pas avoir de prédécesseur immédiat. Le branchement compte ces seuls successeurs.

**Confiance et limites :** Quantificateurs et démonstration inchangés ; le canon informatique atteste parent et fils, enfant est le choix éditorial plus neutre.

**Question de révision :** Faut-il annoncer explicitement immédiat à chaque reprise du mot successeur ou sa définition suffit-elle ?

Passages de référence : T01, T02, L14.

## C46 — OLP-0018-B15

**Choix :** chaîne maximale ; domaine A dans z appartenant à A privé de B

**Autre formulation envisagée :** chaîne maximum ; conserver X non défini

**Motif :** Maximale signifie qu’aucun autre nœud ne peut être ajouté, non qu’elle ait la plus grande cardinalité. A est le domaine déclaré de l’arbre ; X est une coquille signalée en note.

**Confiance et limites :** La condition explicite de non-comparabilité contrôle la maximalité ; correction de variable vérifiable dans la source.

**Question de révision :** La phrase française conserve-t-elle assez clairement la portée existentielle de u pour chaque z extérieur ?

Passages de référence : L14, T01.

## C47 — OLP-0018-B17

**Choix :** partie non vide stable par passage aux segments initiaux

**Autre formulation envisagée :** partie fermée sous prolongement sans direction ni non-vacuité

**Motif :** La fermeture est vers les préfixes, non vers tous les prolongements. Non vide assure la racine vide selon la définition précédente. La précision ajoutée est signalée.

**Confiance et limites :** Le contre-exemple de la partie vide est immédiat ; toute partie non vide fermée vers les préfixes contient la suite vide.

**Question de révision :** La locution stable par passage aux segments initiaux est-elle préférable à fermée vers le bas pour ce lectorat ?

Passages de référence : L14, T01.

## C48 — OLP-0018-B18, OLP-0018-B19

**Choix :** lemme de König ; lemme faible de König ; branche infinie

**Autre formulation envisagée :** lemme de Koenig ; faible lemme ; chemin infini

**Motif :** Le nom conserve le codage diacritique TeX original. Branche renvoie à la chaîne maximale déjà définie ; faible qualifie la version du lemme sur les arbres binaires. T03 ne fournit que le registre de preuve, pas une validation française de ce théorème.

**Confiance et limites :** Fidélité à l’énoncé OLP ; terminologie spécialisée encore sans passage primaire français dédié dans cet index.

**Question de révision :** La dénomination lemme faible de König doit-elle être préférée à forme faible du lemme de König dans le chapitre de calculabilité ?

Passages de référence : T03.

## C49 — OLP-0019-B06, OLP-0019-B07, OLP-0019-B11, OLP-0019-B12, OLP-0019-B16

**Choix :** relation inverse ; produit relatif suivant R puis S ; par récurrence

**Autre formulation envisagée :** relation réciproque ; composition R après S ; par récursion sans précision

**Motif :** L’inversion échange les coordonnées. Le produit R|S suit R puis S, comme S composé avec R dans H10. La notation OLP reste intacte ; la définition des puissances conserve son point de départ 1.

**Confiance et limites :** Formules directement comparées au témoin intermédiaire de H10 et aux coordonnées de H15.

**Question de révision :** Le terme produit relatif mérite-t-il un renvoi explicite au mot composition avant le chapitre sur les fonctions ?

Passages de référence : H10, H15.

## C50 — OLP-0019-B08, OLP-0019-B09, OLP-0019-B13, OLP-0019-B14

**Choix :** restriction à A par intersection avec A² ; image de A par R

**Autre formulation envisagée :** restriction du premier argument seul ; application de R à A

**Motif :** La restriction porte sur les deux coordonnées selon la formule OLP. Image évite la confusion avec une application comme objet fonctionnel et traduit le résultat ensembliste de l’opération.

**Confiance et limites :** Les formules et leurs exemples sont conservés ; H15 atteste image dans le cas fonctionnel seulement.

**Question de révision :** Faut-il employer image directe dans les reprises où une image réciproque apparaît aussi ?

Passages de référence : H01, H04, H15.

## C51 — OLP-0020-B03, OLP-0021-B03, OLP-0021-B04, OLP-0021-B07

**Choix :** fonction pour une correspondance partout définie sur A

**Autre formulation envisagée :** application pour le cas total ; fonction pouvant être partielle sans précision

**Motif :** OLP réserve la fonction partielle à une section ultérieure. Fonction garde la continuité du manuel ; toute entrée a explicitement une unique valeur. Le cours Habermehl permet un domaine effectif plus petit : cette convention est documentée sans être importée.

**Confiance et limites :** La convention OLP est explicite et la notation totale est confirmée par Lyon ; les deux canons ne sont pas artificiellement présentés comme identiques.

**Question de révision :** Faut-il annoncer la convention totale dès la définition plutôt que seulement à l’introduction des fonctions partielles ?

Passages de référence : L15, H16.

## C52 — OLP-0021-B08, OLP-0021-B09, OLP-0021-B10, OLP-0021-B11, OLP-0021-B12, OLP-0021-B16

**Choix :** domaine ; ensemble d’arrivée ; image ; argument ; valeur

**Autre formulation envisagée :** ensemble de départ ; codomaine ; ensemble des valeurs ; entrée/sortie partout

**Motif :** Domaine reste compatible avec dom f dans les chapitres suivants. Ensemble d’arrivée distingue B de l’image réellement atteinte. Image suit les deux passages consultés ; ensemble d’arrivée est un choix lexical éditorial, non une citation de ces pages.

**Confiance et limites :** Sens contrôlé par les formules et l’exemple du successeur ; attestation du terme précis ensemble d’arrivée non acquise dans l’index actuel.

**Question de révision :** Faut-il donner codomaine comme synonyme pour faciliter les renvois entre manuels francophones ?

Passages de référence : L15, H16.

## C53 — OLP-0021-B05, OLP-0021-B06, OLP-0021-B15, OLP-0021-B18

**Choix :** boîte noire ; correspondance définie par ses valeurs ; même domaine et ensemble d’arrivée

**Autre formulation envisagée :** algorithme ; supprimer la condition sur l’ensemble d’arrivée

**Motif :** La fonction abstraite n’est pas la méthode qui calcule ses valeurs. L’extensionnalité porte sur des fonctions de mêmes domaine et ensemble d’arrivée, condition conservée expressément. Les différents calculs peuvent donc définir la même fonction.

**Confiance et limites :** Égalités et condition finale de l’anglais conservées ; le graphe ensembliste de Lyon ne doit pas effacer le typage choisi par OLP.

**Question de révision :** L’identification ultérieure à un graphe devra-t-elle rappeler le rôle séparé de l’ensemble d’arrivée ?

Passages de référence : L15, H16, L01.

## C54 — OLP-0021-B13

**Choix :** racine carrée positive ou nulle

**Autre formulation envisagée :** racine strictement positive ; positive sans précision

**Motif :** Le domaine naturel contient zéro. L’explicitation évite d’exclure cette entrée et est signalée comme précision éditoriale, avec la formule originale inchangée.

**Confiance et limites :** Vérification directe de la valeur en zéro ; aucune nouvelle opération introduite.

**Question de révision :** La note doit-elle préciser que positive en français peut déjà inclure zéro, contrairement à positive dans l’anglais mathématique usuel ?

Passages de référence : L15, H16.

## C55 — OLP-0021-B17

**Choix :** nommer l’entrée x dans toute la phrase

**Autre formulation envisagée :** laisser le passage de n à x implicite

**Motif :** L’exemple décrit une seule entrée. La correction de lettre est signalée et les équations définissant g restent inchangées.

**Confiance et limites :** Coquille textuelle directement visible ; aucun changement de variable liée dans une formule.

**Question de révision :** Le signalement en note est-il proportionné à cette correction typographique mineure ?

Passages de référence : H16.

## C56 — OLP-0022-B05, OLP-0022-B07, OLP-0022-B08, OLP-0022-B09, OLP-0022-B10, OLP-0022-B11, OLP-0022-B12

**Choix :** au moins un pour la surjectivité ; au plus un pour l’injectivité

**Autre formulation envisagée :** un unique antécédent dans les deux définitions

**Motif :** La surjectivité exige l’existence, l’injectivité l’unicité éventuelle. La valeur unique de toute fonction ne doit pas être confondue avec l’unicité de l’antécédent. Restreindre l’ensemble d’arrivée à l’image produit une autre fonction surjective.

**Confiance et limites :** Définitions anglaises et slide19 concordantes, ainsi que les deux critères de preuve.

**Question de révision :** Le mot antécédent mérite-t-il d’être introduit dès ces définitions ou seulement dans la section sur les inverses ?

Passages de référence : H17, H16.

## C57 — OLP-0022-B06, OLP-0022-B10, OLP-0022-B13, OLP-0022-B14, OLP-0022-B15, OLP-0022-B16, OLP-0022-B17, OLP-0022-B18

**Choix :** injective/surjective/bijective au féminin, pluriel explicite ; une injection/surjection/bijection

**Autre formulation envisagée :** formes masculines par défaut ; laisser les macros anglaises sans adaptation

**Motif :** Les adjectifs s’accordent avec fonction, et les pronoms pluriels renvoient aux fonctions. Les tokens français possèdent désormais formes singulière/plurielle et articles féminins pour les noms, à contrôler lors du futur rendu du chapitre.

**Confiance et limites :** Accord grammatical contrôlé sur les phrases et le cours français ; rendu des nouvelles macros encore à vérifier dans le lecteur des fonctions.

**Question de révision :** Les occurrences futures où le sujet est un opérateur masculin devront-elles utiliser une variante de token distincte ?

Passages de référence : H17.

## C58 — OLP-0022-B17, OLP-0022-B18

**Choix :** correspondance biunivoque ; bijection de A dans B ou entre A et B

**Autre formulation envisagée :** correspondance un-à-un ; réserver dans aux seules injections

**Motif :** Biunivoque conserve l’appariement unique des deux côtés sans calquer one-to-one. De A dans B exprime les ensembles associés ; le mot bijection porte déjà la surjectivité. La variante entre rend la symétrie de l’appariement.

**Confiance et limites :** Sens fixé par les deux propriétés ; biunivoque est une décision lexicale propre, non attribuée comme citation à H17.

**Question de révision :** De A sur B serait-il plus idiomatique ici tout en gardant une terminologie homogène avec les autres applications ?

Passages de référence : H17.

## C59 — OLP-0011-B03

**Choix :** Relations

**Autre formulation envisagée :** Théorie des relations

**Motif :** Le titre français coïncide avec l’anglais; ajouter théorie rétrécirait inutilement le titre général qui gouverne huit imports.

**Confiance et limites :** intitulé attesté par H04 et contenu concordant.

**Question de révision :** Le titre commun conserve-t-il une hiérarchie claire avec les sections ?

Passages de référence : H04.

## C60 — OLP-0012-B03

**Choix :** Les relations comme ensembles

**Autre formulation envisagée :** Représentation ensembliste des relations

**Motif :** Comme conserve le statut de présentation qui sera discuté philosophiquement; représentation anticiperait une réponse à cette discussion.

**Confiance et limites :** le titre prépare correctement la définition et sa réserve ultérieure.

**Question de révision :** Le titre laisse-t-il assez ouverte la distinction entre identification et représentation ?

Passages de référence : H04.

## C61 — OLP-0012-B05

**Choix :** Rappelons pour cela ; étant donnés ; dans ce cas ; tels que ; En particulier

**Autre formulation envisagée :** paire ordonnée; pour lesquels; remplacer les deux rappels par une seule définition

**Motif :** L02/L03 contrôlent couple et produit cartésien. Deux rappels ordonnés sont maintenus. Dans ce cas rattache deux éléments à a≠b. Tels que coordonne les deux appartenances; en particulier spécialise B=A sans changer tous.

**Confiance et limites :** dépendances et domaine sont explicites; couple est un choix éditorial face à paire ordonnée dans Lyon.

**Question de révision :** Dans ce cas renvoie-t-il sans ambiguïté à a≠b malgré la phrase intermédiaire ?

Passages de référence : L02, L03.

## C62 — OLP-0012-B06

**Choix :** Considérons maintenant ; tels que ; le fait que ; sans perdre d'information

**Autre formulation envisagée :** représente exactement la relation; n est inférieur à m

**Motif :** Les impératifs conduisent de l’exemple à sa construction. Strictement conserve <; le fait que et appartenance mettent en parallèle une assertion et son codage. La biconditionnelle et est emphatique maintiennent l’identification dont la section suivante discutera.

**Confiance et limites :** H05/H07 et les deux formules concordent; aucune identité métaphysique n’est ici ajoutée.

**Question de révision :** Est emphatique risque-t-il d’être lu comme conclusion métaphysique avant la section suivante ?

Passages de référence : H05, H07.

## C63 — OLP-0012-B07

**Choix :** pour toute relation ; Réciproquement ; celle que ; Cela justifie

**Autre formulation envisagée :** Inversement, tout sous-ensemble définit une relation

**Motif :** Réciproquement porte sur les deux constructions, non sur l’inversion des couples. Entiers naturels explicite le domaine constant N; celle que reprend relation, et si et seulement si fixe exactement ses instances.

**Confiance et limites :** H04/H05 donnent la même correspondance extensionnelle.

**Question de révision :** Une phrase plus courte garderait-elle aussi bien la distinction entre relation et relation inverse ?

Passages de référence : H04, H05.

## C64 — OLP-0012-B11

**Choix :** Énumérer les

**Autre formulation envisagée :** Donnez la liste des

**Motif :** L’infinitif de consigne est attesté par Montrer dans l’exercice1.1.1 de Lyon, passage L02 relu lors de cette correction. H04 et L05 soutiennent relation et ensemble des parties. Les éléments demandés sont des couples de parties, non les trois lettres ni les seules parties.

**Confiance et limites :** objet de l’exercice clair ; L02 soutient le registre infinitif, sans attester le verbe Énumérer dans cette construction.

**Question de révision :** Faut-il uniformiser ultérieurement les consignes à l’impératif dans toute l’édition ?

Passages de référence : H04, L05, L02.

## C65 — OLP-0013-B02

**Choix :** Réflexions philosophiques

**Autre formulation envisagée :** Remarques philosophiques

**Motif :** Réflexions conserve la démarche interrogative et les trois objections, sans les présenter comme de simples notes marginales. P05/P06 attestent le registre philosophique, pas ce titre exact.

**Confiance et limites :** fonction argumentative directement observable.

**Question de révision :** Réflexions convient-il mieux que remarques pour une section qui conclut provisoirement ?

Passages de référence : L13, P05, P06.

## C66 — OLP-0014-B03

**Choix :** Propriétés particulières des relations

**Autre formulation envisagée :** Propriétés remarquables des relations

**Motif :** Particulières annonce les propriétés servant à classer les relations; remarquables ajouterait une appréciation. H06/H07 attestent la famille de propriétés et non une formule de titre imposée.

**Confiance et limites :** sens de special conservé sans suggérer des exceptions.

**Question de révision :** Particulières pourrait-il être pris à tort au sens de propriétés non générales ?

Passages de référence : H06, H07.

## C67 — OLP-0014-B04

**Choix :** si fréquents qu’on ; leurs domaines ; Pour préciser ; Certaines combinaisons

**Autre formulation envisagée :** se ressemblent; propriétés spéciales; ordres et équivalences seuls en apposition

**Motif :** La consécutive explique les dénominations. Domaines respectifs distribue N et P(A). Le double ce qui rapproche/ce qui distingue conserve les deux buts; types de relations répare l’apposition source qui assimilait propriétés et ordres.

**Confiance et limites :** H06/H07 et les exemples fixent les référents.

**Question de révision :** L’explicitation types de relations rend-elle visible le passage de propriétés à leurs combinaisons ?

Passages de référence : H06, H07.

## C68 — OLP-0014-B06

**Choix :** si et seulement si, ; chaque fois que ; on a aussi

**Autre formulation envisagée :** si Rxy et Ryz impliquent Rxz pour tous x,y,z

**Motif :** La biconditionnelle définit la propriété entière; chaque fois que universalise les triples et garde la conjonction des prémisses. Aussi marque la conclusion supplémentaire, pas une nouvelle prémisse.

**Confiance et limites :** traduction directe de la définition H06 et de whenever.

**Question de révision :** Une quantification explicite sur x,y,z améliorerait-elle la lecture sans alourdir la série ?

Passages de référence : H06, H07.

## C69 — OLP-0014-B07

**Choix :** si et seulement si, ; chaque fois que ; on a aussi

**Autre formulation envisagée :** lorsque Rxy, Ryx; Rxy équivaut à Ryx

**Motif :** Chaque fois que porte sur tous les couples. L’implication interne est conservée sous la définition biconditionnelle; substituer directement une équivalence est mathématiquement possible mais modifierait l’énoncé choisi par OLP.

**Confiance et limites :** H06 confirme la direction et son domaine.

**Question de révision :** L’emboîtement de si et seulement si et chaque fois que reste-t-il immédiatement lisible ?

Passages de référence : H06, H07.

## C70 — OLP-0014-B11

**Choix :** Donnez des exemples ; mais non transitives ; mais non réflexives ; N’utilisez pas

**Autre formulation envisagée :** qui ne sont pas transitives; ne sont pas toutes réflexives

**Motif :** Les quatre combinaisons conservent leurs conjonctions et leurs seules négations. Non réflexives n’est pas irréflexives. L’interdiction finale vise les domaines nombres/ensembles des exemples, non le codage ensembliste de toute relation.

**Confiance et limites :** H06/H07 règlent les propriétés; l’interprétation pédagogique évite une impossibilité littérale.

**Question de révision :** Portant sur fait-il assez comprendre que l’exclusion concerne les objets des exemples ?

Passages de référence : H06, H07.

## C71 — OLP-0015-B04

**Choix :** Relations d’équivalence

**Autre formulation envisagée :** Équivalences

**Motif :** Le nom développé évite de confondre la relation sur un domaine avec une équivalence entre propositions, tout en suivant H08.

**Confiance et limites :** désignation standard et exacte.

**Question de révision :** L’abréviation équivalence sera-t-elle utile après cette définition seulement ?

Passages de référence : H08.

## C72 — OLP-0015-B05

**Choix :** La relation d’identité ; ces trois propriétés ; très courantes

**Autre formulation envisagée :** chacune de ces propriétés; fréquentes

**Motif :** Ces trois reprend conjointement réflexive, symétrique, transitive; la fréquence porte sur les relations réunissant les trois. L’identité fournit l’exemple initial sur tout ensemble, y compris vide.

**Confiance et limites :** aucune qualification ni propriété perdue.

**Question de révision :** L’anaphore ces trois pourrait-elle être lue distributivement hors de cette phrase ?

Passages de référence : H08.

## C73 — OLP-0015-B06

**Choix :** est
appelée une ; Deux ; sont dits

**Autre formulation envisagée :** une équivalence; x est équivalent à y relativement à R

**Motif :** La définition conserve la conjonction des trois propriétés de H08. Deux introduit deux variables sans imposer leur distinction. R-équivalents garde le paramètre de la relation et s’accorde avec éléments : cette formulation suit OLP. H09, relu et ajouté, soutient seulement le rôle de R dans les classes indexées.

**Confiance et limites :** H08 soutient le sens ; H09 soutient le paramètre relationnel ; le composé R-équivalents est contrôlé directement contre OLP.

**Question de révision :** Un rappel que x et y peuvent coïncider serait-il superflu ici ?

Passages de référence : H08, H09.

## C74 — OLP-0015-B10

**Choix :** Si ; alors ; seulement si

**Autre formulation envisagée :** Rxy équivaut à l’égalité des classes, lorsque R est une équivalence

**Motif :** L’hypothèse sur R encadre toute la biconditionnelle. Alors ne transforme pas si et seulement si en simple implication; les classes appartiennent au même R.

**Confiance et limites :** énoncé et preuve des deux sens concordent avec H08/H09.

**Question de révision :** L’hypothèse implicite x,y∈A doit-elle être explicitée lors d’une révision source ?

Passages de référence : H08, H09.

## C75 — OLP-0016-B03

**Choix :** Ordres

**Autre formulation envisagée :** Relations d’ordre

**Motif :** Ordres est le nom mathématique des objets définis; relations d’ordre conviendrait mais répéterait le titre du chapitre.

**Confiance et limites :** H13 emploie les deux formes.

**Question de révision :** Le titre court reste-t-il clair dans la table des matières autonome ?

Passages de référence : H13.

## C76 — OLP-0016-B04

**Choix :** sous un certain ; Certaines exigent ; d’autres non ; les classer

**Autre formulation envisagée :** à un certain égard; établir une taxonomie

**Motif :** Sous un certain rapport restreint le critère de comparaison. Deux objets quelconques conserve any two. Certaines/d’autres distingue comparabilité et présence de la diagonale; classer rend taxonomy sans technicité inutile.

**Confiance et limites :** H13/H14 soutiennent la classification, exemples et oppositions conservés.

**Question de révision :** Comprennent l’identité évoque-t-il clairement la diagonale, plutôt qu’une théorie de l’identité ?

Passages de référence : H13, H14.

## C77 — OLP-0016-B10

**Choix :** pas en général ; si ; on constate

**Autre formulation envisagée :** n’est jamais linéaire; car les singletons sont incomparables

**Motif :** Pas en général permet les familles de parties linéairement ordonnées. La condition a≠b rend les deux singletons incomparables. Les trois assertions, y compris leur inégalité explicite, restent présentes.

**Confiance et limites :** contre-exemple exact et H13/H07 concordants.

**Question de révision :** La triple constatation mérite-t-elle d’être conservée malgré sa redondance logique ?

Passages de référence : H13, H07.

## C78 — OLP-0016-B15

**Choix :** correspondant à

**Autre formulation envisagée :** associé à; obtenu par clôture réflexive de

**Motif :** Correspondant reste neutre avant l’explication par ajout de diagonale. L’énoncé affirme un ordre partiel pour l’inclusion, sans exclure la linéarité sur une famille particulière ; sur {∅,{a}}, l’inclusion est aussi linéaire.

**Confiance et limites :** implication source préservée et contre-exemple à une lecture nécessairement non linéaire vérifié ; H14 ne prouve pas cette non-linéarité.

**Question de révision :** Le mécanisme de correspondance devient-il clair dès le paragraphe suivant ?

Passages de référence : H14.

## C79 — OLP-0016-B18

**Choix :** Supposons que ; Posons ; Il faut montrer

**Autre formulation envisagée :** Soit R un ordre strict; il suffit de vérifier

**Motif :** Supposons introduit les hypothèses, posons la nouvelle notation, il faut montrer les trois obligations. Les accords féminins suivent relation R malgré ordre masculin; asymétrique dans les hypothèses devient antisymétrique dans le but.

**Confiance et limites :** les trois rôles sont séparés et la hiérarchie H13/H14 respectée.

**Question de révision :** Le changement d’accord entre ordre et R appelle-t-il une répétition du mot relation ?

Passages de référence : H13, H14.

## C80 — OLP-0016-B19

**Choix :** manifestement réflexive ; puisque ; pour tout

**Autre formulation envisagée :** est réflexive : pour tout x...

**Motif :** Puisque donne réellement la justification par inclusion de la diagonale; manifestement n’en tient pas lieu. Pour tout porte sur A et non sur un témoin arbitraire choisi une fois.

**Confiance et limites :** la preuve développe exactement H06.

**Question de révision :** Supprimer manifestement rendrait-il le ton plus accueillant sans affaiblir l’argument ?

Passages de référence : H06.

## C81 — OLP-0016-B20

**Choix :** par l’absurde ; on a nécessairement ; De même ; Cela contredit

**Autre formulation envisagée :** supposons x≠y et les deux sens; utiliser directement l’asymétrie

**Motif :** La contradiction suppose les deux sens dans R+ et x≠y. L’exclusion de la diagonale force chaque couple dans R. De même répète ce passage pour le couple inversé; la contradiction porte sur l’asymétrie de R.

**Confiance et limites :** L06/H06 et chaque dépendance de la preuve concordent.

**Question de révision :** L’étape De même nécessite-t-elle une répétition de l’exclusion du couple inverse de la diagonale ?

Passages de référence : L06, H06.

## C82 — OLP-0016-B21

**Choix :** à la fois ; Sinon, ; Dans le premier cas ; Le second cas ; Dans tous les cas

**Autre formulation envisagée :** Paraphrase viable : Sinon, au moins l’un des deux couples appartient à la diagonale ; la substitution dans l’une des hypothèses donne alors R+ xz. Contrôles sémantiques rejetés : sinon exactement un couple est diagonal; réutiliser R plutôt que R+

**Motif :** À la fois conserve le premier cas conjonctif. Sinon laisse au moins un couple diagonal, éventuellement les deux. Les substitutions x=y et y=z utilisent les hypothèses R+; tous les cas inclut aussi le premier cas où R suffit.

**Confiance et limites :** aucune disjonction exclusive introduite, H06 confirme transitivité.

**Question de révision :** Dans tous les cas rend-il clairement les trois branches du raisonnement ?

Passages de référence : H06, H03.

## C83 — OLP-0016-B23

**Choix :** Si ; De plus

**Autre formulation envisagée :** Tout ordre partiel privé de sa diagonale devient strict, et linéaire s’il l’était

**Motif :** Deux implications imbriquées sont conservées; la linéarité de R est une hypothèse supplémentaire, pas une conséquence de sa seule partialité. La notation R− est inchangée.

**Confiance et limites :** H13/H14 et la soustraction de diagonale concordent.

**Question de révision :** L’omission de alors dans la seconde phrase laisse-t-elle une portée conditionnelle limpide ?

Passages de référence : H13, H14.

## C84 — OLP-0016-B24

**Choix :** La démonstration est laissée en exercice

**Autre formulation envisagée :** À démontrer; preuve laissée au lecteur

**Motif :** L’article défini renvoie à la proposition immédiatement précédente. La phrase est une formulation éditoriale de l’instruction OLP qui laisse la démonstration en exercice. L02 fournit seulement un exemple de consigne de preuve ; il n’atteste pas cette locution. H03 est retiré, car il ne porte pas sur une consigne.

**Confiance et limites :** anaphore locale et instruction source vérifiées ; aucune attestation exacte de la locution revendiquée.

**Question de révision :** La répétition avec l’exercice suivant doit-elle rester pour conserver la structure source ?

Passages de référence : L02.

## C85 — OLP-0016-B25

**Choix :** Démontrez la

**Autre formulation envisagée :** Donnez une preuve de la

**Motif :** L’impératif Démontrez est un choix éditorial pour demander une démonstration complète. L02 atteste une consigne de preuve à l’infinitif, non cet impératif exact. La précède le nom féminin proposition produit par le renvoi. La vérification du rendu relève du reçu PDF, distinct du témoin lexical.

**Confiance et limites :** objet et genre du renvoi vérifiés ; le registre impératif est éditorial, et la lecture du PDF est une vérification séparée.

**Question de révision :** L’impératif doit-il devenir la forme uniforme des futures consignes ?

Passages de référence : L02.

## C86 — OLP-0016-B26

**Choix :** résultat élémentaire ; analogue à l’extensionnalité

**Autre formulation envisagée :** résultat simple; propriété d’extensionnalité

**Motif :** Élémentaire indique la difficulté locale sans déclarer la lecture évidente. Analogue distingue la propriété de l’axiome ensembliste L01. Strict et linéaire sont les hypothèses conservées de l’énoncé source ; leur nécessité logique n’est pas affirmée.

**Confiance et limites :** fidélité de l’analogie et des hypothèses suffisantes ; aucune nécessité déduite des témoins.

**Question de révision :** Analogue annonce-t-il suffisamment la comparaison des segments initiaux ?

Passages de référence : L01, H14.

## C87 — OLP-0016-B27

**Choix :** Si ; alors

**Autre formulation envisagée :** Pour tout ordre linéaire strict sur A, ...

**Motif :** L’hypothèse contient strict et linéaire; alors introduit la formule universelle entière. Aucun changement de l’ordre ∀a,b puis ∀x ni de la biconditionnelle interne.

**Confiance et limites :** formule et portée intactes, H14 fixe le type d’ordre.

**Question de révision :** Une paraphrase des segments initiaux aiderait-elle sans doubler la formule ?

Passages de référence : H14.

## C88 — OLP-0017-B03

**Choix :** Graphes

**Autre formulation envisagée :** Graphes orientés

**Motif :** Le titre général convient à l’introduction qui compare plusieurs conventions avant la définition orientée. G01 atteste graphe, pas graphique.

**Confiance et limites :** progression de la section préservée.

**Question de révision :** Le titre général rend-il assez visible que la définition retenue est orientée ?

Passages de référence : G01.

## C89 — OLP-0017-B08

**Choix :** Considérez ; comme un graphe ; dessinez le diagramme correspondant

**Autre formulation envisagée :** Dessinez le graphe de ≤

**Motif :** Les deux actions distinguent l’objet relationnel et son dessin. Inférieur ou égal garde les boucles réflexives, et le domaine fini garde le sommet4; G02 donne le sens des flèches.

**Confiance et limites :** domaine et relation fixent exactement le diagramme demandé.

**Question de révision :** La consigne doit-elle rappeler explicitement les boucles ou laisser cette déduction au lecteur ?

Passages de référence : G02, G03.

## C90 — OLP-0018-B03

**Choix :** Arbres

**Autre formulation envisagée :** Arbres ordonnés

**Motif :** Arbres garde la dénomination source; le texte fournit aussitôt la convention par ordre partiel. Ajouter ordonnés évoquerait à tort des arbres planaires à ordre des enfants.

**Confiance et limites :** T01 illustre justement une autre convention qu’il faut distinguer.

**Question de révision :** Le contraste entre ordre sur les nœuds et ordre des enfants est-il suffisamment annoncé ?

Passages de référence : T01.

## C91 — OLP-0018-B05

**Choix :** notion ensembliste ; étroitement liée ; représentation d’un arbre fini

**Autre formulation envisagée :** identique à la notion graphique; dessin d’arbre

**Motif :** Liée n’affirme pas identité de définitions. Représentation sépare l’objet du dessin; fini fixe la portée de l’exemple et du parent unique qui suit. T02 atteste le lien parents/arêtes.

**Confiance et limites :** distinctions conservées, portée locale défendable.

**Question de révision :** Une précision Dans l’arbre représenté au paragraphe suivant serait-elle pédagogiquement utile ?

Passages de référence : T02.

## C92 — OLP-0018-B16

**Choix :** suites finies ; Comme on peut toujours prolonger ; exactement ; Sa racine

**Autre formulation envisagée :** chaînes binaires; deux descendants; l’arbre de toutes les suites infinies

**Motif :** Les nœuds sont des suites finies, l’ensemble des nœuds est infini. Toujours et chaque conservent la possibilité de prolonger tout mot; exactement deux vise les successeurs immédiats s0,s1. La suite vide est la racine.

**Confiance et limites :** P04 confirme le codage par mots/préfixes, OLP fixe successeur.

**Question de révision :** L’alternance mot/suite pourrait-elle gêner sans rappel de leur identification déjà donnée ?

Passages de référence : T01, H02, P04.

## C93 — OLP-0019-B03

**Choix :** Opérations sur les relations

**Autre formulation envisagée :** Calcul des relations

**Motif :** Opérations annonce plusieurs constructions définies successivement; calcul suggérerait un système algébrique développé qui n’est pas exposé ici. H10/H11 soutiennent composition et clôtures.

**Confiance et limites :** portée du titre conforme à la section.

**Question de révision :** Faut-il réserver calcul des relations à un traitement ultérieur plus systématique ?

Passages de référence : H10, H11.

## C94 — OLP-0019-B04

**Choix :** modifier ou de combiner ; prises comme ensembles de couples ; De même ; différence ensembliste

**Autre formulation envisagée :** union; différence relative

**Motif :** Modifier et combiner couvrent les opérations unaires et binaires. Prises comme rappelle le statut ensembliste des relations. H01 soutient les opérations union et différence, sans attester ici réunion ni la locution différence ensembliste ; ces mots suivent le choix éditorial du chapitre précédent. De même relie les propositions sans identifier leurs opérations.

**Confiance et limites :** opérations et renvois contrôlés ; soutien conceptuel de H01 distingué des formulations éditoriales.

**Question de révision :** Différence ensembliste est-il plus clair que différence relative pour ce lectorat ?

Passages de référence : H01.

## C95 — OLP-0019-B05

**Choix :** Soient ; un ensemble quelconque

**Autre formulation envisagée :** Étant données deux relations R,S et un ensemble A

**Motif :** Soient introduit simultanément les paramètres; quelconque ne suppose ni A non vide ni un domaine commun des deux relations, ce que les définitions ne demandent pas.

**Confiance et limites :** H04 et les formules suivantes ne donnent aucune restriction omise.

**Question de révision :** L’absence de domaines explicites pour R,S reste-t-elle claire dans ce calcul ensembliste ?

Passages de référence : H04.

## C96 — OLP-0019-B10

**Choix :** relation de succession ; Ainsi,

**Autre formulation envisagée :** relation successeur; c’est-à-dire ... de sorte que ...

**Motif :** Soit fixe S sur Z; les deux points présentent sa définition. Ainsi traduit la conséquence notationnelle Sxy ssi x+1=y. Le domaine entier conserve l’existence du prédécesseur employé ensuite.

**Confiance et limites :** H05/L04 et la formule concordent.

**Question de révision :** Succession distingue-t-il suffisamment une relation binaire de la fonction successeur ?

Passages de référence : H05, L04.

## C97 — OLP-0019-B18

**Choix :** Reprenons ; pour un certain ; Autrement dit

**Autre formulation envisagée :** pour tout n≥1; strictement avant; remplacer les biconditionnelles par si

**Motif :** Reprenons rattache l’exemple à S sur Z. Les puissances2,3 puis le témoin existentiel positif conservent la progression; autrement dit identifie S+ à <, tandis que S* ajoute l’égalité.

**Confiance et limites :** H10/H11 et l’arithmétique fixent les deux clôtures.

**Question de révision :** Le caractère entier du témoin n reste-t-il assez clair par la définition précédente des puissances ?

Passages de référence : H10, H11.

## C98 — OLP-0019-B19

**Choix :** Montrez que ; effectivement transitive

**Autre formulation envisagée :** Vérifiez que; prouver que R+ est la plus petite relation transitive contenant R

**Motif :** La consigne demande seulement la transitivité annoncée par le nom. Effectivement garde la fonction de contrôle; ajouter la minimalité changerait l’exercice source.

**Confiance et limites :** H11 donne la construction et la propriété demandée reste précise.

**Question de révision :** Effectivement apporte-t-il une aide ou peut-il être supprimé lors d’une harmonisation stylistique ?

Passages de référence : H11, H03.

## C99 — OLP-0012-B04

**Choix :** Chacun porte ; avec aucun autre objet ; encore ; Avant de les examiner

**Autre formulation envisagée :** Chacun possède une relation d’ordre; est égal à; relations envisageables

**Motif :** Chacun distribue les quatre ensembles; usuelle ne prétend pas qu’il n’existe qu’un ordre. Identique exclut tout autre objet. Encore plus nombreuses distingue exemples futurs et possibilités; avant conserve la progression pédagogique.

**Confiance et limites :** H04/H07 et l’enchaînement source concordent.

**Question de révision :** Entretenir une relation avec soi-même est-il aussi naturel ici que être en relation ?

Passages de référence : H04, H07.

## C100 — OLP-0012-B08

**Choix :** sur un ensemble ; et si ; parfois

**Autre formulation envisagée :** relation de A dans A; on note toujours

**Motif :** Sur A conserve un seul domaine. Le second si maintient la condition x,y∈A; parfois garde le caractère optionnel des deux écritures Rxy et xRy. Binaire qualifie la relation, non la cardinalité de A.

**Confiance et limites :** H04/H05 concordent exactement.

**Question de révision :** Relation sur distingue-t-il assez nettement ce cas d’une relation entre deux ensembles ?

Passages de référence : H04, H05.

## C101 — OLP-0012-B09

**Choix :** tableau à deux dimensions ; au-dessus ; au-dessous ; Notons ici ; ni ; lorsqu'elles

**Autre formulation envisagée :** matrice; inférieur; non réflexives

**Motif :** Tableau évite de suggérer des coefficients scalaires. Diagonale en gras, ordre ligne/colonne, deux directions strictes, puis adjonction de I sont conservés. La note définit seulement I=Id(N). Aucun/ni porte sur chaque entier; lorsqu’elles ajoute l’hypothèse ordre pour strict.

**Confiance et limites :** formules et placement de tous les couples contrôlés; H05–H07 soutiennent les propriétés.

**Question de révision :** Le tableau devrait-il aussi porter le nom de matrice relationnelle, sans introduire une matrice de valeurs ?

Passages de référence : H05, H06, H07.

## C102 — OLP-0012-B10

**Choix :** tout ; aussi artificielle ; ne relie aucun ; elle relie tout ; ici entre entiers naturels

**Autre formulation envisagée :** certaines parties; relation pleine; aucun élément n’est relié

**Motif :** Tout garde l’absence de condition de naturalité. Relation vide signifie aucun couple; universelle tous les couples du domaine, non tous les ensembles. La précision finale conserve N dans l’exemple numérique artificiel et son ou inclusif.

**Confiance et limites :** H04 et les cas extrêmes fixent la portée.

**Question de révision :** Relie un couple est-il moins idiomatique que met deux éléments en relation, malgré son économie ?

Passages de référence : H04.

## C103 — OLP-0013-B03

**Choix :** certains ensembles ; que \emph{fait} ; fort douteux ; se serait révélée être

**Autre formulation envisagée :** découvert des faits d’identité métaphysique; démontré une identité

**Motif :** La question vise le rôle de la définition. Certains restreint les ensembles servant au codage ; il ne quantifie pas les relations. La réserve métaphysique est portée par le doute et le conditionnel. P05 appuie ce registre, sans importer sa doctrine.

**Confiance et limites :** portée grammaticale vérifiée directement ; faits d’identité serait plus explicite mais alourdirait la phrase.

**Question de révision :** Identités métaphysiques peut-il être lu comme une catégorie d’entités plutôt que des affirmations d’identité ?

Passages de référence : L13, P05.

## C104 — OLP-0013-B04

**Choix :** Pourtant ; tout aussi ; tous deux ; dans les faits ; réductionnisme ensembliste

**Autre formulation envisagée :** modéliser; réduction en théorie des ensembles; aucun des deux n’est la relation

**Motif :** Le conditionnel souligne le choix de codage équivalent, non égal. R≠S empêche qu’ils soient tous deux identiques à la relation; il ne démontre pas qu’aucun ne l’est. Arbitrage et embarras restent modérés. P03 atteste réductionnisme; Benacerraf reste l’attribution d’OLP.

**Confiance et limites :** argument et formules cohérents, portée de la négation préservée.

**Question de révision :** L’enchaînement arbitraire donc embarrassant doit-il garder sa nuance rhétorique dans un manuel ?

Passages de référence : L02, L13, P03, P05.

## C105 — OLP-0013-B05

**Choix :** si \emph{toute} ; devrait ; ne va pas de soi ; exclura ; même si certaines

**Autre formulation envisagée :** la théorie nie; cet ensemble n’existe dans aucune théorie

**Motif :** La prémisse universelle engendre le cas ∈. Le conditionnel et la question d’existence précèdent l’exclusion dans la théorie annoncée. Les deux branches TeX et la preuve par double réunion restent présentes. Même si certaines conserve la concession restreinte.

**Confiance et limites :** L06/L13 soutiennent la distinction classe/ensemble; aucune négation absolue ajoutée.

**Question de révision :** Exclura rend-il mieux le statut théorique que démontrera l’inexistence dans le lecteur complet ?

Passages de référence : L06, L13.

## C106 — OLP-0013-B06

**Choix :** comme} un prédicat ; termes singuliers ; une proposition ; la tasse le pot à crayons la table ; Cet argument réunit

**Autre formulation envisagée :** noms propres; une phrase; le concept de cheval

**Motif :** Comme marque le rôle prédicatif, désigne le rôle nominal. Trois termes ne forment pas une proposition structurée; la liste reste sans verbe. P06 atteste le problème de nominalisation et P07 le contraste structure/constituants; l’attribution précise à Wittgenstein reste source-only.

**Confiance et limites :** distinctions philosophiques étayées par pages réelles; pas de certification exhaustive des filiations.

**Question de révision :** Proposition convient-il mieux que pensée ici sans importer toute la sémantique frégéenne ?

Passages de référence : L13, P06, P07.

## C107 — OLP-0013-B07

**Choix :** à condition ; Nous n'affirmons pas ; dans certains ; certaines relations ; certains ensembles

**Autre formulation envisagée :** les relations sont représentées par des ensembles; toutes les relations

**Motif :** La conclusion autorise une pratique sous une condition d’interprétation. Elle nie l’affirmation métaphysique, pas la possibilité du traitement. Les trois restrictions contextes/relations/ensembles et l’engagement futur sont conservés.

**Confiance et limites :** P05 et la totalité de l’argument soutiennent le contraste de statuts.

**Question de révision :** La répétition certains protège-t-elle suffisamment la portée sans nuire à la fluidité ?

Passages de référence : L13, P05.

## C108 — OLP-0014-B05

**Choix :** si et seulement si, ; pour tout

**Autre formulation envisagée :** est réflexive si Rxx; tous les éléments sont reliés

**Motif :** La biconditionnelle définit réflexive; pour tout x∈A porte sur Rxx. La variante tous reliés effacerait la réflexivité en suggérant la relation universelle.

**Confiance et limites :** H06 et formule exacte.

**Question de révision :** Faut-il réintroduire domaine dans l’explication orale de cette série de définitions ?

Passages de référence : H06, H07.

## C109 — OLP-0014-B08

**Choix :** à la fois ; autrement dit ; alors

**Autre formulation envisagée :** antisymétrique si aucun aller-retour; ou bien mais pas les deux

**Motif :** À la fois exige les deux directions seulement avant x=y. La reformulation par contraposée conserve la disjonction inclusive des négations pour x≠y; l’égalité peut rester reliée.

**Confiance et limites :** H06 et la contraposée ont la même portée.

**Question de révision :** La contraposée rend-elle plus nette la différence avec asymétrique ?

Passages de référence : H06, H07.

## C110 — OLP-0014-B09

**Choix :** toutes
les deux ; que si ; n’\emph{exige} pas ; n’est pas
nécessairement ; à la fois

**Autre formulation envisagée :** seulement lorsque; toute relation antisymétrique est non réflexive

**Motif :** Les deux valeurs simultanées caractérisent la symétrie. Que si donne une condition nécessaire, non suffisante. N’est pas nécessairement évite la négation universelle; l’identité montre la compatibilité symétrie/antisymétrie.

**Confiance et limites :** toutes les exceptions et la négation modale sont explicites.

**Question de révision :** Vraies pour Rxy/Ryx est-il préférable à vérifiées pour éviter une impression de catégories grammaticales instables ?

Passages de référence : H06, H07.

## C111 — OLP-0014-B10

**Choix :** connexe ; pour tous ; lorsque

**Autre formulation envisagée :** totale; connectée; pour tous x,y, Rxy ou Ryx sans condition

**Motif :** P01 confirme connexe avec termes distincts et ou inclusif. La condition x≠y exclut toute obligation de réflexivité; totale serait ambigu avant la définition d’ordre total.

**Confiance et limites :** témoin lexical direct et formule exacte.

**Question de révision :** Une note sur l’homonyme graph-théorique sera-t-elle utile quand les graphes connexes seront introduits ?

Passages de référence : H06, H07, P01.

## C112 — OLP-0014-B12

**Choix :** irréflexive ; pour tout ; on n’a pas

**Autre formulation envisagée :** non réflexive; il existe x tel que non Rxx

**Motif :** La négation reste sous pour tout. Irréflexive exclut toute boucle, alors que non réflexive n’exige qu’un contre-exemple.

**Confiance et limites :** H06 et la quantification concordent.

**Question de révision :** La distinction doit-elle être rappelée à chaque futur usage ou seulement ici ?

Passages de référence : H06, H07.

## C113 — OLP-0014-B13

**Choix :** s’il n’existe ; à la fois

**Autre formulation envisagée :** Paraphrase viable : si Rxy, alors non Ryx. Contrôles sémantiques rejetés : non symétrique.

**Motif :** L’absence de tout couple réalisant les deux directions comprend x=y. La négation existentielle suit OLP ; la variante implication est équivalente. La comparaison avec l’antisymétrie déjà définie est rétrospective. H06 et H07 soutiennent des propriétés voisines, mais n’attestent pas asymétrique ; le contrôle de cette définition est direct et déductif.

**Confiance et limites :** définition source et conséquences vérifiées ; aucune attestation lexicale d’asymétrique n’est attribuée à H06/H07.

**Question de révision :** Aucun couple est-il assez explicite pour inclure les couples diagonaux ?

Passages de référence : H06, H07.

## C114 — OLP-0014-B14

**Choix :** aucune relation ; au moins deux éléments ; ni réflexives ni ; sur tout ensemble non vide

**Autre formulation envisagée :** sur tout ensemble non vide pour les deux existences; ni réflexive ni asymétrique

**Motif :** La première incompatibilité suppose A non vide. L’existence ni/ni exige deux éléments; la seconde existe déjà sur un singleton via l’identité. La note conserve les deux seuls cas du singleton et divulgue la correction.

**Confiance et limites :** contre-exemples finis décisifs, accords et scopes contrôlés.

**Question de révision :** Faut-il expliciter que l’implication asymétrique⇒antisymétrique vaut aussi sur le domaine vide ?

Passages de référence : H06, H07.

## C115 — OLP-0015-B07

**Choix :** blocs ; une partition ; Dans chaque bloc ; aucun objet ; directement

**Autre formulation envisagée :** partitions; classes seulement; morceaux

**Motif :** Blocs désigne les parties d’une partition unique, correction explicitement attribuée. Tous à l’intérieur et aucun entre blocs expriment les deux conditions; directement prépare leur traitement comme objets.

**Confiance et limites :** H09 et la preuve suivante fixent les classes.

**Question de révision :** La métaphore découpe risque-t-elle de suggérer un nombre fini de blocs ?

Passages de référence : H09, L01.

## C116 — OLP-0015-B08

**Choix :** Pour chaque ; dans~$A$ ; ensemble quotient ; par~$R$

**Autre formulation envisagée :** quotient de A sous R; classe de x sans domaine

**Motif :** Pour chaque x∈A conserve l’indexation et classe dans A fixe le domaine. H09 soutient la classe indexée par R, non la locution ensemble quotient ni de A par R. Ces formulations sont éditoriales ; la construction comme ensemble des classes est justifiée par la formule OLP, et non par une division numérique.

**Confiance et limites :** classe et formule du quotient contrôlées séparément ; soutien lexical de H09 limité aux classes.

**Question de révision :** Faut-il réserver classe de x modulo R à l’exemple arithmétique suivant ?

Passages de référence : H09.

## C117 — OLP-0015-B09

**Choix :** justifie cette définition ; les blocs d’une partition

**Autre formulation envisagée :** Paraphrase viable : Le résultat suivant montre que ces classes constituent les blocs d’une partition de A. Contrôles sémantiques rejetés : prouve que les classes sont les partitions de A

**Motif :** Cette définition renvoie à celle des classes; le résultat explique leur rôle de blocs, sans multiplier les partitions. Le texte n’ajoute pas une nouvelle définition du quotient.

**Confiance et limites :** correction terminologique cohérente avec B07, preuve pertinente.

**Question de révision :** Justifie est-il trop fort pour une proposition ne formulant pas séparément la réunion de tous les blocs ?

Passages de référence : H09, L01.

## C118 — OLP-0015-B11

**Choix :** Pour le sens direct ; Explicitons ; alors ; pour tout ; De la même manière ; Par extensionnalité

**Autre formulation envisagée :** sens gauche-droite; on généralise sans préciser z

**Motif :** Sens direct fixe Rxy comme hypothèse. Symétrie donne Ryx, puis transitivité avec Rxz donne Ryz. Tout tel objet quantifie z avant l’inclusion; l’inclusion inverse puis l’extensionnalité donnent l’égalité.

**Confiance et limites :** chaque dépendance est reconstruite dans l’ordre adéquat.

**Question de révision :** L’anaphore tout tel objet devrait-elle répéter z pour faciliter la première lecture ?

Passages de référence : H06, H09, L07.

## C119 — OLP-0015-B12

**Choix :** Pour la réciproque ; Comme ; L’hypothèse ; donc

**Autre formulation envisagée :** sens inverse; conclure par symétrie

**Motif :** La réciproque part de l’égalité des classes; réflexivité donne Ryy, égalité transfère y, définition donne Rxy. Aucun recours inutile à la symétrie ni renversement des classes.

**Confiance et limites :** H06/H09 et la chaîne d’inférences concordent.

**Question de révision :** Les noms des propriétés suffisent-ils à distinguer nettement cette preuve du sens direct ?

Passages de référence : H06, H09.

## C120 — OLP-0015-B13

**Choix :** zéro compris ; si et seulement s’il existe ; exactement ; Ces classes sont

**Autre formulation envisagée :** Paraphrase viable : Deux naturels sont congrus modulo n lorsque leur différence est un multiple entier de n ; les n restes déterminent exactement les classes. Contrôles sémantiques rejetés : a,b strictement positifs; k naturel; au moins n classes

**Motif :** La correction domaine N/module positif est divulguée. Le même reste équivaut à un multiple avec k entier relatif. Exactement et distinctes sont conservés; la liste couvre0 à n−1, y compris n=1.

**Confiance et limites :** calcul modulaire et H08/L04 fixent le domaine.

**Question de révision :** La note de domaine pourrait-elle être abrégée sans masquer la correction de source ?

Passages de référence : H08, L04.

## C121 — OLP-0015-B14

**Choix :** pour tout ; exactement

**Autre formulation envisagée :** Paraphrase viable : Pour chaque entier strictement positif n, établissez l’équivalence de la relation et le nombre exact n de classes sur N. Contrôles sémantiques rejetés : pour un n; au plus n éléments

**Motif :** La consigne exige deux résultats pour chaque module strictement positif : équivalence et cardinal exact du quotient sur N. Le et coordonne les deux obligations sans modifier leur quantification.

**Confiance et limites :** hypothèse et résultat demandés concordent avec l’exemple.

**Question de révision :** Le lecteur comprend-il que les membres du quotient sont des classes, pas les entiers eux-mêmes ?

Passages de référence : H08, H09.

## C122 — OLP-0016-B05

**Choix :** à la fois ; préordre

**Autre formulation envisagée :** relation réflexive ou transitive; quasi-ordre

**Motif :** À la fois conserve la conjonction définitoire. Préordre suit H13 et évite quasi-ordre, variante possible mais moins cohérente avec le cours consulté.

**Confiance et limites :** même définition et même terme.

**Question de révision :** Quasi-ordre mérite-t-il seulement une mention terminologique ultérieure ?

Passages de référence : H13.

## C123 — OLP-0016-B06

**Choix :** qui est aussi antisymétrique

**Autre formulation envisagée :** ordre; préordre non symétrique

**Motif :** Aussi ajoute l’antisymétrie aux deux propriétés héritées, sans la remplacer par absence de symétrie. Partiel est conservé pour la hiérarchie même lorsque le canon abrège en ordre.

**Confiance et limites :** H13 et la définition précédente concordent.

**Question de révision :** Faut-il rappeler les propriétés héritées lors du premier théorème utilisant un ordre partiel ?

Passages de référence : H13.

## C124 — OLP-0016-B07

**Choix :** aussi connexe ; ordre total ; ordre linéaire

**Autre formulation envisagée :** ordre total uniquement; ordre connecté

**Motif :** La connexité s’ajoute à l’ordre partiel; les deux noms sont explicitement synonymes. P01 confirme le sens de connexe sur les paires distinctes, donc sans exiger une propriété plus forte nouvelle.

**Confiance et limites :** H13 plus P01 fixent la construction.

**Question de révision :** L’édition doit-elle privilégier ensuite linéaire tout en gardant total comme synonyme ?

Passages de référence : H13, H06, P01.

## C125 — OLP-0016-B08

**Choix :** Tout ; les réciproques sont fausses ; plus d’un

**Autre formulation envisagée :** les inverses sont faux; toute relation universelle est non antisymétrique

**Motif :** Tout conserve les inclusions de classes. Réciproques désigne les implications, non des relations inverses. Plus d’un maintient l’exception des domaines vide/singleton pour l’antisymétrie de la relation universelle.

**Confiance et limites :** hiérarchie et exemple exacts.

**Question de révision :** Le pluriel réciproques peut-il être compris avant le second contre-exemple qui suit ?

Passages de référence : H13, H06.

## C126 — OLP-0016-B09

**Choix :** est de longueur inférieure ou égale à ; qui est même connexe ; alors que

**Autre formulation envisagée :** pas plus long que; ordre des longueurs

**Motif :** La lecture développée préserve ≤ et porte sur les longueurs, pas sur les mots. Réflexif/transitif/connexe s’accordent avec préordre; 01 et10 distinguent égalité de longueur et identité.

**Confiance et limites :** H13/P01 et le contre-exemple concordent.

**Question de révision :** Pas plus long que serait-il plus idiomatique sans créer une négation supplémentaire à traiter ?

Passages de référence : H13, H06, P01.

## C127 — OLP-0016-B11

**Choix :** sans reste ; il existe un entier ; Sur~$\Nat$ ; Sur $\Int$

**Autre formulation envisagée :** Paraphrase viable : divisibilité entière. Contrôles sémantiques rejetés : k naturel ; même ordre sur Z.

**Motif :** Divisibilité est le terme éditorial, sans reste son explication ; ni H13 ni H07 ne l’attestent dans l’exemple des entiers. Le critère m=kn et k entier sont vérifiés sur OLP et par arithmétique directe. Les paires 2,3 et 1,−1 justifient non-linéarité sur N et défaut d’antisymétrie sur Z. Les témoins soutiennent seulement le vocabulaire des propriétés d’ordre.

**Confiance et limites :** calculs et changements de domaine contrôlés ; aucune attestation lexicale de divisibilité attribuée à ces passages.

**Question de révision :** Le cas0 dans N devrait-il être explicité ou conservé comme conséquence de la définition ?

Passages de référence : H13, H07.

## C128 — OLP-0016-B12

**Choix :** prolongement ; segment initial ; dès que ; au plus un symbole ; véritables suites finies

**Autre formulation envisagée :** ordre des préfixes; s prolonge s′ pour s⊑s′

**Motif :** Prolongement nomme la relation mais la formule et segment initial en fixent le sens : s est préfixe de s′. Les cas vide/égalité sont inclus. Deux symboles conditionnent la non-linéarité; la note préserve l’identité des suites par longueur.

**Confiance et limites :** P04/L14 soutiennent préfixes, prolongement reste choix contextuel.

**Question de révision :** Ordre des préfixes serait-il moins sujet à une lecture orientée inverse de prolongement ?

Passages de référence : L14, H13, H02, P04.

## C129 — OLP-0016-B13

**Choix :** irréflexive, asymétrique et transitive

**Autre formulation envisagée :** irréflexive et transitive seulement

**Motif :** Les trois propriétés source sont gardées même si l’asymétrie suit des deux autres. H14 n’énonce que deux propriétés; sa variante n’autorise pas à supprimer une qualification d’OLP.

**Confiance et limites :** redondance mathématique comprise et conservée.

**Question de révision :** La redondance mérite-t-elle un exercice plutôt qu’une réécriture de la définition ?

Passages de référence : H14.

## C130 — OLP-0016-B14

**Choix :** aussi connexe ; ordre total strict ; ordre linéaire strict

**Autre formulation envisagée :** ordre strict total; strictement total

**Motif :** Connexe ajoute la comparabilité aux éléments distincts. Les deux synonymes gardent strict attaché à ordre, sans suggérer une intensification de total.

**Confiance et limites :** H14/P01 et la définition non stricte concordent.

**Question de révision :** L’ordre des adjectifs linéaire strict doit-il être uniforme dans tous les titres ultérieurs ?

Passages de référence : H14, H06, P01.

## C131 — OLP-0016-B16

**Choix :** tout ordre strict ; clôture réflexive ; Réciproquement ; en en retirant

**Autre formulation envisagée :** fermeture réflexive; ajouter tous les couples; supprimer les boucles

**Motif :** Tout porte sur les ordres stricts; seuls les couples diagonaux sont ajoutés. Réciproquement inverse l’opération entre classes d’ordres, non la relation. En en reprend partir de l’ordre puis en retirer sa diagonale.

**Confiance et limites :** H06/H14 et les deux propositions fixent le mécanisme.

**Question de révision :** La répétition en en pourrait-elle être remplacée par en retirant sa diagonale à celui-ci ?

Passages de référence : H06, H14.

## C132 — OLP-0016-B17

**Choix :** Si ; De plus

**Autre formulation envisagée :** Paraphrase viable : L’ajout de la diagonale à un ordre strict donne un ordre partiel ; si l’ordre de départ est aussi linéaire, l’ordre obtenu l’est aussi. Contrôles sémantiques rejetés : R+ est la clôture transitive de R

**Motif :** Le signe R+ conserve ici son sens local de clôture réflexive. L’hypothèse supplémentaire strict linéaire donne linéaire; la première ne donne que partiel. La note de section19 signale ensuite la collision de notation.

**Confiance et limites :** sens local et deux implications vérifiés.

**Question de révision :** Faut-il rappeler la collision dès cette première occurrence dans une prochaine édition ?

Passages de référence : H13, H14.

## C133 — OLP-0016-B22

**Choix :** en outre connexe ; Pour tous ; cela reste vrai ; elle aussi

**Autre formulation envisagée :** la relation devient connexe; toujours pour tous x,y sans distinction

**Motif :** En outre introduit la nouvelle hypothèse. La disjonction est conservée par l’inclusion R⊆R+; cela reprend cette disjonction pour x≠y. Elle s’accorde avec relation.

**Confiance et limites :** inclusion et P01 suffisent, aucune connexité créée sans hypothèse.

**Question de révision :** Dernière affirmation est-il un renvoi plus clair que clause de plus ?

Passages de référence : H06, H03, P01.

## C134 — OLP-0016-B28

**Choix :** Si ; ce qui contredit ; De la même manière ; Puisque

**Autre formulation envisagée :** a et b ont les mêmes propriétés donc sont égaux

**Motif :** La preuve instancie la biconditionnelle pour exclure a<b puis b<a par irréflexivité; la connexité impose alors a=b. Elle ne recourt pas à un principe général d’identité des indiscernables.

**Confiance et limites :** deux contradictions et conclusion séparées.

**Question de révision :** Les substitutions x=a et x=b devraient-elles être explicites pour des débutants ?

Passages de référence : L06, H14.

## C135 — OLP-0017-B04

**Choix :** se représente ; nœuds ; arêtes ; orientées ou non ; ou interdire

**Autre formulation envisagée :** un graphe est un diagramme; arcs; labels

**Motif :** Se représente dissocie objet et dessin en accord avec G03 et la définition suivante. La liste conserve orientations, étiquettes, boucles et arêtes multiples comme conventions possibles. L’explication anglaise du pluriel vertex devient inutile en français.

**Confiance et limites :** G01–G03 attestent les termes et la distinction; aucune convention locale indue.

**Question de révision :** Faut-il nommer explicitement boucles dans cette introduction ou laisser la description concrète ?

Passages de référence : G01, G02, G03.

## C136 — OLP-0017-B05

**Choix :** est constitué d’un ensemble ; arêtes

**Autre formulation envisagée :** est un ensemble V et E; arcs orientés

**Motif :** Est constitué respecte le couple G=(V,E), pas deux identités avec des ensembles. Sommets et arêtes sont définis; E⊆V² garde l’orientation et interdit les arêtes multiples dans cette convention précise.

**Confiance et limites :** définition exacte et G01/G02 concordants.

**Question de révision :** Une remarque sur l’écart entre la liste des conventions et celle-ci serait-elle utile ?

Passages de référence : G01, G02.

## C137 — OLP-0017-B06

**Choix :** du ; vers le sommet ; si et seulement si ; sommets isolés ; réciproquement

**Autre formulation envisagée :** relier deux sommets; tout graphe est simplement sa relation

**Motif :** Du...vers rend l’ordre des coordonnées. Le graphe garde V et donc les sommets isolés. Les deux conversions gardent leurs domaines explicites, sans identifier des graphes de supports différents.

**Confiance et limites :** G02/G03 et exemple suivant fixent le sens.

**Question de révision :** La seule différence est-il adéquat dans le cadre local de graphes orientés simples avec boucles ?

Passages de référence : G02, G03, H04.

## C138 — OLP-0017-B07

**Choix :** se représente ainsi ; Il diffère du graphe ; représenté ci-dessous

**Autre formulation envisagée :** Paraphrase viable : Malgré le même ensemble d’arêtes, les ensembles de sommets diffèrent. Contrôles sémantiques rejetés : même graphe dessiné sans le sommet4

**Motif :** Les deux descriptions portent sur des graphes différents malgré le même E : V diffère de V′ par4. Toutes les flèches et la boucle1 sont identiques; le second dessin ne cache pas un sommet de son propre support.

**Confiance et limites :** supports et commandes TikZ contrôlés.

**Question de révision :** Le renvoi Il identifie-t-il assez nettement le premier graphe, plutôt que son dessin ?

Passages de référence : G02, G03.

## C139 — OLP-0018-B04

**Choix :** analysées ; elles aussi ; dès la démonstration ; complétude

**Autre formulation envisagée :** dérivations de formules; complétude des arbres

**Motif :** Les accords portent sur formules/dérivations féminines. Les arbres finis décrivent syntaxe et preuves; les infinis interviennent dans les preuves de complétude des deux logiques. T01/T02 appuient arbre; l’attribution théorique reste OLP.

**Confiance et limites :** emplois et portée contrôlés, aucune doctrine de complétude tirée du canon d’arbres.

**Question de révision :** Les futurs tokens masculins nécessiteront-ils une variante d’accord explicite ?

Passages de référence : T01, T02.

## C140 — OLP-0018-B07

**Choix :** situé tout en bas ; exactement un ; vers le haut ; ancêtre

**Autre formulation envisagée :** racine en haut; au plus un parent dans cet exemple

**Motif :** La description est celle du dessin fini : racine en bas, parent immédiatement inférieur, ascendance par chemin montant. Elle ne généralise pas exactement un aux nœuds limites de la définition suivante.

**Confiance et limites :** dessin et paragraphe précédent fixent le cadre; convention de T01 distincte.

**Question de révision :** Dans l’arbre représenté rendrait-il cette portée locale plus immédiatement perceptible ?

Passages de référence : T01, T02.

## C141 — OLP-0018-B08

**Choix :** ordre partiel strict ; plus petit élément ; pour tout ; chacune de ses parties non vides

**Autre formulation envisagée :** élément minimal; toute partie a un minimum

**Motif :** Plus petit signifie inférieur à tous, pas seulement minimal. Non vide reste sur les parties quantifiées, ce qui permet le bon ordre du domaine vide. La relation d’ascendance est stricte avant le passage à ≤.

**Confiance et limites :** L14 est une attestation directe et les quantificateurs concordent.

**Question de révision :** Ordre partiel strict devrait-il être rappelé comme synonyme d’ordre strict selon la convention présente ?

Passages de référence : L14, H14.

## C142 — OLP-0018-B09

**Choix :** un couple ; unique plus petit élément ; pour tout ; soit bien ordonné

**Autre formulation envisagée :** arbre éventuellement vide; chaque ensemble de successeurs bien ordonné

**Motif :** Le couple est (A,≤). L’existence de la racine impose A non vide; l’unicité conservée est redondante mais exacte. Le bon ordre porte sur les prédécesseurs y≤x, pour chaque x, pas sur les descendants.

**Confiance et limites :** OLP et L14 concordent; convention informatique T01 non importée.

**Question de révision :** Faut-il indiquer explicitement que cette définition autorise des hauteurs transfinies ?

Passages de référence : L14, T01.

## C143 — OLP-0018-B10

**Choix :** qu’il n’existe aucun ; successeur

**Autre formulation envisagée :** descendant; successeur immédiat

**Motif :** La négation existentielle entre x et y fait de successeur un voisin immédiat. La condition x<y demeure distincte. Le nom court conserve la convention source, avec immédiat contenu dans la définition.

**Confiance et limites :** absence de point intermédiaire et T02 concordent.

**Question de révision :** Successeur immédiat serait-il utile en synonyme lors du premier emploi ?

Passages de référence : T01, T02.

## C144 — OLP-0018-B11

**Choix :** enfants ; Si ; prédécesseur ; parent

**Autre formulation envisagée :** fils; ancêtre

**Motif :** Enfants est inclusif et idiomatique; T01 emploie fils dans un contexte binaire. La condition inverse les rôles sans inverser la relation : x est parent de son successeur y, non tout ancêtre.

**Confiance et limites :** convention locale exacte; enfants est un choix éditorial réversible.

**Question de révision :** Enfant reste-t-il aussi familier que fils dans le lectorat mathématique visé ?

Passages de référence : T01.

## C145 — OLP-0018-B12

**Choix :** autre que la racine ; au plus un

**Autre formulation envisagée :** exactement un; un unique prédécesseur

**Motif :** L’exception de la racine et la borne au plus un sont conservées. Le théorème ne garantit pas l’existence d’un prédécesseur pour un nœud de hauteur limite.

**Confiance et limites :** portée mathématique décisive.

**Question de révision :** Un exemple de nœud limite est-il nécessaire ici ou relève-t-il du chapitre ordinal ultérieur ?

Passages de référence : T01, L14.

## C146 — OLP-0018-B13

**Choix :** nécessairement ; Or ; on en déduit ; pas être tous deux

**Autre formulation envisagée :** Paraphrase viable : La comparabilité place l’un des deux candidats entre l’autre et x, si bien qu’ils ne peuvent être tous deux immédiats. Contrôles sémantiques rejetés : l’un des deux n’est pas ancêtre; nécessairement y1<y2

**Motif :** Le bon ordre rend comparables les deux candidats distincts; leur inégalité rend la comparaison stricte. Dans chacun des deux cas, l’autre s’intercale avant x, excluant qu’ils soient tous deux prédécesseurs immédiats.

**Confiance et limites :** les deux cas et la portée de pas tous deux sont préservés.

**Question de révision :** Répéter immédiats dans la conclusion améliorerait-il la distinction avec ancêtres ?

Passages de référence : L14, T03.

## C147 — OLP-0018-B14

**Choix :** infini ; sinon ; Si chaque ; à branchement fini

**Autre formulation envisagée :** Paraphrase viable : La finitude du domaine et le nombre fini de successeurs immédiats à chaque nœud sont deux propriétés distinctes. Contrôles sémantiques rejetés : arbre fini s’il a un nombre fini d’enfants par nœud

**Motif :** Infini/fini concerne A entier. Branchement fini quantifie un nombre fini de successeurs à chaque nœud, sans borne uniforme et sans imposer la finitude de A.

**Confiance et limites :** OLP distingue clairement les deux finitudes; P04 en donne un cas.

**Question de révision :** Branchement fini est-il plus naturel que ramification finie pour unifier les chapitres à venir ?

Passages de référence : T01, P04.

## C148 — OLP-0018-B15

**Choix :** chaîne maximale ; pour tous ; pour tout ; il existe ; ni ; Correction éditoriale

**Autre formulation envisagée :** Paraphrase viable : Une branche est une chaîne qui ne peut être agrandie dans l’arbre ; tout point extérieur est incomparable à au moins un point de la chaîne. Contrôles sémantiques rejetés : chaîne maximum; même u pour tous z; X comme domaine

**Motif :** Maximale signifie inextensible par inclusion. La première clause donne comparabilité interne; pour chaque z extérieur peut dépendre un témoin u incomparable. La double négation exclut les deux sens; A remplace X indéfini dans une note visible.

**Confiance et limites :** quantification exacte et correction de domaine contrôlées; P04 limité au cas binaire.

**Question de révision :** La définition explicite rend-elle suffisamment claire la différence entre maximale et de cardinal maximal ?

Passages de référence : L14, T01, P04.

## C149 — OLP-0018-B17

**Choix :** un pour chaque ; Toute partie non vide ; stable par passage aux ; si ; Tout arbre fini

**Autre formulation envisagée :** Paraphrase viable : Les sous-arbres considérés sont non vides et contiennent, avec toute suite, chacun de ses préfixes. Contrôles sémantiques rejetés : fermée vers les prolongements; toute partie même vide

**Motif :** Chaque mot a une infinité de successeurs indexés par N. La stabilité descend vers les préfixes, non vers leurs prolongements. Non vide garantit la racine; la note le divulgue. Représenté ne promet pas une égalité littérale avec un sous-ensemble de N*.

**Confiance et limites :** P04/L14 contrôlent l’orientation; la correction suit la définition d’arbre.

**Question de révision :** Représenté doit-il être développé en isomorphe à dans une édition plus avancée ?

Passages de référence : L14, T01, H02, P04.

## C150 — OLP-0018-B18

**Choix :** arbre infini à branchement fini ; branche infinie

**Autre formulation envisagée :** Paraphrase viable : Tout arbre infini à branchement fini admet au moins une branche infinie. Contrôles sémantiques rejetés : tout arbre infini; une infinité de branches

**Motif :** Les deux hypothèses sont conjointes. La conclusion garantit au moins une branche infinie ; elle n’affirme ni l’unicité ni l’infinitude du nombre de branches. T03 ne prouve pas ce lemme général ; P04 atteste seulement le cas binaire.

**Confiance et limites :** portée existentielle vérifiée sur OLP ; le plein arbre binaire exclut une lecture unique. Les références ne certifient pas le lemme général.

**Question de révision :** La convention d’arbres transfinis demande-t-elle une preuve explicite adaptée dans une future édition ?

Passages de référence : T03, P04.

## C151 — OLP-0018-B19

**Choix :** cas particulier ; théorie
de la calculabilité ; lemme faible ; tout sous-arbre infini

**Autre formulation envisagée :** lemme de König faible; chemin infini comme définition générale de branche

**Motif :** P04 atteste le nom et le théorème binaire. Dans ce cas, la suite d’un chemin et la chaîne de tous ses préfixes correspondent; hors de ce cas, branche garde la définition OLP par chaîne maximale. Couramment conserve le registre d’usage.

**Confiance et limites :** attestation directe; aucun remplacement des définitions générales.

**Question de révision :** Une phrase expliquant la correspondance chemin/branche serait-elle utile lors de l’usage en calculabilité ?

Passages de référence : T03, P04.

## C152 — OLP-0019-B06

**Choix :** La relation ; inverse

**Autre formulation envisagée :** réciproque; fonction inverse

**Motif :** Relation inverse évite de présumer fonctionnalité. La permutation y,x porte sur chaque couple x,y de R; aucun domaine ou témoin supplémentaire n’est introduit. H15 l’atteste pour un graphe de fonction dont l’inverse peut ne pas être fonction.

**Confiance et limites :** opération exacte; extension aux relations contrôlée par la formule OLP.

**Question de révision :** Réciproque risquerait-il davantage la confusion avec la réciproque d’un théorème ?

Passages de référence : H15.

## C153 — OLP-0019-B07

**Choix :** produit relatif

**Autre formulation envisagée :** composition de S avec R; produit relationnel

**Motif :** P02 donne le terme historique; H10 fixe le passage R puis S. Le témoin y est existentiel et partagé par les deux relations. L’endpoint fautif du témoin historique reste rejeté.

**Confiance et limites :** formule OLP et H10 concordent, lexique désormais directement attesté.

**Question de révision :** Ajouter composé serait-il utile comme synonyme sans inverser l’ordre de notation ?

Passages de référence : H10, P02.

## C154 — OLP-0019-B08

**Choix :** restriction ; à $A$

**Autre formulation envisagée :** Paraphrase viable : On ne conserve de R que les couples dont les deux coordonnées appartiennent à A. Contrôles sémantiques rejetés : restriction de la première coordonnée à A

**Motif :** La restriction supprime les couples dont au moins une coordonnée est hors de A, car on intersecte A². La variante fonctionnelle ne convient pas ici; le futur passage OLP0023 devra distinguer les deux conventions.

**Confiance et limites :** formule explicite, H01 soutient l’intersection seulement.

**Question de révision :** Le terme restriction doit-il recevoir une note comparative au chapitre des fonctions ?

Passages de référence : H01, H04.

## C155 — OLP-0019-B09

**Choix :** image ; par $R$

**Autre formulation envisagée :** application de R à A; ensemble des valeurs de la fonction R

**Motif :** Image évite de faire d’une opération sur ensembles une application au sens fonction. Un y appartient dès qu’un x∈A le relie par R, sans unicité. H15 atteste image pour les fonctions; la généralisation vient de la formule OLP.

**Confiance et limites :** quantificateur et orientation exacts, limite du témoin explicitée.

**Question de révision :** Image relationnelle serait-il utile lors de la première occurrence seulement ?

Passages de référence : H15.

## C156 — OLP-0019-B11

**Choix :** à chaque entier son prédécesseur

**Autre formulation envisagée :** relation prédécesseur; prédécesseur de chaque naturel

**Motif :** Chaque entier conserve Z, donc le prédécesseur existe même pour0 et les négatifs. Son rattache x−1 à l’entrée x. La formule reste une relation, malgré le verbe associer.

**Confiance et limites :** calcul et H15 concordent.

**Question de révision :** Associe suggère-t-il à tort une définition fonctionnelle dans cet exemple pourtant fonctionnel ?

Passages de référence : H15.

## C157 — OLP-0019-B12

**Choix :** est

**Autre formulation envisagée :** est égal à; associe x à son successeur

**Motif :** Est identifie l’ensemble de couples du double pas, pas la relation à un entier. Deux compositions de succession donnent x+2=y; aucune simplification en un pas n’est admise.

**Confiance et limites :** calcul direct et H10 concordants.

**Question de révision :** La phrase purement symbolique mérite-t-elle une glose double succession ?

Passages de référence : H10.

## C158 — OLP-0019-B13

**Choix :** relation de succession

**Autre formulation envisagée :** fonction successeur restreinte

**Motif :** La restriction relationnelle conserve les couples naturels aux deux extrémités. Ici x∈N implique x+1∈N, ce qui rend cet exemple compatible avec la restriction fonctionnelle sans prouver une équivalence générale.

**Confiance et limites :** stabilité de N sous succession vérifiée.

**Question de révision :** Cet exemple trop favorable pourrait-il masquer la différence générale des restrictions ?

Passages de référence : H04.

## C159 — OLP-0019-B14

**Choix :** est

**Autre formulation envisagée :** a pour éléments; est incluse dans

**Motif :** Est conserve l’égalité exacte de l’image avec {2,3,4}; chaque entrée1,2,3 a son successeur, et aucun autre témoin du domaine restreint n’est disponible.

**Confiance et limites :** trois images directement calculées.

**Question de révision :** Une glose est-elle utile ou la formule suffit-elle après la définition ?

Passages de référence : H15.

## C160 — OLP-0019-B15

**Choix :** Clôture transitive ; dans cette section ; Il n’a donc pas ; conservées

**Autre formulation envisagée :** uniformiser partout R+ en une autre notation

**Motif :** La note borne le nouveau sens à la section, distingue expressément la clôture réflexive précédente et explique la conservation des notations source. La relation binaire reste sur A.

**Confiance et limites :** collision réelle et traitement divulgué, H11 confirme le nouveau sens.

**Question de révision :** La mise en garde gagnerait-elle à être aussi placée près de la première notation R+ ?

Passages de référence : H11.

## C161 — OLP-0019-B16

**Choix :** où l’on définit par récurrence

**Autre formulation envisagée :** définit récursivement; commencer les puissances à zéro

**Motif :** Par récurrence introduit base1 et étape n+1. La réunion porte sur les naturels strictement positifs, ce qui exclut l’identité en général. H10/H11 utilisent aussi la puissance0, sans imposer son importation ici.

**Confiance et limites :** indices et opérations contrôlés.

**Question de révision :** Récurrence pour une définition est-il assez distingué de la méthode de preuve dans les sections suivantes ?

Passages de référence : H10, H11.

## C162 — OLP-0019-B17

**Choix :** réflexive et transitive

**Autre formulation envisagée :** réflexive-transitive; transitive de la clôture réflexive

**Motif :** Et garde les deux propriétés réunies. L’adjonction de Id(A) se fait à R+, dont le sens transitive est désormais fixé. Aucun changement de domaine pour l’identité.

**Confiance et limites :** H11 correspond exactement à la formule.

**Question de révision :** La variante avec trait d’union apporterait-elle quelque chose à la cohérence terminologique ?

Passages de référence : H11.

## C163 — OLP-0023-B04

**Choix :** Les fonctions comme relations

**Autre formulation envisagée :** Graphes des fonctions

**Motif :** Comme prépare l’identification méthodologique, sans réduire le titre à sa définition technique suivante.

**Confiance et limites :** L15/H16 et le propos source concordent.

**Question de révision :** Représentation serait-il trop conclusif ici ?

Passages de référence : L15, H16.

## C164 — OLP-0023-B05

**Choix :** sur des ; si et
seulement si ; identifier

**Autre formulation envisagée :** envoie A sur B; représente

**Motif :** Sur des éléments n’implique pas la surjectivité sur B. La biconditionnelle définit les couples; identifier conserve l’hypothèse de réduction des notions, sans découverte métaphysique.

**Confiance et limites :** conditions et statut hypothétique explicites.

**Question de révision :** Envoie vers serait-il encore moins susceptible d’une lecture surjective ?

Passages de référence : L15, H16.

## C165 — OLP-0023-B06

**Choix :** Graphe d’une fonction ; définie par

**Autre formulation envisagée :** graphique; représentation graphique

**Motif :** Graphe désigne l’ensemble de couples, non un dessin. Le produit ambiant A×B demeure explicite dans la définition.

**Confiance et limites :** L15/H16 attestent le sens.

**Question de révision :** Faut-il rappeler la différence avec graphe orienté ?

Passages de référence : L15, H16.

## C166 — OLP-0023-B07

**Choix :** de mêmes domaine et ensemble d’arrivée ; en chaque point

**Autre formulation envisagée :** même graphe suffit indépendamment de l’arrivée

**Motif :** Le principe conserve les deux données typées et l’égalité point par point. L’extensionnalité des ensembles justifie celle des graphes dans ce cadre fixé.

**Confiance et limites :** L15/L01 et l’hypothèse source concordent.

**Question de révision :** De mêmes domaine et ensemble d’arrivée mérite-t-il d’être développé en même domaine et même ensemble d’arrivée ?

Passages de référence : L15, H16, L01.

## C167 — OLP-0023-B08

**Choix :** « fonctionnelle »

**Autre formulation envisagée :** univoque; fonctionnelle sans guillemets

**Motif :** Les guillemets annoncent les deux conditions précisées ensuite. H16 ne demande que l’unicité pour une fonction partielle; ce sens ne doit pas annuler la totalité qu’OLP ajoute ici.

**Confiance et limites :** fidélité conservée, terme volontairement préliminaire.

**Question de révision :** Faudrait-il ajouter et totale après fonctionnelle pour éviter l’ambiguïté technique ?

Passages de référence : L15, H16.

## C168 — OLP-0023-B09

**Choix :** si ; pour tout ; il existe ; si et seulement si

**Autre formulation envisagée :** une et une seule image pour chaque x

**Motif :** La première condition donne au plus une valeur, la seconde au moins une pour chaque entrée. La conclusion fixe f par biconditionnelle sans changer de domaine.

**Confiance et limites :** L15/H16 et les deux conditions concordent.

**Question de révision :** Les variables y,z devraient-elles être explicitement déclarées dans B ?

Passages de référence : L15, H16.

## C169 — OLP-0023-B10

**Choix :** première condition ; La seconde condition ; pour chaque

**Autre formulation envisagée :** la condition sur R suffit

**Motif :** La preuve distingue unicité par contradiction et existence par la seconde hypothèse, implicite dans l’original. Cette explicitation ne change pas l’énoncé; elle rend bien définie justifié.

**Confiance et limites :** les deux obligations sont nécessaires et vérifiées.

**Question de révision :** Cette explicitation doit-elle être signalée dans les notes éditoriales publiques ou suffit-elle au journal des choix ?

Passages de référence : L15, H16.

## C170 — OLP-0023-B11

**Choix :** incluse dans ; Réciproquement ; traiter ; On peut ainsi envisager

**Autre formulation envisagée :** relation sur A×B; toutes les relations sont des fonctions

**Motif :** Incluse dans corrige la locution source relation on A×B : le graphe est une partie de A×B, non une partie de (A×B)². Les deux branches conditionnelles restent grammaticalement complètes; l’identification garde son statut pratique.

**Confiance et limites :** domaines et branches TeX relus; P05 soutient le registre seulement.

**Question de révision :** Le passage conditionnel conserve-t-il sa fluidité dans les deux lecteurs possibles ?

Passages de référence : L15, H16, P05.

## C171 — OLP-0023-B12

**Choix :** et soit

**Autre formulation envisagée :** avec C inclus dans A

**Motif :** Deux soit introduisent la fonction et le sous-domaine C, sans imposer C non vide.

**Confiance et limites :** hypothèse inchangée.

**Question de révision :** Avec serait-il plus léger ?

Passages de référence : L15, H16.

## C172 — OLP-0023-B13

**Choix :** restriction ; pour tout ; Autrement dit

**Autre formulation envisagée :** intersection du graphe avec C²

**Motif :** Seule l’entrée est restreinte; l’arrivée reste B. La formule des couples sélectionne x∈C, et la phrase pour tout garde toutes les entrées de C.

**Confiance et limites :** L15 et formule exacte; différence relationnelle explicite plus loin.

**Question de révision :** Une notation différente éviterait-elle l’homonymie sans rompre celle d’OLP ?

Passages de référence : L15, H16, H01.

## C173 — OLP-0023-B14

**Choix :** image ; image directe

**Autre formulation envisagée :** application de f à C

**Motif :** Image directe suit l’usage de la page Yger consultée; application désignerait aussi un type de fonction. Les deux noms désignent le même ensemble de valeurs, pas une nouvelle fonction.

**Confiance et limites :** H16 et Yger PDF23, ouverture, attestent cet usage.

**Question de révision :** Image directe doit-il être réservé au contraste avec image réciproque ?

Passages de référence : L15, H16, Y04.

## C174 — OLP-0023-B15

**Choix :** La notion d’image concorde ; distinguer les deux ; ne
restreint que ; Les deux coïncident

**Autre formulation envisagée :** ces notions concordent toutes avec les relations

**Motif :** La formule de l’image totale reste intacte. La restriction source contredit R∩C² : le successeur sur N et C={0} le démontre. La note conserve les deux définitions et donne la condition exacte f[C]⊆C de coïncidence des graphes.

**Confiance et limites :** contre-exemple fini calculable et condition vérifiée.

**Question de révision :** Faut-il expliciter que la coïncidence concerne les graphes plutôt que les données d’arrivée typées ?

Passages de référence : L15, H16, H01.

## C175 — OLP-0024-B03

**Choix :** Inverses des fonctions

**Autre formulation envisagée :** Fonctions réciproques

**Motif :** Inverse suit Y01 et permet les variantes à gauche/à droite sans réserver d’emblée le terme aux bijections.

**Confiance et limites :** terminologie directement attestée.

**Question de révision :** Réciproque mérite-t-il un synonyme après la définition bilatérale ?

Passages de référence : Y01, Y02, Y03, H17.

## C176 — OLP-0024-B04

**Choix :** correspondances entre objets ; « défait »

**Autre formulation envisagée :** applications; annule

**Motif :** Correspondance garde l’image intuitive sans introduire un nouveau type technique. Défait décrit le retour à l’entrée, non une annulation vers zéro.

**Confiance et limites :** exemple x+1 puis y−1 exact.

**Question de révision :** Défait reste-t-il suffisamment naturel dans le registre du manuel ?

Passages de référence : Y01, Y02, Y03, H17.

## C177 — OLP-0024-B05

**Choix :** mais elle ne définit pas ; peut dépendre

**Autre formulation envisagée :** n’est jamais inversible sur N

**Motif :** La formule de g est une fonction Z→Z mais pas N→N à cause de0. Peut dépendre garde la condition sur domaine et arrivée, sans prétendre que toute restriction empêche une inversion.

**Confiance et limites :** exemple décisif, L15 précise les données de fonction.

**Question de révision :** Le rôle de l’ensemble d’arrivée demande-t-il un autre exemple ?

Passages de référence : Y01, Y02, Y03, H17, L15.

## C178 — OLP-0024-B06

**Choix :** permet de préciser

**Autre formulation envisagée :** formalise entièrement

**Motif :** Le renvoi cette idée reprend l’inversion intuitive, sans annoncer plus que la définition suivante.

**Confiance et limites :** progression fidèle.

**Question de révision :** Le bref paragraphe doit-il rester séparé pour suivre la mise en page source ?

Passages de référence : Y01, Y02, Y03, H17.

## C179 — OLP-0024-B07

**Choix :** un \emph{inverse} ; pour tous

**Autre formulation envisagée :** une fonction réciproque; un inverse à gauche seulement

**Motif :** Le nom masculin inverse est attesté par Y01; deux identités distinctes portent sur tous les x et y des ensembles respectifs. Aucun sens unique n’est encore prouvé.

**Confiance et limites :** domaines et quantificateurs conservés.

**Question de révision :** La définition en deux clauses séparées serait-elle plus lisible ?

Passages de référence : Y01, Y02, Y03, H17.

## C180 — OLP-0024-B08

**Choix :** Si ; souvent

**Autre formulation envisagée :** on définit toujours f−1

**Motif :** La notation dépend de l’existence d’un inverse; souvent n’anticipe pas une convention universelle ni la preuve d’unicité.

**Confiance et limites :** condition source exacte.

**Question de révision :** L’unicité devrait-elle être mentionnée seulement après sa preuve ?

Passages de référence : Y01, Y02, Y03, H17.

## C181 — OLP-0024-B09

**Choix :** un et un seul ; chaque ; aucun ; ainsi définie

**Autre formulation envisagée :** un x choisi arbitrairement; f doit seulement être surjective

**Motif :** Les guillemets mettent en doute la définition. Unicité et existence pour chaque y sont traitées séparément; ainsi définie restreint la conclusion à cette construction d’inverse, et non à toute fonction g.

**Confiance et limites :** H17/Y01 et les deux contre-cas concordent.

**Question de révision :** La citation de le dans la formule est-elle suffisamment visible au rendu ?

Passages de référence : Y01, Y02, Y03, H17.

## C182 — OLP-0024-B10

**Choix :** Procédons par étapes ; inverse à gauche ; inverse à droite ; cette fois

**Autre formulation envisagée :** antécédent; rétraction/coretraction

**Motif :** Les rôles suivent les identités : g défait f, puis f défait h. Le vocabulaire gauche/droite suit Y01; les synonymes catégoriques ajouteraient un cadre absent.

**Confiance et limites :** direction vérifiée sur les compositions.

**Question de révision :** Les mots gauche/droite deviennent-ils intuitifs avant la définition explicite de composition ?

Passages de référence : Y01, Y02, Y03, H17.

## C183 — OLP-0024-B11

**Choix :** et si $A$ est non vide ; L’unique fonction ; Si les deux ensembles

**Autre formulation envisagée :** toute injection a un inverse à gauche

**Motif :** L’existence d’un inverse exige ici un élément par défaut dans A. Le cas A vide, B non vide est un contre-exemple; le double vide est explicitement sauvegardé dans la note.

**Confiance et limites :** contre-exemple et Y02 confirment la correction.

**Question de révision :** Présenter la condition A≠∅ ou B=∅ dans l’énoncé serait-il plus élégant que la note ?

Passages de référence : Y01, Y02, Y03, H17.

## C184 — OLP-0024-B12

**Choix :** Fixons donc ; dans le premier cas ; dans le second

**Autre formulation envisagée :** choisir un nouvel a pour chaque y

**Motif :** Un seul a fixe règle toutes les valeurs hors image; les antécédents dans l’image sont uniques par injectivité. La construction n’exige pas un choix dans une famille arbitraire. La séparation des deux cas justifie la totalité.

**Confiance et limites :** Y02 et le calcul g(f(x)) concordent.

**Question de révision :** Faut-il préciser x∈A dans la première branche du tableau malgré le contexte ?

Passages de référence : Y01, Y02, Y03, H17.

## C185 — OLP-0024-B13

**Choix :** si ; alors

**Autre formulation envisagée :** établissez la réciproque

**Motif :** La consigne conserve existence d’un inverse gauche comme hypothèse, puis injectivité comme but; aucune hypothèse non-vide supplémentaire n’est nécessaire dans ce sens.

**Confiance et limites :** appliquer g à deux valeurs égales suffit.

**Question de révision :** Le mot réciproque serait-il moins autonome pour cet exercice ?

Passages de référence : Y01, Y02, Y03, H17.

## C186 — OLP-0024-B14

**Choix :** inverse à droite ; pour tout

**Autre formulation envisagée :** une section; un inverse bilatéral

**Motif :** Seule l’identité f(h(y))=y est exigée pour chaque y. L’existence générale relève du choix, explicitement expliqué dans la preuve source suivante.

**Confiance et limites :** Y01 fixe le côté, note OLP conserve l’hypothèse de choix.

**Question de révision :** Une référence à l’axiome du choix devrait-elle apparaître dans l’énoncé lui-même ?

Passages de référence : Y01, Y02, Y03, H17.

## C187 — OLP-0024-B15

**Choix :** pour chaque ; au moins un ; un seul ; axiome du choix ; exactement un

**Autre formulation envisagée :** choisir sans axiome; utiliser le même antécédent pour tous y

**Motif :** La famille d’antécédents est indexée par y. La note source garde le choix général, ses deux branches de renvoi, les cas N/fini et bijectif; exactement un explique pourquoi une bijection n’exige aucun choix arbitraire.

**Confiance et limites :** quantification et exceptions conservées; le cours Yger ne remplace pas la réserve axiomatique d’OLP.

**Question de révision :** La phrase aucun choix à faire devrait-elle préciser aucun choix arbitraire ?

Passages de référence : Y01, Y02, Y03, H17.

## C188 — OLP-0024-B16

**Choix :** inverse à droite ; surjective

**Autre formulation envisagée :** inverse implique bijective

**Motif :** La consigne ne requiert que l’identité à droite, qui produit un antécédent h(y) pour chaque y; elle ne donne pas l’injectivité.

**Confiance et limites :** Y01 et H17 concordent.

**Question de révision :** Le côté droite doit-il être répété dans la solution éventuelle ?

Passages de référence : Y01, Y02, Y03, H17.

## C189 — OLP-0024-B17

**Choix :** une même fonction ; à la fois

**Autre formulation envisagée :** une fonction unique; deux inverses séparés

**Motif :** Une même rend single au sens d’un inverse bilatéral, sans faire porter ici la phrase sur son unicité. Y03 établit la compatibilité des deux côtés.

**Confiance et limites :** rôle logique de la phrase conservé.

**Question de révision :** Une même est-il plus clair que une seule avant le théorème d’unicité ?

Passages de référence : Y01, Y02, Y03, H17.

## C190 — OLP-0024-B18

**Choix :** pour tout $x ; pour tout $y

**Autre formulation envisagée :** pour certains x,y; permutation des domaines

**Motif :** Chaque identité a son quantificateur et son domaine. La notation f−1 conserve la direction B→A, y compris le cas de la bijection vide.

**Confiance et limites :** formules intactes et Y03 concordant.

**Question de révision :** Faut-il ajouter explicitement la fonction vide dans l’exercice ?

Passages de référence : Y01, Y02, Y03, H17.

## C191 — OLP-0024-B19

**Choix :** La démonstration est laissée en exercice

**Autre formulation envisagée :** Exercice

**Motif :** La phrase complète rend la note source sans la faire passer pour une démonstration donnée.

**Confiance et limites :** rôle pédagogique inchangé.

**Question de révision :** L’harmonisation des blocs preuve laissée peut-elle rester identique dans tout le chapitre ?

Passages de référence : Y01, Y02, Y03, H17.

## C192 — OLP-0024-B20

**Choix :** Il faut définir ; puis ; pour tous

**Autre formulation envisagée :** montrer seulement les identités

**Motif :** Trois obligations sont conservées : définir, justifier la fonction, vérifier les deux compositions. Puis organise les étapes sans supprimer les domaines finaux.

**Confiance et limites :** consigne source et définitions concordent.

**Question de révision :** L’existence et l’unicité des antécédents devraient-elles être nommées explicitement ?

Passages de référence : Y01, Y02, Y03, H17.

## C193 — OLP-0024-B21

**Choix :** légèrement plus générale ; induit ; un inverse, ; Cet inverse est unique ; \olref{prop:inverse-unique} ; abus de notation

**Autre formulation envisagée :** f elle-même devient surjective sur B

**Motif :** L’arrivée de f′ est son image, tandis que le domaine et les valeurs restent ceux de f. L’injectivité donne la bijectivité de f′; l’abus ne change pas rétroactivement l’arrivée de f. Le texte corrigé attribue séparément l’existence à prop:bijection-inverse et l’unicité à prop:inverse-unique ; note source-critique visible.

**Confiance et limites :** H17/L15 fixent bijectivité et changement d’arrivée. La source OLP distingue existence (lignes127–131) et unicité (167–174) ; Y03 illustre cette dernière par composition. Renvois maintenant séparés.

**Question de révision :** La référence prospective et la note distinguent-elles assez clairement existence et unicité ?

Passages de référence : Y01, Y02, Y03, H17, L15.

## C194 — OLP-0024-B22

**Choix :** Montrez que ; inverse à gauche ; inverse à droite

**Autre formulation envisagée :** Si ... alors, sans impératif

**Motif :** L’impératif dans un environnement proposition est conservé comme dans la source. Les deux côtés différents sont nécessaires pour conclure h=g.

**Confiance et limites :** Y03 fournit le raisonnement, structure OLP préservée.

**Question de révision :** La source souhaite-t-elle réellement conserver cette proposition sous forme de consigne ?

Passages de référence : Y01, Y02, Y03, H17.

## C195 — OLP-0024-B23

**Choix :** La démonstration est laissée en exercice

**Autre formulation envisagée :** À prouver

**Motif :** Le statut de preuve non fournie reste explicite et renvoie à la proposition précédente.

**Confiance et limites :** renvoi local univoque.

**Question de révision :** Le bloc reste-t-il utile avant l’exercice qui répète la consigne ?

Passages de référence : Y01, Y02, Y03, H17.

## C196 — OLP-0024-B24

**Choix :** Démontrez la

**Autre formulation envisagée :** Prouvez que g=h

**Motif :** La référence rend la consigne autonome et conserve le label; la s’accorde avec proposition.

**Confiance et limites :** référence exacte.

**Question de révision :** Remplacer la référence par la formule ferait-il perdre la portée des hypothèses ?

Passages de référence : Y01, Y02, Y03, H17.

## C197 — OLP-0024-B25

**Choix :** au plus un inverse

**Autre formulation envisagée :** un inverse unique

**Motif :** Au plus un n’affirme pas l’existence pour toute fonction. Le terme inverse reste bilatéral.

**Confiance et limites :** quantification essentielle et Y03 concordants.

**Question de révision :** Le contraste existence/unicité est-il clair après les cas précédents ?

Passages de référence : Y01, Y02, Y03, H17.

## C198 — OLP-0024-B26

**Choix :** deux inverses ; En particulier ; on a

**Autre formulation envisagée :** tous les inverses à gauche sont égaux

**Motif :** Deux inverses bilatéraux fournissent en particulier un gauche et un droite; le résultat précédent s’applique. Deux inverses seulement à gauche peuvent différer hors image.

**Confiance et limites :** dépendance exacte sur Y03.

**Question de révision :** La dernière phrase doit-elle répéter le nom du résultat cité ?

Passages de référence : Y01, Y02, Y03, H17.

## C199 — OLP-0025-B03

**Choix :** Composition des fonctions

**Autre formulation envisagée :** Fonctions composées

**Motif :** Composition nomme l’opération étudiée; composée nommera son résultat dans la définition.

**Confiance et limites :** Y01 atteste la distinction de registre.

**Question de révision :** Le titre au singulier de l’opération reste-t-il cohérent avec Opérations sur les relations ?

Passages de référence : Y01, H18.

## C200 — OLP-0025-B04

**Choix :** d’abord ; puis ; l’image de~$f$ ; incluse dans

**Autre formulation envisagée :** l’arrivée de f doit être égale au domaine de g

**Motif :** La compatibilité générale concerne l’image de f incluse dans le domaine de g, pas l’égalité des ensembles déclarés. Les deux branches initiales donnent on/On grammatical; le produit relatif suit f puis g.

**Confiance et limites :** La condition générale image(f) incluse dans dom(g) vient du texte OLP et du raisonnement direct. H18/Y01 illustrent le cas à ensemble intermédiaire commun et l’ordre d’application ; ils ne formulent pas dans les passages lus la condition générale, et Y01 suppose les ensembles non vides.

**Question de révision :** Le passage du cas général au diagramme avec arrivée B égale au domaine de g est-il assez explicite ?

Passages de référence : Y01, H18.

## C201 — OLP-0025-B05

**Choix :** leur composée ; chaque ; d’abord ; puis ; La composée

**Autre formulation envisagée :** appliquer g puis f; le dessin est la fonction

**Motif :** La construction donne successivement x, y=f(x), z=g(y). La légende garde g∘f malgré l’ordre des arguments de la macro; le diagramme représente la fonction, ne la définit pas à lui seul.

**Confiance et limites :** Y01 et la formule fixent l’ordre; asset encore à inspecter dans le prochain rendu.

**Question de révision :** La macro de composition et la légende seront-elles identiques à l’œil dans le PDF ?

Passages de référence : Y01, H18.

## C202 — OLP-0025-B06

**Choix :** composée ; suivie de

**Autre formulation envisagée :** composition de f avec g

**Motif :** Suivie de rend l’ordre explicite : g est appliquée après f. Composée nomme la fonction obtenue et conserve g(f(x)).

**Confiance et limites :** Y01/H18 concordent.

**Question de révision :** La formule rend-elle inutile suivie de ou cette précision aide-t-elle le premier apprentissage ?

Passages de référence : Y01, H18.

## C203 — OLP-0025-B07

**Choix :** d’abord son successeur ; puis multiplier

**Autre formulation envisagée :** 2x+1; multiplier puis ajouter1

**Motif :** La phrase suit les deux étapes définies; le résultat 2(x+1) conserve les parenthèses, nécessaires pour distinguer l’autre composition.

**Confiance et limites :** calcul direct.

**Question de révision :** Faut-il montrer l’autre composition dans la solution ou préserver l’exemple unique ?

Passages de référence : Y01, H18.

## C204 — OLP-0025-B08

**Choix :** toutes deux ; !!{injective}s

**Autre formulation envisagée :** chacune injective; l’une injective suffit

**Motif :** Toutes deux maintient la conjonction des hypothèses et les tokens féminins pluriels; la conclusion reste au singulier pour la composée.

**Confiance et limites :** H17 et injectivité par deux applications successives concordent.

**Question de révision :** Le pluriel des tokens est-il correctement développé au rendu ?

Passages de référence : Y01, H18, H17.

## C205 — OLP-0025-B09

**Choix :** toutes deux ; !!{surjective}s

**Autre formulation envisagée :** chacune surjective; seule la première surjective

**Motif :** Les deux surjectivités produisent deux antécédents successifs. La composée a pour arrivée C, pas B; accord féminin pluriel des hypothèses conservé.

**Confiance et limites :** H17 et les domaines rendent la preuve exacte.

**Question de révision :** Le changement d’ensemble d’arrivée est-il assez visible dans la consigne ?

Passages de référence : Y01, H18, H17.

## C206 — OLP-0025-B10

**Choix :** le graphe ; est

**Autre formulation envisagée :** le produit Rg suivi de Rf

**Motif :** La relation Rf puis Rg représente le même ordre que g∘f. La consigne porte sur l’égalité des graphes, non des dessins.

**Confiance et limites :** H10/H18 concordent.

**Question de révision :** Faut-il renvoyer explicitement à la définition du produit relatif ?

Passages de référence : Y01, H18, H10.

## C207 — OLP-0026-B04

**Choix :** Fonctions partielles

**Autre formulation envisagée :** Applications partielles

**Motif :** Fonctions suit le vocabulaire déjà choisi; partielles distingue l’assouplissement de totalité sans modifier l’unicité.

**Confiance et limites :** H16/L15 donnent les conventions à distinguer.

**Question de révision :** Application serait-il utile comme synonyme plus tard ?

Passages de référence : H16, L15.

## C208 — OLP-0026-B05

**Choix :** n’exigeant plus ; pour toute entrée

**Autre formulation envisagée :** autoriser plusieurs valeurs

**Motif :** L’assouplissement retire seulement l’existence pour toutes les entrées, jamais l’unicité lorsqu’une valeur existe.

**Confiance et limites :** H16 et OLP concordent sur cette distinction.

**Question de révision :** La négation de toute entrée reste-t-elle lisible sans symbolisation ?

Passages de référence : H16, L15.

## C209 — OLP-0026-B06

**Choix :** au plus un ; non définie ; la partie de~$A$

**Autre formulation envisagée :** indéfinie; domaine égal à A

**Motif :** Au plus un laisse zéro ou une valeur. Non définie évite indéterminée, qui suggérerait plusieurs valeurs. Définie s’accorde avec valeur/fonction; domaine désigne ici l’ensemble effectif, possiblement strictement inclus dans A.

**Confiance et limites :** H16 atteste domaine effectif; conventions OLP conservées.

**Question de révision :** Ensemble de départ serait-il utile pour nommer A sans le confondre avec dom(f) ?

Passages de référence : H16, L15.

## C210 — OLP-0026-B07

**Choix :** définies partout ; jusqu’ici ; totales

**Autre formulation envisagée :** totale signifie surjective

**Motif :** Toute fonction antérieure est totale sur A; la totalité concerne les entrées et non la couverture de B. Jusqu’ici signale un changement de vocabulaire maîtrisé.

**Confiance et limites :** H17 est consulté uniquement pour distinguer surjectivité (couverture de l’arrivée) et totalité (définition sur les entrées). Il n’atteste pas le lexème totale ; la convention est celle d’OLP, éclairée par L15/H16.

**Question de révision :** Faut-il répéter que total n’est pas surjectif dans un encadré ?

Passages de référence : H16, L15, H17.

## C211 — OLP-0026-B08

**Choix :** pour $x = 0$ ; partout ailleurs

**Autre formulation envisagée :** la fonction n’existe pas; indéfinie sur R

**Motif :** Une seule entrée est exclue. La fonction partielle est définie sur R\{0}; la déclaration R⇀R reste inchangée.

**Confiance et limites :** exemple arithmétique exact.

**Question de révision :** Non définie est-il assez distinct de non continue pour ce lectorat ?

Passages de référence : H16, L15.

## C212 — OLP-0026-B09

**Choix :** un unique ; sinon ; pour tout $x ; pour tout $y

**Autre formulation envisagée :** choisir un antécédent même s’il n’est pas unique

**Motif :** Le sinon couvre absence et multiplicité; sous injectivité, les identités portent seulement sur dom(f) et ran(f). Aucun axiome du choix n’est nécessaire pour les valeurs uniques.

**Confiance et limites :** H16/H17 et les domaines rendent les conclusions correctes.

**Question de révision :** La notion d’injectivité des fonctions partielles devrait-elle être rappelée dans la consigne ?

Passages de référence : H16, L15, H17.

## C213 — OLP-0026-B10

**Choix :** Graphe d’une fonction partielle ; définie par

**Autre formulation envisagée :** compléter par des couples pour les entrées non définies

**Motif :** Le graphe contient seulement les valeurs effectivement définies; la même formule que pour les fonctions totales n’impose aucune entrée supplémentaire.

**Confiance et limites :** H16 définit précisément ce type de graphe.

**Question de révision :** La convention f(x)=y lorsque f(x) est définie demande-t-elle une note ?

Passages de référence : H16, L15.

## C214 — OLP-0026-B11

**Choix :** chaque fois que ; sinon ; sérielle ; pour chaque

**Autre formulation envisagée :** totale à gauche; sérielle implique surjective

**Motif :** La première propriété assure une valeur au plus, le sinon l’absence de valeur. Sérielle est un choix lexical provisoire, non attribué à H16; sa définition exacte ∀x∃y vient d’OLP et assure la totalité, pas la surjectivité.

**Confiance et limites :** sens formel certain, attestation lexicale dédiée à compléter lors de la logique modale.

**Question de révision :** Totale à gauche serait-il moins ambigu tout en restant compatible avec les futurs cadres modaux ?

Passages de référence : H16, L15.

## C215 — OLP-0026-B12

**Choix :** lorsqu’il existe ; unique ; totale si

**Autre formulation envisagée :** l’existence de y suit de l’unicité

**Motif :** La preuve établit unicité conditionnelle, suffisante pour une fonction partielle. Seule l’hypothèse sérielle garantit existence partout; Rf=R conserve toutes et seulement les valeurs de la relation.

**Confiance et limites :** les deux obligations sont correctement séparées.

**Question de révision :** Le parallèle avec la preuve des fonctions totales aide-t-il à comprendre la différence ?

Passages de référence : H16, L15.

## C216 — OLP-0020-B03

**Choix :** Fonctions

**Autre formulation envisagée :** Applications

**Motif :** Le titre conserve fonction pour la notion totale du manuel ; application reste disponible dans les témoins, sans changer la convention.

**Confiance et limites :** cohérence avec toutes les six sections et la notation totale de Lyon.

**Question de révision :** Le titre permet-il de retrouver sans ambiguïté les fonctions partielles de la dernière section ?

Passages de référence : L15, H16.

## C217 — OLP-0021-B03

**Choix :** Notions de base

**Autre formulation envisagée :** Généralités

**Motif :** Le titre annonce des définitions et des exemples, sans suggérer des résultats généraux.

**Confiance et limites :** portée introductive vérifiée dans la section entière.

**Question de révision :** Notions de base annonce-t-il assez précisément la distinction entre fonction et méthode de calcul ?

Passages de référence : L15, H16.

## C218 — OLP-0021-B04

**Choix :** associe à chaque ; qui peut être le même ; l’unique nombre

**Autre formulation envisagée :** Envoie chaque élément dans un autre ensemble

**Motif :** Associer exprime la correspondance, chaque et unique conservent totalité et univocité ; la parenthèse source autorise le même ensemble.

**Confiance et limites :** les quantificateurs sont explicites et l’exemple du successeur les vérifie.

**Question de révision :** La précision sur le même ensemble est-elle placée sans interrompre la définition ?

Passages de référence : L15, H16.

## C219 — OLP-0021-B05

**Choix :** couples,
des triplets ; en renvoient un troisième

**Autre formulation envisagée :** Prend des paires et retourne des sorties

**Motif :** Couples et triplets portent l’ordre des entrées ; le singulier troisième désigne le résultat des opérations binaires.

**Confiance et limites :** le produit cartésien de l’exemple suivant fixe l’interprétation.

**Question de révision :** Le vocabulaire entrée et sortie facilite-t-il ici le passage du calcul à la correspondance abstraite ?

Passages de référence : L15, H16.

## C220 — OLP-0021-B06

**Choix :** boîte noire ; seule compte la sortie associée à chaque entrée

**Autre formulation envisagée :** La fonction est son algorithme

**Motif :** La métaphore conservée isole les valeurs de leur méthode de calcul ; elle prépare l’extensionnalité sans identifier fonction et procédure. L15/H16 soutiennent le contexte extensionnel, sans attester boîte noire dans ces passages. L’alternative historique La fonction est son algorithme change le sens et est désormais étiquetée comme contre-exemple sémantique, sans inventer une délibération antérieure.

**Confiance et limites :** opposition explicite du texte source et exemple ultérieur de deux formules.

**Question de révision :** La restriction seule compte anticipe-t-elle suffisamment la fixation du domaine et de l’arrivée ?

Passages de référence : L15, H16.

## C221 — OLP-0021-B07

**Choix :** associe à chaque ; un unique

**Autre formulation envisagée :** Associe un élément à certains éléments

**Motif :** Chaque et unique rendent la convention totale du manuel explicite ; Habermehl admet ailleurs les fonctions partielles et n’impose donc pas sa convention.

**Confiance et limites :** confirmation par l’introduction et la dernière section.

**Question de révision :** Faut-il rappeler localement que cette convention diffère de certains cours français ?

Passages de référence : L15, H16.

## C222 — OLP-0021-B08

**Choix :** domaine ; ensemble d’arrivée ; valeur de~$f$

**Autre formulation envisagée :** Domaine de départ, codomaine, résultat

**Motif :** Ensemble d’arrivée se distingue immédiatement de l’image ; valeur en x et arguments relient le langage usuel à la notation f(x).

**Confiance et limites :** domaine et image sont attestés ; ensemble d’arrivée est un choix explicatif de registre.

**Question de révision :** La succession de ces quatre termes reste-t-elle lisible lors d’une première rencontre ?

Passages de référence : L15, H16.

## C223 — OLP-0021-B09

**Choix :** partie de son ensemble d’arrivée ; valeurs effectivement prises

**Autre formulation envisagée :** L’étendue est l’ensemble des sorties possibles

**Motif :** Image suit Lyon et Habermehl ; effectivement prises évite de confondre les membres de B avec les valeurs atteintes.

**Confiance et limites :** formule inchangée et exemple du successeur.

**Question de révision :** Le mot effectivement risque-t-il d’évoquer à tort la calculabilité effective ?

Passages de référence : L15, H16.

## C224 — OLP-0021-B10

**Choix :** aide à se représenter ; part d’un ; aboutit à la

**Autre formulation envisagée :** Illustre un transfert du domaine au codomaine

**Motif :** Les verbes décrivent les flèches sans transformer la fonction en processus temporel ; chaque flèche relie argument et valeur.

**Confiance et limites :** correspondance vérifiable sur le diagramme.

**Question de révision :** Les deux ellipses et le sens des flèches suffisent-ils à identifier l’image comme sous-ensemble ?

Passages de référence : L15, H16.

## C225 — OLP-0021-B11

**Choix :** associe à chaque ; aboutit à la valeur correspondante

**Autre formulation envisagée :** Met en relation des éléments

**Motif :** La légende conserve la totalité et le sens des flèches ; l’unicité a été donnée dans la définition immédiatement précédente.

**Confiance et limites :** légende cohérente avec la définition et l’asset original.

**Question de révision :** La légende gagnerait-elle à répéter unique sans devenir redondante ?

Passages de référence : L15, H16.

## C226 — OLP-0021-B12

**Choix :** couples d’entiers naturels ; Son image est elle aussi

**Autre formulation envisagée :** Multiplication de naturels dans les naturels

**Motif :** L’entrée est un couple et non un seul entier ; n fois 1 prouve que chaque naturel appartient à l’image, zéro inclus.

**Confiance et limites :** domaine produit et témoin de surjectivité exacts.

**Question de révision :** La préposition dans conserve-t-elle clairement la distinction domaine/arrivée ?

Passages de référence : L15, H16.

## C227 — OLP-0021-B13

**Choix :** unique sortie ; strictement positif ; positive ou nulle

**Autre formulation envisagée :** Racine positive

**Motif :** La racine retenue doit inclure zéro ; strictement positif réserve les deux racines distinctes aux n non nuls. La précision est signalée en note.

**Confiance et limites :** contre-exemple n=0 et deux racines pour n>0.

**Question de révision :** La note explique-t-elle suffisamment pourquoi positive ou nulle corrige le domaine de la source ?

Passages de référence : L15, H16.

## C228 — OLP-0021-B14

**Choix :** sa note finale ; ne peut pas recevoir deux ; zéro, deux
ou davantage

**Autre formulation envisagée :** Chaque étudiant a exactement deux parents

**Motif :** Le texte conserve l’exemple conventionnel de la note finale et les possibilités données pour les parents, sans ajouter de présupposé familial.

**Confiance et limites :** fidélité à l’exemple ; l’existence de la note est présupposée par sa note finale.

**Question de révision :** Cet exemple conventionnel reste-t-il assez clair pour distinguer absence et multiplicité des valeurs ?

Passages de référence : L15, H16.

## C229 — OLP-0021-B15

**Choix :** chaque
argument possible ; une valeur et une seule

**Autre formulation envisagée :** On peut donner une formule qui calcule f

**Motif :** La liste de méthodes est conservée sans restreindre les fonctions aux fonctions calculables ; le dernier énoncé porte sur toute méthode.

**Confiance et limites :** totalité et univocité clairement distinguées de la présentation.

**Question de révision :** Une liste des valeurs évoque-t-elle inutilement une énumération effective dans le cas infini ?

Passages de référence : L15, H16.

## C230 — OLP-0021-B16

**Choix :** son
successeur ; n’est le successeur d’aucun ; strictement positifs

**Autre formulation envisagée :** L’image est l’ensemble d’arrivée

**Motif :** L’absence d’antécédent de zéro explique exactement pourquoi l’image est plus petite ; strictement positifs respecte Nat contenant zéro.

**Confiance et limites :** calcul direct et convention initiale.

**Question de révision :** Le contraste des deux ensembles est-il suffisamment explicite sans nouvelle notation ?

Passages de référence : L15, H16.

## C231 — OLP-0021-B17

**Choix :** À un entier naturel~$x$ ; du successeur du successeur

**Autre formulation envisagée :** À n elle associe le prédécesseur de x

**Motif :** La même variable x est employée comme entrée et dans le calcul ; la coquille n/x est signalée et l’ordre des trois opérations conservé.

**Confiance et limites :** x+2-1=x+1 pour tout naturel.

**Question de révision :** La répétition successeur est-elle préférable ici à une simplification qui effacerait l’exemple ?

Passages de référence : L15, H16.

## C232 — OLP-0021-B18

**Choix :** même fonction ; principe d’extensionnalité ; à condition que

**Autre formulation envisagée :** Deux formules égales sont la même fonction

**Motif :** L’identité porte sur les fonctions malgré deux définitions ; la condition commune de domaine et d’arrivée limite explicitement le principe.

**Confiance et limites :** formule, calcul et condition de typage vérifiés ensemble.

**Question de révision :** La distinction correspondance/fonction typée demeure-t-elle cohérente avec la section sur les graphes ?

Passages de référence : L15, H16, L01.

## C233 — OLP-0021-B19

**Choix :** définir une fonction par cas ; cas disjoints ; qu’ils attribuent la même valeur ; doivent néanmoins être couvertes

**Autre formulation envisagée :** Toute définition par cas exige des cas mutuellement exclusifs

**Motif :** La partition pair/impair est une méthode suffisante ; la source en fait abusivement une nécessité générale. La note autorise les recouvrements compatibles sans perdre l’exhaustivité.

**Confiance et limites :** deux cas x≥0 et x≤0 donnant x définissent l’identité malgré leur intersection.

**Question de révision :** La distinction entre condition suffisante disjointe et condition générale compatible est-elle nette ?

Passages de référence : L15, H16.

## C234 — OLP-0022-B03

**Choix :** Types de fonctions

**Autre formulation envisagée :** Espèces de fonctions

**Motif :** Types annonce les propriétés injective, surjective et bijective sans introduire une théorie des types.

**Confiance et limites :** sens fixé immédiatement par les trois propriétés.

**Question de révision :** Le titre peut-il être confondu avec le typage domaine/arrivée vu auparavant ?

Passages de référence : H17, H16.

## C235 — OLP-0022-B04

**Choix :** classer certains types ; fréquemment

**Autre formulation envisagée :** Introduire une taxonomie

**Motif :** Classer évite un terme abstrait inutile ; certains et fréquemment maintiennent la portée limitée de la classification.

**Confiance et limites :** aucune exhaustivité ajoutée.

**Question de révision :** Cette phrase de transition peut-elle rester aussi courte sans perdre sa fonction pédagogique ?

Passages de référence : H17, H16.

## C236 — OLP-0022-B05

**Choix :** chaque élément de l’ensemble
d’arrivée ; valeur prise

**Autre formulation envisagée :** Chaque valeur possède un argument

**Motif :** Chaque porte sur B entier ; la formulation évite la tautologie qui consisterait à ne parler que des valeurs déjà atteintes.

**Confiance et limites :** équivalence avec le quantificateur universel sur B.

**Question de révision :** La référence à la figure après surjectives est-elle suffisamment immédiate ?

Passages de référence : H17, H16.

## C237 — OLP-0022-B06

**Choix :** Une fonction !!{surjective} ; chaque
    !!{element}

**Autre formulation envisagée :** Une application couvrante

**Motif :** Surjective conserve le terme technique de Habermehl ; la légende donne le critère de couverture de B.

**Confiance et limites :** féminin requis par fonction.

**Question de révision :** La légende suffit-elle à montrer que plusieurs flèches peuvent atteindre le même point ?

Passages de référence : H17, H16.

## C238 — OLP-0022-B07

**Choix :** si et
seulement si ; pour tout ; au moins un

**Autre formulation envisagée :** Si chaque y a exactement un antécédent

**Motif :** Au moins un préserve l’existence sans ajouter l’injectivité ; le biconditionnel définit la propriété.

**Confiance et limites :** ordre et portée des quantificateurs identiques.

**Question de révision :** L’explication avant la formule prépare-t-elle clairement la dépendance de x envers y ?

Passages de référence : H17, H16.

## C239 — OLP-0022-B08

**Choix :** chaque
objet ; une certaine
entrée

**Autre formulation envisagée :** Trouver une entrée qui donne toutes les sorties

**Motif :** La phrase garde pour tout objet puis une entrée dépendante de cet objet, sans permuter les quantificateurs.

**Confiance et limites :** consigne équivalente à la définition précédente.

**Question de révision :** Une certaine entrée peut-elle être lue par erreur comme fixée une fois pour toutes ?

Passages de référence : H17, H16.

## C240 — OLP-0022-B09

**Choix :** induit ; $f' \colon A \to \ran{f}$ ; nécessairement

**Autre formulation envisagée :** Toute fonction est surjective

**Motif :** La nouvelle fonction f′ conserve les valeurs mais change l’arrivée ; induit ne confond donc pas f avec f′ dans la convention typée.

**Confiance et limites :** typage et formule du graphe respectés.

**Question de révision :** Faut-il accentuer davantage que c’est l’arrivée et non la règle qui change ?

Passages de référence : H17, H16.

## C241 — OLP-0022-B10

**Choix :** en outre ; ne jamais associer ; deux entrées différentes

**Autre formulation envisagée :** Une fonction injective donne une seule valeur

**Motif :** En outre distingue l’injectivité de l’univocité déjà exigée ; la négation porte sur l’égalité des sorties pour deux entrées distinctes.

**Confiance et limites :** corps et légende expriment le même critère.

**Question de révision :** La répétition entre corps et légende aide-t-elle la lecture du schéma ?

Passages de référence : H17, H16.

## C242 — OLP-0022-B11

**Choix :** au plus un ; !!a{injection}

**Autre formulation envisagée :** Chaque y a un antécédent

**Motif :** Au plus un autorise l’absence d’antécédent et empêche la confusion avec surjection ; féminin contrôlé dans les macros.

**Confiance et limites :** convention et définition de Habermehl compatibles.

**Question de révision :** La formulation par les fibres est-elle bien reliée au critère par égalité des images juste après ?

Passages de référence : H17, H16.

## C243 — OLP-0022-B12

**Choix :** pour tous les ; si $f(x)=f(y)$, alors $x=y$

**Autre formulation envisagée :** Si x=y alors f(x)=f(y)

**Motif :** La consigne conserve la direction caractéristique de l’injectivité ; l’autre implication n’est que l’univocité.

**Confiance et limites :** implication et domaine vérifiés.

**Question de révision :** Le choix des variables x et y reste-t-il clair après leur autre rôle dans la définition précédente ?

Passages de référence : H17, H16.

## C244 — OLP-0022-B13

**Choix :** n’est ni !!{injective} ni !!{surjective}

**Autre formulation envisagée :** La constante n’est pas bijective

**Motif :** Ni…ni affirme les deux échecs : 0 et 1 ont la même image, et zéro n’est pas atteint.

**Confiance et limites :** témoins explicites avec Nat contenant zéro.

**Question de révision :** Les deux contre-exemples doivent-ils être laissés au lecteur comme dans la source ?

Passages de référence : H17, H16.

## C245 — OLP-0022-B14

**Choix :** fonction identité ; à la fois

**Autre formulation envisagée :** Fonction identique

**Motif :** Identité est le nom mathématique attesté ; à la fois affirme séparément les deux propriétés.

**Confiance et limites :** toute valeur a elle-même pour unique antécédent.

**Question de révision :** Le terme fonction identité est-il préférable ici à application identique ?

Passages de référence : H17, H16.

## C246 — OLP-0022-B15

**Choix :** fonction successeur ; mais n’est pas

**Autre formulation envisagée :** La fonction suivante

**Motif :** Successeur nomme x↦x+1 ; mais relie injectivité vraie et surjectivité fausse, cette dernière dépendant de zéro.

**Confiance et limites :** x+1=y+1 implique x=y, et zéro n’est pas atteint.

**Question de révision :** Le rappel du domaine Nat suffit-il pour ne pas généraliser le résultat à Int ?

Passages de référence : H17, H16.

## C247 — OLP-0022-B16

**Choix :** si $x$ est pair ; si $x$ est impair. ; mais n’est pas !!{injective}

**Autre formulation envisagée :** Elle est injective mais non surjective

**Motif :** Chaque k est atteint par 2k, tandis que 1 et 2 ont l’image 1 ; les deux branches restent des naturels.

**Confiance et limites :** calculs directs, y compris k=0.

**Question de révision :** Les exemples précédents rendent-ils souhaitable une justification de cette dernière propriété ?

Passages de référence : H17, H16.

## C248 — OLP-0022-B17

**Choix :** à la fois !!{injective}s ; correspondances biunivoques ; de manière unique

**Autre formulation envisagée :** Correspondances un-à-un

**Motif :** Biunivoque rend le vocabulaire explicatif de la source ; Habermehl atteste bijective et sa définition, pas ce synonyme exact.

**Confiance et limites :** définition solide, synonyme choisi éditorialement sans fausse attribution.

**Question de révision :** Le synonyme biunivoque ajoute-t-il une aide réelle pour le public visé ?

Passages de référence : H17, H16.

## C249 — OLP-0022-B18

**Choix :** si et seulement ; entre $A$ et~$B$

**Autre formulation envisagée :** Une bijection est seulement une injection

**Motif :** Les deux propriétés sont nécessaires et suffisantes ; entre conserve la possibilité d’une correspondance inverse sans l’introduire encore.

**Confiance et limites :** définition conjonctive inchangée.

**Question de révision :** La coexistence de de A dans B et entre A et B reste-t-elle transparente ?

Passages de référence : H17, H16.

## C250 — OLP-0028-B04

**Choix :** Introduction

**Autre formulation envisagée :** Présentation

**Motif :** Le titre garde sa fonction d’ouverture sans anticiper les résultats techniques.

**Confiance et limites :** titre identique de portée.

**Question de révision :** Faut-il un titre plus descriptif dans la table générale ?

Passages de référence : L10.

## C251 — OLP-0028-B05

**Choix :** faire admettre ; infini en acte ; tous distincts ; Ont-ils tous la même taille ?

**Autre formulation envisagée :** Rendre acceptable l’idée d’un infini achevé

**Motif :** Infini en acte est attesté par V01 ; faire admettre rend palatable sans notion de goût. L’attribution médiévale reste celle d’OLP, non une conclusion de V01. La distinction des trois objets et la question sur tous les infinis sont conservées.

**Confiance et limites :** terme philosophique directement attesté ; chronologie et attribution limitées à l’original.

**Question de révision :** Le conditionnel suffit-il à préserver la prudence de l’allusion médiévale ?

Passages de référence : V01, L10.

## C252 — OLP-0028-B06

**Choix :** dresser
la liste ; certains ensembles
infinis ; elle-même infinie

**Autre formulation envisagée :** Énumérer les éléments dans une liste éventuellement infinie

**Motif :** La liste est l’objet qui peut être infini ; certains ne porte pas sur les éléments. Au plus dénombrable sera explicitement inclusif, selon L10 et la définition OLP suivante.

**Confiance et limites :** convention inclusive établie ; annonce conservée sans ajouter d’algorithme.

**Question de révision :** La première occurrence précède-t-elle de trop loin la convention expliquée dans la section suivante ?

Passages de référence : L10.

## C253 — OLP-0029-B04

**Choix :** Énumérations et ensembles \usetoken{p}{enumerable}

**Autre formulation envisagée :** Listes et ensembles au plus dénombrables

**Motif :** Énumérations conserve le terme défini ; la forme plurielle p accorde l’adjectif avec ensembles dans un titre français.

**Confiance et limites :** macro p vérifiée dans open-logic-tokenize.sty.

**Question de révision :** La longueur du titre reste-t-elle compatible avec les en-têtes ?

Passages de référence : L10, L15, H17.

## C254 — OLP-0029-B05

**Choix :** procède progressivement ; au plus dénombrable ; sans condition de
calculabilité

**Autre formulation envisagée :** Dénombrable, avec une convention incluant les ensembles finis

**Motif :** La forme explicite choisie après lecture d’OLP tranche la préférence C21. La note distingue existence d’une énumération et algorithme. L10 atteste l’usage inclusif, sans imposer sa formulation.

**Confiance et limites :** définition source vide ou surjection et conventions Lyon directement comparées.

**Question de révision :** La distinction calculabilité doit-elle être rappelée seulement lors du futur chapitre informatique ?

Passages de référence : L10, L15, H17.

## C255 — OLP-0029-B06

**Choix :** comment et dans
quels cas ; même infini

**Autre formulation envisagée :** Dans quelles conditions peut-on énumérer les éléments ?

**Motif :** Comment et dans quels cas conserve la méthode et l’existence ; même infini étend la question sans promettre une énumération universelle.

**Confiance et limites :** deux axes interrogatifs gardés.

**Question de révision :** La transition avec l’introduction paraît-elle trop répétitive ?

Passages de référence : L10, L15, H17.

## C256 — OLP-0029-B07

**Choix :** éventuellement infinie ; chaque
!!{element} ; position finie

**Autre formulation envisagée :** Une liste finie ou infinie où tout élément apparaît à un rang fini

**Motif :** Chaque élément de A doit apparaître, mais les répétitions restent permises ; finie qualifie la position, non nécessairement la liste.

**Confiance et limites :** quantificateurs et possibilité d’infinitude conservés.

**Question de révision :** Position ou rang sera-t-il le plus clair avant le passage aux fonctions ?

Passages de référence : L10, L15, H17.

## C257 — OLP-0029-B08

**Choix :** Sauf pour la liste vide ; Nous exigeons
  en outre ; comptent ; positions finies

**Autre formulation envisagée :** Une liste non vide commence par un terme et tous ses termes ont un rang naturel

**Motif :** L’exception vide explicite le dernier item. Le rang fini est une condition, non la conséquence d’un simple prédécesseur immédiat : un ordre de type 1+Z réfute cette conséquence. L’ordre distingue les listes, tandis que les répétitions ne changent pas l’ensemble énuméré ; les sept remarques et tous les exemples demeurent.

**Confiance et limites :** contre-exemple ordinal élémentaire et positions des listes contrôlés ; précision signalée.

**Question de révision :** La note sur le prédécesseur est-elle suffisamment précise sans introduire les ordinaux ?

Passages de référence : L10, L15, H17.

## C258 — OLP-0029-B09

**Choix :** il en possède une sans répétitions

**Autre formulation envisagée :** Toute énumération peut être remplacée par une énumération sans doublons

**Motif :** L’existence d’une autre liste ne prétend pas que la liste donnée soit injective ni que son domaine formel reste infini.

**Confiance et limites :** convention informelle encore active.

**Question de révision :** Faut-il rappeler informelle avant la définition par surjection qui suit ?

Passages de référence : L10, L15, H17.

## C259 — OLP-0029-B10

**Choix :** Si $A$ est vide ; on conserve $x_i$ ; on le retire

**Autre formulation envisagée :** Ne conserver que la première occurrence de chaque élément

**Motif :** La règle élimine les occurrences ultérieures, sans choisir un représentant par une famille de choix. Le cas vide est énoncé avant d’introduire x1.

**Confiance et limites :** chaque élément garde sa première occurrence ; aucun algorithme de décision de l’égalité n’est supposé.

**Question de révision :** Le langage retirer risque-t-il de suggérer une procédure calculable ?

Passages de référence : L10, L15, H17.

## C260 — OLP-0029-B11

**Choix :** une définition plus précise

**Autre formulation envisagée :** Une définition rigoureuse permettra de démontrer ces propriétés

**Motif :** Plus précise prépare le changement de représentation sans déclarer l’explication précédente erronée.

**Confiance et limites :** transition pédagogique fidèle.

**Question de révision :** Le renvoi à ce dernier raisonnement reste-t-il clair après la note ?

Passages de référence : L10, L15, H17.

## C261 — OLP-0029-B12

**Choix :** $A \neq \emptyset$ ; fonction !!{surjective}

**Autre formulation envisagée :** Une surjection de PosInt sur A non vide

**Motif :** Le domaine formel est PosInt entier ; l’arrivée doit être atteinte totalement. L’exclusion du vide évite de demander une fonction d’un ensemble non vide vers le vide.

**Confiance et limites :** typage source et totalité vérifiés.

**Question de révision :** La différence entre listes finies et surjections infinies apparaît-elle assez tôt ?

Passages de référence : L10, L15, H17.

## C262 — OLP-0029-B13

**Choix :** correspond à ; un certain~$n ; pas nécessairement !!{injective}

**Autre formulation envisagée :** Une surjection fournit la suite de ses valeurs, avec répétitions possibles

**Motif :** La correspondance est expliquée comme représentation ; pour chaque valeur, un rang fini existe et peut dépendre d’elle. L’absence éventuelle d’injectivité autorise les répétitions.

**Confiance et limites :** les quantificateurs suivent la définition de surjectivité.

**Question de révision :** Correspond à est-il préférable à une égalité littérale de définitions ?

Passages de référence : L10, L15, H17.

## C263 — OLP-0029-B14

**Choix :** son dernier
!!{element} ; toute liste non vide qui énumère~$A$

**Autre formulation envisagée :** Prolonger une liste finie non vide en répétant son dernier terme

**Motif :** La dernière valeur fournit toutes les entrées restantes ; aucune dernière valeur n’est requise pour une liste infinie. L’exception vide demeure explicite.

**Confiance et limites :** prolongement total et surjectivité vérifiés.

**Question de révision :** La clause si elle n’a pas de n-ième terme exprime-t-elle assez clairement la finitude ?

Passages de référence : L10, L15, H17.

## C264 — OLP-0029-B15

**Choix :** si et seulement s’il est vide
ou possède

**Autre formulation envisagée :** Être vide ou admettre une surjection depuis PosInt

**Motif :** Le biconditionnel inclut séparément le vide, qui n’a pas d’énumération au sens formel juste défini.

**Confiance et limites :** les deux cas couvrent exactement la convention inclusive.

**Question de révision :** La convention terminologique est-elle maintenant suffisamment établie ?

Passages de référence : L10, L15, H17.

## C265 — OLP-0029-B16

**Choix :** strictement positifs ; $g(n) = n - 1$

**Autre formulation envisagée :** L’identité énumère PosInt et le décalage de un énumère Nat

**Motif :** Strictement distingue l’arrivée PosInt du domaine Nat contenant zéro ; l’entrée commence à1 dans les deux fonctions.

**Confiance et limites :** images exactes calculées.

**Question de révision :** Faut-il rappeler explicitement le domaine commun des deux fonctions ?

Passages de référence : L10, L15, H17.

## C266 — OLP-0029-B17

**Choix :** respectivement ; aucune n’est !!{surjective} sur cet ensemble

**Autre formulation envisagée :** Leurs images sont les pairs positifs et les impairs, et aucune n’atteint tout PosInt

**Motif :** Respectivement conserve l’association aux deux formules ; sur cet ensemble fixe l’arrivée complète, différente des sous-ensembles énumérés.

**Confiance et limites :** f manque les impairs et g les pairs.

**Question de révision :** Le mot énumèrent, appliqué à des fonctions non surjectives vers PosInt, demande-t-il une mention d’arrivée restreinte ?

Passages de référence : L10, L15, H17.

## C267 — OLP-0029-B18

**Choix :** carrés strictement positifs

**Autre formulation envisagée :** Donnez une fonction énumérant les carrés non nuls

**Motif :** La liste commence à1 ; strictement prévient une inclusion involontaire du carré nul.

**Confiance et limites :** valeurs de la liste et domaine PosInt cohérents.

**Question de révision :** L’exemple n² suffit-il comme réponse implicite à l’exercice ?

Passages de référence : L10, L15, H17.

## C268 — OLP-0029-B19

**Choix :** plafond ; supérieur
ou égal ; rétablit la valeur $-3$

**Autre formulation envisagée :** La partie entière supérieure arrondit vers le haut

**Motif :** Plafond est un choix éditorial défini explicitement, sans fausse attestation dans L10/H17. La formule donne0,1,−1,2,−2,3,−3 ; le tableau omettait−3 sous f(7). La note signale sa restauration, et les trois cas restent inchangés.

**Confiance et limites :** sept calculs et formule par cas vérifiés ; vocabulaire plafond non attesté par les passages liés.

**Question de révision :** Partie entière supérieure serait-elle plus familière que plafond pour ce lectorat ?

Passages de référence : L10, L15, H17.

## C269 — OLP-0029-B20

**Choix :** $A \cup B$ l’est aussi ; Traitez aussi les cas

**Autre formulation envisagée :** Construisez une énumération de la réunion en traitant séparément les ensembles vides

**Motif :** Deux surjections ne sont supposées qu’au stade de la construction principale ; l’exercice exige aussi les cas où cette supposition n’existe pas.

**Confiance et limites :** hypothèses et cas vides préservés.

**Question de révision :** L’ordre de la consigne indique-t-il assez clairement que le cas vide se traite à part ?

Passages de référence : L10, L15, H17.

## C270 — OLP-0029-B21

**Choix :** $B \subseteq A$ ; Que se passe-t-il si
$B = \emptyset$ ?

**Autre formulation envisagée :** Établissez qu’une partie d’un ensemble au plus dénombrable l’est encore

**Motif :** L’inclusion fixe le sens du résultat ; la question finale empêche d’exiger une surjection vers B vide. L10 donne un motif proche de sélection de première préimage, non toute cette preuve.

**Confiance et limites :** direction et exception contrôlées.

**Question de révision :** La question finale doit-elle aussi rappeler implicitement le cas A vide ?

Passages de référence : L10, L15, H17.

## C271 — OLP-0029-B22

**Choix :** par récurrence sur $n$ ; tous !!{enumerable}s

**Autre formulation envisagée :** Déduisez par récurrence le résultat pour une réunion finie

**Motif :** La portée tous concerne les n ensembles ; le résultat de réunion binaire peut être admis, sans importation d’un théorème de réunion dénombrable.

**Confiance et limites :** induction finie et prémisse permise conservées.

**Question de révision :** La base n=0, si admise, doit-elle être rappelée lors de la révision finale ?

Passages de référence : L10, L15, H17.

## C272 — OLP-0029-B23

**Choix :** terme d’indice~$0$ ; Les deux définitions sont équivalentes

**Autre formulation envisagée :** Numéroter à partir de zéro au lieu de un

**Motif :** Indices évite le calque zéroième ; l’équivalence porte sur l’existence d’énumérations après décalage, non sur l’égalité des listes indexées.

**Confiance et limites :** Nat et PosInt clairement distingués.

**Question de révision :** L’introduction du mot indice prépare-t-elle correctement les preuves suivantes ?

Passages de référence : L10, L15, H17.

## C273 — OLP-0029-B24

**Choix :** si et seulement
s’il existe

**Autre formulation envisagée :** Les surjections depuis Nat et depuis PosInt existent dans les mêmes cas

**Motif :** L’énoncé conserve les deux sens, y compris le cas A vide où les deux existences sont fausses.

**Confiance et limites :** bijection de décalage entre les domaines.

**Question de révision :** La formulation d’existence évite-t-elle assez clairement une identification des fonctions ?

Passages de référence : L10, L15, H17.

## C274 — OLP-0029-B25

**Choix :** $g(n) = f(n+1)$ ; $f(n) = g(n-1)$

**Autre formulation envisagée :** Précomposer avec les deux décalages inverses

**Motif :** Les domaines garantissent n+1 positif et n−1 naturel ; les deux transformations préservent toute l’image.

**Confiance et limites :** bornes et surjectivité vérifiées.

**Question de révision :** Aisément garde-t-il le ton pédagogique sans escamoter un point difficile ?

Passages de référence : L10, L15, H17.

## C275 — OLP-0029-B26

**Choix :** On obtient ainsi

**Autre formulation envisagée :** Il en résulte que

**Motif :** Ainsi relie le corollaire à la définition et au décalage, sans ajouter une nouvelle hypothèse.

**Confiance et limites :** dépendance locale immédiate.

**Question de révision :** Cette transition suffit-elle à retrouver les deux prémisses ?

Passages de référence : L10, L15, H17.

## C276 — OLP-0029-B27

**Choix :** s’il est vide
ou s’il existe

**Autre formulation envisagée :** Le cas vide ou une surjection depuis Nat caractérise la dénombrabilité inclusive

**Motif :** Le vide reste séparé de l’existence de fonction, même lorsque le domaine de numérotation change.

**Confiance et limites :** dérivation du corollaire et exception exacte.

**Question de révision :** La répétition de la clause vide est-elle utile à la mémorisation ?

Passages de référence : L10, L15, H17.

## C277 — OLP-0029-B28

**Choix :** au sens formel ; un autre domaine ; L’absence de répétitions

**Autre formulation envisagée :** Il faut indexer une liste finie sans doublons par un ensemble fini

**Motif :** La distinction liste informelle/fonction totale explique pourquoi le domaine doit changer lorsque A est fini ; injectivité et surjectivité motivent la bijection.

**Confiance et limites :** obstruction du principe des tiroirs et rôle du domaine vérifiés.

**Question de révision :** Le passage explique-t-il assez tôt pourquoi le cas vide ne relève pas de PosInt ?

Passages de référence : L10, L15, H17.

## C278 — OLP-0029-B29

**Choix :** soit~$\PosInt$, soit ; un certain~$n \in \PosInt$

**Autre formulation envisagée :** Une bijection depuis PosInt ou depuis un intervalle fini non vide

**Motif :** L’alternative distingue A infini et fini non vide. A ne peut être vide puisque f est une surjection depuis PosInt.

**Confiance et limites :** hypothèse excluant le vide et borne positive contrôlées.

**Question de révision :** Le symbole Z risque-t-il une confusion avec Int malgré la typographie ?

Passages de référence : L10, L15, H17.

## C279 — OLP-0029-B30

**Choix :** la première valeur ; s’il en existe une ; une
infinité d’!!{element}s

**Autre formulation envisagée :** Retenir successivement la première valeur encore absente

**Motif :** Première désigne l’ordre des indices de f, non un ordre sur A. La construction s’arrête exactement après le nombre d’éléments si A est fini ; elle reste définie partout si A est infini. Récurrence ne veut pas dire calculabilité.

**Confiance et limites :** définition par minimum d’indice et deux domaines cohérents avec L10.

**Question de révision :** Une mention explicite des indices clarifierait-elle encore première valeur ?

Passages de référence : L10, L15, H17.

## C280 — OLP-0029-B31

**Choix :** finit
donc par être ; contrairement à la définition

**Autre formulation envisagée :** Tout élément est retenu au plus tard après avoir parcouru son premier indice, et aucune valeur n’est retenue deux fois

**Motif :** La surjectivité découle du rang fini d’une première occurrence ; l’injectivité découle de la règle d’exclusion. La paraphrase explicite la justification que l’original laisse courte.

**Confiance et limites :** argument contrôlé, formulation finale encore concise.

**Question de révision :** Faut-il rendre la borne du rang explicite dans le corps de la preuve ?

Passages de référence : L10, L15, H17.

## C281 — OLP-0029-B32

**Choix :** $N = \Nat$
ou $N = \{0, \dots, n\}$

**Autre formulation envisagée :** Une bijection depuis Nat ou depuis un segment initial fini non vide

**Motif :** Le paramètre n naturel donne n+1 éléments ; vide est séparé. Aucune taille n n’est attribuée à ce segment.

**Confiance et limites :** bornes zéro et n comprises, clause vide conservée.

**Question de révision :** Le changement de convention des bornes doit-il être souligné après le segment1…n ?

Passages de référence : L10, L15, H17.

## C282 — OLP-0029-B33

**Choix :** équivaut
à l’existence ; $N = \{0, \dots, n-1\}$

**Autre formulation envisagée :** Le décalage d’un indice transforme les bijections dans les deux sens

**Motif :** Les deux équivalences sont conservées ; le n de la preuve est positif, donc n−1 naturel. La formule0…n−1 est compatible avec l’énoncé0…n par renommage du paramètre.

**Confiance et limites :** sens réciproque restauré explicitement avant l’alignement et bornes vérifiées.

**Question de révision :** Faut-il préciser ce renommage pour éviter de confondre les deux n locaux ?

Passages de référence : L10, L15, H17.

## C283 — OLP-0029-B34

**Choix :** fonction !!{injective} $g\colon A \to \PosInt$ ; si et seulement si $A = \emptyset$

**Autre formulation envisagée :** Prouvez l’équivalence entre une injection vers PosInt et la définition précédente

**Motif :** L’injection va de A vers PosInt, pas en sens inverse. Elle couvre le vide sans exception, tandis que la surjection exige la disjonction. L10 soutient le sens de la dénombrabilité, OLP fixe l’exercice.

**Confiance et limites :** orientation et cas vide vérifiés.

**Question de révision :** La consigne donne-t-elle assez d’indices sans fournir toute la preuve ?

Passages de référence : L10, L15, H17.

## C284 — OLP-0030-B04

**Choix :** La méthode en zigzag de Cantor

**Autre formulation envisagée :** Le parcours en zigzag de Cantor

**Motif :** Le titre nomme le procédé de parcours du tableau. Méthode restitue method ; en zigzag décrit son trajet sans annoncer l’argument diagonal de non-dénombrabilité. L10 établit le cadre de dénombrabilité, sans attester cette dénomination ; la formulation du titre reste un choix éditorial d’après OLP.

**Confiance et limites :** Le procédé et son attribution sont explicites dans OLP ; la forme du titre reste révisable.

**Question de révision :** Parcours en zigzag conviendrait-il mieux au registre des titres voisins ?

Passages de référence : L10.

## C285 — OLP-0030-B05

**Choix :** quelques énumérations simples ; disposer ces couples dans un \emph{tableau} ; exactement une fois ; les indices commençant à~$0$ ; dans l’ordre suivant

**Autre formulation envisagée :** Passons maintenant à une énumération moins immédiate ; chaque couple occupe une unique case, repérée à partir de zéro.

**Motif :** L03 soutient produit cartésien et l’ordre des coordonnées ; L04 confirme que les naturels commencent à zéro ; L10 fixe la notion inclusive. Le tableau, ses numéros et leur ordre sont ceux d’OLP. Indice évite que ligne zéro devienne la première ligne numérotée un. Simples et passons maintiennent l’adresse pédagogique sans traduire easy par une appréciation du lecteur. Les deux branches conditionnelles donnent une phrase française complète.

**Confiance et limites :** Toutes les valeurs du tableau et de la liste sont conservées ; les ajouts précisent uniquement le repérage.

**Question de révision :** Le passage du tableau de couples au tableau de numéros est-il assez explicite ?

Passages de référence : L03, L04, L10.

## C286 — OLP-0030-B06

**Choix :** est !!{enumerable}

**Autre formulation envisagée :** L’ensemble des couples d’entiers naturels est au plus dénombrable.

**Motif :** La macro adopte la convention C254 appuyée sur L10. La proposition affirme l’existence d’une énumération du produit entier, sans restreindre les coordonnées ni prétendre que la fonction est calculable par définition.

**Confiance et limites :** Même ensemble, même propriété ; token français déjà préparé pour le chapitre.

**Question de révision :** Faut-il rappeler la convention inclusive à cette première application au produit ?

Passages de référence : L10.

## C287 — OLP-0030-B07

**Choix :** la fonction qui associe ; porte le numéro~$k$ ; Chaque couple est atteint ; La fonction $f$ est donc surjective

**Autre formulation envisagée :** À chaque numéro k on fait correspondre le couple occupant la case numérotée k ; toute case est atteinte après un parcours fini.

**Motif :** L15 soutient la construction d’une fonction avec domaine fixé et L10 le résultat visé. La relation entre numéro et coordonnées vient du tableau OLP. La justification par les diagonales de somme constante développe l’argument de surjectivité laissé implicite dans la courte preuve source ; elle ne remplace pas la fonction ni n’invoque un choix d’une infinité d’objets. Cette expansion est éditoriale, non une citation de Lyon.

**Confiance et limites :** Les diagonales sont finies et rangées par somme croissante ; chaque couple a une somme naturelle finie.

**Question de révision :** Faut-il expliciter aussi la partition des numéros en blocs consécutifs pour justifier que f est définie partout ?

Passages de référence : L10, L15.

## C288 — OLP-0030-B08

**Choix :** se généralise aisément ; couples emboîtés ; un axe suit l’énumération ; on adopte la convention ; l’exposant~$0$

**Autre formulation envisagée :** En remplaçant un axe par la liste des couples, on énumère les triplets ; on répète la construction pour toute longueur finie, avec une seule suite vide à longueur zéro.

**Motif :** L03 soutient le produit ; L11 et L16 donnent la récurrence sur les puissances finies et une convention explicite au cas vide. Le tableau emboîté et l’ordre des triplets sont conservés d’OLP et concordent avec son codage antérieur. La convention Nat^0 est ajoutée et signalée parce que la définition antérieure commence à1 tandis que la proposition quantifie n dans Nat. Le produit vide du canon motive le traitement d’un cas limite, sans être confondu avec la représentation ensembliste du0-uplet.

**Confiance et limites :** L’étape produit et le cas de base couvrent exactement tous les exposants naturels ; notation du source conservée.

**Question de révision :** La note sur l’exposant zéro doit-elle être déplacée à la première définition des puissances lors de l’intégration finale ?

Passages de référence : L03, L11, L16.

## C289 — OLP-0030-B09

**Choix :** pour tout $n \in \Nat$

**Autre formulation envisagée :** Pour chaque entier naturel n, l’ensemble Nat^n admet une énumération.

**Motif :** L10 soutient le prédicat choisi ; L16 éclaire la construction par récurrence et le cas vide précisé juste avant. Pour tout porte sur l’exposant ; aucune seule énumération commune à tous les produits n’est prétendue.

**Confiance et limites :** La portée universelle est inchangée et le cas0 est désormais défini.

**Question de révision :** La notation du0-uplet reste-t-elle cohérente avec les variantes à intégrer ?

Passages de référence : L10, L16.

## C290 — OLP-0030-B10

**Choix :** Montrez que ; pour tout $n \in \Nat$

**Autre formulation envisagée :** Établissez que toute puissance cartésienne finie des entiers strictement positifs est au plus dénombrable.

**Motif :** L02 atteste le registre d’un exercice à démontrer, avec l’infinitif Montrer ; l’impératif Montrez suit le choix éditorial du lecteur. L10 justifie le prédicat ; les naturels strictement positifs viennent du token PosInt et non d’un changement de convention sur Nat. La longueur zéro reste incluse.

**Confiance et limites :** Objet et quantification préservés ; l’alternative explicite une notation déjà familière.

**Question de révision :** L’explicitation en mots de PosInt serait-elle utile ici ?

Passages de référence : L10, L02.

## C291 — OLP-0030-B11

**Choix :** Montrez que ; Vous pouvez admettre le résultat de l’

**Autre formulation envisagée :** Prouvez que l’ensemble des mots finis sur les entiers strictement positifs est au plus dénombrable, en utilisant au besoin l’exercice précédent.

**Motif :** H02 soutient les mots finis construits à partir du mot vide ; L10 la dénombrabilité et L02 l’injonction d’exercice. Le renvoi exact reste celui d’OLP. Pouvez admettre exprime une permission d’utiliser le résultat, sans exiger la solution préalable. L’article élidé est compatible avec le nom exercice rendu par cref.

**Confiance et limites :** Même alphabet, fermeture étoile et dépendance autorisée ; label conservé.

**Question de révision :** L’expression résultat de l’exercice évite-t-elle suffisamment de confondre une hypothèse et une consigne ?

Passages de référence : L10, H02, L02.

## C292 — OLP-0031-B03

**Choix :** Fonctions de couplage et codes

**Autre formulation envisagée :** Couplage des couples et codage arithmétique

**Motif :** K01 atteste directement fonction de couplage pour pairing function et conserve la condition d’injectivité. Codes nomme les nombres produits, distincts de la procédure de codage. Le titre n’annonce pas des fonctions qui fabriquent des couples à partir de deux nombres : ici elles codent les couples par un naturel.

**Confiance et limites :** Correspondance terminologique explicite dans un article de logique français.

**Question de révision :** Appariement serait-il plus familier au lectorat sans perdre l’attestation technique de couplage ?

Passages de référence : K01, L10, L15.

## C293 — OLP-0031-B04

**Choix :** permet de voir ; au numéro~$7$ ; disposer de l’\emph{inverse} ; la position exacte du couple

**Autre formulation envisagée :** Le tableau rend la dénombrabilité visible ; cherchons une formule donnant directement le rang de chaque couple.

**Motif :** L10 soutient la notion ; K01 l’identification d’un couplage naturel, avec une convention de coordonnées différente explicitement écartée. L15 soutient les domaines de fonctions. Voir n’est pas une preuve par simple intuition : il reprend la construction finie démontrée au paragraphe précédent. Inverse garde la direction Nat²→Nat du tableau, et le numéro7 ne devient pas la septième position dans une liste commençant à1.

**Confiance et limites :** Domaines, sens de l’inverse et quatre valeurs affichées conservés.

**Question de révision :** Faut-il employer rang numéroté à partir de zéro plutôt que position exacte ?

Passages de référence : K01, L10, L15.

## C294 — OLP-0031-B05

**Choix :** Deux observations ; pour $m\geq 1$ ; de $0$ à $k$ inclus ; pour alléger
la notation ; on lui ajoute~$n$

**Autre formulation envisagée :** On descend d’une ligne en reculant d’une colonne, à condition que celle-ci existe ; les débuts de diagonales sont les sommes de0 àk.

**Motif :** K01 fournit le terme couplage, mais sa formule ajoute la seconde coordonnée : la formule OLP ajoutant n est maintenue. La borne triangulaire source est fautive : somme des entiers strictement inférieurs à k vaut k(k−1)/2, contrairement à sa formule k(k+1)/2. La traduction corrige en0 àk inclus et signale la correction. m≥1 rend légitime la colonne m−1. Indice remplace les ordinaux ambigus et alléger la notation rend le motif stylistique sans image corporelle. L15 soutient uniquement l’usage fonctionnel.

**Confiance et limites :** Identité des diagonales et exemple7 vérifiés directement ; corrections localisées et annoncées.

**Question de révision :** Le détail sur les deux conventions de la fonction de Cantor doit-il apparaître dans le lecteur ou rester dans le dossier de choix ?

Passages de référence : K01, L10, L15.

## C295 — OLP-0031-B06

**Choix :** Cette fonction~$g$ ; De telles fonctions ; \emph{fonctions de couplage}

**Autre formulation envisagée :** On appelle fonctions de couplage les fonctions de codage de couples de ce type.

**Motif :** K01 atteste le nom, en autorisant les injections qui ne sont pas surjectives. Cette fonction renvoie au g particulier, qui est bijectif ; de telles fonctions prépare une classe plus générale. Il ne faut pas lire ce passage comme affirmant que toute énumération surjective possède un inverse unique, ni que chaque couplage est bijectif sur Nat.

**Confiance et limites :** Le g construit est bijectif ; la définition suivante fixe la généralisation par injectivité.

**Question de révision :** La transition du cas bijectif à la définition injective mérite-t-elle une phrase supplémentaire ?

Passages de référence : K01, L10, L15.

## C296 — OLP-0031-B07

**Choix :** fonction de couplage arithmétique ; si elle est injective ; \emph{code} $A \times B$ ; le \emph{code} du couple

**Autre formulation envisagée :** Une injection du produit A×B dans les naturels est un codage arithmétique des couples ; la valeur obtenue est le code du couple.

**Motif :** K01 soutient explicitement fonction de couplage et injection, pas une exigence de surjectivité. OLP étend cette désignation de Nat² à A×B ; arithmétique signifie que les codes sont naturels. Coder et code conservent la distinction action/résultat. Le si définitoire exprime la condition retenue dans la définition sans ajouter un algorithme de calcul.

**Confiance et limites :** Le domaine général et la seule condition injective restent ceux d’OLP.

**Question de révision :** Fonction de couplage arithmétique ou fonction arithmétique de couplage est-il préférable dans cette définition ?

Passages de référence : K01, L10, L15.

## C297 — OLP-0031-B08

**Choix :** chaque \emph{couple} ; un \emph{seul} nombre ; défini sur son image ; retrouver le couple

**Autre formulation envisagée :** Le code remplace le couple par un naturel ; le décodage sur l’ensemble des codes utilisés restitue ce couple.

**Motif :** K01 distingue injection et bijection et L15 fixe domaine/image. L’unicité du décodage découle de l’injectivité, mais son domaine n’est que l’image : l’ajout défini sur son image prévient précisément l’erreur reprise par le dernier exercice. Le verbe décoder décrit cette fonction mathématique sans lui attribuer automatiquement la calculabilité.

**Confiance et limites :** La restriction au domaine de l’inverse est nécessaire et suffisante ; elle conserve le mécanisme source.

**Question de révision :** Le mot inverse doit-il systématiquement être accompagné de sur l’image pour les couplages généraux ?

Passages de référence : K01, L10, L15.

## C298 — OLP-0031-B09

**Choix :** Donnez une énumération ; positifs ou nuls

**Autre formulation envisagée :** Énumérez les rationnels supérieurs ou égaux à zéro.

**Motif :** L10 fixe le sens d’énumération ; le registre d’exercice est celui des constructions du chapitre. Positifs ou nuls évite l’ambiguïté du seul positifs et conserve exactement non-negative, y compris0. Aucune contrainte de représentation irréductible n’est ajoutée.

**Confiance et limites :** Le sous-ensemble demandé est exactement préservé.

**Question de révision :** Supérieurs ou égaux à zéro serait-il plus clair que positifs ou nuls ?

Passages de référence : L10, L11.

## C299 — OLP-0031-B10

**Choix :** Montrez que ; tout
nombre rationnel ; avec $z \in \Int$ et $m \in \Nat^+$

**Autre formulation envisagée :** Démontrez la dénombrabilité de tous les rationnels en utilisant leur écriture avec un numérateur entier et un dénominateur strictement positif.

**Motif :** L10 soutient le prédicat et L11 le registre d’une démonstration par codage fini. Tout conserve le rappel universel ; z peut être négatif ou nul, m doit être strictement positif. Le rappel ne prétend pas que cette représentation est unique et ne demande pas de supprimer les répétitions.

**Confiance et limites :** Les domaines et l’absence d’exigence d’unicité concordent avec les énumérations admises.

**Question de révision :** La notation Nat^+ doit-elle être harmonisée avec PosInt dans l’édition intégrée, en conservant sa trace source ?

Passages de référence : L10, L11.

## C300 — OLP-0031-B11

**Choix :** Définissez une énumération

**Autre formulation envisagée :** Construisez une liste énumérant tous les mots binaires finis.

**Motif :** H02 atteste mots sur un alphabet et la génération à partir du mot vide ; L10 fournit le sens inclusif. Définissez demande une règle d’énumération et non seulement l’affirmation de son existence. La notation Bin* garde le mot vide, les deux symboles et toutes les longueurs finies.

**Confiance et limites :** Même ensemble et même type de construction ; aucune solution ajoutée.

**Question de révision :** Un rappel que Bin désigne0 et1 est-il nécessaire à ce stade ?

Passages de référence : L10, H02, L02.

## C301 — OLP-0031-B12

**Choix :** toute table de vérité ; fonction de vérité,
ou fonction booléenne ; pour un certain entier
naturel~$k$ ; l’ensemble de toutes ces fonctions

**Autre formulation envisagée :** Une table de vérité spécifie une fonction booléenne d’arité finie ; montrez que l’ensemble de ces fonctions, toutes arités finies confondues, est au plus dénombrable.

**Motif :** H19 atteste fonction booléenne et H20 tables de vérité, avec V/F ; OLP fixe ici0/1. Fonction de vérité est conservé comme traduction explicite du terme source, accompagné du terme directement attesté. Pour un certain k dépend de la fonction ; la dernière quantification réunit toutes les arités finies, elle ne se limite pas à un seul k fixé. Aucun résultat sur l’ensemble de toutes les fonctions Nat→Bin n’est prétendu.

**Confiance et limites :** Domaines finis et variation d’arité préservés ; les deux termes sont distingués de fonction vraie.

**Question de révision :** Le synonyme fonction de vérité doit-il rester dans le corps du texte ou passer dans un index terminologique ?

Passages de référence : H19, H20, L10.

## C302 — OLP-0031-B13

**Choix :** parties finies ; infini
!!{enumerable} quelconque

**Autre formulation envisagée :** Établissez que les sous-ensembles finis de tout ensemble infini au plus dénombrable forment un ensemble au plus dénombrable.

**Motif :** L11 contient précisément les parties finies et leur codage par longueur ; L10 fixe le sens. Finies porte sur les parties, infini sur l’ensemble ambiant. Quelconque conserve l’universalité et n’exclut pas la partie vide. Bien que le lemme canonique traite aussi les ensembles ambiants finis, la qualification infini d’OLP reste présente.

**Confiance et limites :** Rôle des deux qualifications et domaine universel conservés.

**Question de révision :** Le mot quelconque est-il utile en plus de l’article indéfini générique ?

Passages de référence : L10, L11.

## C303 — OLP-0031-B14

**Choix :** cofinie ; le complémentaire, dans $\Nat$ ; les parties finies et les parties
cofinies

**Autre formulation envisagée :** Une partie est cofinie lorsque tous les naturels sauf un nombre fini lui appartiennent ; réunissez les parties finies et les parties cofinies.

**Motif :** H01 fixe le complément relatif à un univers et les parties ; L10 fixe le résultat. Cofinie transpose le terme source avec une définition française explicite, sans fausse attestation lexicale dans H01. On corrige l’ellipse source finite set Nat en partie finie de Nat, conformément à la formule immédiatement donnée. Le et final forme la réunion de deux classes de parties, pas leur intersection.

**Confiance et limites :** Formule et univers de complément sont explicites ; terme cofinie reste défini sur place.

**Question de révision :** La paraphrase tous les naturels sauf un nombre fini aiderait-elle la première occurrence ?

Passages de référence : L10, L11.

## C304 — OLP-0031-B15

**Choix :** la réunion d’une famille ; dont chacun est ; cet exercice est difficile ; l’axiome du choix dénombrable

**Autre formulation envisagée :** La réunion d’une suite d’ensembles au plus dénombrables est au plus dénombrable ; choisissez leurs énumérations avant de les parcourir ensemble.

**Motif :** L10 traite la dénombrabilité inclusive et L16 distingue constructions canoniques et choix arbitraires. La famille est au plus dénombrable, chacun de ses membres aussi, puis sa réunion reçoit la conclusion ; les trois occurrences du token ont leur propre portée. Le pluriel des ensembles est explicite dans usetoken. La note révèle l’usage possible du choix dénombrable lorsque les énumérations ne sont pas fournies ; elle ne prétend pas que cet axiome entier est nécessaire à chaque famille particulière. La difficulté originale reste signalée.

**Confiance et limites :** La preuve usuelle est correcte avec ce principe suffisant ; les dépendances axiomatiques générales méritent une révision au chapitre du choix.

**Question de révision :** La future section sur l’axiome du choix doit-elle fournir un renvoi remplaçant cette note autonome ?

Passages de référence : L10, L16.

## C305 — OLP-0031-B16

**Choix :** quelconque ; défini sur $\ran{f}$ ; permet d’obtenir une énumération ; le cas où $A \times B$ est vide

**Autre formulation envisagée :** À partir de l’inverse sur l’image d’un codage injectif, construisez une énumération du produit, en distinguant le produit vide.

**Motif :** K01 autorise toute injection, L15 distingue domaine et image et L10 admet l’ensemble vide. L’exercice source est faux avec sa définition formelle d’énumération : un inverse défini seulement sur l’image n’a pas forcément domaine Nat ou PosInt. La nouvelle consigne conserve l’objectif constructif, mais demande de déduire l’énumération de cet inverse. La note annonce la correction, et le cas vide empêche d’exiger une surjection d’un domaine non vide sur le vide.

**Confiance et limites :** Un codage à valeurs paires donne un contre-exemple immédiat au domaine annoncé ; une énumération du produit reste constructible.

**Question de révision :** Faut-il proposer explicitement le codage à valeurs paires comme contre-exemple, sans dévoiler la construction demandée ?

Passages de référence : K01, L10, L15.

## C306 — OLP-0031-B17

**Choix :** Donnez une fonction qui code

**Autre formulation envisagée :** Construisez un codage injectif des triplets d’entiers naturels par des entiers naturels.

**Motif :** K01 donne le couplage injectif des couples ; OLP demande son itération aux triplets. Code est interprété d’après la définition du chapitre, donc exige injectivité, mais n’ajoute pas l’exigence de bijectivité sur Nat. Le produit emboîté reste celui de la section en zigzag.

**Confiance et limites :** Objet et propriété de codage sont déterminés par les définitions proches.

**Question de révision :** La référence explicite à l’itération des couplages serait-elle un indice excessif pour l’exercice ?

Passages de référence : K01, L10, L15.

## C307 — OLP-0032-B04

**Choix :** Une autre fonction de couplage

**Autre formulation envisagée :** Un autre codage des couples

**Motif :** K01 atteste fonction de couplage. Une autre annonce une construction supplémentaire, sans attribuer au premier procédé un statut canonique exclusif ni présenter cette section comme un chapitre de remplacement.

**Confiance et limites :** Même désignation technique et même fonction du titre.

**Question de révision :** Codage des couples serait-il plus transparent comme titre secondaire ?

Passages de référence : K01, L10, L15.

## C308 — OLP-0032-B05

**Choix :** toutes vides
au départ ; la première coordonnée ; une place vide sur deux ; puis $\tuple{3,m}$ ; Pour commencer la numérotation
à~$0$

**Autre formulation envisagée :** On remplit d’abord les places impaires, puis une place restante sur deux, en augmentant la première coordonnée ; le code naturel s’obtient en retranchant1 au numéro de place.

**Motif :** K01 appuie le nom du procédé de codage, L15 les fonctions et L10 l’énumération. Tous les tableaux et facteurs de puissances de2 restent ceux d’OLP. La prose source donne0,2 au lieu de0,1 pour le deuxième couple et répète2,m au lieu de3,m ; les deux corrections sont annoncées. Vide qualifie les places encore disponibles, de sorte que sauter une place s’applique à la liste résiduelle. Les numéros positifs et les codes naturels à partir de0 restent distingués.

**Confiance et limites :** Les valeurs des tableaux et la factorisation2^n(2m+1) déterminent sans ambiguïté les deux coquilles et le décalage.

**Question de révision :** Une image supplémentaire des places résiduelles serait-elle utile, sans remplacer les tableaux originaux ?

Passages de référence : K01, L10, L15.

## C309 — OLP-0032-B06

**Choix :** définie par ; est une fonction de couplage

**Autre formulation envisagée :** La formule donnée associe injectivement à chaque couple d’entiers naturels un entier naturel.

**Motif :** K01 donne la convention injective de couplage ; la formule2^n(2m+1)−1 vient d’OLP, sans substitution de la formule de Cantor du témoin. L15 garantit le sens de la fonction avec domaine fixé. La décomposition unique d’un entier strictement positif en puissance de2 multipliée par un impair justifie ce codage ; la proposition ne dépend d’aucune énumération choisie arbitrairement.

**Confiance et limites :** Décomposition unique et retrait de1 vérifient injectivité et même surjectivité.

**Question de révision :** Faut-il ajouter la décomposition unique comme justification explicite lors de la révision du chapitre ?

Passages de référence : K01, L10, L15.

## C310 — OLP-0032-B07

**Choix :** a donc pour code ; a pour code

**Autre formulation envisagée :** Les couples0,0 ;1,2 ;2,6 reçoivent respectivement les codes0,9,51.

**Motif :** L15 soutient la lecture fonctionnelle ; K01 le sens de code injectif. Les trois calculs détaillés d’OLP sont conservés, et non réduits à la liste de résultats de l’alternative. Deuxième énumération désigne le nouveau procédé après le décalage de1, ce qui explique pourquoi0,0 a désormais code0.

**Confiance et limites :** Les trois substitutions numériques sont exactes.

**Question de révision :** Le rappel du décalage doit-il précéder les trois calculs ?

Passages de référence : K01, L10, L15.

## C311 — OLP-0032-B08

**Choix :** sans exiger que le codage soit surjectif ; considéré sur l’ensemble d’arrivée entier ; définie seulement sur les codes effectivement utilisés

**Autre formulation envisagée :** Un codage injectif peut laisser des nombres inutilisés ; son décodage sur tous les naturels est alors partiel.

**Motif :** K01 autorise explicitement les injections non surjectives ; L15 distingue domaine/image. L’original dit que les inverses sont seulement partiels : la traduction précise l’ensemble sur lequel on les considère. Sur l’image, l’inverse est total ; sur tout l’ensemble d’arrivée, il peut être partiel. On ne confond pas cette distinction avec une indétermination de la valeur.

**Confiance et limites :** Précision directement imposée par la définition de fonction partielle déjà traduite.

**Question de révision :** Cette précision rend-elle cohérente la terminologie avec l’exercice corrigé de la section précédente ?

Passages de référence : K01, L10, L15.

## C312 — OLP-0032-B09

**Choix :** est injective ; ses valeurs comme des éléments de ; une fonction !!{injective}

**Autre formulation envisagée :** Le codage2^n3^m est injectif à valeurs strictement positives et reste injectif si l’on élargit l’ensemble d’arrivée aux naturels.

**Motif :** L15 distingue le type complet de la fonction et l’inclusion de son image ; K01 soutient le codage injectif. OLP donne successivement Nat^+ puis Nat comme arrivée : l’élargissement est explicité sans changer le polynôme exponentiel. Les facteurs premiers2 et3 rendent les exposants uniques. La macro adjective suit fonction et ne conserve pas l’ordre anglais a injective function.

**Confiance et limites :** L’inclusion des positifs dans les naturels conserve l’injectivité ; aucun zéro n’est produit.

**Question de révision :** Doit-on nommer l’unicité de la décomposition en facteurs premiers ici ?

Passages de référence : K01, L10, L15.

## C313 — OLP-0033-B04

**Choix :** Ensembles \usetoken{p}{nonenumerable}

**Autre formulation envisagée :** Les ensembles qui ne sont pas au plus dénombrables

**Motif :** L10 fixe l’opposition entre dénombrabilité inclusive et non-dénombrabilité ; le pluriel explicite de la macro accorde l’adjectif avec ensembles. La forme concise non dénombrables garde le niveau du titre sans déplacer la négation vers l’infinitude.

**Confiance et limites :** Complément exact du prédicat défini, avec inflexion française.

**Question de révision :** Faut-il conserver la graphie sans trait d’union dans tous les titres adjectivaux ?

Passages de référence : L06, L10.

## C314 — OLP-0033-B05

**Choix :** à partir de la définition ; un peu plus
élémentaire et détaillée ; la variante de la \olref[nen-alt]{sec}

**Autre formulation envisagée :** Cette présentation développe davantage les preuves que leur variante fondée sur des bijections.

**Motif :** L05 soutient l’ensemble des parties, L06 le type de preuve et L10 les conventions. La comparaison porte sur les présentations, pas sur la capacité des lecteurs. Le renvoi source enm-alt pointe aux définitions ; après lecture du début de non-enumerability-alt, il est corrigé en nen-alt et signalé dans une note. La dépendance correcte envers enm est conservée.

**Confiance et limites :** La section parallèle visée est identifiable par son titre, son contenu et son identifiant.

**Question de révision :** L’intégration des variantes doit-elle remplacer cette comparaison par une transition vers leur contenu nouveau ?

Passages de référence : L05, L06, L10.

## C315 — OLP-0033-B06

**Choix :** tous les exemples
d’ensembles infinis rencontrés ; Il existe pourtant ; ne possèdent pas
cette propriété

**Autre formulation envisagée :** Les exemples infinis déjà étudiés sont au plus dénombrables ; certains ensembles infinis ne le sont pas.

**Motif :** L10 permet de distinguer infinitude et dénombrabilité. Tous est limité par rencontrés aux exemples antérieurs ; la phrase suivante est existentielle. La traduction ne suggère pas que toute infinitude implique la non-dénombrabilité.

**Confiance et limites :** Portée du bilan antérieur et existence du contraste conservées.

**Question de révision :** Rencontrés suffit-il à marquer la portée locale de tous ?

Passages de référence : L06, L10.

## C316 — OLP-0033-B07

**Choix :** Pour tout ensemble non vide~$A$ ; aucune telle fonction ; atteindre
tous les éléments ; en ce sens, « plus »

**Autre formulation envisagée :** Un ensemble non vide est au plus dénombrable s’il est l’image d’une liste de naturels positifs ; un ensemble non dénombrable dépasse toute telle liste.

**Motif :** L10 admet le vide dans la notion inclusive ; la correction non vide est donc nécessaire pour l’existence d’une fonction de PosInt vers A, et elle est signalée. L06 démontre comment la surjectivité peut échouer malgré un domaine infini. Plus reste entre guillemets et est qualifié en ce sens : aucune définition anticipée de l’ordre cardinal n’est substituée à l’explication.

**Confiance et limites :** Le vide est le contre-exemple exact à la généralisation source ; l’explication de surjectivité reste intacte.

**Question de révision :** La note sur le vide peut-elle devenir un rappel bref après la révision de toutes les variantes ?

Passages de référence : L06, L10.

## C317 — OLP-0033-B08

**Choix :** Pour un ensemble non vide ; toute
liste d’éléments de~$A$ en omet au moins un ; Étant donnée une liste ; on construit un autre élément

**Autre formulation envisagée :** Pour réfuter une énumération supposée, construisez à partir de chaque liste un élément de A qui en est absent.

**Motif :** L06 fournit le schéma de supposition et de témoin diagonal ; L10 la notion visée. Le terme méthode diagonale transpose la dénomination OLP ; le passage Lyon atteste le mécanisme, pas ce syntagme. Toute liste puis un autre élément conservent la dépendance du témoin à la liste. Le cas non vide est rappelé pour l’équivalence avec l’absence de surjection.

**Confiance et limites :** La structure pour toute liste, il existe un élément omis est intacte.

**Question de révision :** Le terme diagonalisation devra-t-il être rapproché d’un témoin lexical explicite lors du chapitre de calculabilité ?

Passages de référence : L06, L10.

## C318 — OLP-0033-B09

**Choix :** toutes
les suites infinies ; indexés par les entiers strictement positifs ; sans position manquante

**Autre formulation envisagée :** L’ensemble considéré réunit les fonctions de PosInt vers0,1, vues comme des suites infinies.

**Motif :** L15 soutient la lecture d’une suite comme fonction définie à chaque indice ; L10 situe la dénombrabilité. Sans position manquante rend non-gappy au moyen du domaine explicite PosInt utilisé par la preuve OLP. La notation omega n’est pas remplacée par une suite finie ni par des indices entiers dans les deux sens.

**Confiance et limites :** La convention d’indices correspond aux formules de la preuve.

**Question de révision :** Une note future doit-elle rappeler le décalage canonique entre indices naturels et strictement positifs ?

Passages de référence : L06, L10, L15.

## C319 — OLP-0033-B10

**Choix :** est !!{nonenumerable}

**Autre formulation envisagée :** Il n’existe aucune liste de toutes les suites binaires infinies.

**Motif :** L10 gouverne le prédicat, L15 l’ensemble de fonctions implicite ; la preuve qui suit établit la propriété annoncée. La macro reste au singulier pour l’ensemble Bin^omega.

**Confiance et limites :** Même objet et même théorème.

**Question de révision :** La dénomination suites binaires peut-elle être réutilisée ensuite sans rappeler0 et1 ?

Passages de référence : L06, L10, L15.

## C320 — OLP-0033-B11

**Choix :** Supposons, par l’absurde ; de tous les éléments ; le $j$-ième terme
de la $i$-ième suite

**Autre formulation envisagée :** Supposons qu’une liste contienne toutes les suites binaires ; s_i(j) désigne le terme en colonne j de la suite en ligne i.

**Motif :** L06 atteste le raisonnement par l’absurde et la supposition d’un élément dans l’image ; L15 soutient l’égalité fonctionnelle utilisée plus loin. Tous appartient à l’hypothèse réfutée. Terme désigne une occurrence de la suite, distincte des éléments de l’ensemble de suites. Les indices i et j ne sont pas échangés.

**Confiance et limites :** Les deux niveaux de listes et les indices sont conservés.

**Question de révision :** La distinction entre terme d’une suite et élément de l’ensemble est-elle assez constante dans le chapitre ?

Passages de référence : L06, L10, L15.

## C321 — OLP-0033-B12

**Choix :** Les numéros à gauche ; ceux du haut ; désigne le nombre, $0$ ou~$1$

**Autre formulation envisagée :** Les lignes repèrent les suites et les colonnes les positions dans chaque suite.

**Motif :** L15 soutient que chaque indice possède une valeur ; le tableau et les règles de repérage viennent entièrement d’OLP. Désigne évite de transformer le nom symbolique s_1(1) en un troisième type de valeur : sa valeur est0 ou1. Aucun bit n’est choisi à l’avance dans le tableau générique.

**Confiance et limites :** Toutes les cellules et la diagonale typographique sont conservées.

**Question de révision :** Les numéros du haut doivent-ils être appelés indices plutôt que numéros pour la cohérence avec le zigzag ?

Passages de référence : L06, L10, L15.

## C322 — OLP-0033-B13

**Choix :** Sa définition
dépendra de la liste ; Toute liste infinie ; absente de cette liste

**Autre formulation envisagée :** À chaque liste proposée correspond une suite binaire qui n’y figure pas.

**Motif :** L06 fournit le témoin construit à partir de la fonction supposée ; L15 garantit le type de la nouvelle suite. La répétition explicite de cette liste conserve la dépendance essentielle et évite l’énoncé faux d’une même suite absente de toutes les listes possibles.

**Confiance et limites :** Dépendance du témoin et quantificateurs exacts.

**Question de révision :** La répétition de liste peut-elle être allégée sans obscurcir cette dépendance ?

Passages de référence : L06, L10, L15.

## C323 — OLP-0033-B14

**Choix :** pour chaque $n \in \PosInt$ ; en remplaçant chaque $1$ par un $0$ ; selon que ; une formule à cette définition par cas

**Autre formulation envisagée :** Définissez chaque bit de la nouvelle suite comme1 moins le bit diagonal correspondant.

**Motif :** L06 appuie l’inversion de la condition d’appartenance ; L15 le fait de définir une fonction point par point. La source fournit le complément binaire, conservé dans les deux branches et dans la formule1−s_n(n). Selon que maintient l’appariement0/1 avec1/0. La possibilité stylistique d’employer la formule au lieu des cas est gardée.

**Confiance et limites :** Les deux définitions donnent le même bit pour chaque indice.

**Question de révision :** Faut-il employer inverser les bits comme abréviation après cette définition explicite ?

Passages de référence : L06, L10, L15.

## C324 — OLP-0033-B15

**Choix :** en échangeant les deux valeurs ; appartient
à~$\Bin^\omega$ ; elle ne figure pas

**Autre formulation envisagée :** Le complément de la diagonale est lui-même une suite binaire infinie, mais ne coïncide avec aucune ligne.

**Motif :** L15 soutient l’appartenance à l’ensemble des fonctions de même domaine et arrivée ; L06 le contraste entre témoin bien défini et absent de l’image. Échanger les deux valeurs rend mirror sequence et évite la lecture d’un ordre renversé. L’appartenance précède l’argument de non-présence.

**Confiance et limites :** Le type du témoin est prouvé sans permutation des indices.

**Question de révision :** L’expression complément de la diagonale serait-elle plus concise sans suggérer un complément d’ensemble ?

Passages de référence : L06, L10, L15.

## C325 — OLP-0033-B16

**Choix :** son premier
terme est différent ; au deuxième terme ; et inversement ; On poursuit de même

**Autre formulation envisagée :** La nouvelle suite diffère de la première au premier terme, de la deuxième au deuxième, et ainsi de suite.

**Motif :** L06 justifie le schéma de différence au point indexant le candidat ; les deux exemples viennent d’OLP. Les valeurs sont échangées entre0 et1, plutôt que remplacées par leur opposé arithmétique. Les étapes illustratives sont conservées avant la formalisation universelle.

**Confiance et limites :** Aucun changement de position ni de valeur logique.

**Question de révision :** Le mot inversement est-il assez clair après les deux valeurs explicites ?

Passages de référence : L06, L10, L15.

## C326 — OLP-0033-B17

**Choix :** il existerait un indice~$k$ ; pour tout~$n$ ; En particulier, pour $n = k$ ; Dans les deux cas

**Autre formulation envisagée :** Supposer que la suite construite égale une ligne k impose l’égalité au terme k, en contradiction avec la définition de ce terme.

**Motif :** L15 donne le modèle fonctionnel de l’égalité en chaque point ; L06 atteste la spécialisation de l’argument au témoin qui produirait l’égalité. L’existence de k précède le pour tout n ; l’instanciation n=k conserve l’ordre logique. Les deux possibilités du bit diagonal et leur contradiction restent exposées.

**Confiance et limites :** Existence, universalité et instanciation sont toutes présentes.

**Question de révision :** Le rappel de l’égalité des suites doit-il renvoyer à l’extensionnalité des fonctions ?

Passages de référence : L06, L10, L15.

## C327 — OLP-0033-B18

**Choix :** à partir de cette liste ; dès lors
que toutes les suites ; de \emph{tous} les éléments ; conduit à une contradiction

**Autre formulation envisagée :** Toute liste de suites binaires engendre une autre suite binaire qui lui échappe ; aucune liste ne peut donc les contenir toutes.

**Motif :** L06 appuie la conclusion par exclusion de toute surjection ; L10 relie cette conclusion à la dénombrabilité. La reprise garde les deux obligations de preuve : le témoin appartient au bon ensemble et il n’est pas listé. Le mot tous demeure la propriété impossible, non la simple existence d’une liste de quelques suites.

**Confiance et limites :** Conclusion exacte de la construction, sans déduire une cardinalité numérique particulière.

**Question de révision :** La reprise complète est-elle utile au registre pédagogique choisi ?

Passages de référence : L06, L10, L15.

## C328 — OLP-0033-B19

**Choix :** la « diagonalisation » ; n’exige toutefois pas de tableau ; au sens géométrique

**Autre formulation envisagée :** On appelle diagonalisation ce procédé de construction d’un objet différent de chaque objet listé au point correspondant.

**Motif :** L06 présente précisément le procédé sans tableau ; le mot diagonalisation et la distinction géométrique viennent de la présentation OLP. Aucun passage lié n’est présenté comme attestation lexicale de diagonalisation. La traduction conserve la généralisation conceptuelle : on peut appliquer la méthode même sans dessiner une diagonale.

**Confiance et limites :** Le schéma est solidement attesté ; le choix lexical français demeure révisable avec un témoin direct ultérieur.

**Question de révision :** Un passage canonique ultérieur doit-il renforcer l’attestation du mot diagonalisation ?

Passages de référence : L06, L10.

## C329 — OLP-0033-B20

**Choix :** n’est pas !!{enumerable}

**Autre formulation envisagée :** L’ensemble des parties des entiers strictement positifs est non dénombrable.

**Motif :** L05 définit l’ensemble des parties et L06 en donne le théorème de Cantor ; L10 fixe la formulation inclusive niée. L’original écrit not enumerable, conservé comme négation explicite plutôt que remplacé automatiquement par un autre token.

**Confiance et limites :** L’ensemble des parties et la portée de la négation sont intacts.

**Question de révision :** Faut-il harmoniser les deux formulations équivalentes des titres de théorèmes ?

Passages de référence : L05, L06, L10.

## C330 — OLP-0033-B21

**Choix :** toute liste de parties ; pour tout
$n \in \PosInt$ ; si et seulement si ; Par définition ; pour tout $k \in \PosInt$

**Autre formulation envisagée :** À partir d’une liste de parties, formez l’ensemble des indices qui n’appartiennent pas à la partie de même indice ; montrez qu’il diffère de chacune d’elles.

**Motif :** L05 fixe les parties, L06 fournit directement le schéma Y={x:x n’appartient pas àf(x)} et L10 le résultat visé. Par définition justifie l’appartenance à PosInt par la restriction explicite n dansPosInt ; elle ne dépend pas d’un raisonnement implicite sur l’union des Z_n. La double quantification et le biconditionnel restent complets.

**Confiance et limites :** Même ensemble diagonal et mêmes obligations de preuve.

**Question de révision :** La transition entre l’indice n de la définition et l’indice k arbitraire est-elle assez nette ?

Passages de référence : L05, L06, L10.

## C331 — OLP-0033-B22

**Choix :** quelconque ; En particulier, pour $n=k$ ; à l’un et pas à l’autre ; Comme $k$ était quelconque

**Autre formulation envisagée :** Fixez un indice k arbitraire : l’appartenance de k distingue l’ensemble diagonal de Z_k ; aucun indice ne peut donc le lister.

**Motif :** L01 donne l’extensionnalité et L06 l’argument de Cantor au point diagonal. À l’un et pas à l’autre garde l’alternative exclusive provenant du biconditionnel avec négation. La conclusion pour toute la liste découle de k arbitraire, et non d’un seul exemple.

**Confiance et limites :** Le témoin de différence pour chaque Z_k est précisément k.

**Question de révision :** La mention explicite de l’extensionnalité apporterait-elle quelque chose après le premier chapitre ?

Passages de référence : L06, L10, L01.

## C332 — OLP-0033-B23

**Choix :** chaque élément~$j \in Z_i$ ; on exclut ; on inclut les indices~$j$ ; la case à la ligne~$j$ et à la colonne~$j$ est vide

**Autre formulation envisagée :** Dans le tableau d’appartenance, retenez exactement les indices dont la case diagonale est vide.

**Motif :** L06 fournit le sens de la négation diagonale ; les quatre ensembles et toutes les cellules sont ceux d’OLP. La case vide n’est pas un élément indéfini d’une suite : elle représente l’absence du nombre dans un ensemble. Les exclusions1,2,4 et l’inclusion3 sont conservées et restent un début d’exemple, non la définition complète de l’ensemble diagonal.

**Confiance et limites :** Correspondance tableau/formule vérifiée cellule par cellule dans le préfixe affiché.

**Question de révision :** Faut-il distinguer visuellement une case vide d’une valeur0 dans les deux tableaux successifs ?

Passages de référence : L06, L10.

## C333 — OLP-0033-B24

**Choix :** Montrez, par un argument diagonal

**Autre formulation envisagée :** Démontrez directement par diagonalisation la non-dénombrabilité de l’ensemble des parties de Nat.

**Motif :** L05 et L06 donnent l’objet et la méthode ; L02 atteste le registre d’exercice à démontrer, l’impératif restant éditorial. Nat remplace ici PosInt dans la consigne source, ce changement de domaine n’est pas effacé. Le zéro doit donc être traité selon la numérotation choisie dans la solution.

**Confiance et limites :** Même exercice et même méthode imposée.

**Question de révision :** Faut-il rappeler que Nat comprend zéro sans donner la construction ?

Passages de référence : L05, L06, L10, L02.

## C334 — OLP-0033-B25

**Choix :** par un argument diagonal explicite ; dont chacune vérifie ; construisez
une fonction ; qui ne figure
pas dans cette liste

**Autre formulation envisagée :** Pour toute liste de fonctions des entiers strictement positifs dans eux-mêmes, donnez une fonction de même type qui manque à la liste.

**Motif :** L06 appuie la construction d’un témoin diagonal, L10 le résultat et L02 la consigne. Chacune conserve le type de toutes les fonctions listées ; la nouvelle fonction a exactement le même domaine et la même arrivée. Construisez rend explicite le show there is demandé par un explicit diagonal argument, sans fournir la formule de solution.

**Confiance et limites :** Le type et les quantificateurs de la fonction omise sont entièrement maintenus.

**Question de révision :** La formule de la solution doit-elle rester entièrement à la charge du lecteur ?

Passages de référence : L06, L10, L02.

## C335 — OLP-0034-B04

**Choix :** Réduction

**Autre formulation envisagée :** Méthode par réduction

**Motif :** Titre bref conforme au rôle de la section : transférer une énumération hypothétique par une surjection. L17 atteste le mécanisme, pas le lexème réduction ; celui-ci est adopté provisoirement comme transposition du terme OLP. Contrôle final du rendu : une réserve locale de place empêche le titre Réduction de rester isolé en bas de page. Aucun mot ni contenu mathématique ne change.

**Confiance et limites :** sens mathématique assuré, attestation lexicale française spécifique absente des témoins lus

**Question de révision :** Préférer le titre explicite Méthode par réduction dans cette première exposition ?

Passages de référence : L17.

## C336 — OLP-0034-B05

**Choix :** établit la non-dénombrabilité par réduction ; un peu plus
  condensée ; correspondant aux résultats

**Autre formulation envisagée :** Cette section démontre par réduction les résultats de non-dénombrabilité présentés précédemment ; une variante plus concise suit.

**Motif :** Établit convient à des résultats démontrés ; correspondant décrit la dépendance aux deux sections sans les confondre. Les trois renvois sont conservés. L17 éclaire réduction et L10 la convention de dénombrabilité, sans attester cette phrase éditoriale.

**Confiance et limites :** relations entre les trois sections contrôlées dans OLP

**Question de révision :** La formule correspondant aux résultats rend-elle assez visible le choix de version ?

Passages de référence : L10, L17.

## C337 — OLP-0034-B06

**Choix :** montré par diagonalisation ; l'ensemble de toutes les suites
infinies ; si
$\Pow{\PosInt}$ est !!{enumerable}, alors $\Bin^\omega$ l'est aussi ; nous réduisons le problème ; Une solution du second problème ; fournirait une solution du premier

**Autre formulation envisagée :** Une énumération supposée de l'ensemble des parties donnerait une énumération des suites binaires, ce qui est impossible.

**Motif :** La chaîne conditionnelle, sa contraposition et le sens du transfert sont tous conservés, avec premier/second explicités. L17 justifie l'image surjective d'un dénombrable ; L10 préserve fini/vide. Diagonalisation reste la formulation éditoriale déjà motivée dans le lot précédent, sans prétendre que L17 la nomme.

**Confiance et limites :** implication et sens de réduction suivis sur les deux ensembles nommés

**Question de révision :** Le rappel en quatre phrases reste-t-il suffisamment fluide sans réduire l'explication ?

Passages de référence : L10, L17.

## C338 — OLP-0034-B07

**Choix :** transformer une énumération de~$A$ en une énumération de~$B$ ; une fonction !!{surjective} ; Si $x_1$, $x_2$, \dots{} énumèrent~$A$ ; nous cherchons donc

**Autre formulation envisagée :** Pour obtenir une énumération de B à partir d'une énumération de A, on applique une surjection de A vers B à chaque terme.

**Motif :** La question est suivie de sa construction explicite ; surjective suit le nom français fonction. L17 contrôle le transfert, H17 sa condition sur l'arrivée. L'hypothèse d'une liste infinie implique ici A non vide ; le paragraphe n'affirme pas l'existence d'une telle liste pour l'ensemble vide.

**Confiance et limites :** hypothèses de liste et surjectivité conservées

**Question de révision :** Faut-il rappeler le cas vide dans ce paragraphe général malgré son exclusion implicite par la liste donnée ?

Passages de référence : L17, H17.

## C339 — OLP-0034-B08

**Choix :** s'il existe une fonction !!{injective} $g\colon B \to A$ ; et si $B$ est !!{nonenumerable} ; transformer une énumération de~$A$
en une énumération de~$B$

**Autre formulation envisagée :** Étant donnée une injection de B dans A avec B non dénombrable, montrer que A est non dénombrable en transférant une énumération supposée.

**Motif :** Montrer suivi de deux hypothèses coordonnées préserve l'injection en sens inverse de la surjection précédente. L02 atteste le registre d'exercice, H17 l'injectivité et L17 le mécanisme des premiers antécédents. B non dénombrable assure B non vide, condition utile à la construction.

**Confiance et limites :** sens de flèche et deux hypothèses vérifiés

**Question de révision :** Le terme transformer laisse-t-il assez de place à la construction demandée sans fournir la solution ?

Passages de référence : L02, H17, L17.

## C340 — OLP-0034-B09

**Choix :** Démonstration du ; Supposons que $\Pow{\PosInt}$ soit !!{enumerable} ; Il en existe alors
une énumération

**Autre formulation envisagée :** Raisonnons par l'absurde et énumérons les parties des entiers strictement positifs.

**Motif :** Supposons au subjonctif introduit l'hypothèse contraire. Le passage à une suite est licite car l'ensemble des parties contient au moins l'ensemble vide ; L10 ne transforme pas la convention finie-inclusive en infinité obligatoire. Contrôle du rendu : olref produit « théorème » sans article. La contraction du remplace donc de devant ces renvois, y compris les branches alternatives. Correction grammaticale de l’édition, sans changement de référence ni de mathématiques ; le registre des preuves reste celui des passages déjà consultés, sans nouvelle attestation lexicale revendiquée.

**Confiance et limites :** ensemble énuméré non vide et renvoi conservé

**Question de révision :** L'annonce explicite par l'absurde améliorerait-elle le repérage ?

Passages de référence : L10, L17.

## C341 — OLP-0034-B10

**Choix :** en associant
à chaque $Z$ la suite $s$ ; $s(n) = 1$ si et seulement si
$n \in Z$ ; $s(n) = 0$ sinon ; Cela définit bien une fonction ; entiers
pairs strictement positifs ; l'ensemble vide a pour image

**Autre formulation envisagée :** Associons à Z sa suite caractéristique, dont le terme d'indice n vaut 1 lorsque n appartient à Z et 0 sinon.

**Motif :** Le biconditionnel, la totalité et les trois exemples restent explicites ; pas de remplacement de la preuve par le seul terme caractéristique. L15 contrôle domaine/image et L05 les parties. L'indice source k sans définition est retiré avec note visible ; indexation par PosInt conservée, donc 0101 pour les pairs.

**Confiance et limites :** définition et exemples vérifiés terme à terme

**Question de révision :** Employer en plus suite caractéristique aiderait-il sans anticiper une notion nouvelle ?

Passages de référence : L15, L05, H17.

## C342 — OLP-0034-B11

**Choix :** à toute suite de $0$ et de
$1$ ; celui des
indices auxquels la suite vaut~$1$ ; Z = \Setabs{n \in \PosInt}{s(n) = 1} ; On a alors $f(Z) = s$

**Autre formulation envisagée :** Chaque suite binaire est l'image de l'ensemble des indices de ses termes égaux à 1.

**Motif :** La surjectivité est prouvée à partir d'un élément arbitraire de l'arrivée et d'un antécédent construit ; H17 fixe ce sens et L05 la partie de PosInt. La formule et la vérification f(Z)=s ne sont pas remplacées par une simple affirmation.

**Confiance et limites :** antécédent explicite pour toute suite

**Question de révision :** Préférer termes égaux à 1 à indices auxquels la suite vaut 1 ?

Passages de référence : H17, L05.

## C343 — OLP-0034-B12

**Choix :** chaque élément de $\Bin^\omega$ ; en un certain argument ; doit donc figurer dans
cette liste ; énumère ainsi tout~$\Bin^\omega$

**Autre formulation envisagée :** Tout élément de l'arrivée est atteint par f, donc apparaît parmi les images des termes de l'énumération.

**Motif :** Chaque et certain conservent la portée universelle/existentielle. La liste des Z épuise le domaine, la surjectivité épuise l'arrivée : L17 et H17 soutiennent séparément ces deux étapes.

**Confiance et limites :** aucun passage de toute suite à certaines suites

**Question de révision :** Le lien entre l'argument et l'un des Z_i mérite-t-il un rappel supplémentaire ?

Passages de référence : L17, H17.

## C344 — OLP-0034-B13

**Choix :** était !!{enumerable} ; le serait
donc aussi ; Or $\Bin^\omega$ est !!{nonenumerable} ; Par conséquent

**Autre formulation envisagée :** La dénombrabilité de l'ensemble des parties entraînerait celle des suites binaires, déjà réfutée.

**Motif :** Conditionnel et Or distinguent l'hypothèse contrefactuelle du théorème acquis. L17 fournit la propagation ; L10 garde la négation exacte de la dénombrabilité adoptée. Renvoi au théorème conservé.

**Confiance et limites :** contradiction et conclusion exactes

**Question de révision :** La conclusion répétée alourdit-elle le passage ou renforce-t-elle utilement la réduction ?

Passages de référence : L17, L10.

## C345 — OLP-0034-B14

**Choix :** le sens de la réduction ; ne permet
\emph{pas} ; son premier terme ; Pourtant, $\Bin$ est fini ; doit être !!{surjective} ; $n$ zéros ; Nous le complétons ici par une infinité de $1$ ; la suite constante égale à $0$

**Autre formulation envisagée :** Une surjection depuis les suites binaires n'impose aucune non-dénombrabilité à son arrivée ; une application vers elles ne suffit pas sans surjectivité.

**Motif :** Les deux écueils sont distincts : direction de la flèche puis nécessité de surjectivité. H17/L17 justifient cette distinction ; premier terme convient à une suite. Le mot fini h(n) de la source est complété par 111… avec note, préservant ses n zéros et donnant une vraie valeur dans Bin^omega. Ce complément est une réparation éditoriale, pas une intention attribuée à OLP.

**Confiance et limites :** exemples et contre-exemple vérifiés, correction déclarée

**Question de révision :** Une autre complétion infinie serait-elle pédagogiquement plus simple que la queue constante égale à 1 ?

Passages de référence : H17, L17, L10.

## C346 — OLP-0034-B15

**Choix :** l'ensemble de tous les \emph{ensembles de}
couples ; entiers strictement positifs

**Autre formulation envisagée :** Montrer par réduction la non-dénombrabilité de l'ensemble des parties du produit PosInt×PosInt.

**Motif :** L'emphase conserve le niveau supplémentaire de parties : l'exercice ne porte pas sur le seul ensemble des couples, qui est dénombrable. L02 soutient couples et registre Montrer ; L05 identifie la formation de parties.

**Confiance et limites :** deux niveaux d'ensembles et positivité préservés

**Question de révision :** La formulation par ensemble des parties serait-elle plus directe à ce stade ?

Passages de référence : L02, L05, L10.

## C347 — OLP-0034-B16

**Choix :** l'ensemble~$X$ de toutes les fonctions ; $f\colon \Nat \to \Nat$ ; une fonction surjective de $X$ dans~$\Bin^\omega$

**Autre formulation envisagée :** Construire une surjection de l'espace des fonctions Nat→Nat sur les suites binaires pour établir sa non-dénombrabilité.

**Motif :** Toutes porte sur les fonctions totales selon OLP ; l'indication conserve le sens X→Bin^omega. L15 contrôle le domaine exact et H17 la surjectivité ; L02 donne le registre de consigne.

**Confiance et limites :** type fonctionnel et sens de réduction conservés

**Question de révision :** Préférer sur à dans pour l'arrivée d'une surjection ?

Passages de référence : L02, L15, H17.

## C348 — OLP-0034-B17

**Choix :** $\Nat^\omega$, l'ensemble des suites
infinies d'entiers naturels ; Montrer par réduction

**Autre formulation envisagée :** Établir la non-dénombrabilité de l'ensemble des suites infinies à valeurs naturelles par un transfert d'énumération.

**Motif :** L'apposition explicite le symbole sans confondre suite infinie et mot fini ; L10 conserve le sens de non-dénombrable. L17 fonde le schéma de réduction, sans prétention d'attestation lexicale directe.

**Confiance et limites :** infinité de longueur et valeurs naturelles préservées

**Question de révision :** Suites infinies d'entiers naturels ou suites à valeurs naturelles ?

Passages de référence : L02, L10, L17.

## C349 — OLP-0034-B18

**Choix :** fonctions de l'ensemble des entiers
strictement positifs dans $\{0\}$ ; fonctions \emph{partielles} entre ces mêmes ensembles ; $P$ est !!{enumerable} et que $Q$ ne l'est pas ; à celui de
l'énumération de~$Q$

**Autre formulation envisagée :** Comparer les applications totales à valeur 0, réduites à une seule application, avec les applications partielles à valeur 0.

**Motif :** Ces mêmes ensembles évite une répétition tout en conservant départ/arrivée. H16 est consulté pour le vocabulaire fonction, avec sa convention partielle expressément non importée dans P ; L15 fixe la totalité OLP. La différence porte sur les domaines de définition, et l'indication oriente Bin^omega vers Q.

**Confiance et limites :** distinction total/partiel et portée de la négation vérifiées

**Question de révision :** Répéter explicitement totales dans P serait-il utile après la définition générale de fonction ?

Passages de référence : L02, L15, H16, L17.

## C350 — OLP-0034-B19

**Choix :** toutes les fonctions !!{surjective}s ; $\{0,1\}$ ; contient exactement ; $f\colon \PosInt \to \Bin$

**Autre formulation envisagée :** Soit S la famille des surjections des entiers strictement positifs sur {0,1} ; prouver sa non-dénombrabilité.

**Motif :** L'adjectif pluriel suit fonctions et doit produire surjectives via la configuration de macros. Contient exactement rend consists of all, sans élargir aux suites constantes exclues par surjectivité. H17 atteste la propriété, L02 le registre.

**Confiance et limites :** quantification sur les seules surjections conservée

**Question de révision :** La répétition fonctions surjectives peut-elle être raccourcie après la formule ?

Passages de référence : H17, L02, L10.

## C351 — OLP-0034-B20

**Choix :** l'ensemble~$\Real$ des nombres réels

**Autre formulation envisagée :** Établir que les réels ne sont pas au plus dénombrables.

**Motif :** Le registre infinitif et la notation restent ceux des autres exercices. L10 soutient le prédicat ; il n'est pas revendiqué ici comme une preuve du résultat, que l'exercice OLP demande au lecteur.

**Confiance et limites :** consigne intégrale sans ajout de méthode imposée

**Question de révision :** Conserver l'absence d'indication comme dans OLP ?

Passages de référence : L02, L10.

## C352 — OLP-0035-B04

**Choix :** Équipotence

**Autre formulation envisagée :** Ensembles de même cardinalité

**Motif :** L18 atteste équipotents et L19 classes d'équipotence. Le substantif est donc directement fondé en français et s'accorde à la définition suivante ; le titre alternatif est plus explicatif mais moins compact.

**Confiance et limites :** terme effectivement lu dans la page française

**Question de révision :** Le titre pourrait-il joindre les deux formes à la première occurrence ?

Passages de référence : L18, L19.

## C353 — OLP-0035-B05

**Choix :** ensembles
\emph{quelconques} ; autant de
  couteaux que d'assiettes ; ni les uns ni les
  autres ; à droite de chaque
  assiette ; chaque couteau sur la table ; univoque dans les deux sens ; la
  même relation de position ; Traduction
  établie pour cette édition

**Autre formulation envisagée :** Pour comparer des ensembles arbitraires, partir de la même taille ; Frege illustre une correspondance bijective par le placement des couteaux et assiettes.

**Motif :** Quelconques maintient any size sans finitude implicite. F01 allemand contrôle beiderseits eindeutig et gleiche Lagenverhältniss : univoque dans les deux sens et même relation de position, plutôt que simple rapprochement spatial. Serveur actualise Kellner sans familiarité. Traduction propre déclarée, aucune attribution à un traducteur français publié. L18 soutient l'exposition par comparaison avant cardinalité.

**Confiance et limites :** passage allemand lu, double unicité et réciprocité conservées

**Question de révision :** Relation de position ou relation spatiale restitue-t-il mieux Lagenverhältniss dans cette citation ?

Passages de référence : L18, F01.

## C354 — OLP-0035-B06

**Choix :** \emph{équipotent} à $B$ ; $\cardeq{A}{B}$ ; si et seulement s'il existe une !!{bijection}

**Autre formulation envisagée :** Deux ensembles sont équipotents lorsqu'il existe une bijection de l'un sur l'autre.

**Motif :** On dit que et et on écrit articulent définition et notation ; à est la construction française d'équipotent, attestée par le contexte de L18. Le biconditionnel est explicite et la flèche A→B intacte.

**Confiance et limites :** définition conforme au témoin français et à OLP

**Question de révision :** Privilégier Deux ensembles sont équipotents ou garder l'orientation A à B de la source ?

Passages de référence : L18, H17.

## C355 — OLP-0035-B07

**Choix :** relation d'équivalence ; réflexive, symétrique et
transitive ; elle-même un ensemble ; on ne suppose pas l'existence d'un
ensemble de tous les ensembles

**Autre formulation envisagée :** L'équipotence satisfait les trois propriétés d'équivalence ; sa restriction à tout ensemble de sets est une relation d'équivalence au sens strict.

**Motif :** La proposition originale est conservée, avec une précision qui distingue la classe globale du cadre ensembliste antérieur. L06 explique classe propre et absence d'ensemble universel ; L19 parle de classes d'équipotence. La note n'ajoute pas d'axiome et ne restreint aucune des trois propriétés universelles sur les ensembles.

**Confiance et limites :** clarification de cadre, pas modification du théorème

**Question de révision :** La note est-elle mieux placée lors de la première relation entre ensembles arbitraires ?

Passages de référence : L06, L19.

## C356 — OLP-0035-B08

**Choix :** Il faut montrer ; réflexive, symétrique et
transitive ; Soient $A$, $B$ et $C$

**Autre formulation envisagée :** Vérifions successivement les trois propriétés sur des ensembles arbitraires A, B et C.

**Motif :** La nécessité démonstrative reste distincte d'une définition supplémentaire. La triade est celle de l'équivalence OLP ; L19 justifie le contexte d'équipotence, L18 le registre Soient/ensembles. La page n'est pas présentée comme contenant cette preuve exacte.

**Confiance et limites :** objectif et variables de preuve conservés

**Question de révision :** Annoncer successivement les propriétés améliorerait-il l'orientation du lecteur ?

Passages de référence : L18, L19.

## C357 — OLP-0035-B09

**Choix :** L'application identité ; pour tout $x \in A$ ; est une
!!{bijection} ; $\cardeq{A}{A}$

**Autre formulation envisagée :** L'identité de A est bijective, donc A est équipotent à lui-même.

**Motif :** H16 atteste fonction identité et sa formule, H17 la bijectivité. Application est cohérent avec L15. La portée pour tout et la conclusion formelle sont conservées.

**Confiance et limites :** identité y compris domaine vide vérifiée

**Question de révision :** Uniformiser fonction identité et application identité dans tout le chapitre ?

Passages de référence : H16, H17, L15.

## C358 — OLP-0035-B10

**Choix :** sa réciproque $f^{-1}$ existe ; elle aussi !!{bijective} ; $f^{-1}\colon B \to A$ ; $\cardeq{B}{A}$

**Autre formulation envisagée :** La bijection réciproque de f donne une correspondance de B vers A.

**Motif :** Réciproque distingue l'inverse fonctionnel de la relation inverse, déjà réglé au chapitre fonctions. H15/H17 contrôlent que la bijectivité assure ici l'inverse fonctionnel ; flèche et conclusion sont préservées.

**Confiance et limites :** inverse d'une bijection seulement, sans généralisation abusive

**Question de révision :** Rappeler le résultat sur la réciproque par un renvoi serait-il utile ?

Passages de référence : H15, H17, L18.

## C359 — OLP-0035-B11

**Choix :** il existe des !!{bijection}s ; La composée $\comp{f}{g}\colon A \to C$ ; $\cardeq{A}{C}$

**Autre formulation envisagée :** En composant la bijection de A vers B puis celle de B vers C, on obtient une bijection de A vers C.

**Motif :** H18 fixe l'ordre d'application : la macro OLP comp(f,g) se lit g après f. Composée est féminin substantivé, et les deux hypothèses d'équipotence restent explicites. Aucun échange de f et g.

**Confiance et limites :** domaines, arrivée et ordre de composition contrôlés

**Question de révision :** Développer g(f(x)) à cette occurrence ou garder la notation déjà définie ?

Passages de référence : H18, H17, L18.

## C360 — OLP-0035-B12

**Choix :** Si $\cardeq{A}{B}$ ; si et seulement si
$B$ l'est

**Autre formulation envisagée :** Deux ensembles équipotents sont simultanément au plus dénombrables ou non dénombrables.

**Motif :** Le biconditionnel sous hypothèse d'équipotence conserve le cas vide et les ensembles finis de L10. La variante choisie reste proche de la formulation propositionnelle OLP sans changer le sens en infinité dénombrable.

**Confiance et limites :** hypothèse et deux directions intactes

**Question de révision :** Le terme simultanément ferait-il gagner en concision au prix d'une formule moins explicite ?

Passages de référence : L10, L18.

## C361 — OLP-0035-B13

**Choix :** si la \olref[enm]{sec} est incluse ; dans le cas contraire ; les deux versions sont présentées ci-dessous

**Autre formulation envisagée :** La preuve s'adapte à la définition de dénombrabilité incluse dans le lecteur.

**Motif :** Les deux renvois de définition et celui de section sont maintenus ; dans le cas contraire traduit une branche conditionnelle réelle. L10 contrôle que les deux présentations concernent la même convention finie-inclusive, pas deux sens distincts de dénombrable. Intégration ultérieure : le lecteur complet expose les deux branches, annoncées explicitement dans cet éditorial ; les versions restent sélectionnables en réutilisation isolée.

**Confiance et limites :** test d'inclusion et renvois inchangés

**Question de révision :** Faut-il nommer les deux présentations dans l'édition intégrée ?

Passages de référence : L10.

## C362 — OLP-0035-B14

**Choix :** Ou bien $A = \emptyset$ ; contrairement à la surjectivité de~$f$ ; C'est la fonction
  $f\colon A \to B$ ; celle de $g$ fournit ; (\comp{g}{f})(n) = f(g(n)) = f(x) = y ; un segment
  initial des entiers naturels ; de même domaine que~$g$ ; Avec une énumération par surjection. ; Avec une énumération bijective.

**Autre formulation envisagée :** Dans le cas vide la bijection f force B vide ; sinon composer une énumération g de A avec f, sous l'une ou l'autre définition, donne une énumération de B.

**Motif :** L10 contrôle la disjonction vide/nonvide, H17 la recherche des antécédents et H18 l'ordre f après g. Les deux branches OLP sont intégralement traduites ; g(x)=y dans le cas vide est corrigé en f(x)=y avec notes dans chacune des branches. Segment initial remplace initial sequence sans confondre domaine fini et image. Toutes les étapes n→x→y et la formule affichée demeurent. Intégration ultérieure : deux intertitres Avec une énumération par surjection / Avec une énumération bijective rendent visibles les deux preuves sans modifier leur contenu ni doubler le chapitre.

**Confiance et limites :** deux branches et cas vide vérifiés séparément

**Question de révision :** L'expression d'image B conserve-t-elle assez explicitement que B est aussi l'arrivée de la bijection composée ?

Passages de référence : L10, H17, H18, L15.

## C363 — OLP-0035-B15

**Choix :** en
reprenant l'argument ; $f^{-1}\colon B \to A$ ; à la place de~$f$

**Autre formulation envisagée :** L'implication réciproque s'obtient en appliquant la même preuve à la bijection inverse.

**Motif :** La reprise ne supprime pas une direction : elle en donne la construction à partir de f inverse. H15/H17 assurent sa bijectivité, L10 le même prédicat des deux côtés.

**Confiance et limites :** sens réciproque explicite et typé

**Question de révision :** Faut-il nommer implication réciproque plutôt que répéter les ensembles ?

Passages de référence : H15, H17, L10.

## C364 — OLP-0035-B16

**Choix :** si $\cardeq{A}{C}$ et $\cardeq{B}{D}$ ; $A \cap B = C \cap D = \emptyset$ ; $\cardeq{A \cup B}{C \cup D}$

**Autre formulation envisagée :** Montrer que les unions de deux paires disjointes d'ensembles respectivement équipotents sont équipotentes.

**Motif :** Le second si isole l'hypothèse de disjonction aux deux côtés, indispensable pour assembler les bijections. Toutes les intersections/unions et leurs positions sont gardées ; L18 éclaire équipotence et L02 le registre d'exercice, sans prétendre y trouver ce résultat d'union.

**Confiance et limites :** les deux disjonctions et correspondances A/C, B/D vérifiées

**Question de révision :** La paraphrase respectivement équipotents serait-elle moins facile à lire que les formules ?

Passages de référence : L02, L18.

## C365 — OLP-0035-B17

**Choix :** si $A$ est infini et !!{enumerable} ; $\cardeq{A}{\Nat}$

**Autre formulation envisagée :** Établir qu'un ensemble infini au plus dénombrable est équipotent aux naturels.

**Motif :** Infini est conservé à côté du prédicat finie-inclusive, et non absorbé dans dénombrable. L10 discute exactement les conventions qui rendent ce cumul nécessaire ; L18 fonde la conclusion d'équipotence.

**Confiance et limites :** hypothèse d'infinité conservée

**Question de révision :** Conserver la coordination infini et au plus dénombrable plutôt qu'une terminologie supplémentaire ?

Passages de référence : L02, L10, L18.

## C366 — OLP-0036-B04

**Choix :** Ensembles de tailles différentes et théorème de Cantor

**Autre formulation envisagée :** Comparaison des tailles et théorème de Cantor

**Motif :** Tailles reprend l'exposition française de L18 et l'intuition OLP ; Cantor correspond à L06. Le titre source comporte à la fois diversité de tailles et résultat nommé, tous deux conservés.

**Confiance et limites :** titre complet et vocabulaire attesté

**Question de révision :** Le titre alternatif paraît-il plus idiomatique sans perdre l'accent sur des tailles différentes ?

Passages de référence : L18, L06.

## C367 — OLP-0036-B05

**Choix :** une !!{injection} du premier ensemble
dans le second ; au lieu d'une !!{bijection} ; inférieure ou
égale ; l'image contient au moins autant d'éléments que le domaine ; deux éléments distincts

**Autre formulation envisagée :** Une injection du premier ensemble dans le second permet de comparer leurs tailles, car elle ne confond pas deux éléments du départ.

**Motif :** L18 définit la comparaison par injection ; H17 en donne le sens. Image traduit range précisément et ne devient pas ensemble d'arrivée. L'image est même équipotente au domaine, mais l'énoncé plus faible au moins de la source reste vrai ; aucune identification image/arrivée n'est introduite.

**Confiance et limites :** comparaison non stricte et propriété d'injection distinctes

**Question de révision :** Dire exactement autant pour l'image clarifierait-il au prix d'un renforcement inutile de la phrase ?

Passages de référence : L18, H17, L15.

## C368 — OLP-0036-B06

**Choix :** de taille inférieure ou égale à celle
de ; si et seulement s'il existe
une !!{injection} $f \colon A \to B$

**Autre formulation envisagée :** La taille de A ne dépasse pas celle de B lorsqu'une injection de A vers B existe.

**Motif :** La formulation choisie explicite qu'on compare les tailles, pas une inclusion. L18 atteste la construction inférieure et l'injection ; égale rend explicite le caractère non strict qui serait moins visible dans plus petit seul.

**Confiance et limites :** définition et orientation conformes

**Question de révision :** Le groupe de taille inférieure ou égale à celle de est-il trop long pour un terme défini ?

Passages de référence : L18, H17.

## C369 — OLP-0036-B07

**Choix :** réflexive et transitive ; elle n'est pas
symétrique ; on laisse la vérification en exercice ; strictement plus
petit

**Autre formulation envisagée :** Vérifier réflexivité, transitivité et défaut de symétrie, puis passer à la comparaison stricte.

**Motif :** Les trois propriétés sont préservées et la consigne de preuve n'est pas remplacée par une preuve ajoutée. L19 fournit le contexte d'ordre sur cardinalités ; sur les ensembles eux-mêmes l'équipotence ne doit pas être confondue avec égalité.

**Confiance et limites :** propriétés annoncées dans le cadre correct

**Question de révision :** Nommer préordre ici aiderait-il ou anticiperait-il inutilement ?

Passages de référence : L18, L19.

## C370 — OLP-0036-B08

**Choix :** strictement plus petit que ; une !!{injection} ; mais aucune !!{bijection} ; $\cardle{A}{B}$ et $\cardneq{A}{B}$

**Autre formulation envisagée :** A est de taille strictement inférieure à B lorsqu'il s'injecte dans B sans lui être équipotent.

**Motif :** Strictement lève l'ambiguïté de smaller ; mais aucune conserve l'inexistence universelle de bijection, non l'échec d'une seule fonction. L18/L19 soutiennent la comparaison et l'équipotence, OLP gouverne sa notation cardless.

**Confiance et limites :** existence d'injection et absence de toute bijection distinguées

**Question de révision :** Préférer de taille strictement inférieure à l'expression plus petit ?

Passages de référence : L18, L19, H17.

## C371 — OLP-0036-B09

**Choix :** irréflexive et transitive ; $\cardle{A}{\Nat}$ ; $\cardless{\Nat}{A}$ ; Sous l'axiome
du choix ; la négation de $\cardle{A}{\Nat}$ ; \emph{tout à fait général}

**Autre formulation envisagée :** Avec le choix, les ensembles non dénombrables dépassent les naturels ; le théorème de Cantor étend la stricte croissance à tout ensemble et son ensemble des parties.

**Motif :** L10 fournit le sens finie-inclusive ; L19 distingue comparaison et questions de choix. La source omet que non A≤Nat n'implique pas Nat≤A dans ZF ; la note indique AC comme hypothèse suffisante, sans la déclarer minimale. Ca01 vérifie l'extension générale dans l'original de Cantor, reformulée par OLP en parties via fonctions caractéristiques. Les deux renvois conditionnels Nat/PosInt restent distincts. Contrôle du rendu : olref produit « théorème » sans article. La contraction du remplace donc de devant ces renvois, y compris les branches alternatives. Correction grammaticale de l’édition, sans changement de référence ni de mathématiques ; le registre des preuves reste celui des passages déjà consultés, sans nouvelle attestation lexicale revendiquée.

**Confiance et limites :** hypothèse suffisante documentée, non minimale

**Question de révision :** La note devrait-elle citer une hypothèse plus faible que l'axiome du choix ou garder la formulation accessible ?

Passages de référence : L10, L19, Ca01.

## C372 — OLP-0036-B10

**Choix :** Pour tout ensemble $A$ ; $\cardless{A}{\Pow{A}}$

**Autre formulation envisagée :** Tout ensemble est strictement moins grand que l'ensemble de ses parties.

**Motif :** Pour tout conserve la portée y compris le vide. L06 énonce l'absence de surjection et L18 le sens de comparaison ; Ca01 confirme la généralisation historique, sans prétendre que Cantor utilise la notation Pow.

**Confiance et limites :** énoncé universel inchangé

**Question de révision :** Le placement de Pour tout avant la formule améliore-t-il la lecture orale ?

Passages de référence : L06, L18, Ca01.

## C373 — OLP-0036-B11

**Choix :** L'application $f(x) = \{x\}$ ; si $x \neq y$ ; par extensionnalité ; $f(x) \neq f(y)$

**Autre formulation envisagée :** L'application qui associe son singleton à chaque élément est injective par extensionnalité.

**Motif :** L01 atteste extensionnalité, L05 ensemble des parties, H17 l'injectivité. Les quatre étapes explicites singleton/valeurs/comparaison sont conservées. Le domaine vide est permis, sans choisir d'élément de A.

**Confiance et limites :** preuve et cas vide contrôlés

**Question de révision :** Nommer singleton ajouterait-il un repère utile sans remplacer la formule ?

Passages de référence : L01, L05, H17.

## C374 — OLP-0036-B12

**Choix :** la démonstration
détaillée ; une démonstration plus brève ; correspondant à la ; Le lecteur complet conserve les deux démonstrations

**Autre formulation envisagée :** La version détaillée accompagne la section principale ; une preuve condensée accompagne la variante.

**Motif :** Détaillée traduit slow comme degré d'explicitation plutôt que lenteur du lecteur. L06 donne un témoin de preuve courte, OLP fixe les dépendances éditoriales ; tous les renvois sont gardés. Intégration ultérieure : le lecteur complet rend successivement les preuves détaillée et condensée, tandis que la sélection de version reste disponible hors lecteur complet.

**Confiance et limites :** registre adapté sans changer la sélection conditionnelle

**Question de révision :** Détaillée/brève exprime-t-il suffisamment la différence pédagogique des deux versions ?

Passages de référence : L06.

## C375 — OLP-0036-B13

**Choix :** a fortiori
  aucune fonction !!{bijective} ; Puisque $g$ est totale ; \overline{A} = \Setabs{x \in A}{x \notin g(x)} ; Soit $x \in A$ quelconque ; Inversement, si
  $x \notin g(x)$ ; pour chaque
  $x \in A$ ; Il faut considérer chaque $x \in A$ ; Raisonnons par
  l'absurde ; $D \in \Pow{A}$ ; $g(y) = D$ ; Démonstration détaillée. ; Démonstration condensée.

**Autre formulation envisagée :** Construire la partie diagonale et montrer qu'elle diffère de toute valeur de g ; la preuve brève suppose directement un antécédent de cette partie et obtient une contradiction.

**Motif :** L06 a la même construction diagonale et le registre par l'absurde ; L15/H17 contrôlent totalité et surjectivité. La restriction source fautive aux x dans A barré est corrigée en x dans A avec note. Les deux cas d'appartenance et la réciproque sont explicites ; le raisonnement ne suppose pas A non vide. Les deux branches restent intégrales, avec toutes les formules de la preuve courte. Intégration ultérieure : les intertitres Démonstration détaillée / Démonstration condensée exposent les deux branches déjà traduites. Le label de sélection source est préservé dans la macro locale à cinq arguments.

**Confiance et limites :** preuve générale et deux branches vérifiées, quantificateur corrigé explicitement

**Question de révision :** La phrase ajoutée tout x dans A barré satisfait cette condition fait-elle double emploi avec les deux cas, tout en conservant le contenu source ?

Passages de référence : L06, L15, H17.

## C376 — OLP-0036-B14

**Choix :** pour
  toute liste $Z_1$, $Z_2$ ; pour chaque
  $n \in \PosInt$ ; les
  indices~$n$ sont désormais des éléments de~$A$ ; pour chaque $x \in A$,
  cet élément ; ne peut pas appartenir à l'image de~$g$

**Autre formulation envisagée :** La diagonale appliquée à une liste indexée par PosInt devient une diagonale indexée par les éléments de A.

**Motif :** Ca01 montre le passage de la diagonale de suites à l'argument général ; L06 donne sa forme française par parties. La formulation pour chaque x, cet élément évite une existence globale d'élément de A, fausse si A est vide, tout en conservant le témoin de différence pour chaque valeur g(x). Contrôle du rendu : olref produit « théorème » sans article. La contraction du remplace donc de devant ces renvois, y compris les branches alternatives. Correction grammaticale de l’édition, sans changement de référence ni de mathématiques ; le registre des preuves reste celui des passages déjà consultés, sans nouvelle attestation lexicale revendiquée.

**Confiance et limites :** dépendance du témoin à l'indice et cas vide explicites

**Question de révision :** Le parallèle détaillé peut-il être condensé lors de l'intégration des variantes sans supprimer de contenu ?

Passages de référence : L06, Ca01, L15.

## C377 — OLP-0036-B15

**Choix :** $N_0$, $N_1$, $N_2$ ; pour chaque $n \in \Nat$ ; des éléments de~$A$ au lieu d'être des éléments de~$\Nat$ ; pour chaque $x \in A$

**Autre formulation envisagée :** La variante commence l'indexation à zéro mais utilise la même différence diagonale à chaque indice.

**Motif :** La suite N commence à zéro comme OLP alternatif, à la différence des Z indexés positivement. L06/Ca01 soutiennent le principe, pas un changement des conventions d'indexation. Les formules n∈N_n iff n∉D et x∈g(x) iff x∉D sont conservées. Contrôle du rendu : olref produit « théorème » sans article. La contraction du remplace donc de devant ces renvois, y compris les branches alternatives. Correction grammaticale de l’édition, sans changement de référence ni de mathématiques ; le registre des preuves reste celui des passages déjà consultés, sans nouvelle attestation lexicale revendiquée.

**Confiance et limites :** indexation et deux biconditionnels vérifiés

**Question de révision :** La mention explicite variante indexée à zéro faciliterait-elle le rapprochement ?

Passages de référence : L06, Ca01.

## C378 — OLP-0036-B16

**Choix :** rapprocher cette démonstration ; paradoxe
de Russell ; a en effet inspiré à Russell son propre paradoxe

**Autre formulation envisagée :** Le raisonnement peut être comparé au paradoxe de Russell, historiquement issu du théorème de Cantor selon l'exposé OLP.

**Motif :** L06 juxtapose effectivement les deux arguments et justifie le rapprochement mathématique. Il n'est pas présenté comme preuve de l'influence historique ; cette attribution est conservée d'OLP sans précision chronologique supplémentaire et reste distinctement à vérifier dans une source historique primaire.

**Confiance et limites :** comparaison mathématique attestée, attribution historique héritée non vérifiée ici

**Question de révision :** Une référence au témoignage de Russell peut-elle préciser l'attribution sans alourdir le lecteur ?

Passages de référence : L06.

## C379 — OLP-0036-B17

**Choix :** pour tout ensemble~$A$ ; d'!!{injection} $g\colon \Pow{A} \to A$ ; $D = \Setabs{g(B)}{B \subseteq A \text{ et } g(B) \notin B}$ ; $x = g(D)$ ; Utiliser l'injectivité

**Autre formulation envisagée :** Supposer une injection des parties dans A et exploiter la partie diagonale définie dans l'indication pour obtenir une contradiction.

**Motif :** L02 fournit le registre infinitif, L05 la portée B partie de A et H17 le rôle indispensable de l'injectivité. L'indication garde g(B) comme élément de D, et non B lui-même ; aucune inversion du sens de flèche.

**Confiance et limites :** objet D typé partie de A et usage de l'injectivité vérifiés

**Question de révision :** L'élision d'injection via macro produit-elle correctement la typographie lors du rendu ?

Passages de référence : L02, L05, H17.

## C380 — OLP-0037-B04

**Choix :** La notion de taille et le théorème de Schr\"oder-Bernstein

**Autre formulation envisagée :** Taille des ensembles : le théorème de Schröder-Bernstein

**Motif :** L18 emploie tailles et L19 nomme le théorème. La graphie TeX accentuée et le nom source sont conservés ; le titre garde la liaison entre notion intuitive et résultat.

**Confiance et limites :** vocabulaire et nom attestés

**Question de révision :** Titre avec deux-points ou coordination de la source ?

Passages de référence : L18, L19.

## C381 — OLP-0037-B05

**Choix :** si $A$ n'est pas plus grand que $B$ ; si $B$ n'est pas plus grand que $A$ ; équipotents ; si cette idée était \emph{fausse} ; cette intuition est correcte

**Autre formulation envisagée :** La comparaison dans les deux sens doit donner une même taille ; sinon l'interprétation intuitive de l'équipotence serait difficile à défendre.

**Motif :** Les deux comparaisons orientées et le conditionnel contrefactuel sont gardés. L19 fournit la justification mathématique, L18 le vocabulaire d'équipotence ; À vrai dire conserve le ton explicatif adulte sans surenchère. Contrôle final du rendu : des espaces insécables gardent les guillemets avec tailles et un groupe vide après le point d’exclamation empêche le raccourci Babel actif d’absorber l’espace qui suit. Ponctuation et mots conservés.

**Confiance et limites :** intuition distinguée de sa preuve

**Question de révision :** Le ton À vrai dire convient-il au registre du chapitre ?

Passages de référence : L18, L19.

## C382 — OLP-0037-B06

**Choix :** Si $\cardle{A}{B}$ et $\cardle{B}{A}$ ; $\cardeq{A}{B}$

**Autre formulation envisagée :** Deux injections en sens opposés impliquent une bijection.

**Motif :** L19 énonce exactement le principe dans une notation de cardinalités ; les macros OLP restent inchangées. Il ne s'agit pas de conclure A=B, ni de déclarer les deux injections réciproques.

**Confiance et limites :** hypothèses et conclusion identiques

**Question de révision :** Aucune incertitude mathématique ; faut-il rappeler la lecture des symboles ?

Passages de référence : L19.

## C383 — OLP-0037-B07

**Choix :** une !!{injection} de $A$ dans~$B$ ; une !!{injection} de $B$ dans~$A$ ; une
!!{bijection} de $A$ dans~$B$

**Autre formulation envisagée :** S'injecter l'un dans l'autre suffit pour être équipotents.

**Motif :** La reformulation explicite toutes les flèches au lieu de laisser la réciprocité implicite. L19 atteste cette paraphrase du théorème et H17 distingue propriétés d'injection et de bijection.

**Confiance et limites :** aucun lien inverse supplémentaire entre les injections

**Question de révision :** Préférer une bijection de A sur B à dans B pour marquer la surjectivité ?

Passages de référence : L19, H17.

## C384 — OLP-0037-B08

**Choix :** assez \emph{difficile} à démontrer ; d'autres mathématiciens ; \citet[pp.~165--6]{Potter2004} ; outils nécessaires ; Pour le moment, vous pouvez, et devez, l'admettre

**Autre formulation envisagée :** La preuve est différée à une section ultérieure ; en attendant, le théorème est admis et une référence historique est fournie.

**Motif :** L19 prouve le théorème, donc son admission locale n'est pas un doute mathématique. Difficile garde l'appréciation pédagogique OLP, non un classement objectif. L'entrée Oxford de Potter et le chapitre155–166 sont retrouvés, mais les pages165–166 ne sont pas accessibles dans le résultat consulté ; aucune consultation intégrale ni attestation historique indépendante n'est revendiquée. Citation et branche de renvoi conservées.

**Confiance et limites :** théorème attesté et texte source conservé ; détail historique Potter non consulté intégralement

**Question de révision :** Contrôler les pages165–166 lorsqu'elles deviennent accessibles et nuancer au besoin l'attribution sans suspendre la production ?

Passages de référence : L19.

## C385 — OLP-0037-B09

**Choix :** comparaisons de « taille » ; Construire une !!{bijection} ; scinder ce travail en deux ; puis une autre dans le sens inverse

**Autre formulation envisagée :** Le théorème donne un critère pratique : construire deux injections, une dans chaque sens, au lieu de trouver directement une bijection.

**Motif :** L19 justifie le critère et L18 l'interprétation par taille. Scinder ce travail en deux rend break down into cases comme deux constructions suffisantes, non une preuve par cas sur les éléments. Puis ordonne l'exposition sans exiger que les deux injections soient inverses.

**Confiance et limites :** conséquence pratique exacte et aucune hypothèse supplémentaire

**Question de révision :** Le mot puis peut-il être remplacé par et pour éviter une dépendance temporelle suggérée ?

Passages de référence : L19, L18, H17.

## C386 — OLP-0027-B03

**Choix :** La taille des ensembles

**Autre formulation envisagée :** Cardinalité des ensembles

**Motif :** L18 introduit les tailles par comparaison, avant de définir un objet cardinal. Taille garde cette progression OLP ; cardinalité serait plus technique et moins proche de l'ouverture intuitive.

**Confiance et limites :** notion et titre cohérents avec le canon lu

**Question de révision :** Préférer le singulier taille au pluriel tailles dans un titre général ?

Passages de référence : L18.

## C387 — OLP-0027-B04

**Choix :** des énumérations, de la dénombrabilité ; listes, ou des surjections depuis $\PosInt$ ; des bijections avec
$\Nat$ ou un segment initial ; les segments initiaux sont nécessaires

**Autre formulation envisagée :** Deux présentations sont proposées : listes avec répétitions permises et énumérations bijectives sans répétitions.

**Motif :** Le double régime d'énumération est explicité sans transformer la dénombrabilité en calculabilité. L10 fixe le sens finie-inclusive ; L17 soutient les listes obtenues par surjection. Le complément segment initial répare l'abréviation du premier éditorial source et est déclaré en note, conformément à la définition détaillée OLP.

**Confiance et limites :** les deux définitions ont été lues et comparées

**Question de révision :** La note sur l'abréviation de la source peut-elle rester discrète à l'ouverture du chapitre ?

Passages de référence : L10, L17.

## C388 — OLP-0027-B15

**Choix :** sont des variantes de la ; rédigées par Tim Button ; \emph{Open Set Theory} ; une autre définition des énumérations ; ou avec un segment initial

**Autre formulation envisagée :** Les trois variantes dues à Tim Button reprennent les mêmes thèmes selon la convention bijective de la théorie des ensembles.

**Motif :** L'attribution de source est conservée exactement sans ajouter de crédit personnel. Définition des énumérations précise le changement opérationnel : le prédicat au plus dénombrable reste équivalent. Les six renvois et les deux types de domaine demeurent ; le lapsus anglais difference est rendu idiomatiquement par autre. Contrôle final du rendu : les six macros produisent chacune le nom section ; leurs articles sont exprimés individuellement pour éviter sections section. Attribution et correspondances conservées, sans nouvelle attestation de canon revendiquée.

**Confiance et limites :** attribution et dépendances contrôlées dans le driver OLP

**Question de révision :** Nommer définition des énumérations évite-t-il mieux de suggérer deux classes différentes d'ensembles dénombrables ?

Passages de référence : L10, L17, L18.

## C389 — OLP-0038-B04

**Choix :** Énumérations bijectives ; \usetoken{p}{enumerable}

**Autre formulation envisagée :** Énumérations sans répétition et ensembles au plus dénombrables

**Motif :** Bijectives distingue la variante dans la table des matières intégrée. Le token passe de S anglais à p français pour qualifier ensembles au pluriel sans capitale ; la notion finie-inclusive reste celle de L10 et la bijection celle de H17.

**Confiance et limites :** accord et distinction de version intentionnels

**Question de révision :** Sans répétition serait-il plus parlant comme sous-titre, tout en conservant bijectives dans le texte ?

Passages de référence : L10, H17.

## C390 — OLP-0038-B05

**Choix :** avec
  $\Nat$ ou avec un segment initial ; diffère donc légèrement ; tous les exemples sont repris ; un peu plus concise

**Autre formulation envisagée :** La convention ensembliste demande une bijection ; cette variante reprend les exemples sous une forme condensée.

**Motif :** Le conflit annoncé porte sur la définition d'une énumération, non sur les ensembles au plus dénombrables. L10 explicite les conventions de dénombrable et L18 le rôle des bijections ; les exemples sont effectivement présents dans les deux sources.

**Confiance et limites :** différence locale de définition correctement bornée

**Question de révision :** Ajouter sans répétition aiderait-il à comprendre immédiatement la différence ?

Passages de référence : L10, L18, H17.

## C391 — OLP-0038-B06

**Choix :** les éléments $a_1$, \dots, $a_n$ sont tous distincts ; les $n$ premiers
entiers naturels ; où
$n$ est le nombre d'éléments ; pour $n=0$ ; des
segments non vides

**Autre formulation envisagée :** Un ensemble fini à n éléments peut être mis en bijection avec le segment des n premiers naturels ; le segment est vide pour n=0.

**Motif :** Tous distincts est conservé, condition nécessaire pour que la liste donne une bijection. La borne n−1 diffère de la borne n de la définition suivante : note explicite sur n=0 et sur sa convention séparée. L10 traite le vide, L18 la bijection et L15 le domaine. Aucun changement de formule de liste.

**Confiance et limites :** cardinal fini et deux conventions de borne vérifiés

**Question de révision :** Une notation de segment [0,n[ éviterait-elle l'ambiguïté tout en s'écartant inutilement d'OLP ?

Passages de référence : L10, L18, L15.

## C392 — OLP-0038-B07

**Choix :** certains ensembles infinis ; des énumérations infinies ; entre cet ensemble et tout~$\Nat$

**Autre formulation envisagée :** Une énumération d'un ensemble infini sera une bijection avec l'ensemble entier des naturels.

**Motif :** Certains préserve la réserve de la source : tous les infinis ne deviennent pas énumérables. Tout Nat exclut le segment fini dans ce cas ; H17/L18 donnent le sens bijectif, L10 distingue infinité et dénombrabilité.

**Confiance et limites :** aucune généralisation à tous les infinis

**Question de révision :** La première phrase hypothétique garde-t-elle un intérêt après l'introduction du chapitre ?

Passages de référence : L10, L18, H17.

## C393 — OLP-0038-B08

**Choix :** Énumération au sens ensembliste ; dont
l'image est $A$ ; dont le domaine est soit un segment initial ; $\Nat$ tout entier

**Autre formulation envisagée :** Une énumération bijective de A a pour domaine Nat ou un segment initial fini non vide.

**Motif :** Au sens ensembliste restitue la convention annoncée, pas une prétention que toute autre convention serait non mathématique. L15 distingue domaine/image ; H17 contrôle bijectivité. La borne inclusive n source est conservée, donc le vide n'a pas d'énumération sous cette définition mais est dénombrable séparément.

**Confiance et limites :** types, image et borne inchangés

**Question de révision :** Expliciter non vide dans le corps de définition ou laisser la formule et la note précédente le faire ?

Passages de référence : L15, H17, L10.

## C394 — OLP-0038-B09

**Choix :** en compter les éléments un à un ; L'élément d'indice
$0$ ; celui
d'indice $n$ ; commencer à $1$ ; remplacer
$\Nat$ par~$\PosInt$

**Autre formulation envisagée :** La bijection numérote les éléments de A à partir de zéro ; une numérotation à partir de un serait équivalente.

**Motif :** Indice évite le maladroit zéroième, avec les valeurs f(0),f(1),f(n) intactes. Les indices sont explicités en math là où l'anglais emploie 1st ; la note maintient la possibilité du décalage. L15 gouverne les valeurs et L10 la convention d'ensemble énuméré, sans fausse attestation de zéroième.

**Confiance et limites :** convention de départ et valeurs conservées

**Question de révision :** La note gagnerait-elle à mentionner aussi le décalage des segments finis ?

Passages de référence : L15, L10.

## C395 — OLP-0038-B10

**Choix :** $A = \emptyset$ ou s'il existe une énumération ; si et seulement s'il
  n'est pas !!{enumerable}

**Autre formulation envisagée :** Est au plus dénombrable un ensemble vide ou muni d'une énumération au sens défini ; non dénombrable en est la négation.

**Motif :** L10 accepte vide/fini et signale l'usage concurrent dénombrable au sens infini. La disjonction source est conservée, essentielle puisque les domaines autorisés de la définition précédente sont non vides.

**Confiance et limites :** vide explicitement inclus, négation exacte

**Question de révision :** Le rappel au sens défini serait-il utile dans la proposition française ?

Passages de référence : L10.

## C396 — OLP-0038-B11

**Choix :** s'il est
vide ou si une énumération ; compter les éléments un à un

**Autre formulation envisagée :** Le vide est inclus ; sinon une énumération numérote chaque élément.

**Motif :** La reformulation garde les deux branches au lieu d'identifier dénombrable et possédant une liste non vide. Compter un à un reste une image intuitive du rôle de bijection, et non un algorithme de calcul.

**Confiance et limites :** disjonction et registre adulte préservés

**Question de révision :** Compter ou numéroter rend-il le mieux la notion sans connotation algorithmique ?

Passages de référence : L10, H17.

## C397 — OLP-0038-B12

**Choix :** L'identité ; $\Id{\Nat}(n) = n$ ; la fonction successeur ; \emph{strictement positifs} ; $\Nat^+ = \Nat \setminus \{0\}$

**Autre formulation envisagée :** L'identité énumère Nat et le successeur énumère Nat privé de zéro.

**Motif :** H16 atteste identité, L15 le sens de fonction, L10 dénombrabilité. Strictement positifs évite l'usage français parfois non strict de positif ; l'arrivée implicite de g est Nat+, ce qui en fait une bijection sur cette image.

**Confiance et limites :** domaines/images et exclusion de zéro vérifiés

**Question de révision :** Faut-il afficher g:Nat→Nat+ dans l'exemple ?

Passages de référence : H16, L15, L10.

## C398 — OLP-0038-B13

**Choix :** $A = \emptyset$ ou s'il existe une !!{surjection} ; $f\colon \Nat \to A$ ; une !!{injection} $g\colon A \to \Nat$

**Autre formulation envisagée :** Prouver les caractérisations de la dénombrabilité par une surjection depuis Nat dans le cas non vide et par une injection vers Nat dans tous les cas.

**Motif :** Les deux directions de flèche et l'exception vide asymétrique sont conservées. L17 fournit le principe du premier antécédent ; H17 les propriétés ; L02 le registre d'exercice. Il n'est pas affirmé que la surjection donnée soit elle-même une énumération bijective.

**Confiance et limites :** cas vide et propriétés distinctes

**Question de révision :** La formulation permet-elle de voir pourquoi seule la première caractérisation isole le vide ?

Passages de référence : L02, L10, L17, H17.

## C399 — OLP-0038-B14

**Choix :** respectivement les entiers naturels pairs ; leur image respective comme
ensemble d'arrivée ; par coréstriction à leur image ; aucune des deux fonctions à valeurs dans $\Nat$ ; aucune n'est donc une énumération de~$\Nat$

**Autre formulation envisagée :** Les applications de double et double plus un deviennent des bijections sur les pairs et les impairs, mais ne sont pas surjectives sur Nat.

**Motif :** Respectivement conserve l'appariement formule/image. L15 distingue image et arrivée ; H17 contrôle la différence entre injectivité et bijection. Une note précise la coréstriction implicite dans OLP pour la convention bijective, sans changer les flèches Nat→Nat affichées ni leur non-surjectivité.

**Confiance et limites :** formules et double typage expliqués

**Question de révision :** La coréstriction déjà présentée dans Fonctions doit-elle être rappelée par renvoi ?

Passages de référence : L15, H17, L18.

## C400 — OLP-0038-B15

**Choix :** Définir une énumération des nombres carrés ; $1$, $4$, $9$, $16$

**Autre formulation envisagée :** Donner une bijection de Nat sur les carrés strictement positifs.

**Motif :** La liste commence à1, donc exclut0 ; l'énumération possible est (n+1)^2. Le mot carrés plutôt que carrés parfaits évite une précision supplémentaire inutile ; L02 soutient la consigne, L15 la fonction attendue.

**Confiance et limites :** point de départ et objet vérifiés

**Question de révision :** Ajouter strictement positifs rendrait-il l'exclusion de zéro plus visible ?

Passages de référence : L02, L15, H17.

## C401 — OLP-0038-B16

**Choix :** \emph{plafond} ; le plus petit entier supérieur ou égal ; f(n) = (-1)^{n} ; entre entiers positifs et négatifs ; On peut aussi la définir par cas

**Autre formulation envisagée :** La partie entière supérieure permet d'énumérer les relatifs en alternant −1,1,−2,2 après zéro.

**Motif :** Réemploi contextualisé de C268 : plafond reste un terme éditorial défini, sans attestation lexicale prétendue dans L10/L15/H17. La variante commence à n=0 et inverse les signes par rapport à l'exemple principal ; formule, tableau et cas pair/impair sont préservés et donnent0,−1,1,−2,2,−3,3. Supérieur ou égal exprime la borne exacte, pas un arrondi au plus proche.

**Confiance et limites :** plafond reste explicité

**Question de révision :** Partie entière supérieure serait-elle plus familière que plafond pour les lecteurs visés ?

Passages de référence : L15, L10, H17.

## C402 — OLP-0038-B17

**Choix :** si $A$ et $B$ sont !!{enumerable}s ; $A \cup B$ l'est aussi

**Autre formulation envisagée :** La réunion de deux ensembles au plus dénombrables est au plus dénombrable.

**Motif :** Accord pluriel des hypothèses, singulier de la réunion, sans disjonction supposée. L17 fournit la clôture par image surjective après combinaison de listes ; L02 le registre. A ou B vide est permis.

**Confiance et limites :** deux hypothèses et cas vides conservés

**Question de révision :** Faut-il indiquer le retrait des répétitions pour faire le lien avec la nouvelle définition ?

Passages de référence : L02, L10, L17.

## C403 — OLP-0038-B18

**Choix :** par récurrence sur $n$ ; sont tous !!{enumerable}s ; $A_1 \cup \dots \cup A_n$

**Autre formulation envisagée :** Déduire par récurrence la stabilité sous toute réunion finie.

**Motif :** Tous maintient la conjonction des n hypothèses ; récurrence est attestée dans L16. Les n=1 et n=0 conventionnel n'exigent pas de choix, et la réunion vide est dénombrable. Le résultat n'est pas étendu à une famille infinie.

**Confiance et limites :** réunion finie et méthode demandée préservées

**Question de révision :** Préciser n≥1 ou laisser la convention de réunion vide couvrir n=0 ?

Passages de référence : L02, L10, L16.

## C404 — OLP-0039-B04

**Choix :** \printtoken{p}{nonenumerable} ; variante bijective

**Autre formulation envisagée :** Non-dénombrabilité selon la définition ensembliste

**Motif :** Le pluriel français modifie le commutateur du token, et le sous-titre signale l'alternative dans le lecteur intégré. Le terme non dénombrable reste la négation de la convention L10, indépendamment de la présentation de l'énumération.

**Confiance et limites :** accord et identité de prédicat maintenus

**Question de révision :** Variante bijective nomme-t-il assez clairement la définition utilisée ?

Passages de référence : L10, H17.

## C405 — OLP-0039-B05

**Choix :** $\Bin^\omega$
  et de $\Pow{\Nat}$ ; Pour énumérer un ensemble infini ; une bijection avec~$\Nat$ ; au lieu d'une
  surjection

**Autre formulation envisagée :** La preuve utilise des énumérations sans répétition, indexées par Nat, pour les deux ensembles infinis indiqués.

**Motif :** L'hypothèse infini précise la comparaison des définitions : pour le fini il faut un segment initial. L10 et H17 distinguent convention dénombrable et propriété de l'énumération ; les deux ensembles source restent Nat plutôt que PosInt.

**Confiance et limites :** qualification nécessaire et sens d'énumération contrôlés

**Question de révision :** Ajouter depuis PosInt dans la paraphrase finale serait-il utile ?

Passages de référence : L10, H17.

## C406 — OLP-0039-B06

**Choix :** infini et manifestement
!!{enumerable} ; \emph{!!{nonenumerable}s} ; qui ne sont pas
!!{enumerable}s

**Autre formulation envisagée :** Nat est infini dénombrable, mais il existe des ensembles qui ne sont pas au plus dénombrables.

**Motif :** Manifestement garde le caractère immédiat par l'identité sans transformer l'énoncé en évidence universelle. Les prédicats après ensembles sont au pluriel et la négation est explicitée ; renvoi définition conservé.

**Confiance et limites :** contraste logique et grammaire des tokens prévus

**Question de révision :** La répétition négative aide-t-elle le premier contact avec le terme ?

Passages de référence : L10, H16.

## C407 — OLP-0039-B07

**Choix :** Pour un ensemble $A$ \emph{infini} ; aucune
fonction des entiers naturels ; en ce sens, « davantage » ; l'original omet ici l'hypothèse ; l'ensemble vide est
lui aussi

**Autre formulation envisagée :** Pour A infini, absence de bijection avec Nat équivaut à absence de surjection depuis Nat ; cette qualification est indispensable.

**Motif :** L10 montre pourquoi l'absence de bijection ne suffit pas pour un ensemble fini, et L17 relie surjection et dénombrabilité. La note distingue aussi le vide et renvoie au cadre de choix déjà précisé pour comparer des tailles. Davantage reste entre guillemets comme intuition source, sans prétendre déduire une injection Nat→A sans hypothèse.

**Confiance et limites :** défaut source identifié et conditions explicites

**Question de révision :** La note gagnerait-elle à nommer un exemple singleton concret ?

Passages de référence : L10, L17, L19.

## C408 — OLP-0039-B08

**Choix :** un ensemble infini ; omet nécessairement au moins un élément ; aucune fonction
$f\colon \Nat \to A$ ; \emph{méthode diagonale} ; par sa construction
même

**Autre formulation envisagée :** Toute liste candidate omet un élément construit en modifiant sa diagonale.

**Motif :** L'hypothèse infini ferme la possibilité d'une énumération par segment fini. Ca01 atteste la construction diagonale d'une suite nouvelle, L06 son analogue par parties ; le lexème français méthode diagonale est une formulation éditoriale guidée par ces constructions, pas une citation de Ca01 allemand.

**Confiance et limites :** quantificateur sur toutes les listes et élément omis conservés

**Question de révision :** La liste x1,x2,… malgré Nat à partir de0 mérite-t-elle une note de simple réindexation ?

Passages de référence : Ca01, L06, L10.

## C409 — OLP-0039-B09

**Choix :** suites infinies de $0$ et
de $1$ ; l'ensemble à deux éléments $\{0,1\}$ ; indexées par $\omega$ ; $\funfromto{\omega}{\{0,1\}}$ ; Les trois arguments

**Autre formulation envisagée :** L'ensemble des suites binaires est précisé conditionnellement comme l'ensemble des fonctions de omega dans {0,1}.

**Motif :** Suite plutôt que mot évite la confusion fini/infini ; L15 contrôle les fonctions, Ca01 les suites binaires. Les trois arguments de oliflabeldef sont réparés : le source conserve dans son deuxième argument le supposé {} et la phrase suivante, puis consomme le token end comme troisième argument. Le commentaire de correction décrit cette structure ; référence et explication demeurent.

**Confiance et limites :** source macro à trois arguments lue, groupes contrôlés

**Question de révision :** Cette note technique doit-elle rester uniquement dans les sources et le relevé critique ?

Passages de référence : L15, Ca01.

## C410 — OLP-0039-B10

**Choix :** $\Bin^\omega$ est !!{nonenumerable}

**Autre formulation envisagée :** L'ensemble de toutes les suites binaires infinies n'est pas au plus dénombrable.

**Motif :** Le prédicat reprend exactement la convention L10 ; Ca01 fournit la preuve originale de non-listabilité de toutes les suites. Aucun passage à un ensemble de mots finis.

**Confiance et limites :** énoncé et domaine inchangés

**Question de révision :** Aucune incertitude de fond ; développer le symbole seulement dans le titre ?

Passages de référence : L10, Ca01.

## C411 — OLP-0039-B11

**Choix :** une liste quelconque ; est infini, puisque ; le terme d'indice $m$ de la suite d'indice $n$ ; la ligne d'indice $n$ ; chaque $1$ par $0$ et chaque $0$ ; $d(n) \neq s_n(n)$ ; pour tout $n\in \Nat$

**Autre formulation envisagée :** Une liste infinie de suites binaires forme une matrice ; inverser chaque bit diagonal produit une suite qui diffère de sa ligne à l'indice correspondant.

**Motif :** Ca01 montre la même construction, avec deux caractères m/w ; OLP fixe0/1 et l'indexation. Deux fautes source sont signalées : n/m inversés dans la définition de s_n(m), et remplacement1→0 répété au lieu du double retournement. L'infinité de Bin^omega est justifiée par les suites à un seul1, pour exclure une énumération finie. Tableau et définition par cas sont conservés ; chaque terme d est défini et l'inégalité porte sur tout n.

**Confiance et limites :** indices, bits, tableau et portée de la contradiction contrôlés

**Question de révision :** La grande note de correction des indices est-elle mieux placée après la phrase plutôt qu'après la matrice ?

Passages de référence : Ca01, L15, L10.

## C412 — OLP-0039-B12

**Choix :** toute liste d'éléments d'une partie ; omet au moins un élément ; aucune énumération

**Autre formulation envisagée :** Toute liste de suites binaires manque au moins une suite ; une énumération complète est donc impossible.

**Motif :** Toute liste évite de supposer qu'une partie finie possède une liste bijective infinie. L'infinité de l'ensemble total a été justifiée dans la preuve ; la conclusion peut donc utiliser la définition de L10 sous les deux régimes OLP.

**Confiance et limites :** portée de liste arbitraire et conclusion exactes

**Question de révision :** Répéter la justification de l'infinité serait-il superflu ?

Passages de référence : Ca01, L10.

## C413 — OLP-0039-B13

**Choix :** ne nécessite toutefois pas toujours un tableau ; même sans tableau ni diagonale représentée ; en donne un exemple

**Autre formulation envisagée :** Le principe de diagonalisation s'applique sans qu'on dessine une matrice.

**Motif :** L06 donne la preuve par appartenance sans tableau, Ca01 généralise l'argument. Diagonale représentée maintient la nuance : la structure de différence à l'indice subsiste même sans représentation visuelle. Rien ne supprime le mécanisme diagonal.

**Confiance et limites :** principe abstrait et représentation distingués

**Question de révision :** Diagonale explicite aurait-il été plus naturel que représentée ?

Passages de référence : L06, Ca01.

## C414 — OLP-0039-B14

**Choix :** $\Pow{\Nat}$ n'est pas !!{enumerable}

**Autre formulation envisagée :** L'ensemble des parties des naturels est non dénombrable.

**Motif :** La formulation négative source est conservée au lieu d'un remplacement systématique par le prédicat positif nonenumerable. L05 nomme parties, L06 justifie la construction sous-jacente et L10 le sens de dénombrable.

**Confiance et limites :** objet et négation identiques

**Question de révision :** Uniformiser ou conserver cette variation négative de la source ?

Passages de référence : L05, L06, L10.

## C415 — OLP-0039-B15

**Choix :** toute liste de parties ; $n \in D$ si et seulement si
$n \notin N_n$ ; $D\subseteq \Nat$ ; $D \neq N_n$ pour tout

**Autre formulation envisagée :** Définir D par non-appartenance à la partie située au même indice garantit qu'il diffère de chaque partie de la liste.

**Motif :** L06 est le témoin français exact du type d'argument ; la formule impose n∈Nat. Le biconditionnel et l'appartenance de D à Pow(Nat) restent garantis, sans quantification seulement sur D. Les singletons montrent aussi que Pow(Nat) est infini ; pas de liste finie complète possible.

**Confiance et limites :** appartenance et inégalité pour chaque indice contrôlées

**Question de révision :** Ajouter ici l'infinité par les singletons serait-il utile pour faire miroir à la preuve précédente ?

Passages de référence : L05, L06, L10.

## C416 — OLP-0039-B16

**Choix :** la ligne d'indice $n$ ; la colonne d'indice $m$ ; si et seulement si
$m \in N_n$ ; \emph{ne figure pas} ; on exclut donc $0$ et $1$ ; on inclut~$2$ ; Nous rétablissons ces quatre
valeurs

**Autre formulation envisagée :** La matrice d'appartenance permet de lire D comme les indices absents de leur position diagonale.

**Motif :** Les lignes sont ensembles, colonnes entiers ; la diagonale est complémentée. L05/L06 fixent l'appartenance et la séparation, Ca01 le repérage diagonal. Les quatre ensembles et le tableau source sont conservés ;0,1,3 exclus et2 inclus vérifiés. Correction supplémentaire après comparaison du tableau au texte : N0=Nat exige3,4,5 dans les colonnes correspondantes. Les trois cellules vides source sont complétées avec une note visible ; la diagonale reste identique. Revue bilingue finale : N3={2,3,4,…} impose aussi5 en colonne5. Quatre cellules source au total sont rétablies, avec une note actualisée ; les quatre valeurs diagonales ne changent pas. Justification par les ensembles explicitement donnés par OLP, pas par une attestation lexicale du canon.

**Confiance et limites :** exemples diagonaux vérifiés ; représentation hors diagonale à contrôler au rendu

**Question de révision :** Les cellules vides de la première ligne peuvent-elles être confondues avec de véritables absences hors diagonale ?

Passages de référence : L05, L06, Ca01.

## C417 — OLP-0039-B17

**Choix :** diagonalisation explicite ; toutes
les fonctions $f \colon \Nat \to \Nat$ ; pour chaque $i$ ; ne figure
pas dans cette liste

**Autre formulation envisagée :** Construire une fonction naturelle différente de chacune des fonctions f1,f2,… à un indice adapté.

**Motif :** La liste de fonctions commence à1 tandis que leur domaine commence à0 : une construction g(i)=f_i(i)+1 pour i≥1, avec g(0) fixé, suffit. L15 fixe le type fonctionnel, Ca01 la stratégie et L02 l'exercice. Aucun choix de valeurs hors Nat.

**Confiance et limites :** différence entre indices de liste et domaine respectée

**Question de révision :** Une liste f0,f1,… serait-elle plus uniforme, mais modifierait inutilement les indices source ?

Passages de référence : L02, L15, Ca01.

## C418 — OLP-0040-B04

**Choix :** Réduction : variante bijective

**Autre formulation envisagée :** Réduction avec énumérations sans répétition

**Motif :** Le qualificatif distingue cette section dans le chapitre intégré. C335 est réemployé pour réduction avec la même limite lexicale ; L17 contrôle le transfert, H17 la condition bijective de l'énumération finale.

**Confiance et limites :** mécanisme assuré, lexème réduction éditorial non directement attesté dans les témoins

**Question de révision :** Le titre alternatif expose-t-il plus clairement le nouveau retrait des répétitions ?

Passages de référence : L17, H17.

## C419 — OLP-0040-B05

**Choix :** reprenant les résultats de la \olref[nen-alt]{sec} ; un peu plus détaillée ; correspondant aux résultats

**Autre formulation envisagée :** La variante courte correspond à la preuve ensembliste ; la section principale en fournit une version plus développée.

**Motif :** Détaillée conserve le degré d'explication sans jugement sur le lecteur. Les trois renvois sont conservés et la variante est nommée dans le bon sens. L10/L17 soutiennent la notion et le mécanisme, pas cette phrase éditoriale exacte.

**Confiance et limites :** dépendances OLP vérifiées

**Question de révision :** Le renvoi à l'autre version suffit-il à guider le lecteur sans un rappel de sa convention ?

Passages de référence : L10, L17.

## C420 — OLP-0040-B06

**Choix :** prouvé par diagonalisation ; un argument semblable ; si
$\Pow{\Nat}$ est !!{enumerable} ; il en
résultera

**Autre formulation envisagée :** Une énumération des parties des naturels fournirait une énumération des suites binaires, déjà prouvée impossible.

**Motif :** La conclusion suit la non-dénombrabilité acquise, pas sa négation. Ca01 soutient le rappel diagonal et L17 la réduction ; Nat reste l'ensemble à partir de0, distinct de PosInt dans la principale.

**Confiance et limites :** implication et variantes d'ensemble conservées

**Question de révision :** Le conditionnel français fournirait serait-il plus clair que l'annonce au futur de conclusion ?

Passages de référence : Ca01, L17, L10.

## C421 — OLP-0040-B07

**Choix :** le problème de l'énumération de $\Bin^\omega$ ; à celui de l'énumération de $\Pow{\Nat}$ ; Une solution du second ; une
solution du premier

**Autre formulation envisagée :** Réduire l'énumération de B à celle de A consiste à résoudre la première au moyen de la seconde.

**Motif :** Les deux problèmes et leur ordre sont nommés entièrement pour éviter une inversion. L17 atteste le mécanisme, tandis que le mot réduire reste le choix éditorial C335, contextualisé sans fausse attestation lexicale.

**Confiance et limites :** premier/second rattachés à leurs ensembles explicites

**Question de révision :** Conserver c'est-à-dire deux fois ou alterner avec à savoir ?

Passages de référence : L17.

## C422 — OLP-0040-B08

**Choix :** une !!{surjection} $f\colon A \to B$ ; parcourt tout~$B$ ; en retirant les répétitions ; à sa première apparition ; on réindexe la liste ; si elle est finie

**Autre formulation envisagée :** Appliquer une surjection à une énumération donne une liste exhaustive ; conserver seulement les premières occurrences produit une énumération bijective.

**Motif :** Correction substantielle de l'implicite source : une surjection peut répéter des valeurs et ne suffit pas à une liste bijective telle quelle. L17 construit avec le plus petit antécédent, sans choix arbitraire, et H17 distingue les propriétés. La réindexation par Nat ou segment fini maintient la définition exacte et couvre B fini non vide ; la liste de A donnée exclut A vide.

**Confiance et limites :** première-occurrence construction valide et note explicite

**Question de révision :** La note doit-elle préciser le passage à une énumération croissante de l'ensemble des premiers indices ?

Passages de référence : L17, H17, L10.

## C423 — OLP-0040-B09

**Choix :** fonction !!{injective} $g\colon B \to A$ ; si $B$ est !!{nonenumerable} ; transformer une énumération
de~$A$

**Autre formulation envisagée :** Utiliser une injection B→A pour ramener une énumération hypothétique de A à B.

**Motif :** Réemploi contrôlé de C339 avec nouvelle convention : filtrer la liste sur l'image de g puis appliquer l'inverse fournit des valeurs distinctes, et B non dénombrable est non vide. L17 guide les premiers indices, H17 l'injectivité ; L02 la consigne.

**Confiance et limites :** sens de flèche et convention sans répétition vérifiés

**Question de révision :** Le renvoi à l'exercice homologue pourrait-il guider sans supprimer sa présence dans la variante ?

Passages de référence : L02, L17, H17.

## C424 — OLP-0040-B10

**Choix :** soit !!{enumerable} ; $N_{1}$, $N_{2}$, $N_{3}$ ; est infini, puisqu'il
contient tous les singletons ; décaler d'une unité

**Autre formulation envisagée :** Supposer une énumération de Pow(Nat) ; elle est infinie et peut être écrite avec indices commençant à1.

**Motif :** Le décalage explicite préserve les indices source N1,N2 sans les confondre avec les positions0,1 des suites binaires. L05 fournit singletons/parties, L10 la convention vide/fini et L15 le domaine. La justification d'infinité exclut un segment initial fini. Contrôle du rendu : olref produit « théorème » sans article. La contraction du remplace donc de devant ces renvois, y compris les branches alternatives. Correction grammaticale de l’édition, sans changement de référence ni de mathématiques ; le registre des preuves reste celui des passages déjà consultés, sans nouvelle attestation lexicale revendiquée.

**Confiance et limites :** infinie et réindexation exacte

**Question de révision :** La note de décalage peut-elle être raccourcie une fois la convention rappelée dans0038 ?

Passages de référence : L05, L10, L15.

## C425 — OLP-0040-B11

**Choix :** en associant
à $N$ la suite $s$ ; $s(n) = 1$ si et seulement si
$n \in N$ ; $s(n) = 0$ sinon ; sans définir l'indice $k$

**Autre formulation envisagée :** Associer à N sa suite caractéristique, avec positions indexées par Nat.

**Motif :** Comme C341, l'indice k non défini est supprimé et déclaré. La définition reste biconditionnelle et totale, L15/L05 en fixent le type. Suite caractéristique est une paraphrase viable, mais la rédaction conserve la définition élément par élément de la source.

**Confiance et limites :** dépendance à N et valeurs0/1 exactes

**Question de révision :** Nommer la fonction caractéristique aiderait-il à relier les deux versions ?

Passages de référence : L15, L05.

## C426 — OLP-0040-B12

**Choix :** chaque $n \in \Nat$ ; appartient ou n'appartient pas ; $2\Nat = \Setabs{2n}{n \in \Nat} ; $1010101\dots$ ; $\emptyset$ a pour image

**Autre formulation envisagée :** La fonction est totale par décision d'appartenance ; les pairs comprenant0 donnent1010…, le vide000…, Nat111….

**Motif :** Le mot décision n'est pas utilisé dans le texte pour éviter d'impliquer un algorithme de décision. Appartient ou non conserve la dichotomie classique OLP ; l'indexation à0 inverse le premier bit par rapport aux pairs de PosInt. Les trois exemples sont vérifiés.

**Confiance et limites :** exemples et totalité sans calculabilité contrôlés

**Question de révision :** Le rappel comprenant0 dans le texte serait-il utile ?

Passages de référence : L15, L05, L10.

## C427 — OLP-0040-B13

**Choix :** toute suite de $0$ et
de $1$ ; N = \Setabs{n \in \Nat}{s(n) = 1} ; $f(N) = s$ ; De plus, $f$ est injective ; au terme de cet indice

**Autre formulation envisagée :** Construire l'antécédent d'une suite prouve la surjectivité ; deux parties distinctes donnent deux suites distinctes, donc aussi l'injectivité.

**Motif :** H17 distingue les deux preuves ; L05 donne la partie reconstruite. L'injectivité supplémentaire est indiquée en note comme ajout nécessaire pour obtenir directement une énumération bijective dans la liste suivante. Elle découle de l'extensionnalité L01, sans changer la définition f.

**Confiance et limites :** inverse caractéristique et différence d'ensembles contrôlés

**Question de révision :** Retirer les répétitions suffirait, mais l'injectivité particulière apporte-t-elle une simplification plus claire ?

Passages de référence : H17, L05, L01.

## C428 — OLP-0040-B14

**Choix :** chaque élément de $\Bin^\omega$ ; figure donc dans cette liste ; les $N_i$ sont distincts ; aucune répétition ; au sens bijectif

**Autre formulation envisagée :** La liste des images est exhaustive par surjectivité et sans répétition par injectivité, donc une énumération bijective.

**Motif :** La source ne mentionne que la surjectivité ; le complément s'appuie sur l'injectivité démontrée juste avant et déclarée en note. H17 contrôle chaque propriété, L17 le transfert d'exhaustivité. Aucune assimilation d'une liste quelconque à une bijection.

**Confiance et limites :** deux propriétés suffisantes établies séparément

**Question de révision :** La conclusion au sens bijectif devrait-elle rappeler la réindexation à partir de0 ?

Passages de référence : H17, L17.

## C429 — OLP-0040-B15

**Choix :** Si $\Pow{\Nat}$ était ; le serait
donc aussi ; Or $\Bin^\omega$ ; Par conséquent

**Autre formulation envisagée :** L'hypothèse contredirait la non-dénombrabilité des suites binaires, donc Pow(Nat) est non dénombrable.

**Motif :** Même contraposition que C344, avec Nat au lieu de PosInt et énumération désormais bijective établie. Le renvoi au théorème alternatif est conservé. L10 gouverne le prédicat, L17 l'implication.

**Confiance et limites :** conclusion suit le transfert corrigé

**Question de révision :** Conserver la répétition complète du prédicat dans la conclusion ?

Passages de référence : L10, L17.

## C430 — OLP-0040-B16

**Choix :** ne permet \emph{pas} ; $g(s) = s(1)$ ; le deuxième ; $f\colon A \to B$ ; $n$ zéros ; Son $Y$
final n'est pas défini

**Autre formulation envisagée :** Le passage commenté avertit que la direction de la réduction et la surjectivité sont essentielles ; les exemples restent de vrais contre-exemples sous indexation à0.

**Motif :** Prose inactive traduite et mappée comme telle. La projection s(1) est conservée et dite deuxième terme ; B remplace le Y sans définition en reprenant le transfert A→B. h(n) reçoit la queue infinie de1 comme C345, avec note dans les commentaires, afin d'appartenir à Bin^omega. H17/L17 fixent les deux écueils ; L15 le type, pas une attestation de la formulation commentée. Intégration ultérieure : prose commentée dans la source exposée dans le lecteur sous la mention Passage conservé en commentaire dans l’original, avec notes rendues lisibles. Statut source inactif conservé dans le relevé ; aucune attribution à une suppression source.

**Confiance et limites :** statut inactif, indices et types corrigés explicitement

**Question de révision :** Faut-il présenter ces commentaires traduits dans une note de variantes du lecteur sans doubler le passage principal ?

Passages de référence : H17, L17, L15.

## C431 — OLP-0040-B17

**Choix :** \label{sfr:siz:red-alt:prob:nat-nat} ; l'ensemble~$X$ de toutes les fonctions ; donner une fonction surjective

**Autre formulation envisagée :** Montrer la non-dénombrabilité des fonctions naturelles par une surjection sur les suites binaires.

**Motif :** Comme C347, type Nat→Nat et sens X→Bin^omega conservés. Le label absolu source doublonne celui de0034 ; seul celui de la variante est renommé red-alt et commenté. Les seuls usages trouvés dans sets-functions-relations sont les deux définitions, donc aucun renvoi local n'est cassé ; vérifier les autres parties lors de l'intégration intégrale.

**Confiance et limites :** consigne intacte, doublon attesté et réparation locale explicite

**Question de révision :** Faut-il étendre la recherche du label à tout content lors du prochain contrôle de graphe ?

Passages de référence : L02, L15, H17.

## C432 — OLP-0040-B18

**Choix :** tous les \emph{ensembles de}
couples ; $\Pow{\Nat \times \Nat}$

**Autre formulation envisagée :** Établir la non-dénombrabilité de l'ensemble des parties de Nat×Nat.

**Motif :** La variante source explicite la puissance et utilise Nat comprenant0 ; ces deux éléments sont conservés. L02 soutient couples et consigne, L05 parties. L'objet n'est pas remplacé par Nat×Nat lui-même.

**Confiance et limites :** niveau de parties et produit exacts

**Question de révision :** La double formulation verbale/formelle est-elle utile ici ?

Passages de référence : L02, L05, L10.

## C433 — OLP-0040-B19

**Choix :** $\Nat^\omega$ ; suites
infinies d'entiers naturels ; Montrer par réduction

**Autre formulation envisagée :** Montrer par transfert de dénombrabilité que les suites naturelles infinies sont non dénombrables.

**Motif :** Réemploi de C348 avec même objet et même convention finie-inclusive. L15 fixe les suites comme fonctions, L17 le transfert, L02 le registre ; aucune procédure calculable n'est requise.

**Confiance et limites :** infinité de longueur et naturel des valeurs préservés

**Question de révision :** Une indication supplémentaire risquerait-elle de résoudre trop directement l'exercice ?

Passages de référence : L02, L15, L17.

## C434 — OLP-0040-B20

**Choix :** $P$ l'ensemble des fonctions de $\Nat$ ; fonctions partielles des entiers strictement positifs ; $P$ est !!{enumerable} et que $Q$ ; de l'énumération de~$Q$ ; Exercice conservé en commentaire dans l'original.

**Autre formulation envisagée :** Le commentaire compare les fonctions totales sur Nat à valeur0 avec les fonctions partielles sur PosInt à valeur0.

**Motif :** Les domaines différents Nat/PosInt sont réellement dans la source inactive ; ils sont conservés, le résultat reste vrai. P est singleton ; Q s'identifie aux parties de PosInt. L15/H16 distinguent domaine exact et convention partielle ; L10 inclut singleton et L17 guide la réduction. Statut commenté préservé. Intégration ultérieure : l’exercice commenté est exposé sous la même mention de provenance ; P a pour départ Nat, Q les entiers strictement positifs, comme dans l’original. Réparation de rendu : la mention de provenance est placée dans le corps de l’exercice afin de l’accompagner lors du report des exercices en fin de chapitre.

**Confiance et limites :** totalité/partialité et domaines distincts vérifiés

**Question de révision :** Une note de variantes peut-elle simplement signaler les domaines différents sans répéter l'exercice actif analogue ?

Passages de référence : L15, H16, L10, L17.

## C435 — OLP-0040-B21

**Choix :** toutes les !!{surjection}s ; de $\Nat$ dans
$\{0,1\}$ ; contient exactement

**Autre formulation envisagée :** La famille de toutes les surjections de Nat sur Bin n'est pas dénombrable.

**Motif :** Toutes et exactement gardent la restriction aux suites qui prennent les deux valeurs, en excluant les constantes. H17 soutient surjections, L10 le prédicat ; la variante utilise Nat, pas PosInt. Macro de nom surjection au pluriel distincte de l'adjectif surjective du passage principal.

**Confiance et limites :** propriété, accord et domaine exacts

**Question de révision :** Sur ou dans pour l'arrivée d'une surjection : uniformiser lors du contrôle grammatical ?

Passages de référence : H17, L10, L02.

## C436 — OLP-0040-B22

**Choix :** l'ensemble~$\Real$ des nombres réels

**Autre formulation envisagée :** Établir la non-dénombrabilité des réels.

**Motif :** Réemploi contrôlé de C351 : même consigne sans indication imposée ; L10 soutient le prédicat et L02 le registre infinitif, sans revendiquer que ces passages contiennent la preuve demandée.

**Confiance et limites :** objet et tâche conservés

**Question de révision :** Faut-il un renvoi à l'exercice identique de la présentation principale dans le lecteur intégré ?

Passages de référence : L02, L10.

## C437 — OLP-0042-B03

**Choix :** De $\Nat$ à $\Int$

**Autre formulation envisagée :** Construction des entiers relatifs

**Motif :** Le titre conserve le trajet entre deux ensembles déjà notés, sans ajouter une structure d'anneau absente du titre OLP. Y05 atteste la construction des entiers relatifs ; le choix De… à… est une adaptation éditoriale transparente du titre anglais, et non une citation du témoin.

**Confiance et limites :** même direction de construction

**Question de révision :** Un titre nominal Construction de Z serait-il préférable dans l'ensemble du chapitre ?

Passages de référence : Y05.

## C438 — OLP-0042-B04

**Choix :** Partons de deux observations simples ; Tout entier relatif ; peut tout aussi bien être représentée par le couple ; nous supposons connue la structure de $\Nat$ ; une première idée, un peu naïve

**Autre formulation envisagée :** Voici deux constats élémentaires ; représentons provisoirement les entiers relatifs par des couples de naturels.

**Motif :** Y05 appelle les éléments de Z entiers relatifs et raisonne en classes de couples ; couple suffit en français mathématique pour ordered pair, sans retirer l'ordre des composantes. Observations traduit realisations comme des constats, sans l'anglicisme réalisations. Tout garde la portée universelle et avec conserve les deux variables naturelles. Représentée distingue l'information codée de l'identité d'un nombre et d'un couple. Supposons connue la structure de N traduit l'hypothèse de connaissance préalable ; ce n'est pas une nouvelle construction de N. Première idée, un peu naïve garde le caractère provisoire que le contre-exemple suivant invalide. L'exposition et cette réserve viennent d'OLP ; Y05 n'atteste pas ces phrases mot à mot.

**Confiance et limites :** quantification, codage et statut provisoire conservés

**Question de révision :** Le mot structure risque-t-il ici d'anticiper inutilement le vocabulaire algébrique formel ?

Passages de référence : Y05.

## C439 — OLP-0042-B05

**Choix :** Cette idée est en fait trop naïve ; Or $\tuple{0, 2 }\neq \tuple{4, 6}$ ; pas simplement déclarer

**Autre formulation envisagée :** Cette première identification ne convient pas : des couples distincts doivent représenter le même entier relatif.

**Motif :** Le connecteur Or rend l'opposition entre l'égalité voulue des différences et l'inégalité réelle des couples. Le rejet porte sur l'identification directe de N² à Z, pas sur l'usage des couples comme représentants. Y05 fournit le cadre français classe/couple/identifier ; le contre-exemple numérique et sa conclusion restent ceux d'OLP.

**Confiance et limites :** même contre-exemple et même restriction de la conclusion

**Question de révision :** Conserver trop naïve ou préférer ne convient pas pour éviter une connotation évaluative ?

Passages de référence : Y05.

## C440 — OLP-0042-B06

**Choix :** la propriété recherchée ; \liff ; sont \emph{censés} se comporter ; aux deux membres ; Il faut maintenant vérifier ; réflexive, symétrique et transitive

**Autre formulation envisagée :** Nous cherchons à reproduire l'égalité des différences ; définissons la relation correspondante, puis vérifions les trois propriétés d'une équivalence.

**Motif :** Y05 présente la relation par une égalité entre représentants avant de construire les classes. La propriété recherchée et censés maintiennent le raisonnement heuristique dans Z, sans supposer que la soustraction est déjà définie dans N. Membres est le vocabulaire usuel d'une égalité, cohérent avec les calculs du témoin. Liff remplace seulement le texte mathématique iff par le symbole d'équivalence ; les deux sens sont conservés. La relation est d'abord proposée puis son caractère d'équivalence est à vérifier : le futur programme ne devient pas une preuve circulaire. Le triplet réflexive/symétrique/transitive est conservé de l'OLP et des chapitres français précédents ; Y05 seul n'est pas invoqué comme preuve de ces trois propriétés.

**Confiance et limites :** heuristique distinguée de la définition et de la vérification

**Question de révision :** Faut-il écrire la propriété recherchée avec si et seulement si en toutes lettres hors de la formule ?

Passages de référence : Y05.

## C441 — OLP-0042-B07

**Choix :** \emph{Réflexivité :} ; Nous avons ; en effet, $a + b = b + a$

**Autre formulation envisagée :** La réflexivité est immédiate par le critère définissant la relation.

**Motif :** L'énoncé et l'égalité commutative citée sont conservés. La substitution directe dans le critère donne aussi a+b=a+b ; l'égalité a+b=b+a de l'original est vraie mais n'est pas la substitution littérale du critère. Aucune fausse égalité n'est introduite et aucune correction silencieuse n'est faite. Y05 situe l'argument dans les naturels munis de leur addition ; la justification logique est contrôlée directement dans OLP, pas empruntée au témoin.

**Confiance et limites :** conclusion vraie ; justification originale un peu indirecte explicitée au dossier

**Question de révision :** Préférer lors d'une révision une justification littérale a+b=a+b, avec déclaration de la modification ?

Passages de référence : Y05.

## C442 — OLP-0042-B08

**Choix :** \emph{Symétrie :} ; Supposons que ; c'est-à-dire que ; Alors $c + b = a + d$, donc

**Autre formulation envisagée :** Si deux couples sont en relation, l'égalité définissante se lit aussi dans l'autre sens.

**Motif :** Supposons que introduit l'hypothèse ; c'est-à-dire que déroule la définition, puis Alors… donc distingue la symétrie de l'égalité et le retour à la relation. Le critère d'équivalence par somme est présent dans Y05, mais le sens b−a de ses représentants n'est pas importé. Les quatre positions a,b,c,d restent exactement celles d'OLP.

**Confiance et limites :** mêmes hypothèse, égalités et conclusion

**Question de révision :** La répétition explicite du nom de la relation à la dernière étape améliorerait-elle la lecture ?

Passages de référence : Y05.

## C443 — OLP-0042-B09

**Choix :** \emph{Transitivité :} ; Par addition ; par simplification dans $\Nat$ ; Ainsi,

**Autre formulation envisagée :** En additionnant les deux égalités puis en simplifiant les termes communs, on obtient la relation entre le premier et le troisième couple.

**Motif :** La traduction explicite les opérations qui relient les trois égalités OLP. Simplification dans N désigne la cancellation de termes égaux, sans faire intervenir une soustraction encore non construite. Y05 justifie seulement le registre de la construction par couples ; il ne prouve pas cette cancellation à notre place. La chaîne de deux relations, les six variables et les deux hypothèses restent inchangées.

**Confiance et limites :** explicitation de l'algèbre effectivement utilisée

**Question de révision :** Faut-il rappeler à cet endroit la propriété de cancellation de l'addition naturelle ?

Passages de référence : Y05.

## C444 — OLP-0042-B10

**Choix :** former les classes d'équivalence pour cette relation

**Autre formulation envisagée :** Passons maintenant à l'ensemble quotient associé.

**Motif :** Former les classes d'équivalence suit l'étape explicitement accomplie dans Y05. L'alternative ensemble quotient est correcte, mais anticipe le résultat global alors que cette phrase OLP introduit d'abord les classes ; nous gardons sa progression.

**Confiance et limites :** opération et progression conservées

**Question de révision :** Uniformiser pour cette relation ou modulo cette relation dans tout le chapitre ?

Passages de référence : Y05.

## C445 — OLP-0042-B11

**Choix :** Les entiers relatifs sont les classes d'équivalence ; de couples de nombres naturels ; autrement dit

**Autre formulation envisagée :** L'ensemble Z est le quotient de N² par la relation Intequiv.

**Motif :** Y05 atteste le vocabulaire entiers relatifs et classes de couples. La phrase définit les objets comme des classes, puis donne leur ensemble quotient : elle ne définit pas un entier comme un couple individuel. Pour garde l'indice de la relation ; la macro equivclass et son argument N² sont inchangés. Autrement dit annonce une seconde écriture de la même définition, sans ajouter une équivalence à démontrer.

**Confiance et limites :** type des objets et quotient préservés

**Question de révision :** Préférer classes modulo Intequiv à classes pour Intequiv pour éviter une répétition ?

Passages de référence : Y05.

## C446 — OLP-0042-B12

**Choix :** Cette définition, posée par convention ; réactions \emph{philosophiques} très diverses ; Avant de les examiner

**Autre formulation envisagée :** Cette définition stipulative appelle plusieurs lectures philosophiques ; achevons d'abord la construction technique.

**Motif :** Posée par convention restitue stipulative sans introduire le terme philosophique stipulative comme un emprunt peu expliqué. Y05 emploie on décide pour la convention de construction ; ce passage appuie ce registre sans constituer une doctrine sur les définitions stipulatives. Peut susciter conserve la possibilité, et Avant de garde le report des réactions, non leur rejet. Très diverses conserve la pluralité. Aucune attestation philosophique exhaustive n'est revendiquée.

**Confiance et limites :** sens clair, terme philosophique rendu par une périphrase sans témoin spécialisé

**Question de révision :** Un canon philosophique ultérieur justifiera-t-il définition stipulative plutôt que la périphrase actuelle ?

Passages de référence : Y05.

## C447 — OLP-0042-B13

**Choix :** Notons ; la classe d'équivalence pour $\Intequiv$ qui contient le couple ; La notation abrégée est simplement plus lisible ; Posons maintenant ; afin d'alléger les axiomes ; les propriétés \emph{attendues} ; les détails sont reportés à la

**Autre formulation envisagée :** Notons la classe du couple (m,n), définissons les opérations et l'ordre, puis vérifions que ces définitions conviennent.

**Motif :** Y05 fournit classe, couple, addition des classes et la définition du produit ; nous conservons cependant l'encodage OLP a−b, contraire au b−a du témoin. Contient le couple comme élément maintient la distinction entre représentant et classe, avec les deux notations complètes de la note originale. Notons introduit un symbole ; Posons introduit les opérations : ces actes ne sont pas confondus. Les trois formules restent celles d'OLP, liff ne change que le rendu de iff. Propriétés attendues garde la portée générale de behave as they ought, sans la réduire à la seule indépendance du représentant. Y07 atteste compatible pour l'ordre ; l'OLP reste responsable du renvoi à la vérification détaillée. Le nous remplace le I éditorial sans attribution nouvelle ; alléger ne supprime aucun axiome.

**Confiance et limites :** représentants, conventions et portée de la vérification distingués

**Question de révision :** Le dernier paragraphe devrait-il nommer explicitement l'indépendance du représentant avant le renvoi technique ?

Passages de référence : Y05, Y07.

## C448 — OLP-0042-B14

**Choix :** Dans cette construction ; ne sont pas eux-mêmes des entiers relatifs ; Précision éditoriale ; traiter les nombres naturels \emph{comme} ; respecte les opérations et l'ordre ; pour tous $m, n \in \Nat$ ; il suffit d'utiliser les propriétés des nombres naturels ; La vérification des deux autres conditions est laissée en exercice

**Autre formulation envisagée :** La construction fournit une copie des naturels dans Z ; l'application n↦[n,0] préserve l'addition, la multiplication et l'ordre.

**Motif :** Le contraste entre objets de départ et classes est le point philosophique d'OLP. Y05 parle de contenir N via une construction ; cette pratique d'identification ne justifie pas une impossibilité ensembliste universelle. Une note éditoriale limite donc explicitement l'affirmation à la distinction préalable à l'identification, sans effacer l'accent original. Comme garde cette identification au lieu de prétendre que les objets étaient déjà identiques. Respecte les opérations et l'ordre déplie well-behaved avec les trois conditions aussitôt écrites ; Y07 appuie le registre, non la preuve. Pour tous préserve la portée sur m,n ; les trois identités, le calcul du produit et le calcul d'addition commenté sont inchangés. Le commentaire anglais de preuve est traduit aussi. La consigne finale conserve exactement l'addition et l'ordre laissés au lecteur, sans lui redemander la multiplication déjà montrée.

**Confiance et limites :** formules intégralement conservées et affirmation philosophique bornée par une note explicite

**Question de révision :** L'expression copie des naturels devrait-elle être introduite dans le corps ou réservée à la réflexion ultérieure ?

Passages de référence : Y05, Y07.

## C449 — OLP-0043-B03

**Choix :** De $\Int$ à $\Rat$

**Autre formulation envisagée :** Construction des nombres rationnels

**Motif :** Réemploi contextualisé du titre C437 : le trajet va ici des entiers relatifs aux rationnels. Y06 atteste cette construction par classes de couples ; aucune extension aux réels n'est ajoutée au titre.

**Confiance et limites :** parallèle exact entre les deux titres

**Question de révision :** Conserver les deux titres symétriques De… à… dans la table des matières ?

Passages de référence : Y06.

## C450 — OLP-0043-B04

**Choix :** théorie naïve des ensembles ; Tout nombre rationnel ; $j$ est non nul ; peut tout aussi bien être représentée par le couple ; Comme précédemment ; Il faut vérifier ; Nous pouvons alors poser ; dont la seconde composante est non nulle

**Autre formulation envisagée :** En quotientant les couples d'entiers à seconde composante non nulle par l'égalité des produits croisés, nous obtenons les rationnels.

**Motif :** Y06 atteste rationnel, quotient, classe et couple ; nous gardons les dénominateurs OLP dans Z privé de zéro, alors que Yger les prend dans N strictement positif. Non nul ne devient donc jamais positif dans cette définition. Théorie naïve des ensembles nomme le cadre, sans qualificatif péjoratif appliqué au contenu mathématique. Représentée par distingue à nouveau codage et identité ; le contre-exemple 3/2=6/4 est conservé. Liff conserve les deux sens du produit croisé et tous ses facteurs. Il faut vérifier, la consigne d'exercice et Nous pouvons alors poser maintiennent la dépendance de la définition envers la preuve de l'équivalence. Seconde composante évite de prendre un couple pour un ensemble à deux éléments non ordonnés ; cette précision est cohérente avec les couples du témoin, mais la formulation exacte est éditoriale. Les deux marqueurs d'exercice et de définition sont conservés.

**Confiance et limites :** domaine, codage, relation et obligations de preuve préservés

**Question de révision :** Le rappel seconde composante non nulle mérite-t-il d'être répété après la formule du quotient ?

Passages de référence : Y06.

## C451 — OLP-0043-B05

**Choix :** la classe d'équivalence pour
$\Ratequiv$ ; positif ou nul ; strictement positif ; pour certains ; Correction éditoriale ; seuls les témoins $i$ et $j$ de cette condition d'ordre

**Autre formulation envisagée :** Définissons la somme et le produit sur les classes ; ordonnons les rationnels en exigeant que leur différence dans le bon sens admette un numérateur naturel et un dénominateur naturel non nul.

**Motif :** Y06 fournit le registre des opérations sur les classes et les mêmes formules de somme et de produit, avec une convention de dénominateur différente que nous n'importons pas. Positif ou nul traduit non-negative sans ambiguïté ; strictement positif traduit ici positive parce que j est explicitement naturel non nul. Pour certains maintient l'existence des deux témoins, et ne transforme pas le critère en exigence sur tous les représentants. L'original écrit une fois r−s dans le texte après avoir posé correctement s−r ; la formule finale donne aussi [c,d]−[a,b]. La correction textuelle s−r est déclarée dans une note, ainsi que la différence entre les dénominateurs généraux et ceux des témoins de positivité. Y07 appuie seulement le langage d'ordre ; la correction se fonde sur les équations OLP et la vérification directe, non sur une attribution au canon.

**Confiance et limites :** signe de la différence prouvé par le critère et le display source

**Question de révision :** La note distingue-t-elle suffisamment les représentants généraux des témoins naturels de positivité ?

Passages de référence : Y06, Y07.

## C452 — OLP-0043-B06

**Choix :** les propriétés
\emph{attendues} ; traiter les
entiers relatifs \emph{comme} des rationnels ; Pour chaque $i \in \Int$ ; cette identification respecte
les opérations et l'ordre

**Autre formulation envisagée :** Après vérification des propriétés requises, l'application i↦[i,1] permet d'identifier les entiers à des rationnels.

**Motif :** Réemploi contextualisé de C447/C448 : propriétés attendues ne réduit pas le contrôle à une seule propriété technique. Chaque préserve la portée de l'application de Z dans Q ; son représentant et l'unité 1_Int restent exacts. Y06 décrit le prolongement des opérations de Z sur Q et leur identification ; Y07 fournit le registre de compatibilité avec l'ordre. Les deux renvois à check et le ton affirmatif sur les résultats à vérifier sont conservés, sans prétendre que la vérification a déjà été exposée ici.

**Confiance et limites :** inclusion par identification et vérification différée distinctes

**Question de révision :** Préférer identification ou application dans ce paragraphe avant l'exercice qui prouve sa compatibilité ?

Passages de référence : Y06, Y07.

## C453 — OLP-0043-B07

**Choix :** Montrer que ; et que $i \leq j \liff i_\Rat \leq j_\Rat$ ; pour tous $i, j \in \Int$

**Autre formulation envisagée :** Vérifier, pour tous les entiers relatifs i et j, que leur identification dans Q conserve les deux opérations et l'ordre dans les deux sens.

**Motif :** Montrer que garde une consigne de démonstration, sans fournir de solution supplémentaire. Les trois conditions sont jointes par et et la dernière reste une équivalence, non une simple monotonie. Pour tous conserve les deux quantificateurs restreints à Z. Y06 atteste les opérations prolongées et Y07 le langage d'ordre ; aucun de ces passages n'est cité comme contenant cet exercice ou le démontrant à la place du lecteur.

**Confiance et limites :** tâche, trois conditions et portée quantifiée inchangées

**Question de révision :** Le regroupement des trois vérifications en une seule consigne reste-t-il lisible avec ces notations de classes ?

Passages de référence : Y06, Y07.

## C454 — OLP-0044-B03

**Choix :** La droite réelle

**Autre formulation envisagée :** Les nombres réels

**Motif :** Le titre conserve l'entrée géométrique de la source et prépare la construction des réels à partir des rationnels ; Co03 atteste le cadre des coupures.

**Confiance et limites :** objets et trajet inchangés

**Question de révision :** Un titre nominal serait-il préférable ?

Passages de référence : Co03.

## C455 — OLP-0044-B04

**Choix :** L'étape suivante consiste ; ce qui \emph{distingue}

**Autre formulation envisagée :** Avant la construction, examinons ce qui caractérise les réels.

**Motif :** La transition française garde l'ordre pédagogique de la source ; distinguer prépare la propriété de la borne supérieure sans l'annoncer prématurément. Co03 et M01 fixent le registre.

**Confiance et limites :** portée et progression conservées

**Question de révision :** Faut-il nommer la propriété dès cette transition ?

Passages de référence : Co03, M01.

## C456 — OLP-0044-B05

**Choix :** Les réels possèdent ; \emph{corps ordonnés} ; strictement plus
de réels ; Cantor fut le premier

**Autre formulation envisagée :** Les réels partagent la structure de corps ordonné des rationnels, tout en étant plus nombreux.

**Motif :** M02 atteste corps ordonné ; les cardinalités et repères historiques restent ceux de la source OLP. La note sur sqrt(2) est traduite et corrigée explicitement, sans confondre racine positive et racine négative.

**Confiance et limites :** Le sens mathématique et la portée sont contrôlés contre le texte source.

**Question de révision :** Faut-il ajouter une source historique primaire à ces repères ?

Passages de référence : M02, CW01.

## C457 — OLP-0044-B06

**Choix :** Supposons, pour raisonner ; strictement positifs ; fraction soit
irréductible

**Autre formulation envisagée :** Raisonnons par l'absurde avec une fraction irréductible de naturels positifs.

**Motif :** La positivité implicite est explicitée pour les divisions et la descente ; irréductible conserve la minimalité. CW01 justifie le choix positif.

**Confiance et limites :** hypothèses nécessaires explicitées

**Question de révision :** Faut-il détailler le lien entre irréductibilité et minimalité ?

Passages de référence : CW01.

## C458 — OLP-0044-B07

**Choix :** Premièrement, par un raisonnement géométrique ; p=2n-m ; q=m-n ; Cela contredit

**Autre formulation envisagée :** La figure produit une solution entière positive plus petite.

**Motif :** CW01 donne les côtés 2n-m et m-n et l'attribution à Tennenbaum ; la note établit n<m<2n. TikZ et toutes les aires sont conservés. La clé Conway2006 est gardée malgré sa discordance bibliographique documentée.

**Confiance et limites :** descente comparée à l'original cité

**Question de révision :** Une source française améliorerait-elle le registre de cette preuve ?

Passages de référence : CW01.

## C459 — OLP-0044-B08

**Choix :** Deuxièmement, par un raisonnement algébrique ; $m$ est pair ; $n$ est donc lui aussi pair

**Autre formulation envisagée :** La seconde preuve utilise la parité pour contredire l'irréductibilité.

**Motif :** Les étapes m=2r, 2r²=n² et la contradiction restent intactes ; le commentaire en q demeure inactif. Algébrique décrit la méthode sans prétendre à une attestation française.

**Confiance et limites :** calcul vérifié directement

**Question de révision :** Algébrique ou arithmétique serait-il plus précis ?

Passages de référence : CW01.

## C460 — OLP-0044-B09

**Choix :** preuve par le dessin ; Tennenbaum (1927--2006) ; parfaitement rigoureuse

**Autre formulation envisagée :** La preuve géométrique unit intuition et rigueur.

**Motif :** La rhétorique appréciative de l'OLP est conservée ; CW01 atteste la preuve, mais pas les jugements ni les dates, qui restent explicitement hérités.

**Confiance et limites :** registre appréciatif éditorial

**Question de révision :** Le degré d'emphase convient-il au ton du chapitre ?

Passages de référence : CW01.

## C461 — OLP-0044-B10

**Choix :** «~plus riche~» ; propriété de la borne supérieure ; tout ensemble non vide

**Autre formulation envisagée :** Les réels comblent les lacunes des rationnels et satisfont la propriété de la borne supérieure.

**Motif :** M01 atteste le terme exact ; Co01 et Co07 fixent majorant, non-vacuité et plus petit majorant. L'attribution à Weierstrass demeure celle d'OLP.

**Confiance et limites :** Le sens mathématique et la portée sont contrôlés contre le texte source.

**Question de révision :** Faut-il compléter l'attribution à Weierstrass ?

Passages de référence : M01, Co01, Co07.

## C462 — OLP-0044-B11

**Choix :** rationnels ne possèdent pas ; majorant rationnel ; plus petit
majorant rationnel

**Autre formulation envisagée :** L'ensemble rationnel est majoré dans Q mais n'y possède pas de plus petit majorant.

**Motif :** Co01 distingue majorant et borne supérieure ; la disjonction p²<2 ou p<0 et le domaine Q sont conservés. Le signe parasite est retiré avec note typographique.

**Confiance et limites :** domaine et argument préservés

**Question de révision :** Faut-il développer l'absence de plus petit rationnel dans un exercice ?

Passages de référence : Co01, Co07, M01.

## C463 — OLP-0044-B12

**Choix :** attendons intuitivement du continu ; toutes les
«~lacunes~» ; ce qu'assure cette propriété

**Autre formulation envisagée :** La propriété formalise un continu sans lacunes.

**Motif :** M01 et Co06 soutiennent l'interprétation ; l'expression reste une motivation intuitive, pas un nouvel axiome.

**Confiance et limites :** statut motivationnel conservé

**Question de révision :** Le terme continu doit-il recevoir un rappel séparé ?

Passages de référence : M01, Co06.

## C464 — OLP-0045-B02

**Choix :** De $\Rat$ à $\Real$

**Autre formulation envisagée :** Construction des réels par coupures

**Motif :** Le titre garde le trajet de la source et annonce la construction attestée par Co03.

**Confiance et limites :** direction et objets inchangés

**Question de révision :** Un sous-titre Dedekind serait-il utile ?

Passages de référence : Co03.

## C465 — OLP-0045-B03

**Choix :** borne supérieure exprime ; Pour \emph{construire} ; les rationnels

**Autre formulation envisagée :** Une coupure représente la séparation des rationnels en partie inférieure et supérieure.

**Motif :** Co01--Co03 attestent bornes et coupures ; la portée intuitive et les inégalités strictes sont préservées.

**Confiance et limites :** intuition et construction alignées

**Question de révision :** Faut-il préciser le traitement du point frontière ?

Passages de référence : Co01, Co02, Co03, M01.

## C466 — OLP-0045-B04

**Choix :** Précisons cette idée ; partie \emph{inférieure} suffit

**Autre formulation envisagée :** Il suffit de spécifier la partie inférieure ; donnons la définition précise.

**Motif :** Co02 utilise la même convention à une partie ; M01, qui présente une autre paire de parties, est écarté ici.

**Confiance et limites :** convention OLP confirmée

**Question de révision :** Partie inférieure indique-t-elle assez clairement l'ordre ?

Passages de référence : Co02.

## C467 — OLP-0045-B05

**Choix :** Une \emph{coupure} ; segment initial non vide et propre ; sans plus grand élément

**Autre formulation envisagée :** Une coupure est une partie rationnelle non vide, propre, initiale et sans maximum.

**Motif :** Co02 reprend les trois exigences et Co03 le vocabulaire d'identification ; les quantificateurs et la stricte inégalité sont inchangés.

**Confiance et limites :** définition vérifiée clause par clause

**Question de révision :** Faut-il gloser segment initial par stable vers le bas ?

Passages de référence : Co02, Co03.

## C468 — OLP-0045-B06

**Choix :** Nous pouvons maintenant poser ; il faut vérifier ; d'une coupure

**Autre formulation envisagée :** La coupure donnée pour sqrt(2) doit encore satisfaire la définition.

**Motif :** La formule et le renvoi de vérification sont conservés ; Co02 fixe les obligations sans fournir une preuve importée.

**Confiance et limites :** formule et dépendance inchangées

**Question de révision :** Un rappel des trois conditions aiderait-il ici ?

Passages de référence : Co02, Co03.

## C469 — OLP-0045-B07

**Choix :** définir
les fonctions et relations ; relation simple ; propriété de la borne supérieure

**Autre formulation envisagée :** L'inclusion définit l'ordre et toute famille non vide majorée admet une borne supérieure.

**Motif :** Co03 atteste l'ordre par inclusion ; Co07 et M01 fixent l'énoncé complet. La macro liff ne change pas la biconditionnelle.

**Confiance et limites :** domaines et quantificateurs préservés

**Question de révision :** La formule complète reste-t-elle lisible dans ce paragraphe ?

Passages de référence : Co03, Co07, M01.

## C470 — OLP-0045-B08

**Choix :** L'ensemble des coupures possède

**Autre formulation envisagée :** Tout ensemble non vide de coupures majoré possède une borne supérieure.

**Motif :** M01 justifie le nom français ; Co07 en confirme le contenu. Le label technique est conservé pour les renvois.

**Confiance et limites :** terme et portée contrôlés

**Question de révision :** Faut-il répéter les hypothèses dans le théorème ?

Passages de référence : M01, Co07.

## C471 — OLP-0045-B09

**Choix :** Soit $S$ un ensemble non vide ; $\lambda = \bigcup S$ ; C'est l'hypothèse $S\neq\emptyset$ ; un autre majorant

**Autre formulation envisagée :** La réunion est une coupure et l'inclusion prouve qu'elle est le plus petit majorant.

**Motif :** Co06 fournit la méthode de réunion ; Co07 confirme la famille générale. La note corrige l'erreur source sur la non-vacuité et sépare chaque rôle logique.

**Confiance et limites :** dépendances et témoins vérifiés

**Question de révision :** Le rationnel extérieur au majorant pourrait-il être nommé pour alléger la preuve ?

Passages de référence : Co02, Co06, Co07.

## C472 — OLP-0045-B10

**Choix :** objets qui satisfont ; aucune «~lacune~» ; de nouvelles
«~coupures~»

**Autre formulation envisagée :** La construction est complète au sens de l'ordre et n'ajoute pas de nouveau point.

**Motif :** Co06 et Co07 soutiennent l'interprétation ; objets et lacunes restent une métaphore, sans identité littérale de toutes les constructions.

**Confiance et limites :** appréciation source conservée

**Question de révision :** Faut-il remplacer intéressants par nouveaux points ?

Passages de référence : Co06, Co07, M01.

## C473 — OLP-0045-B11

**Choix :** plonger les rationnels ; Pour traiter les autres cas ; puis définissons l'opposé ; produit toujours une
coupure

**Autre formulation envisagée :** Définissons plongement, addition, produit, opposé et cas de signe, puis vérifions leur stabilité.

**Motif :** Co03 et Co04 attestent plongement et addition ; Co05 confirme le produit positif mais son opposé concurrent est rejeté. Les domaines rationnels, le zéro et les corrections typographiques sont explicités sans modifier les commentaires inactifs.

**Confiance et limites :** formules et corrections contrôlées

**Question de révision :** Une preuve séparée de l'opposé faciliterait-elle le renvoi ?

Passages de référence : Co03, Co04, Co05.

## C479 — OLP-0047-B03

**Choix :** Anneaux et corps ordonnés

**Autre formulation envisagée :** Anneaux ordonnés et corps ordonnés

**Motif :** Le titre reprend les deux structures successives de la section. M05 atteste anneau et corps avec ordre total ; ordonnés porte ici sur les deux substantifs.

**Confiance et limites :** Le contenu comporte précisément ces deux définitions, sans restriction à un seul type.

**Question de révision :** Répéter ordonnés rendrait-il le titre plus immédiatement lisible sans lourdeur ?

Passages de référence : M04, M05.

## C480 — OLP-0047-B04

**Choix :** propriétés « attendues » ; montrer, ou esquisser comment montrer

**Autre formulation envisagée :** Préciser en quel sens les définitions donnent les résultats voulus et en esquisser la vérification.

**Motif :** Le calque les définitions se comportent correctement masque les objets et opérations visés. M04 distingue définition des lois et transmission des identités. La reformulation garde la réserve explicite sur les preuves seulement esquissées.

**Confiance et limites :** La modalité sketch est conservée ; aucun exercice n’est présenté comme démontré.

**Question de révision :** Le changement de sujet des définitions vers les objets construits rend-il mieux le référent de behave ?

Passages de référence : M04.

## C481 — OLP-0047-B05

**Choix :** munissent $\Int$ de la structure attendue ; d'une structure d'anneau commutatif

**Autre formulation envisagée :** Montrer que ces lois font de l’ensemble des entiers un anneau commutatif.

**Motif :** M05 formule la construction comme un ensemble muni des opérations, puis comme anneau commutatif. On conserve le renvoi vers la définition des lois et l’objectif conditionné à ces lois exactes.

**Confiance et limites :** Le référent des opérations est explicite et le renvoi int/sec est inchangé.

**Question de révision :** Munir de la structure attendue garde-t-il assez clairement le caractère encore à prouver ?

Passages de référence : M04, M05.

## C482 — OLP-0047-B06

**Choix :** deux éléments
distingués ; Existence d'un opposé ; les variables libres sont implicitement quantifiées ; le $b$ de la formule sur l'opposé est déjà lié

**Autre formulation envisagée :** Inverse additif, avec une phrase disant que chaque égalité vaut pour tous les éléments qui y figurent librement.

**Motif :** M05 oppose élément neutre, opposé additif et inverse multiplicatif. On choisit opposé, tandis que S×S→S rend explicite la fermeture des opérations. Seules les variables libres reçoivent la clôture universelle ; quantifier universellement le b déjà existentiel changerait l’axiome. Les huit formules demeurent exactes.

**Confiance et limites :** Les huit lois ont été comparées terme à terme ; l’ajout décrit leur domaine et ne change pas leur portée.

**Question de révision :** Existence d’un opposé est-il le meilleur intitulé pour rendre visible le quantificateur existentiel ?

Passages de référence : M04, M05.

## C483 — OLP-0047-B07

**Choix :** Aucune n'est difficile à
établir ; l'\emph{associativité} de l'addition

**Autre formulation envisagée :** Les huit vérifications sont élémentaires, mais leur ensemble est assez long ; commençons par l’associativité additive.

**Motif :** La source distingue difficulté conceptuelle et longueur des vérifications. M04 hérite les identités par quotient ; M05 fournit leur réalisation sur les couples. On garde cette distinction et annonce le seul cas additif.

**Confiance et limites :** Ne prétend ni démontrer l’associativité multiplicative ici ni supprimer les autres conditions.

**Question de révision :** Laborieux conserve-t-il le ton explicatif sans décourager inutilement le lecteur ?

Passages de référence : M04, M05.

## C484 — OLP-0047-B08

**Choix :** Il existe donc ; Pour alléger les notations ; en utilisant librement les propriétés

**Autre formulation envisagée :** Choisissons des représentants des trois entiers, puis appliquons deux fois la définition de l’addition et son associativité sur les naturels.

**Motif :** Le quotient M03 permet de choisir des représentants ; M05 donne la loi sur leurs deux coordonnées. Les six naturels, trois classes, convention de suppression de l’indice et sept égalités de la source sont tous conservés. La justification finale porte sur l’addition dans Nat.

**Confiance et limites :** Comparaison exacte des sept lignes actives, sans contraction de la preuve.

**Question de révision :** La convention sur l’indice reste-t-elle assez visible pendant toute la section ?

Passages de référence : M03, M05.

## C485 — OLP-0047-B09

**Choix :** De même, voici comment établir l'\emph{existence d'un opposé}

**Autre formulation envisagée :** Passons à l’existence des opposés.

**Motif :** Ce connecteur met le second exemple sur le même plan que le premier, sans confondre opposé et inverse. Le vocabulaire renvoie au calcul de l’opposé par échange des coordonnées de M05.

**Confiance et limites :** La proposition annoncée correspond exactement à l’axiome suivant.

**Question de révision :** Faut-il répéter additif ici alors que le terme opposé le précise déjà ?

Passages de référence : M05.

## C486 — OLP-0047-B10

**Choix :** Posons $j = \equivrep{b,a}{} \in \Int$ ; Par définition ; Ainsi, $i + j

**Autre formulation envisagée :** La classe du couple inversé est l’opposé, puisque leur somme est la classe de (0,0).

**Motif :** M05 confirme l’échange des deux coordonnées. La preuve conserve la relation sur les couples puis les deux égalités de classes et toute la chaîne finale i+j, que le brouillon avait abrégée. L’égalité des naturels n’est pas une égalité préalable d’entiers construits.

**Confiance et limites :** La version retenue expose les justifications que l’alternative condenserait.

**Question de révision :** La distinction entre couple, classe et zéro construit ressort-elle suffisamment dans cette chaîne ?

Passages de référence : M05.

## C487 — OLP-0047-B11

**Choix :** une démonstration de la \emph{distributivité}

**Autre formulation envisagée :** Démontrons maintenant la distributivité.

**Motif :** M05 emploie la distributivité pour articuler les lois sur les constructions. Le connecteur enfin annonce le dernier exemple prouvé, pas la fin de toutes les vérifications.

**Confiance et limites :** Le paragraphe suivant laisse bien cinq autres conditions en exercice.

**Question de révision :** Enfin pourrait-il être lu comme annonçant la fin de la section ?

Passages de référence : M05.

## C488 — OLP-0047-B12

**Choix :** Comme ci-dessus ; Ligne inactive de la source, erronée par répétition

**Autre formulation envisagée :** Regrouper directement les termes des deux coordonnées, avec seulement les première et dernière égalités.

**Motif :** Les sept lignes actives de distributivité sont rétablies exactement : définition de la somme, produit des couples, développement, regroupement, puis retour aux trois classes. La ligne commentée source contenant un b1b2 supplémentaire demeure inactive et est signalée comme fautive.

**Confiance et limites :** La comparaison des displays confirme toutes les étapes ; le terme commenté est vérifié par développement polynomial.

**Question de révision :** Le commentaire privé source est-il assez distinct des calculs destinés au lecteur ?

Passages de référence : M05.

## C489 — OLP-0047-B13

**Choix :** la démonstration des cinq autres conditions ; Une fois ces vérifications faites

**Autre formulation envisagée :** Les cinq conditions restantes achèvent, une fois démontrées, la preuve que les deux lois donnent un anneau.

**Motif :** Les trois exemples précédents portent sur trois des huit formules, d’où exactement cinq restantes. M04 permet de parler d’identités d’anneau vérifiées ; le futur antérieur marque que la conclusion dépend encore des exercices.

**Confiance et limites :** Le compte huit moins trois est contrôlé ; aucune réussite future n’est présentée comme acquise.

**Question de révision :** Le futur antérieur clarifie-t-il suffisamment le statut conditionnel du bilan ?

Passages de référence : M04.

## C490 — OLP-0047-B14

**Choix :** Démontrer que $\Int$ est un anneau commutatif.

**Autre formulation envisagée :** Vérifier tous les axiomes d’anneau commutatif pour les entiers construits.

**Motif :** L’infinitif d’exercice garde l’objectif entier : compléter les cinq conditions et reprendre les trois déjà prouvées. M05 donne la construction française correspondante, sans importer sa preuve résumée.

**Confiance et limites :** Environnement prob et objet Int conservés.

**Question de révision :** L’énoncé bref suffit-il après l’indication explicite des cinq conditions restantes ?

Passages de référence : M04, M05.

## C491 — OLP-0047-B15

**Choix :** relation réflexive, transitive, antisymétrique et connexe ; exactement l'une des relations ; ses trois cas ne sont pas exclusifs

**Autre formulation envisagée :** Conserver la seule connexité a≤b ou b≤a et supprimer le mot trichotomie.

**Motif :** Collin19 énonce les trois cas stricts mutuellement exclusifs. On restaure le rappel complet de l’ordre total et son renvoi. La disjonction faible source est vraie mais ne constitue pas trois cas exclusifs ; elle est citée dans la note et corrigée sans accuser une fausse implication.

**Confiance et limites :** La correction repose sur le cas a=b et sur le texte strict effectivement lu chez Collin.

**Question de révision :** La note distingue-t-elle assez nettement connexité de l’ordre large et trichotomie de l’ordre strict associé ?

Passages de référence : Co04, M05.

## C492 — OLP-0047-B16

**Choix :** d'ordre total ; pour tous $a,b,c\in S$

**Autre formulation envisagée :** Un anneau muni d’un ordre total compatible avec l’addition et la multiplication par un élément positif ou nul.

**Motif :** M05 et Co04 attestent l’ordre total sur ces constructions. Les deux implications restent exactes, notamment la condition 0≤c pour multiplier ; on rend explicite leur quantification universelle. Ce passage canonique fournit le registre, tandis qu’OLP gouverne la définition abstraite.

**Confiance et limites :** L’alternative résume les lois ; les displays retenus en préservent toute la portée.

**Question de révision :** L’adjectif commutatif explicite évite-t-il les conventions plus générales d’anneau ordonné ?

Passages de référence : M05, Co04.

## C493 — OLP-0047-B17

**Choix :** Démontrer que $\Int$ est un anneau ordonné.

**Autre formulation envisagée :** Établir que l’ordre défini sur les entiers satisfait la définition précédente.

**Motif :** L’exercice porte sur l’ordre précédemment défini, avec les propriétés de relation et les deux compatibilités. La terminologie suit les deux témoins, sans assimiler ordre total et seuls axiomes algébriques.

**Confiance et limites :** Objet et environnement de la source inchangés.

**Question de révision :** Un rappel des compatibilités serait-il utile ou redondant immédiatement après la définition ?

Passages de référence : M05, Co04.

## C494 — OLP-0047-B18

**Choix :** tel que nous l'avons construit ; vérifications laborieuses mais
usuelles

**Autre formulation envisagée :** Les vérifications sont longues mais élémentaires ; nous les laissons au lecteur.

**Motif :** La restriction as constructed importe : il s’agit des classes de couples, pas d’une propriété admise des entiers usuels. M05 fournit exactement ce cadre ; usuelles traduit routine sans effacer laborious ni le travail laissé au lecteur.

**Confiance et limites :** La réserve sur la construction est conservée dans la version retenue.

**Question de révision :** Usuelles ou élémentaires exprime-t-il mieux routine dans ce contexte ?

Passages de référence : M04, M05.

## C495 — OLP-0047-B19

**Choix :** nos définitions de $+$, $\times$ et $\leq$ ; $0\neq1$ ; omise dans la source

**Autre formulation envisagée :** Définir un corps par l’existence d’un inverse pour tout élément non nul, en ajoutant séparément que l’ensemble a au moins deux éléments.

**Motif :** M05 distingue le corps Q de l’anneau Z ; M04 exclut explicitement l’anneau à un élément des corps. L’axiome d’inverse conserve ∀a≠0∃b, avec b dans S. La non-trivialité manquante est ajoutée et disclosed dans un cadre éditorial.

**Confiance et limites :** Le cas du singleton montre exactement pourquoi l’axiome d’inverse seul ne suffit pas.

**Question de révision :** Placer 0≠1 dans la définition puis expliquer l’ajout dans le cadre est-il le plus lisible ?

Passages de référence : M04, M05.

## C496 — OLP-0047-B20

**Choix :** Une fois établi que $\Int$ est un anneau ordonné ; facile, quoique
laborieux

**Autre formulation envisagée :** Les résultats pour les entiers rendent alors les vérifications pour les rationnels élémentaires, mais longues.

**Motif :** Le passage conserve la dépendance de la vérification pour Q envers les résultats obtenus pour Z. M05 expose les constructions dans ce même ordre, sans que cette concordance remplace la preuve demandée.

**Confiance et limites :** La condition initiale et les deux appréciations de difficulté sont présentes.

**Question de révision :** Facile reste-t-il fidèle au ton d’OLP malgré la longueur effective de l’exercice ?

Passages de référence : M04, M05.

## C497 — OLP-0047-B21

**Choix :** Démontrer que $\Rat$ est un corps ordonné.

**Autre formulation envisagée :** Vérifier les axiomes de corps ordonné pour les rationnels construits.

**Motif :** L’objectif inclut désormais la non-trivialité explicite, satisfaite par les classes rationnelles distinctes de 0 et1. L’énoncé source est conservé dans le même environnement.

**Confiance et limites :** Ni exercice supplémentaire ni preuve indûment fournie.

**Question de révision :** Le lecteur identifie-t-il spontanément la dépendance à la définition précédente ?

Passages de référence : M04, M05.

## C498 — OLP-0047-B22

**Choix :** corps ordonné \emph{complet} ; propriété de la borne supérieure ; Il reste toutefois

**Autre formulation envisagée :** Un corps ordonné dans lequel toute partie non vide majorée admet une borne supérieure.

**Motif :** Colmez90 nomme exactement la propriété de la borne supérieure avec non-vacuité et majoration. Complet est ici la propriété analytique, pas la complétude logique. Le renvoi à cuts/realcompleteness prouve seulement cette propriété, laissant les axiomes de corps à vérifier.

**Confiance et limites :** La séparation entre résultat déjà prouvé et vérifications restantes est explicite.

**Question de révision :** Faut-il redonner la propriété entière ici ou le renvoi suffit-il ?

Passages de référence : M01, M02.

## C499 — OLP-0047-B23

**Choix :** nous devons nous assurer ; dès que $\alpha$ et $\beta$ sont des coupures

**Autre formulation envisagée :** Vérifions d’abord que l’opération est une loi sur l’ensemble des coupures.

**Motif :** Co04 définit une somme de coupures avant d’affirmer qu’elle est réelle. On conserve l’ordre logique : bien typer le résultat avant d’en vérifier les identités. La fermeture visée concerne toutes les deux coupures, pas des représentants choisis.

**Confiance et limites :** La version retenue explique concrètement la propriété de fermeture annoncée.

**Question de révision :** Le mot coupure mis en relief suffit-il à faire ressortir ce contrôle de type ?

Passages de référence : Co04, M03.

## C500 — OLP-0047-B24

**Choix :** partie non vide et propre ; Tout $p\in\alpha$ vérifie $p<r$ ; segment initial ; sans maximum

**Autre formulation envisagée :** Conserver l’affirmation de non-vacuité et propreté comme immédiate, puis montrer seulement les deux autres propriétés.

**Motif :** La somme et les propriétés des coupures de Co04 sont directement pertinentes. On développe l’affirmation source non vide et propre avec deux témoins internes et deux externes ; les preuves de segment initial et absence de maximum sont conservées sans sauter x=p+(x−p).

**Confiance et limites :** Les témoins démontrent la propreté sans supposer une borne supérieure réelle déjà construite.

**Question de révision :** La démonstration explicite du caractère propre mérite-t-elle une mention éditoriale ou constitue-t-elle seulement le dépliage du raisonnement source ?

Passages de référence : Co04.

## C501 — OLP-0047-B25

**Choix :** en
excluant, dans le dernier cas ; La source n'active pas ses définitions ; vérifier
que cette construction donne bien l'inverse

**Autre formulation envisagée :** Reformuler l’exercice pour demander au lecteur de définir la division avant d’en prouver les propriétés.

**Motif :** La restriction β≠0 et la tâche laissée au lecteur sont conservées. Les définitions sources de soustraction et division sont commentées ; le cadre donne donc explicitement α+(−β) et αβ⁻¹. Le quotient positif est une coupure stricte construite avec des majorants rationnels hors β. Co04 fournit la convention de coupure ; aucune attestation de cette formule exacte n’est revendiquée. La formule est une réparation éditoriale vérifiée directement.

**Confiance et limites :** Jugement provisoire sur l’exposition ; validité mathématique vérifiée par les témoins et la propriété d’approximation de coupures, avec preuve détaillée dans la revue.

**Question de révision :** La formule explicite d’inverse alourdit-elle l’exercice plus qu’une demande de construction laissée au lecteur ?

Passages de référence : Co04, M03.

## C502 — OLP-0047-B26

**Choix :** Démontrer que $\Real$ est un corps ordonné.

**Autre formulation envisagée :** Achever les vérifications algébriques et d’ordre pour les coupures réelles.

**Motif :** L’exercice demande les axiomes du corps et leur compatibilité avec l’ordre des coupures ; il ne redemande pas la propriété de la borne supérieure déjà établie. Les deux constructions chez Colmez confirment le sens de corps ordonné sans fournir ici une solution.

**Confiance et limites :** Le même environnement prob conserve le même objectif.

**Question de révision :** Le mot complet doit-il rester absent, conformément à la source et à la propriété déjà démontrée ?

Passages de référence : M01, M02, Co04.

## C503 — OLP-0047-B27

**Choix :** Dans \olref[cuts]{sec} ; Il faut cependant montrer

**Autre formulation envisagée :** Vérifions que l’ensemble proposé précédemment pour représenter √2 possède les propriétés d’une coupure.

**Motif :** Le renvoi et la formule de la coupure de √2 avaient disparu du brouillon. Ils sont rétablis ; seul or devient ou. Il s’agit de prouver que l’ensemble satisfait la définition de coupure, sans assimiler chaque p à la racine.

**Confiance et limites :** La formule conserve les rationnels négatifs et la disjonction p²<2, y compris zéro.

**Question de révision :** Le rappel intégral de la formule facilite-t-il assez la lecture autonome de cette dernière preuve ?

Passages de référence : Co04.

## C504 — OLP-0047-B28

**Choix :** il contient $1$ et ne contient pas $2$ ; Si $p\leq0$ ; strictement positif ; Puisque $p+2>0$

**Autre formulation envisagée :** Dire que les trois premières propriétés sont évidentes puis traiter seulement p>0.

**Motif :** La preuve source est restaurée avec ses deux chaînes de quatre et six lignes. Le caractère initial est explicité par les cas x<0 et 0≤x<p. Le cas p≤0, laissé implicite, est couvert par1 ; pour p>0, le dénominateur positif permet les divisions sans inversion d’inégalité. Co04 fournit le registre de coupure ; l’algèbre reste celle d’OLP.

**Confiance et limites :** Les dix lignes de calcul sont identiques à la source après espaces ; les cas de signe comblent le seul raccourci logique.

**Question de révision :** Ces précisions de signe rendent-elles la preuve suffisamment autonome pour le lecteur ?

Passages de référence : Co04.

## C505 — OLP-0048-B05

**Choix :** les réels construits à partir des suites de Cauchy

**Autre formulation envisagée :** Annexe : les réels comme classes de suites de Cauchy

**Motif :** Colmez90 construit le corps comme quotient du système de suites ; le titre à partir de évite d’identifier littéralement un réel à une suite. Annexe et les mêmes objets restent annoncés.

**Confiance et limites :** Le choix annonce le procédé sans anticiper avant l’introduction le terme de classe.

**Question de révision :** Faut-il annoncer explicitement le quotient dans le titre ?

Passages de référence : M02.

## C506 — OLP-0048-B06

**Choix :** une autre construction ; aujourd'hui une suite de Cauchy ; notamment Weierstrass, Heine

**Autre formulation envisagée :** Une construction ultérieure fondée sur le critère de Cauchy, due entre autres à ces auteurs.

**Motif :** La notice MacTutor effectivement lue distingue le critère associé à Cauchy de son emploi ultérieur dans des constructions. Notamment conserve le caractère non exhaustif de la liste. Les trois commandes de citation de cette introduction et de celle sur Stevin restent celles d’OLP.

**Confiance et limites :** Les attributions restent celles de la source ; la notice historique citée les corrobore, sans attester leur formulation française.

**Question de révision :** Définition due à Cauchy garde-t-il assez clairement la réserve historique ce que nous appelons aujourd’hui ?

Passages de référence : OR01, M02.

## C507 — OLP-0048-B07

**Choix :** développement décimal ; le chiffre décimal de rang $n$ ; coder le signe et la partie
entière

**Autre formulation envisagée :** Écriture décimale, en présentant directement d comme application dans l’ensemble des dix chiffres.

**Motif :** M06 atteste développement décimal et chiffres avant la virgule ; KK01 fournit le contexte historique de Stevin. Le codage d:Nat→Nat garde son domaine source mais exige des valeurs0–9, pas des naturels arbitraires. Signe, partie entière et identification des queues de9/0 sont explicités sans présenter Stevin comme auteur d’une construction ensembliste moderne. Les chiffres sont inchangés ; le séparateur devient une virgule française.

**Confiance et limites :** La restriction omise est signalée ; les ajustements de signe et de partie entière couvrent tous les réels.

**Question de révision :** Conserver Nat comme codomaine puis restreindre l’image est-il plus fidèle que modifier directement le codomaine affiché ?

Passages de référence : M06, KK01.

## C508 — OLP-0048-B08

**Choix :** approximations rationnelles de
plus en plus précises ; Une suite de rationnels peut être considérée comme une fonction ; une fonction \emph{quelconque} ; une condition correspondant à

**Autre formulation envisagée :** Remplacer l’image du rapprochement par une annonce immédiate du critère de Cauchy.

**Motif :** Les trois observations source sont gardées dans l’ordre : développement, suite rationnelle, fonction Nat→Rat. Les troncatures gardent exactement les chiffres et le saut source de1,4 à1,414. Le contre-exemple pair/impair conserve0,1,0,1 et mène à une condition correspondant à une limite, pas à l’hypothèse déjà réelle d’une limite. M02 fournit cette distinction constructive ; KK01 ne sert qu’à l’entrée Stevin.

**Confiance et limites :** La version retenue garde l’itinéraire intuitif, les trois observations et l’exemple oscillant complets.

**Question de révision :** Les points-virgules séparent-ils clairement les termes malgré les virgules décimales ?

Passages de référence : M02, M06, KK01.

## C509 — OLP-0048-B09

**Choix :** quantifiait implicitement sur les réels ; pour tout $\epsilon\in\Rat$ strictement positif ; où $m$ et $n$ parcourent les naturels

**Autre formulation envisagée :** Utiliser la précision2⁻ʲ de Colmez au lieu de l’epsilon rationnel de la source.

**Motif :** Colmez90 définit les suites sans employer de limite réelle. L’argument contre la circularité est conservé entièrement et ε reste rationnel. On explicite le sens français strict de positive et le domaine naturel des deux indices universels après le rang existentiel.

**Confiance et limites :** L’alternative est équivalente mais changerait inutilement la définition OLP ; les quantificateurs originaux sont préservés.

**Question de révision :** La précision du domaine m,n doit-elle être écrite dans la formule plutôt qu’après elle ?

Passages de référence : M02.

## C510 — OLP-0048-B10

**Choix :** les termes sont suffisamment proches les uns des autres ; La définition de
Cauchy n'affirme pas ; chaque erreur inférieure à
$\epsilon/2$

**Autre formulation envisagée :** Conserver simplement notre suite a une limite, en renvoyant implicitement à la construction par coupures déjà disponible.

**Motif :** La source glisse du critère de Cauchy à l’existence d’une limite. La phrase principale garde l’explication de précision et de rang, l’exemple et le seuil1/10ⁿ ; la note distingue motivation ou réel par coupures de construction autonome. Deux erreurs ε/2 donnent l’écart ε, ce que ne donnait pas à lui seul le commentaire original.

**Confiance et limites :** La note évite le raisonnement circulaire sans supprimer l’intuition initiale.

**Question de révision :** Le recours possible aux coupures antérieures est-il assez distinct de la preuve autonome annoncée ?

Passages de référence : M02, M06.

## C511 — OLP-0048-B11

**Choix :** plusieurs suites de Cauchy
distinctes ; sauf que
$g(0)\neq f(0)$ ; au terme de la construction

**Autre formulation envisagée :** Dire seulement que des modifications finies ne changent pas la classe.

**Motif :** M03 et M02 distinguent représentants et classes. Le seul changement au rang0 reste l’exemple source. La référence def:CauchySequence concerne le critère, et non une définition de limite qu’elle ne contient pas. Le futur au terme de la construction garde la visée commune sans l’affirmer déjà réalisée.

**Confiance et limites :** Cette alternative abrégerait l’exemple et anticiperait une relation pas encore définie ; la version retenue les conserve.

**Question de révision :** La reformulation du renvoi rend-elle suffisamment visible la correction du mot limit de la source ?

Passages de référence : M02, M03.

## C512 — OLP-0048-B12

**Choix :** identifier les réels à des classes ; pour tout $\epsilon\in\Rat$ strictement positif ; Il faut vérifier que $\Realequiv$ est une relation d'équivalence ; Une suite
représentante et sa classe

**Autre formulation envisagée :** Conserver une convention déclarant dès ici que suite désignera aussi sa classe.

**Motif :** La différence tendant vers zéro est attestée par la construction française M02 et par la source historique OR01. La définition de tendre vers zéro est complète avec tous les domaines ; son renvoi et sa limite formelle sont conservés. La faute source relations pour classes est corrigée et signalée, y compris sa répétition dans les énoncés de corps et de borne supérieure.

**Confiance et limites :** Une telle convention cacherait les erreurs de type dans les expressions h−f ultérieures ; la distinction est maintenue.

**Question de révision :** Le cadre unique couvre-t-il clairement les corrections de type dans les deux théorèmes suivants ?

Passages de référence : M02, M03, OR01.

## C513 — OLP-0048-B13

**Choix :** $g(n)=\frac{1}{(n+1)^2}$ ; toutes deux tendent vers $0$

**Autre formulation envisagée :** Montrer que les deux suites représentent le même réel nul.

**Motif :** L’exercice garde la suite nulle et le dénominateur(n+1)², qui évite toute division par zéro au rang0. La conclusion exige Cauchy, limite nulle et équivalence ; elle n’est pas réduite à la seule dernière propriété.

**Confiance et limites :** La version retenue conserve les deux tâches explicites dont cette conclusion résulte.

**Question de révision :** Plus précisément traduit-il bien indeed en laissant visible la double vérification ?

Passages de référence : M02.

## C514 — OLP-0048-B14

**Choix :** Pour alléger la lecture ; la fonction constante ; ne
dépendent pas des représentants choisis ; ne suffit pas, à elle seule

**Autre formulation envisagée :** Se contenter de vérifier que les sommes et produits sont de Cauchy, comme dans la phrase source.

**Motif :** M02 utilise exactement suites constantes, addition et multiplication terme à terme. Les deux égalités de classes et les trois opérations à vérifier, dont la différence, sont présentes. M03 exige en plus l’invariance sous équivalence : une note distingue cette obligation de la simple fermeture des suites de Cauchy. La macro !!a{element} est conservée pour l’intégration française.

**Confiance et limites :** Le passage au quotient a besoin des deux conditions, sans qu’une note prétende en fournir déjà la preuve complète.

**Question de révision :** Le rappel de bonne définition après les displays est-il placé au moment où le lecteur en a besoin ?

Passages de référence : M02, M03.

## C515 — OLP-0048-B15

**Choix :** \emph{strictement positive} ; $\equivrep{f}{}\neq0_\Real$ ; même signe ; représentante de l'inverse ; Les classes d'équivalence

**Autre formulation envisagée :** Définir directement la positivité par l’existence d’un epsilon rationnel uniformément minorant à partir d’un rang.

**Motif :** Co04 montre que positif peut inclure zéro en français ; strictement est donc nécessaire. M02 notes44–45 gouverne l’inverse éventuel et l’ordre indépendant des représentants. La comparaison avec0_Rat est corrigée en0_Real. Le lemme d’écart rationnel positif, prouvé sans limite réelle, assure non-nullité, stabilité du signe et inverse malgré des zéros initiaux. La variante commentée large est conservée : sa disjonction avec l’égalité des classes est correcte ; seule l’inégalité éventuelle prise isolément ne descend pas au quotient.

**Confiance et limites :** L’alternative est équivalente ; la version retenue conserve les deux conditions originales et prouve le fait qui les rend efficaces.

**Question de révision :** Le lemme dans un cadre éditorial gagne-t-il à devenir ultérieurement un lemme numéroté ?

Passages de référence : M02, M03, Co04.

## C516 — OLP-0048-B16

**Choix :** En exercice.

**Autre formulation envisagée :** Démonstration laissée au lecteur.

**Motif :** La source met le mot Exercise dans un environnement de preuve. Le renvoi de travail au lecteur est conservé, sans inventer une démonstration achevée des axiomes.

**Confiance et limites :** Le statut reste un exercice, malgré l’étiquette typographique de preuve.

**Question de révision :** Le français En exercice est-il suffisamment explicite dans cet environnement ?

Passages de référence : M02.

## C517 — OLP-0048-B17

**Choix :** les classes d'équivalence de suites de Cauchy ; un corps ordonné

**Autre formulation envisagée :** Démontrer que l’ensemble des réels ainsi défini forme un corps ordonné.

**Motif :** L’exercice porte sur le quotient, pas sur l’anneau des suites lui-même. M02 donne précisément cette distinction. Le corrigendum annoncé au bloc12 s’applique ici ; toutes les lois du corps ordonné restent à établir.

**Confiance et limites :** Nommer les classes permet de vérifier le type sans ambiguïté.

**Question de révision :** La répétition complète des classes est-elle utile après le théorème identique ?

Passages de référence : M02, M03.

## C518 — OLP-0048-B18

**Choix :** La propriété de la borne supérieure ; nous allons donc en donner la démonstration

**Autre formulation envisagée :** La complétude de ce corps demande davantage de travail ; en voici une preuve.

**Motif :** M01 nomme la propriété analytique de complétude ; M02 fournit l’autre construction concernée. La comparaison harder et la décision de donner la preuve sont toutes deux conservées.

**Confiance et limites :** La forme retenue évite toute confusion avec une complétude logique et annonce une démonstration que le texte donne ensuite.

**Question de révision :** La répétition du nom long aide-t-elle davantage qu’elle n’alourdit la transition ?

Passages de référence : M01, M02.

## C519 — OLP-0048-B19

**Choix :** Tout ensemble non vide et majoré ; classes d'équivalence ; admet une borne supérieure

**Autre formulation envisagée :** Tout ensemble non vide de ces réels ayant un majorant possède un plus petit majorant.

**Motif :** La non-vacuité et la majoration sont indispensables dans M01 et dans OLP. Le type source suites est corrigé en classes ; borne supérieure signifie le plus petit des majorants, pas un majorant quelconque.

**Confiance et limites :** Les deux hypothèses et l’extrémalité sont intactes.

**Question de révision :** Répéter plus petit majorant entre parenthèses serait-il utile après la section sur les coupures ?

Passages de référence : M01, M02.

## C520 — OLP-0048-B20

**Choix :** notons $S$ l'ensemble de toutes les suites ; ceux de $\mathcal A$ des classes ; toute suite de Cauchy rationnelle est bornée ; bornes comprises

**Autre formulation envisagée :** Faire de S un ensemble de classes et écrire tous les quantificateurs et calculs avec des représentants choisis ad hoc.

**Motif :** Le nouveau nom A désigne l’ensemble de classes et S son image réciproque entière parmi les suites. Cela conserve les h∈S des formules sans les appliquer à des classes, et ne choisit pas simultanément un représentant pour chaque classe. L’élément r est comparé via sa classe. Bornitude d’une suite de Cauchy donne les deux bornes rationnelles qui étaient seulement affirmées.

**Confiance et limites :** La version retenue conserve la notation des displays source et évite une hypothèse implicite de choix.

**Question de révision :** L’introduction de deux ensembles typés mérite-t-elle un rappel supplémentaire avant le premier display ?

Passages de référence : M02, M03.

## C521 — OLP-0048-B21

**Choix :** par valeurs inférieures et supérieures ; définition par récurrence ; les intervalles $[g(n),f(n)]$ sont emboîtés ; les deux premières branches peuvent s'appliquer simultanément ; pour
chaque $n$

**Autre formulation envisagée :** Changer la branche de g en une inégalité stricte pour obtenir un partage exclusif et une division exacte par deux.

**Motif :** Le mouvement simultané des deux suites est conservé avec les branches originales ≤ et≥, leur milieu et la note avouant que la récurrence n’a pas encore été justifiée. La source dit à tort exactement moitié : si le milieu est le maximum, les deux branches valent a_n et l’écart devient0. La contraction ≤ moitié et les deux invariants suffisent pour Cauchy, équivalence et les deux conclusions ultérieures. M02 fournit le langage des suites et classes ; cette correction du cas limite est directement dérivée des formules OLP, pas attribuée à une preuve étrangère.

**Confiance et limites :** Conserver les branches source exige seulement de corriger leur conséquence ; l’exemple singleton dont le maximum est au milieu vérifie le défaut.

**Question de révision :** Le maintien de deux branches inclusives reste-t-il pédagogiquement préférable à une bifurcation exclusive explicitement corrigée ?

Passages de référence : M02, M01.

## C522 — OLP-0048-B22

**Choix :** pour obtenir une contradiction ; un écart rationnel ; $(h-f)-(c_{f(n)}-f)$ ; ce qui contredit

**Autre formulation envisagée :** Dire seulement que f décroît vers sa classe et choisir un terme assez proche.

**Motif :** Le raisonnement source contre [f]<[h] est conservé avec son renvoi au corps ordonné et sa chaîne finale. La positivité fournit δ, puis la propriété de Cauchy de f donne une erreur<δ/2 ; la différence des deux suites est donc minorée positivement, pas simplement positive terme à terme. On ne suppose aucune limite réelle pour justifier le passage à leurs classes.

**Confiance et limites :** L’alternative laisserait le passage crucial sans justification dans une construction des limites ; les quantificateurs assez grand sont ordonnés correctement.

**Question de révision :** L’explication du choix de n est-elle assez concise tout en excluant une dépendance de n au terme m variable ?

Passages de référence : M02, M03.

## C523 — OLP-0048-B23

**Choix :** le
\emph{plus petit} majorant ; la croissance de $g$ ; il existe $h\in S$ ; ne majore pas

**Autre formulation envisagée :** Conclure directement par symétrie avec la preuve de majoration précédente.

**Motif :** La seconde moitié de la preuve utilise la borne inférieure approchante et un témoin de S à chaque rang. Pour [j]<[g], l’écart positif et la condition de Cauchy donnent [j]<c_g(n), puis un h avec c_g(n)≤[h]. Le résultat est absence de majoration par tout j plus petit, donc minimalité ; toutes les étapes et inégalités de la source restent visibles.

**Confiance et limites :** La version retenue garde le témoin existentiel que la symétrie seule masquerait.

**Question de révision :** La répétition du choix d’écart rend-elle la dernière étape autonome sans refaire toute la preuve précédente ?

Passages de référence : M02, M03, M01.

## C524 — OLP-0041-B04

**Choix :** Arithmétisation

**Autre formulation envisagée :** Construction des systèmes de nombres

**Motif :** De Rouilhan311 emploie explicitement arithmétisation de l’analyse pour la réduction de l’étude des réels à l’arithmétique. Le titre bref d’OLP étend ce cadre aux constructions des entiers et rationnels ; on conserve cette extension source sans l’attribuer au témoin français.

**Confiance et limites :** Forte pour le terme attesté ; portée du titre gouvernée par OLP.

**Question de révision :** Un sous-titre descriptif apporterait-il quelque chose après le cadre introductif ?

Passages de référence : R01.

## C525 — OLP-0041-B05

**Choix :** construction des systèmes de nombres ; une théorie naïve des ensembles ; \emph{Open Set Theory} de Tim Button

**Autre formulation envisagée :** Le contenu de ce chapitre est repris d’Open Set Theory, où Tim Button construit les ensembles de nombres en théorie naïve des ensembles.

**Motif :** M05 traite successivement Z et Q, puis R dans un cadre ensembliste ; R01 et P03 contextualisent ce recours aux ensembles. La phrase française distingue la portée du chapitre et sa provenance, toutes deux présentes dans la source. Le nom de l’auteur et le titre original restent exacts ; ni nom d’utilisateur ni crédit inventé.

**Confiance et limites :** Le cadre ne promet pas d’axiomatisation supplémentaire ; l’attribution est directement donnée par la source gelée.

**Question de révision :** Systèmes de nombres exprime-t-il mieux number systems que ensembles de nombres dans ce contexte d’opérations ?

Passages de référence : M05, R01, P03.

## C526 — OLP-0046-B04

**Choix :** Quelques réflexions philosophiques

**Autre formulation envisagée :** Remarques philosophiques

**Motif :** Le titre garde Some et la distinction entre commentaire philosophique et développement technique. P03 fournit le registre de la portée d’une construction, sans imposer sa doctrine propre.

**Confiance et limites :** Le titre annonce correctement une discussion non définitive.

**Question de révision :** Réflexions conserve-t-il mieux le caractère exploratoire de la section ?

Passages de référence : P03.

## C527 — OLP-0046-B05

**Choix :** Voilà pour les aspects techniques. Mais qu'avons-nous obtenu ?

**Autre formulation envisagée :** Les détails techniques étant établis, quel en est l’apport ?

**Motif :** La transition et la question sont toutes deux conservées. P03 distingue la description ensembliste et ce qu’elle apporte à la compréhension ; ce contraste justifie le registre direct, sans transformer la question OLP en une thèse.

**Confiance et limites :** La voix interrogative demeure celle de la source.

**Question de révision :** La formulation orale Voilà convient-elle au registre adulte de cette transition ?

Passages de référence : P03.

## C528 — OLP-0046-B06

**Choix :** cela ne prête guère à contestation ; des résultats conceptuels
profonds ; la différence cruciale ; relative au cadre ensembliste

**Autre formulation envisagée :** Dire que la notion est réalisable, sans utiliser cohérente.

**Motif :** On conserve les trois bénéfices distincts : valeur mathématique, identification de la propriété de la borne supérieure, réalisation du corps ordonné complet. M01/M02 attestent les constructions et la propriété. La notion source coherent est conservée, avec une réserve explicite de cohérence relative au cadre, pas une preuve absolue de la théorie naïve.

**Confiance et limites :** La construction réalise les axiomes ; le cadre éditorial empêche de lui attribuer une force métathéorique supérieure.

**Question de révision :** Cohérente suivi d’une note est-il plus fidèle et clair que réalisable seul ?

Passages de référence : M01, M02, P03.

## C529 — OLP-0046-B07

**Choix :** néanmoins quelques réserves

**Autre formulation envisagée :** Il faut pourtant nuancer la portée de ces résultats.

**Motif :** La concession n’annule pas les acquis précédents. Le registre de P03 admet la légitimité d’une réduction tout en discutant sa portée ; seules cette articulation et la modalité sont pertinentes ici.

**Confiance et limites :** La réserve garde son caractère partiel, sans verdict général négatif.

**Question de révision :** Appellent des réserves suggère-t-il une nécessité plus forte que should air ?

Passages de référence : P03.

## C530 — OLP-0046-B08

**Choix :** il n'est pas clair ; pour l'essentiel ; dès le début du dix-septième siècle ; n'est peut-être pas

**Autre formulation envisagée :** Présenter la construction décimale comme également rigoureuse de manière catégorique.

**Motif :** M06 confirme l’autre construction décimale ; KK01 place l’apport de Stevin avant l’arithmétisation du dix-neuvième siècle. On préserve toutes les atténuations et le renvoi Cauchy, notamment essentially qui avait disparu. OLP évalue l’intérêt philosophique, il ne nie pas la validité des coupures.

**Confiance et limites :** La version retenue conserve exactement l’incertitude comparative et l’hypothèse peut-être de l’auteur.

**Question de révision :** Le terme familiers rend-il familiar sans supposer chez le lecteur une maîtrise technique des décimales infinies ?

Passages de référence : M01, M06, KK01, R01.

## C531 — OLP-0046-B09

**Choix :** Il est encore moins clair ; nous \emph{oublions} immédiatement ; sauf, bien sûr ; c'est-à-dire comme ensembles d'ensembles

**Autre formulation envisagée :** Dire que ces représentations sont rarement utiles dans les preuves ordinaires et supprimer la chaîne répétitive.

**Motif :** Les trois constructions successives et l’exception des preuves portant sur leur comportement sont intégrales. La chaîne visible garde sept niveaux ensemblistes. Les commentaires source expliquent les trois niveaux des rationnels et des entiers, avec les exemples de couples ; ils sont traduits entièrement, pas réduits à etc. M03/M05 attestent couples et classes ; P03 éclaire le contraste avec l’usage sans corroborer l’absolu rhétorique personne.

**Confiance et limites :** L’alternative modérerait et abrégerait OLP ; la version retenue conserve son ton et son exemple complet.

**Question de révision :** Faut-il annoter l’hyperbole personne dans une édition future, sans modifier le texte de l’auteur ?

Passages de référence : M03, M05, P03, R01.

## C532 — OLP-0046-B10

**Choix :** sur le plan métaphysique ; tout aussi bien fonctionné ; constructions
ensemblistes concurrentes ; arbitraire,
et embarrassant

**Autre formulation envisagée :** Conclure directement que les nombres ne sont pas des ensembles.

**Motif :** B01 lu dans l’original montre des représentations arithmétiquement adéquates mais extensionnellement différentes, puis l’absence de raison privilégiant l’une. OLP donne une variante par le codage des couples. Cette variante, ses deux renvois et sa citation sont conservés, sans importer la conclusion plus forte de Benacerraf selon laquelle les nombres ne peuvent être des ensembles.

**Confiance et limites :** La version retenue respecte la portée sceptique et conditionnelle d’OLP et l’attribution précise de l’argument.

**Question de révision :** Sur le plan métaphysique rend-il metaphysically speaking sans jargon supplémentaire ?

Passages de référence : B01, P03, M03, M06.

## C533 — OLP-0046-B11

**Choix :** dans la réalisation ensembliste usuelle ; prise littéralement dans cette
réalisation ; ordinaux finis de von Neumann ; au moyen d'un plongement

**Autre formulation envisagée :** Conserver la disjonction comme si elle suivait des seules définitions de classes, sans préciser la représentation des naturels.

**Motif :** La comparaison0≠[0,0], aucun naturel entier et Nat⊆Rat requiert une réalisation, laissée implicite par OLP. On la restreint explicitement et donne l’exemple des naturels ordinaux finis versus classes infinies. Les plongements de M05 expliquent les identifications mathématiques usuelles ; B01 motive la distinction entre adéquation structurale et identité d’objets. Aucune affirmation de disjonction indépendante du codage n’est conservée.

**Confiance et limites :** Le cas standard se prouve par finitude contre infinitude ; la construction seule n’impose pas un codage universel.

**Question de révision :** La note sur von Neumann anticipe-t-elle trop le chapitre suivant ou explicite-t-elle utilement l’hypothèse nécessaire ?

Passages de référence : M03, M05, B01.

## C534 — OLP-0046-B12

**Choix :** en nous donnant les naturels ; \emph{plonger} les théories ; La portée philosophique

**Autre formulation envisagée :** Interpréter les théories de ces objets dans une théorie des ensembles.

**Motif :** La conclusion reste relative à la théorie naïve et aux naturels admis. P03 distingue légitimité de la réduction et portée/signification ; R01 atteste le cadre d’arithmétisation. Plonger appliqué aux théories conserve la métaphore de embed chez OLP ; aucune attestation exacte de cette collocation ni théorème formel d’interprétabilité n’est revendiqué.

**Confiance et limites :** Confiance moyenne sur la collocation : l’alternative technique pourrait promettre une formalisation absente de la source.

**Question de révision :** Plonger des théories reste-t-il compréhensible ici, ou représenter leur contenu serait-il préférable ?

Passages de référence : P03, M03, R01.

## C535 — OLP-0046-B13

**Choix :** ce n'est pas le dernier mot ; un argument
\emph{philosophique} supplémentaire

**Autre formulation envisagée :** L’arithmétisation n’a donc pas de signification philosophique profonde.

**Motif :** La réserve finale laisse ouverte une portée profonde à condition d’un argument philosophique supplémentaire. P03 distingue ce qui fonde la portée d’une théorie de sa seule structure ; sa réponse propre n’est pas transférée à OLP.

**Confiance et limites :** L’alternative contredirait la modalité exigerait et fermerait le débat que la source laisse ouvert.

**Question de révision :** La répétition philosophique maintient-elle efficacement l’accent argumentatif source ?

Passages de référence : P03, R01.

## C536 — OLP-0046-B14

**Choix :** nous avons tenu les naturels ; Mais que pouvons-nous faire à leur sujet ? ; C'est l'objet du chapitre suivant.

**Autre formulation envisagée :** Résumer le commentaire par La construction des naturels viendra ensuite.

**Motif :** Ce commentaire source comporte une récapitulation, une question et un renvoi futur. Les trois sont traduits dans les sources éditables tout en restant inactifs. Les naturels sont traités comme donnés, pas déclarés déjà construits ; M05 et le cadre R01 ne changent pas cette dépendance.

**Confiance et limites :** L’alternative précédente avait perdu la question ; le commentaire complet est maintenant conservé.

**Question de révision :** Lors de l’édition intégrale, ce commentaire devrait-il devenir une transition visible avec un renvoi vérifié ?

Passages de référence : M05, R01.

## C537 — OLP-0051-B03

**Choix :** Algèbres de Dedekind

**Autre formulation envisagée :** Systèmes simplement infinis

**Motif :** Le titre désigne la structure définie plus loin. Dedekind et Sage parlent de système simplement infini; aucune attestation native de la collocation algèbre de Dedekind n’a été trouvée dans les passages lus. On conserve le nom moderne donné par OLP et sa définition, sans le confondre avec les anneaux de Dedekind.

**Confiance et limites :** Forte sur l’objet défini, moyenne sur l’usage du nom français; l’alternative effacerait le choix terminologique propre à OLP.

**Question de révision :** Faut-il ajouter un renvoi terminologique vers système simplement infini dans l’index ?

Passages de référence : Dk02, Sg01.

## C538 — OLP-0051-B04

**Choix :** en nombre
infini ; certaines propriétés
algébriques ; les autres opérations

**Autre formulation envisagée :** Nous voulons des naturels infinis et une bonne algèbre.

**Motif :** La phrase porte sur l’infinité de l’ensemble des naturels, pas sur des entiers individuellement infinis. Les attentes algébriques et and so forth restent présentes. L20 et Pt01 distinguent les opérations définies de leurs propriétés; aucune propriété nouvelle n’est introduite.

**Confiance et limites :** La version retenue évite une lecture erronée d’infinite appliqué à chaque entier et préserve l’ouverture de la liste.

**Question de révision :** La dernière proposition peut-elle être allégée sans perdre l’exigence portant sur les opérations ?

Passages de référence : L20, Pt01.

## C539 — OLP-0051-B05

**Choix :** \emph{fonction successeur} ; $s$ est !!a{injection} ; contenant $0$ ; ce langage arithmétique ; pas à pas

**Autre formulation envisagée :** Fermé pour le successeur, sans mention de0; la troisième condition ne relève jamais du premier ordre.

**Motif :** Les trois conditions, leurs deux reformulations symboliques et leurs liens sont conservés. Stable par suit l’usage natif. Contenant0 répare une omission: sinon l’ensemble vide satisfait3′. La limite du premier ordre est restreinte au langage arithmétique; la note prévient l’erreur qui consisterait à exclure une formalisation ensembliste du premier ordre. Pas à pas conserve la transition pédagogique adulte.

**Confiance et limites :** Forte: l’omission de0 admet le contre-exemple vide; les langages et leurs domaines de quantification sont distincts.

**Question de révision :** La précision de langage mérite-t-elle une formulation encore plus courte à ce stade ?

Passages de référence : Dk02, Sg01, L20.

## C540 — OLP-0051-B06

**Choix :** $f\colon A\to A$ ; $X\subseteq A$ ; \emph{stable par $f$} ; clôture de $o$ sous $f$ ; ensemble non vide

**Autre formulation envisagée :** Ensemble f-fermé; fermeture de o; intersection de tous les ensembles sans préciser de domaine.

**Motif :** L’ensemble ambiant et l’endomap sont explicites, comme dans§36 de Dedekind. L’intersection porte sur des parties de A et existe car A lui-même convient. Stable évite le faux ami fermé, susceptible d’évoquer la topologie. Clôture nomme l’opération minimale définie; cette collocation est un choix explicatif, non une citation attestée de Sage.

**Confiance et limites :** Forte sur le cadre mathématique; choix terminologique de clôture provisoire et défini localement.

**Question de révision :** Clôture sous f ou clôture pour f s’accorde-t-il mieux avec les chapitres ultérieurs ?

Passages de référence : Dk01, Sg01.

## C541 — OLP-0051-B07

**Choix :** la \emph{plus petite} ; Pour toute application ; si $X\subseteq A$ ; comme !!{element}

**Autre formulation envisagée :** Une partie minimale stable; tout ensemble X, sans préciser son domaine.

**Motif :** Le passage va de l’intuition aux trois propriétés formelles et garde leur numérotation. Plus petite signifie incluse dans toute partie admissible, et non seulement minimale. La grammaire comme élément retire l’article anglais tout en conservant le jeton. Les quantificateurs sont bornés par l’ensemble ambiant de la définition.

**Confiance et limites :** Forte: la propriété de plus petit est exactement la troisième clause; le bornage rend l’application f partout définie sur X.

**Question de révision :** La répétition de partie de A dans l’intuition est-elle utile au lecteur ?

Passages de référence : Dk01, Sg01.

## C542 — OLP-0051-B08

**Choix :** $\ran{f}\cup\{o\}$ ; chacun de ses éléments ; \emph{toutes}

**Autre formulation envisagée :** Prendre simplement A comme témoin et supprimer le témoin de la source.

**Motif :** Le témoin de non-vacuité choisi par OLP est conservé, plutôt que remplacé par A. Sa stabilité est maintenant justifiée parce que ses éléments sont dans le domaine A et que leurs images appartiennent à ran f. La suite annonce les trois vérifications avec leurs renvois.

**Confiance et limites :** Forte sous f:A→A; sans cette hypothèse le témoin original peut être hors domaine.

**Question de révision :** La phrase de vérification du témoin est-elle suffisamment explicite sans alourdir la preuve ?

Passages de référence : Dk01, Sg01.

## C543 — OLP-0051-B09

**Choix :** contiennent tous $o$

**Autre formulation envisagée :** L’intersection n’est pas vide, donc elle contient o.

**Motif :** La propriété d’appartenance découle de la présence du même o dans chaque membre de la famille. Tous porte sur les ensembles intersectés. La justification et le renvoi restent séparés du point suivant.

**Confiance et limites :** Forte: la non-vacuité seule n’établirait pas l’appartenance du point spécifié.

**Question de révision :** La phrase rend-elle visible la portée de tous sans répétition supplémentaire ?

Passages de référence : Dk01.

## C544 — OLP-0051-B10

**Choix :** Si $X\subseteq A$ contient $o$ ; puisque $X$ est stable ; Ainsi

**Autre formulation envisagée :** La stabilité de chaque X entraîne celle de l’intersection, sans détailler le passage par x.

**Motif :** Le raisonnement est mené pour une partie admissible quelconque, puis appliqué à toutes: x appartient à chaque X et sa stabilité y place f(x). La conclusion est l’appartenance à l’intersection. Le rôle du domaine est explicite.

**Confiance et limites :** Forte: la chaîne complète de la preuve est conservée et la conclusion ne suppose aucun choix de X privilégié.

**Question de révision :** Faut-il écrire pour toute partie X avant la condition, ou l’implication actuelle suffit-elle ?

Passages de référence : Dk01, Sg01.

## C545 — OLP-0051-B11

**Choix :** le fait général ; $\bigcap C \subseteq X$

**Autre formulation envisagée :** La minimalité est évidente.

**Motif :** La troisième clause utilise la propriété générale d’une intersection, exactement comme OLP. Dans l’application C est la famille non vide déjà construite; aucun nouvel axiome n’est affirmé.

**Confiance et limites :** Forte: l’alternative supprimerait la raison précise donnée par la source.

**Question de révision :** Le nom C introduit ici doit-il être rappelé comme une famille d’ensembles ?

Passages de référence : Dk01.

## C546 — OLP-0051-B12

**Choix :** maintenant donner la définition suivante

**Autre formulation envisagée :** Cela prouve l’existence d’une algèbre de Dedekind.

**Motif :** La transition lie la définition d’algèbre aux propriétés de clôture démontrées. Elle ne présente pas encore un nouveau résultat d’existence.

**Confiance et limites :** Forte: le théorème d’existence ne vient qu’ensuite et reste conditionnel.

**Question de révision :** La transition conserve-t-elle assez clairement Using this sans répétition ?

Passages de référence : Dk01, Dk02.

## C547 — OLP-0051-B13

**Choix :** muni d'une application ; et d'un élément ; $A = \closureofunder{f}{o}$

**Autre formulation envisagée :** Un ensemble A satisfaisant les trois propriétés, sans préciser la donnée de f et o.

**Motif :** Muni de décrit la structure composée de l’ensemble, de l’application et du point distingué. Les trois conditions demeurent intégrales et dans le même ordre. Le terme algèbre est celui défini par OLP, sans identité historique de terminologie revendiquée.

**Confiance et limites :** Forte: la donnée structurale est nécessaire; Dk02 fournit le contenu correspondant avec point initial1.

**Question de révision :** Faut-il appeler explicitement o point distingué dans l’index, sans modifier la définition source ?

Passages de référence : Dk02, Sg01.

## C548 — OLP-0051-B14

**Choix :** manifestement infinie au sens ; permet de
construire ; une partie de l'ensemble infini donné

**Autre formulation envisagée :** Tout ensemble infini au sens de Dedekind peut être muni d’une telle structure.

**Motif :** Le lien de la clôture à la plus petite partie et les deux clauses d’infinité sont restaurés. La phrase source can be turned into pourrait porter sur tout D; le théorème72 de Dedekind et la preuve OLP ne donnent qu’une partie. La note distingue cette correction du simple travail de traduction.

**Confiance et limites :** Forte: une orbite engendrée par un seul point ne peut couvrir un ensemble non dénombrable; l’existence de la partie suffit au théorème.

**Question de révision :** La note doit-elle citer§72 directement, ou le dossier de provenance suffit-il pour ce commentaire éditorial ?

Passages de référence : Dk01, Dk02, Sg01.

## C549 — OLP-0051-B15

**Choix :** S'il existe ; alors il existe

**Autre formulation envisagée :** Il existe une algèbre de Dedekind.

**Motif :** Les deux quantifications existentielles et leur conditionnalité sont maintenues. Le théorème ne démontre pas encore qu’un ensemble infini existe.

**Confiance et limites :** Forte: l’alternative présupposerait exactement ce que la section suivante discutera.

**Question de révision :** L’énoncé conditionnel se distingue-t-il assez clairement de la discussion historique à venir ?

Passages de référence : Dk02.

## C550 — OLP-0051-B16

**Choix :** $A$ existe et $o \in A$ ; une application de $A$ dans $A$ ; le triplet

**Autre formulation envisagée :** Poser f=g restreinte à A et affirmer aussitôt que c’est une algèbre.

**Motif :** La clôture dans D donne A et son point; sa stabilité permet de restreindre g en une application A→A. Ce contrôle de codomaine, implicite dans OLP, est rendu visible. Le reste du paragraphe annonce les trois vérifications, sans les remplacer par une assertion globale.

**Confiance et limites :** Forte: le codomaine A résulte de la stabilité déjà démontrée, sans circularité avec la troisième clause.

**Question de révision :** L’emploi de triplet rend-il comprise la notation source A,f,o sans parenthèses ?

Passages de référence : Dk01, Dk02, Sg01.

## C551 — OLP-0051-B17

**Choix :** par conséquent ; $o\notin\ran{f}$

**Autre formulation envisagée :** o n’est pas atteint, par définition de f.

**Motif :** Le point n’appartient pas à l’image de g; l’image de sa restriction est incluse dans celle de g. Ces deux prémisses sont toutes deux conservées avant la conclusion.

**Confiance et limites :** Forte: la conclusion dépend aussi du choix de o, pas seulement de f.

**Question de révision :** Le lien d’inclusion des images doit-il être développé ailleurs dans les exercices ?

Passages de référence : Dk02.

## C552 — OLP-0051-B18

**Choix :** sa restriction ; elle aussi injective

**Autre formulation envisagée :** f est injective parce que A est une partie de D.

**Motif :** Une restriction conserve l’injectivité. Le texte garde f⊆g comme inclusion de graphes, convention établie par la source, et distingue cette inclusion de celle des domaines.

**Confiance et limites :** Forte: il faut que f soit précisément la restriction de l’injection g, pas une application quelconque sur A.

**Question de révision :** L’inclusion de graphes f⊆g reste-t-elle lisible avec le vocabulaire restriction ?

Passages de référence : Dk02.

## C553 — OLP-0051-B19

**Choix :** comme c'est une partie de $A$ ; elle est également stable par $g$ ; Puisqu'elle contient $o$ ; Les deux inclusions

**Autre formulation envisagée :** La clôture sous f est celle sous g puisque f est une restriction.

**Motif :** Les deux minimalités sont appliquées dans leurs ambiants respectifs A et D. Pour transférer la stabilité de f à g, la clôture doit être incluse dans A, où f et g coïncident; la présence de o justifie ensuite la seconde inclusion. Tous les renvois originaux sont maintenus.

**Confiance et limites :** Forte: la restriction seule ne suffit pas sans contrôler le domaine et la stabilité; les étapes ajoutées rendent cette dépendance explicite.

**Question de révision :** La dernière phrase est-elle utile après l’affichage des deux inclusions ?

Passages de référence : Dk01, Dk02, Sg01.

## C554 — OLP-0052-B04

**Choix :** Récurrence arithmétique

**Autre formulation envisagée :** Induction arithmétique

**Motif :** Le français récurrence est attesté dans le rappel de Lyon et le développement de Sage. Le titre garde les deux sujets de la source et son titre court, sans confondre le principe de preuve avec une définition de fonction.

**Confiance et limites :** Forte pour l’usage natif consulté; induction est possible mais moins cohérent avec ces témoins.

**Question de révision :** L’index devrait-il donner induction comme terme de renvoi seulement ?

Passages de référence : L20, Sg02, Dk03.

## C555 — OLP-0052-B05

**Choix :** \emph{quelle qu'elle soit} ; tenir lieu d'ensemble ; conséquence immédiate

**Autre formulation envisagée :** Une algèbre particulière donne une imitation des naturels.

**Motif :** L’universalité any est accentuée, le rôle de surrogate devient tenir lieu, et trivial qualifie la facilité de la conséquence, non son insignifiance. On ne réduit pas la phrase à la seule existence d’une algèbre.

**Confiance et limites :** Forte: l’alternative perd l’universalité et suggère un statut mathématique inférieur.

**Question de révision :** Tenir lieu exprime-t-il clairement une représentation structurale plutôt qu’un remplacement approximatif ?

Passages de référence : Dk02, Dk03, Sg02.

## C556 — OLP-0052-B06

**Choix :** Pour tout ensemble $X$ ; N \cap X ; $N \subseteq X$

**Autre formulation envisagée :** Pour toute partie X de N, les mêmes conditions impliquent X=N.

**Motif :** X reste un ensemble quelconque; la transmission ne porte que sur N∩X. Le français si… et… alors conserve l’ordre logique et le cadre typographique de la source.

**Confiance et limites :** Forte: l’alternative est équivalente après reformulation, mais rétrécirait l’énoncé écrit et masquerait sa portée originale.

**Question de révision :** La disposition centrée suffit-elle à rendre les deux hypothèses et la conclusion visibles ?

Passages de référence : Dk03, Sg02, L20.

## C557 — OLP-0052-B07

**Choix :** $Y=N\cap X$ ; $s(n)\in N$ ; $N=\closureofunder{s}{o}\subseteq Y\subseteq X$

**Autre formulation envisagée :** X est stable par s, donc il contient la clôture.

**Motif :** La preuve source applique la clôture à X sans traiter les éléments hors N. On introduit Y=N∩X, qui contient o; s(n) reste dans N par le codomaine et dans X par l’hypothèse. La minimalité dans N donne la conclusion. La note révèle la précision.

**Confiance et limites :** Forte: s n’est pas défini hors N; la preuve de stabilité de Y vérifie les deux appartenances requises.

**Question de révision :** L’explicitation de la source est-elle mieux placée en note ou dans la seule preuve ?

Passages de référence : Dk01, Dk03, Sg02.

## C558 — OLP-0052-B08

**Choix :** n'importe quel ensemble ; former une algèbre ; représenter les entiers naturels

**Autre formulation envisagée :** Tout ensemble infini est l’ensemble des naturels.

**Motif :** Le bilan maintient les deux étapes ensemble infini → algèbre → représentation des naturels. Le verbe représenter développe surrogate sans identifier littéralement tous les codages d’entiers.

**Confiance et limites :** Forte: la conclusion source est structurale et conditionnelle, non une égalité ensembliste.

**Question de révision :** Le rapport entre caractérise et les autres axiomes de l’algèbre est-il clair dans le contexte immédiat ?

Passages de référence : Dk02, Dk03, Sg02.

## C559 — OLP-0052-B09

**Choix :** Certes ; \emph{ensemblistes} ; peut-être plus familière

**Autre formulation envisagée :** Le théorème précédent est trop abstrait; donnons une version simple.

**Motif :** La concession conserve admittedly et la modalité might. Le passage annonce une présentation par formule de la même récurrence; il ne suggère ni nouveau théorème plus fort ni baisse du niveau mathématique.

**Confiance et limites :** Forte: l’alternative ajouterait un jugement dépréciatif et effacerait la nuance d’adresse au lecteur.

**Question de révision :** Peut-être plus familière rend-il la modalité sans affaiblir l’équivalence des présentations ?

Passages de référence : Sg02, L20.

## C560 — OLP-0052-B10

**Choix :** Pour toute formule ; éventuellement avec des paramètres

**Autre formulation envisagée :** Pour toute propriété sans paramètre.

**Motif :** La quantification sur les formules et l’autorisation de paramètres sont intégrales. Les témoins français attestent le schéma de récurrence; Pt01 contient une définition avec paramètre, mais aucune attestation du syntagme français avec des paramètres n’est revendiquée ici. L’explication détaillée reste gouvernée par OLP.

**Confiance et limites :** Forte sur la portée formelle; choix avec plutôt que munie de est stylistique et explicitement sans attestation spécialisée précise.

**Question de révision :** Avec des paramètres ou à paramètres convient-il mieux à la terminologie des chapitres de théorie des modèles ?

Passages de référence : Sg02, L20, Pt01.

## C561 — OLP-0052-B11

**Choix :** Posons ; $X = \Setabs{n \in N}{\phi(n)}$ ; appliquons le théorème

**Autre formulation envisagée :** La propriété φ est stable, donc le résultat est évident.

**Motif :** La preuve construit la partie définie par la formule et applique la récurrence ensembliste. Elle reste distincte de la définition par récurrence des opérations, qui viendra ensuite.

**Confiance et limites :** Forte: l’ensemble X est le pont explicite entre les deux formulations.

**Question de révision :** Le cadre naïf donné auparavant suffit-il à justifier ici la partie définie, avant l’étude formelle de la séparation ?

Passages de référence : Dk03, Sg02.

## C562 — OLP-0052-B12

**Choix :** pour des objets quelconques ; toutes les variables libres ; explicitement indiquées ; beaucoup
plus faciles à lire

**Autre formulation envisagée :** Dire simplement que la formule peut dépendre de c1…ck et omettre la clause sur toutes les variables libres.

**Motif :** Le texte complet conserve l’explication approximative avec objets c1…ck, puis la version précise dont toutes les variables libres sont affichées, la fermeture universelle et le renvoi futur. Les deux témoins français gouvernent seulement le registre du schéma; le traitement détaillé des paramètres vient de la source OLP. Aucune attestation native supplémentaire n’est fabriquée.

**Confiance et limites :** Forte: la clause de complétude de la liste des variables est nécessaire pour la portée du schéma affiché; la collocation choisie reste révisable.

**Question de révision :** Les objets c_i devraient-ils être décrits comme valeurs de paramètres dans une future note, sans alourdir le présent passage ?

Passages de référence : Sg02, L20, Pt01.

## C563 — OLP-0052-B13

**Choix :** pas immédiat ; \emph{définition par récurrence} ; beaucoup plus loin ; un cadre bien plus général ; le moment venu

**Autre formulation envisagée :** On définit simplement les trois opérations de manière récursive.

**Motif :** L20 atteste la distinction entre démontrer et définir par récurrence. Pt01 est la référence originale citée pour les opérations. Le texte conserve la difficulté, le report de la justification, la généralisation future et les deux pistes de lecture. Les six équations sont reprises sans modifier ni exposants ni ordre des facteurs.

**Confiance et limites :** Forte: l’alternative abrégerait les précautions source et pourrait faire croire que l’existence des fonctions est déjà prouvée.

**Question de révision :** Définition par récurrence reste-t-il préférable à définition récursive dans toute la suite de cette édition ?

Passages de référence : L20, Pt01.

## C564 — OLP-0054-B04

**Choix :** une démonstration

**Autre formulation envisagée :** La démonstration définitive de Schröder–Bernstein

**Motif :** Le titre annonce une preuve parmi plusieurs, comme le précise le paragraphe suivant. Démonstration suit le titre de preuve natif de Lyon; ni la clôture ni un énoncé plus fort ne sont ajoutés au titre.

**Confiance et limites :** Forte : l'article indéfini conserve la pluralité explicite des preuves.

**Question de révision :** Harmoniser preuve et démonstration dans les titres sans perdre la variété naturelle ?

Passages de référence : L19, Pt02.

## C565 — OLP-0054-B05

**Choix :** naïve, mais élaborée ; Autrement dit ; il existe

**Autre formulation envisagée :** Une dernière preuve simple; les deux ensembles sont semblables.

**Motif :** Naïve renvoie à la théorie des ensembles et élaborée conserve sophisticated sans suggérer une preuve fausse. La double comparaison, les deux injections et l'existence d'une bijection restent exprimées; Lyon établit exactement cette équivalence.

**Confiance et limites :** Forte sur l'énoncé; élaborée est un choix de registre contextualisé, non une expression attribuée au canon.

**Question de révision :** Élaborée conserve-t-il mieux la nuance que subtile ?

Passages de référence : L19, Pt02.

## C566 — OLP-0054-B06

**Choix :** suit de près ; semblable
pour l'essentiel ; $\sqrt{2}$

**Autre formulation envisagée :** Remplacer ce paragraphe par une seule référence bibliographique.

**Motif :** La référence précise à Potter et l'invitation à consulter une variante sont gardées. L'analogie avec l'irrationalité de racine2 et l'existence de nombreuses preuves restent intégrales. Potter confirme l'architecture, mais ne constitue pas une attestation de la remarque sur le Web.

**Confiance et limites :** Forte sur la conservation de toutes les propositions; l'attribution historique à Dedekind est celle d'OLP, non une nouvelle revendication d'antériorité vérifiée ici.

**Question de révision :** Une note bibliographique historique sera-t-elle utile pour distinguer découverte et publication ?

Passages de référence : Pt02, Dk01, L19.

## C567 — OLP-0054-B07

**Choix :** $f\colon U\to U$ ; $B\subseteq U$ ; X\subseteq U ; plus petite partie ; y compris lorsque $B$ est vide

**Autre formulation envisagée :** L'intersection de tous les ensembles fermés, sans préciser le domaine de f.

**Motif :** L'endomap et l'ensemble ambiant bornent l'intersection comme chez Dedekind et dans le témoin français. La famille contient U, donc l'intersection est définie même pour B vide. Stable par est attesté; clôture conserve le terme OLP avec définition locale, sans prétendre une attestation native exacte de cette collocation.

**Confiance et limites :** Forte mathématiquement : le domaine et la non-vacuité de la famille sont explicitement vérifiés; terminologie clôture définie et révisable.

**Question de révision :** Clôture sous f doit-il devenir une entrée d'index avec le synonyme chaîne engendrée ?

Passages de référence : Dk01, Sg01.

## C568 — OLP-0054-B08

**Choix :** Pour toute application ; $X\subseteq U$ ; stable par

**Autre formulation envisagée :** Une partie minimale stable contenant B.

**Motif :** Les trois propriétés sont conservées avec leurs identifiants. Plus petite signifie incluse dans toute partie admissible, et non seulement minimale. Les domaines U des quantificateurs correspondent exactement à la définition précédente.

**Confiance et limites :** Forte : la troisième clause exprime la propriété de plus petit et conserve les deux hypothèses.

**Question de révision :** La répétition du cadre U facilite-t-elle la lecture autonome du lemme ?

Passages de référence : Dk01, Sg01.

## C569 — OLP-0054-B09

**Choix :** exactement la même

**Autre formulation envisagée :** C'est immédiat.

**Motif :** Le renvoi est conservé sans remplacer par un simple évident. La preuve de l'intersection stable s'applique à une partie initiale B aussi bien qu'à un point : chaque ensemble candidat contient B et les images de ses éléments.

**Confiance et limites :** Forte dans le cadre explicite U; le renvoi vise précisément les trois propriétés déjà prouvées.

**Question de révision :** Le lecteur identifiera-t-il facilement la substitution du point par la partie B ?

Passages de référence : Dk01.

## C570 — OLP-0054-B10

**Choix :** Un dernier résultat

**Autre formulation envisagée :** Une dernière information.

**Motif :** La transition annonce un lemme auxiliaire avant le théorème. Résultat rend fact dans le registre des preuves françaises; aucune notion ensembliste supplémentaire n'est impliquée.

**Confiance et limites :** Forte sur la fonction argumentative; choix discursif et non attestation textuelle exacte.

**Question de révision :** Résultat ou fait est-il préférable dans les transitions voisines ?

Passages de référence : Pt02, L19.

## C571 — OLP-0054-B11

**Choix :** $A \subseteq B \subseteq C$ ; $\cardeq{\cardeq{A}{B}}{C}$

**Autre formulation envisagée :** Si A et C ont même taille, toute partie B convient.

**Motif :** L'énoncé reprend l'intercalation et l'équipotence des extrêmes. La macro imbriquée garde la chaîne de comparaisons; Pt02 donne le même lemme. Aucun choix de représentants cardinaux n'est nécessaire.

**Confiance et limites :** Forte : les deux inclusions sont indispensables; le cas vide est également couvert.

**Question de révision :** Le rendu de la macro imbriquée doit être inspecté dans le futur lecteur intégré.

Passages de référence : Pt02, L19.

## C572 — OLP-0054-B12

**Choix :** comme une application de $C$ dans $C$ ; de domaine $C$ ; $\comp{f^{-1}}{g}\colon A\to B$

**Autre formulation envisagée :** Inverser les arguments de comp pour imiter visuellement l'écriture usuelle.

**Motif :** f:C→A est aussi une endomap de C grâce à A⊆C; la clôture F est donc bien définie. La définition par cas et les domaines sont intégraux. La composition inverse puis g suit la macro OLP comp{f}{g}=g∘f, vérifiée dans le fichier natif.

**Confiance et limites :** Forte : vérification directe du macro-code et des domaines C→A, A→C, C→B.

**Question de révision :** Le texte devra-t-il rappeler la convention d'ordre de composition ailleurs, plutôt qu'ici ?

Passages de référence : Pt02, Dk01.

## C573 — OLP-0054-B13

**Choix :** Supposons le contraire ; $y=g(y)=g(x)=f(x)$ ; $y=f(x)\in F$

**Autre formulation envisagée :** L'injectivité dans le cas mixte est évidente.

**Motif :** Le cas mixte est traité par contradiction : y est hors F, mais la stabilité impose f(x) dans F. Le renvoi à la clôture et toute la chaîne d'égalités sont préservés. Potter ne détaille pas ce raisonnement; la version OLP le gouverne.

**Confiance et limites :** Forte : la contradiction dépend exactement de la stabilité, pas de la seule injectivité de f.

**Question de révision :** Le renvoi global Closureprops est-il suffisant sans préciser sa deuxième clause ?

Passages de référence : Pt02, Dk01.

## C574 — OLP-0054-B14

**Choix :** si et seulement si ; $f(x)=g(x)=g(y)=f(y)$ ; Dans les deux cas

**Autre formulation envisagée :** g est injective puisque f l'est.

**Motif :** Le cas mixte exclu donne la même appartenance à F pour x et y, puis les deux cas donnent x=y. L'injectivité de f découle de sa bijectivité. Les deux chaînes originales restent complètes.

**Confiance et limites :** Forte : l'alternative ne traiterait pas les points où g est l'identité ni le cas mixte.

**Question de révision :** La répétition de x=y rend-elle utile la conclusion finale ?

Passages de référence : Pt02, L19.

## C575 — OLP-0054-B15

**Choix :** $\ran{g}\subseteq B$ ; $g(z)=f(z)\in A\subseteq B$ ; $F\setminus\{x\}$ ; l'absence supposée d'antécédent ; l'inclusion réciproque

**Autre formulation envisagée :** Montrer seulement que chaque x de B a un antécédent et conclure ran g=B.

**Motif :** On explicite d'abord l'inclusion d'image dans B, omise dans l'argument développé d'OLP : sur F, l'image est dans A; hors F, le point n'est pas dans C moins B. Pour l'autre inclusion, retirer x appartenant à B préserve C moins B. Sans antécédent de x dans F, cette partie resterait stable, contredisant le caractère de plus petit de F. L'addition est signalée en note et toute la preuve originale demeure.

**Confiance et limites :** Forte : deux inclusions contrôlées, sans choix d'une suite ni hypothèse de non-vacuité de B.

**Question de révision :** Minimalité est-il suffisamment précis après l'énoncé explicite de la propriété de plus petit ?

Passages de référence : Pt02, Dk01, Sg01.

## C576 — OLP-0054-B16

**Choix :** inclus dans son domaine ; $\funimage{h}{D}=\Setabs{h(x)}{x\in D}$

**Autre formulation envisagée :** Pour tout ensemble D, sans condition sur le domaine.

**Motif :** Le rappel de l'image conserve la formule. On explicite que D est inclus dans le domaine pour que h(x) soit défini pour tout x de D; cette précision de portée sera recensée dans la revue, sans modifier la convention ni la preuve.

**Confiance et limites :** Forte dans la définition d'image utilisée par OLP; une autre définition par restriction au domaine demanderait une autre formule.

**Question de révision :** Faut-il rappeler cette convention une fois dans le chapitre des fonctions plutôt que la répéter ?

Passages de référence : Pt02, L19.

## C577 — OLP-0054-B17

**Choix :** $\funimage{g}{\funimage{f}{A}}\subseteq g[B]\subseteq A$ ; par la définition de son codomaine ; $h\colon A\to\funimage{g}{B}$ ; $\comp{h}{g^{-1}}\colon A\to B$

**Autre formulation envisagée :** Traiter g comme bijection de B sur A et prendre son inverse sur tout A.

**Motif :** La composition est injective par les deux hypothèses, puis surjective sur l'image choisie pour codomaine. Le lemme auxiliaire s'applique aux trois ensembles imbriqués. L'inverse de g est restreint à g[B] et la composition finale va de A vers B. Les citations de lemme et marqueurs sont conservés; aucune surjectivité de g:B→A n'est supposée.

**Confiance et limites :** Forte : domaines, images et ordre des compositions concordent avec Pt02 et le macro-code source.

**Question de révision :** La précision explicite de l'inverse défini sur l'image est-elle assez visible dans cette dernière phrase ?

Passages de référence : Pt02, L19.

## C578 — OLP-0049-B04

**Choix :** Ensembles infinis

**Autre formulation envisagée :** Ensembles de nombres infinis

**Motif :** Titre descriptif conservé. Ensemble est le vocabulaire français déjà établi et infini qualifie l'ensemble, pas chacun de ses éléments. L'étiquette plus précise au sens de Dedekind sera définie dans la première section.

**Confiance et limites :** Forte : l'alternative change l'objet et restreint indûment le chapitre aux nombres.

**Question de révision :** Le titre général s'articule-t-il clairement avec la définition particulière de Dedekind ?

Passages de référence : Sg03, Dk04.

## C579 — OLP-0049-B05

**Choix :** consacré aux ensembles infinis ; tiré de ; \emph{Open Set Theory}, de Tim Button

**Autre formulation envisagée :** Un chapitre de théorie des ensembles, sans nom d'auteur ni ouvrage.

**Motif :** L'attribution éditoriale originale est intégrale. Le titre de l'ouvrage demeure inchangé; il n'est ni francisé artificiellement ni présenté comme le titre de notre édition. Le canon natif porte seulement sur ensembles infinis, l'attribution vient exclusivement de la source OLP.

**Confiance et limites :** Forte sur la fidélité de l'attribution; tournure éditoriale courante, sans attestation prétendue dans Sage.

**Question de révision :** Le rendu editorial préserve-t-il effectivement ce crédit dans le futur chapitre intégré ?

Passages de référence : Sg03.

## C580 — OLP-0050-B03

**Choix :** L'hôtel de Hilbert

**Autre formulation envisagée :** Le paradoxe des chambres

**Motif :** Le titre conserve le nom de l'exemple historique. La traduction hôtel ne vise pas un établissement réel; les hypothèses qui suivent décrivent une expérience de pensée. Kragh confirme l'objet, sans constituer une autorité de formulation française.

**Confiance et limites :** Forte : l'alternative supprimerait le nom historique et ajouterait paradoxe au titre.

**Question de révision :** Conserver cette orthographe homogène dans l'index ?

Passages de référence : Kr01.

## C581 — OLP-0050-B04

**Choix :** supposer d'emblée l'existence ; les entiers naturels
eux-mêmes ; l'hiver 1924--1925 ; d'une manière quelconque ; [mais] ; au plus une personne ; une place pour un client qui vient d'arriver

**Autre formulation envisagée :** Omettre la justification initiale, écrire une personne à toutes les étapes et conserver une date précise non vérifiée.

**Motif :** Le problème est de caractériser l'infini sans présupposer les naturels; help ourselves ne décrit pas leur usage quotidien. La première étape et la restriction sur la formulation restent entières. La datation du cours est précisée avec une note explicite d'après les éditeurs; la séance n'est pas datée. Dans la première citation, exactement un client au départ et au plus une personne après échange sont distincts. L'arbitraire du réarrangement, les crochets [mais], les ellipses et l'impossibilité d'une place pour une arrivée sont tous préservés.

**Confiance et limites :** Forte sur les quantificateurs et la portée; la notice primaire justifie l'intervalle1924–25, pas le jour. L'intégralité de la citation anglaise OLP gouverne notre français.

**Question de révision :** Supposer d'emblée l'existence rend-il clairement l'engagement ontologique sans surcharger l'introduction ?

Passages de référence : Dk04, Sg03, Es01, Kr01.

## C582 — OLP-0050-B05

**Choix :** chacune occupée par exactement
un client ; chacun des clients déjà présents ; supérieur d'une unité ; sera libre pour le
client qui vient d'arriver ; d'après la traduction anglaise ; définir ce que
cela signifie ; anachronisme considérable

**Autre formulation envisagée :** Résumer la citation par déplacer tout le monde; indiquer traduction française sans identifier le relais; supprimer l'anachronisme.

**Motif :** La seconde citation garde l'infinité numérotée, l'occupation unique initiale, le déplacement de chaque ancien client et la place libérée pour le nouvel arrivant. Les chiffres et le schéma TikZ intégral sont conservés. La mention de traduction décrit honnêtement le relais anglais d'OLP; aucun accès au texte allemand de730 n'est revendiqué. La conclusion conserve la définition suggérée par l'exemple et l'anachronisme appuyé, avec la date bibliographique de Dedekind. Le passage Kragh confirme le déplacement, mais ses ajouts sur plusieurs arrivées et la danse restent hors de notre extrait.

**Confiance et limites :** Forte : vérification complète des deux états d'occupation et du schéma; le statut du texte traduit est explicite.

**Question de révision :** Une future consultation de l'édition allemande permettra-t-elle de vérifier les deux citations directement sans modifier leur périmètre ?

Passages de référence : Kr01, Dk04, Sg03.

## C583 — OLP-0050-B06

**Choix :** infini au sens de Dedekind ; si et seulement ; une partie propre de~$A$ ; $o \in A$ ; $f \colon A \to A$ ; $o \notin \ran{f}$

**Autre formulation envisagée :** Un ensemble infini s'il est en bijection avec lui-même; omettre propre ou o∈A.

**Motif :** La définition exige une injection dans une partie propre, puis donne la forme équivalente d'une endomap injective qui omet un élément. Dedekind§64 et sa note20 donnent ces deux formes; Sage fournit le français de l'injectivité et de la non-atteinte. La locution au sens de Dedekind explicite l'adjectif anglais sans revendiquer une occurrence textuelle native consultée. Elle préserve une qualification mathématique distincte de l'infini en l'absence du choix.

**Confiance et limites :** Forte : propre et o∈A sont indispensables; l'équivalence passe par l'image propre de f, et non sa seule injectivité.

**Question de révision :** Infini au sens de Dedekind doit-il rester la forme développée partout, avec Dedekind-infini seulement en renvoi d'index ?

Passages de référence : Dk04, Sg03.

## C584 — OLP-0053-B04

**Choix :** La « preuve » de Dedekind ; l'existence d'un ensemble infini

**Autre formulation envisagée :** La preuve de l'infini

**Motif :** Le titre conserve les guillemets de réserve autour de preuve, son titre court et l'objet précis de la tentative. On ne transforme pas le titre en affirmation d'un théorème valide.

**Confiance et limites :** Forte : guillemets et existence d'un ensemble sont nécessaires à la lecture critique qui suit.

**Question de révision :** Les guillemets français rendent-ils assez visible la réserve dans la table des matières ?

Passages de référence : Dk04.

## C585 — OLP-0053-B05

**Choix :** traitement ensembliste ; entre autres ; portée philosophique

**Autre formulation envisagée :** Supprimer entre autres et renvoyer à une section arith/ref inexistante.

**Motif :** Le cadre ensembliste, le moyen des algèbres et among other things sont tous conservés. R01 atteste arithmétisation de l'analyse; portée exprime significance dans cette discussion, sans prétendue attestation exacte de toute la phrase. Le premier renvoi source était incomplet; il est rétabli vers l'identifiant natif sfr/arith/ref et une note signale la correction.

**Confiance et limites :** Forte : vérification directe du fichier reflections.tex et de son olfileid; les deux réflexions philosophiques restent distinctes.

**Question de révision :** La note de renvoi est-elle mieux regroupée avec les corrections éditoriales lors d'une future édition intégrale ?

Passages de référence : R01, R02.

## C586 — OLP-0053-B06

**Choix :** construire explicitement les entiers relatifs ; pas donné de construction explicite ; quel qu'il soit ; exactement comme nous souhaitons

**Autre formulation envisagée :** Ici, nous n'avons pas construit les naturels; un ensemble infini particulier imite N.

**Motif :** La comparaison oppose les deux méthodes exposées, sans affirmer que toute construction des naturels serait impossible. Given any est intégral : n'importe quel ensemble infini au sens de Dedekind suffit à la construction conditionnelle. Entiers relatifs distingue integers des naturals en français.

**Confiance et limites :** Forte : explicite, universalité et condition d'infinité sont trois qualifications indépendantes de la source.

**Question de révision :** La répétition d'explicite suffit-elle à prévenir une lecture ontologique excessive ?

Passages de référence : Dk02, Dk04, Dk06.

## C587 — OLP-0053-B07

**Choix :** question métaphysique ; $\Real$ comme ensemble des coupures ; une convention commode ; \emph{toute} ; isomorphes ; de nombreux « structuralistes »

**Autre formulation envisagée :** Réduire la thèse à toutes ces structures ont le même nombre d'éléments, ou supprimer la remarque philosophique.

**Motif :** La question d'identité des objets reste une question possible parmi d'autres. La définition de Real par les coupures est une convention qui possède les propriétés requises, pas une découverte ontologique. Toute algèbre a les mêmes propriétés; l'isomorphisme conserve base et successeur, comme le montrent les §§132–133 consultés. La remarque sur les structuralistes demeure celle d'OLP; aucune enquête nouvelle n'est revendiquée. Convention commode est un choix explicatif révisable, non une citation française du canon.

**Confiance et limites :** Forte sur le contraste conceptuel et l'isomorphisme; moyenne sur la préférence convention/stipulation en français, explicitement non attestée mot pour mot ici.

**Question de révision :** Stipulation commode conviendrait-il mieux dans un registre philosophique plus technique tout en restant clair ?

Passages de référence : Dk06, R01, R02.

## C588 — OLP-0053-B08

**Choix :** ne semble pas présupposer ; peut-être ; rien de ce qui est susceptible d'être démontré ; même dans les
méthodes les plus récentes ; des notions ou des intuitions de l'espace et du temps ; lois pures de la pensée ; au sens étendu

**Autre formulation envisagée :** Abréger la préface avec une ellipse; affirmer une réduction déjà accomplie à la logique du premier ordre.

**Motif :** Le paragraphe conserve les modalités apparently et may. La citation de préface est restituée intégralement : exigence de preuve, jugement sur les fondements récents, théorie des nombres comme partie de la logique, parenthèse algèbre/analyse, indépendance de l'espace et du temps, produit immédiat des lois pures. Le bilan garde les deux étapes de construction et la restriction au sens étendu de logique chez Dedekind; aucune réduction au calcul du premier ordre n'est suggérée. Intégrer traduit embed ici comme mise en théorie, sans introduire un plongement de structures non défini.

**Confiance et limites :** Forte : comparaison de l'extrait anglais OLP avec Beman et le paragraphe allemand réellement disponible. R02 fournit le registre français et la distinction entre degrés de logique, sans aval général au logicisme.

**Question de révision :** Notions ou représentations serait-il plus proche de Vorstellungen sans s'écarter inutilement de notions dans OLP ?

Passages de référence : Dk05, Dg01, R02, R01.

## C589 — OLP-0053-B09

**Choix :** arrêtons-nous un instant ; tient lieu ; subordonnée à l'existence ; le projet ne peut aboutir

**Autre formulation envisagée :** Dire que les entiers naturels n'existent pas tant qu'on n'a pas prouvé cette condition.

**Motif :** La mise en garde rétablit la condition d'existence laissée provisoirement implicite dans le bilan précédent. Le renvoi précis à la construction reste présent. La conséquence porte sur le projet de réduction logique si l'infini n'est pas établi ainsi, pas sur toute l'arithmétique.

**Confiance et limites :** Forte : la portée conditionnelle et la cible du projet sont explicites.

**Question de révision :** Ne peut aboutir traduit-il mieux stalls que est dans une impasse, sans suraffirmer une impossibilité absolue ?

Passages de référence : Dk02, Dk04, Dk05.

## C590 — OLP-0053-B10

**Choix :** \emph{peut-elle} ; toutes
les choses qui peuvent être des objets ; la pensée $s'$ ; une image $\phi(s)$ ; infini [au sens de Dedekind] ; pour une grande part

**Autre formulation envisagée :** Supprimer la question et lire s' comme la chose s elle-même; ajouter sans indication tout le §66.

**Motif :** La question initiale, la tentative citée et le jugement qui suit sont tous restaurés. La possibilité porte sur les objets de pensée; la pensée que s peut être un objet est elle-même dans S. L'ellipse appartient au périmètre OLP et n'est pas comblée par l'argument intégral de §66. Les crochets conservent l'ajout éditorial Dedekind. L'ouvrage consiste largement, pas exclusivement, en preuves rigoureuses.

**Confiance et limites :** Forte : l'extrait est comparé au §66 complet mais conserve exactement son périmètre source.

**Question de révision :** Domaine de pensées rend-il realm sans la connotation spatiale excessive de royaume ?

Passages de référence : Dk04, Dk05.

## C591 — OLP-0053-B11

**Choix :** ce que nous reconnaîtrions
aujourd'hui ; objets
psychologiques ; pensées
\emph{possibles}

**Autre formulation envisagée :** C'est une preuve non mathématique fondée sur des pensées existantes.

**Motif :** La critique est située dans l'appréciation contemporaine de la mathematical character, avec hardly et non une condamnation absolue de tout l'ouvrage. Les objets psychologiques sont précisés comme pensées seulement possibles. Cette appréciation appartient à OLP; le canon original sert à vérifier son objet.

**Confiance et limites :** Forte : temporalité, modalité et seules possibilités sont toutes maintenues.

**Question de révision :** Le conditionnel reconnaîtrions restitue-t-il bien would now recognize ?

Passages de référence : Dk04, R02.

## C592 — OLP-0053-B12

**Choix :** du moins dans la présentation ; Si l'argument de Dedekind réussit ; seulement ; un seul \emph{ensemble} ; une infinité d'!!{element}s ; \emph{des choses}, au pluriel

**Autre formulation envisagée :** Toute infinité de pensées est automatiquement un ensemble infini.

**Motif :** La critique technique est conditionnelle et limitée à la présentation des algèbres adoptée par OLP. Même si l'argument démontre une pluralité infinie de choses, il faut encore une raison d'en faire un ensemble unique ayant ces éléments. Potter éclaire la distinction historique totalité/ensemble; on n'affirme pas que toute pluralité forme un ensemble.

**Confiance et limites :** Forte : l'alternative efface précisément la lacune identifiée. Le marqueur élément et l'infinité des membres sont conservés.

**Question de révision :** Des choses rend-il some things sans connotation d'une petite quantité que quelques choses pourrait introduire ?

Passages de référence : Dk04, Pt03.

## C593 — OLP-0053-B13

**Choix :** pourrait suggérer ; \emph{notre} emploi ; d'autres raisons ; dans les deux derniers chapitres ; selon les besoins ; exactement quels ensembles existent ; \emph{certains} principes généraux

**Autre formulation envisagée :** Conclure que Dedekind confondait les ensembles et supprimer le rappel des constructions.

**Motif :** Le diagnostic historique demeure tentative, et notre usage est contrasté avec celui de Dedekind. La note Potter donne d'autres raisons plutôt qu'une preuve définitive. Tout le bilan des deux chapitres est conservé, avec les trois systèmes construits, la naïveté des choix d'ensembles, le manque de principes précis et la nécessité d'en avoir sous peine du paradoxe de Russell. Le texte n'affirme pas que n'importe quels principes suffiraient.

**Confiance et limites :** Forte sur la modalité et l'intégralité du raisonnement; l'interprétation de Potter est identifiée comme son argument historique.

**Question de révision :** Dans quels cas exprime-t-il clairement when sans suggérer une existence temporelle des ensembles ?

Passages de référence : Pt03, R01, R02.

## C594 — OLP-0053-B14

**Choix :** dépasser notre naïveté

**Autre formulation envisagée :** Il faut maintenant apprendre une théorie plus facile.

**Motif :** La phrase conclut la démarche naïve et annonce la nécessité de principes généraux. Le possessif garde l'implication pédagogique du lecteur et de l'exposition. Le témoin français gouverne seulement le registre des fondements, pas cette métaphore particulière.

**Confiance et limites :** Forte sur la fonction argumentative; métaphore source conservée avec une formulation française révisable.

**Question de révision :** La transition reste-t-elle naturelle vers le prochain chapitre axiomaticien ?

Passages de référence : R02.
