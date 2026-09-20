# Lecture de la source — dérivations axiomatiques

Lot OLP-0112–OLP-0125, révision source \`9620cc73f9c8e0ad003c514a5d3748f29611c4c0\`.

Les quatorze unités ont été lues intégralement avant rédaction. Le chapitre définit les dérivations comme suites finies d’axiomes, d’hypothèses et de conséquences de lignes antérieures; sa règle propositionnelle est le modus ponens. Il fixe quatorze schémas d’axiomes propositionnels, deux schémas quantifiés et deux règles quantifiées avec condition de fraîcheur. Les exemples construisent trois dérivations propositionnelles et une dérivation quantifiée. Les sections métalogiques définissent dérivabilité, théorème et cohérence, puis établissent réflexivité, monotonie, transitivité, compacité, théorème de la déduction, propriétés des connecteurs, généralisation forte et correction.

Le passage français GL01 (§3.1, définition 11) a été relu pour la terminologie d’un système de Hilbert, d’une suite finie, des axiomes, hypothèses et règles. GL02 a été relu pour correction, cohérence et complétude. Le passage nouvellement indexé GL04 (§3.1, théorème 15 et paragraphes suivants) atteste « théorème de la déduction », l’équivalence entre ajout d’une hypothèse et implication, ainsi que le commentaire sur la difficulté de lire les preuves hilbertiennes. Les conventions formelles de cette source française ne remplacent pas celles d’OpenLogic.

Défauts source repérés et déclarés dans la traduction :

- OLP-0115 place deux commandes \`\\item\` hors de tout environnement de liste;
- OLP-0118 limite par inadvertance la preuve de compacité au modus ponens alors que la version FOL admet aussi les règles quantifiées;
- OLP-0119 omet une parenthèse fermante dans le premier fait de dérivabilité;
- OLP-0120 omet une parenthèse et conclut \`Γ ⊢ B\` là où son calcul prouve \`Γ ⊢ A → B\`;
- OLP-0122 cite deux fois l’axiome de projection gauche, puis cite le mauvais axiome de négation;
- OLP-0123 invoque une seconde fois le théorème de la déduction là où il faut utiliser l’axiome \`⊤\` et le modus ponens;
- OLP-0124 omet le marqueur de formule devant deux occurrences de \`B\`;
- OLP-0125 énonce des conséquences pour des termes quelconques alors que ses schémas d’axiomes viennent d’être restreints aux termes clos.

Chaque réparation conserve le résultat mathématique manifestement visé et fait l’objet d’une note éditoriale locale.
