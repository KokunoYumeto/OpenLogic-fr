# Réaudit de qualité de trois chapitres

Date : 20 septembre 2026  
Modèle utilisé pour ce passage : GPT-5  
Décision : **conserver et réparer** ; aucune reprise intégrale n'est justifiée par l'échantillon demandé.

## Portée effectivement contrôlée

Neuf pages physiques du lecteur français publié ont été contrôlées, trois par chapitre, en prenant une page au début, au milieu et vers la fin de chaque chapitre. L'échantillon contient 3 916 mots délimités par des espaces.

| Chapitre | Pages physiques | Pages imprimées |
|---|---:|---:|
| Systèmes de preuve | 88, 91, 93 | 84, 87, 89 |
| Calcul des séquents | 95, 103, 109 | 91, 99, 105 |
| Déduction naturelle | 111, 119, 124 | 107, 115, 120 |

Chaque page a été comparée avec les sources TeX anglaises figées. Les termes français ont été contrôlés contre le canon local Saurin, Schmitz, Goubault-Larrecq et Mackie. Les neuf pages ont aussi été rendues à 170 ppp et inspectées à leur définition d'origine.

## Résultat

- Erreurs critiques : 0.
- Erreurs majeures : 0.
- Divergences mathématiques ou logiques : 0.
- Omissions : 0.
- Défauts de rendu, glyphes manquants, chevauchements ou rognages : 0.
- Réparations locales de prose ou de typographie : 5, dans 4 unités.

Les formules, arbres de preuve, étiquettes de règles, hypothèses, conclusions et citations n'ont pas changé.

## Constats page par page

- Page 88 : contenu fidèle. Les guillemets français ont été rendus insécables autour des termes cités et une phrase calquée sur l'anglais a été réécrite en français naturel.
- Page 91 : contenu fidèle. La condition de préservation de la vérité a été formulée comme une implication explicite.
- Page 93 : conforme. La précision éditoriale sur le contexte Gamma corrige utilement une formulation trop étroite de la source et ne modifie pas le résultat.
- Page 95 : conforme. Séquent, antécédent, conséquent, cas vides et concaténation sont exacts.
- Page 103 : conforme. Réflexivité, monotonie, transitivité, coupure, compacité et cohérence sont exactes ; les précisions sur le témoin fini et l'affaiblissement sont valides.
- Page 109 : conforme. Validité de la règle gauche de l'implication, corollaires et exercices sont exacts.
- Page 111 : contenu exact. L'anglicisme « tag » a été remplacé par « étiquette ».
- Page 119 : conforme. Définitions et preuve de compacité sont fidèles ; la remarque sur les contextes infinis et les dérivations finies est exacte.
- Page 124 : preuve exacte. Une note éditoriale a été reformulée pour parler au lecteur plutôt que d'exposer une commande d'implémentation.

## Vérification après réparation

Le lecteur de 126 pages a été recompilé sous la garde TeX. Le PDF réparé a l'empreinte SHA-256 `54d43d89074a4969ee4f08474eca30517df42a32a1133afcbcec923e14737388`. La comparaison intégrale de l'extraction mise en page montre que seules les pages physiques 88, 91, 111 et 124 ont changé. Ces quatre pages ont été rendues à nouveau et inspectées : aucun défaut visuel n'a été trouvé. Le journal ne contient ni débordement, ni référence indéfinie, ni section non marquée en français.

Le contrôle est l'échantillon de neuf pages demandé ; il ne prétend pas remplacer une nouvelle collation ligne à ligne de chaque page des trois chapitres. Il suffit toutefois à rejeter l'hypothèse d'une traduction globalement défaillante et à autoriser la poursuite du travail à partir de l'unité OLP-0098.
