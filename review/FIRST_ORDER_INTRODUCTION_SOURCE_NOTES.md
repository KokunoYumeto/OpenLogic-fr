# Lecture de la source — introduction à la logique du premier ordre

Lot OLP-0139–OLP-0148, révision source `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`.

Les dix unités ont été lues intégralement avant et après rédaction. Le pilote OLP-0139 importe neuf sections. Le chapitre présente le langage du premier ordre, définit inductivement ses formules, introduit structures et assignations de variables, puis explique satisfaction, énoncés clos, validité, conséquence logique et satisfaisabilité. Les dernières sections motivent la substitution, la théorie des modèles, la méthode axiomatique et les théorèmes de correction et de complétude.

Le canon français FR-IRIF-SCHMITZ-2022 a été relu sur les pages PDF 12–13 pour les termes, formules et variables libres ou liées; sur les pages 15–18 pour structures, domaines, assignations, satisfaction, modèles, validité et conséquence logique; et sur les pages 29–31 pour substitution, applicabilité, alpha-renommage et lemme de substitution. Les passages indexés SCH09, SCH10 et SCH12–SCH14 ont effectivement guidé ce lot. Les conventions formelles et la notation d’OpenLogic restent celles de la source traduite.

Défauts source repérés, réparés et déclarés dans la traduction :

- OLP-0140 ferme, dans trois occurrences, le corps de `\lforall` après toute la conséquence logique au lieu de le fermer après la conditionnelle; les trois formules universelles visées sont rétablies.
- OLP-0143 attribue plusieurs places aux constantes, alors que le contexte et la définition formelle exigent « prédicats ».
- OLP-0143 fixe le domaine à `{0,1,2}`, puis affirme que l’assignation prend ses valeurs parmi `{1,2,3}`; le second ensemble est rétabli en `{0,1,2}`.
- OLP-0146 donne des limites d’arguments incompatibles aux macros `\Atom` et `\lforall` de sa première formule; la formule universelle décrite par la phrase est rétablie.

Chaque réparation conserve l’énoncé mathématique manifestement visé et figure dans une note éditoriale locale.
