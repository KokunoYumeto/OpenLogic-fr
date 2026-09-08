# État de cette pièce dans la livraison 0.4

Les observations datées ci-dessous conservent le contexte de leur rédaction. Les 37 unités sont désormais intégrées et le lecteur actuel est validé ; voir provenance/QA.json et review/RELEASE_REVIEW.md pour l’état final. Les mentions de brouillons ou de contrôles encore à venir décrivent les étapes antérieures, pas un travail suspendu. Les hashes intermédiaires sont historiques ; provenance/ALIGNMENT.jsonl contient les identités finales.

# Source observations, first sets chapter

Authority: OpenLogicProject/OpenLogic, revision 9620cc73f9c8e0ad003c514a5d3748f29611c4c0. Source files remain byte-for-byte unchanged under upstream.

- OLP-0008, unions-and-intersections.tex, definition of the intersection of a set of sets: the source does not require A to be nonempty. If A is empty, the displayed universal condition holds for every object; in unrestricted set theory it cannot define a set. The French text adds the nonempty hypothesis and explicitly distinguishes intersection relative to a fixed ambient U. Evidence: source definition, OLP-0010's Russell argument; Lyon printed p.2–3 on existence and comprehension; Habermehl slide 8 explicitly fixes U.
- OLP-0005, basics.tex, closing sentences of the perfect-number example: the claim that extensionality guarantees that there is always one such set overstates existence. OLP-0010 immediately supplies the correct conditional reading. French adds “au plus” and “s’il existe”, with a visible editorial note.
- OLP-0006, subsets.tex, first example: the negative inclusion involving e requires e to be outside {a,b,c}. Taking e=a is an immediate counterexample. The French text makes only this needed assumption explicit and identifies the addition.
- OLP-0005, basics.tex, perfect-number definition: the domain and positivity of the proper divisors are implicit. The worked sum 1+2+3 fixes the intended positive-divisor reading. French makes the positive-integer domain explicit in an editorial footnote; this is a clarification rather than a changed theorem.

These are local editorial repairs. No upstream issue has been submitted, and no external source authority has been substituted for OLP.

Further bounded chapter review:

- OLP-0008-B15: the common-elements example needs c≠d (a sufficient hypothesis); c=d outside {a,b} gives a counterexample. Applied with a visible note after manager review.
- OLP-0008-B22: the three-set-family example needs b≠d (a sufficient hypothesis); b=d outside {a} gives a counterexample. Applied with a visible note after manager review.
- OLP-0008-B14: the illustrative empty intersection assumes a, b, c are all different from 0 and 1. This is now stated locally and disclosed.
- OLP-0009-B18: for arbitrary alphabets, identifying an alphabet symbol with its one-letter word and using the empty set for the empty word is not injective when the alphabet contains the empty set. The original displayed union is preserved, explicitly described as the set of untagged representations; an editorial note explains that attaching each word's length repairs the representation. Fixed-length nested-pair encodings themselves remain unchanged.

# Relations chapter: verified local observations

Paths below are relative to the frozen `content/sets-functions-relations/relations/` directory. Exact source/target SHA-256 values are in RELATIONS_STRUCTURAL_QA.json. No upstream issue submitted.

- OLP-0012, relations-as-sets.tex:98–100: I is used in K=L∪I and H=G∪I after defining Id_A, without defining I. French defines I=Id_Nat locally, with a note, preserving the example formulas.
- OLP-0014, special-properties.tex:79–83: existence of a relation neither reflexive nor irreflexive needs a domain of at least two elements. On a singleton only the empty relation and identity exist, and on the empty domain the unique relation is both reflexive and irreflexive. French explicitly restricts that existence statement and notes the reason. This does not change the separate statement that asymmetry implies antisymmetry.
- OLP-0015, equivalence-relations.tex:25–28 and 40: classes are blocks of one partition, not themselves the different partitions. French corrects this terminology with a note. At line 65, the phrase placing a, b and n in PosInt leaves the later natural-number quotient and zero class outside the stated domain. French specifies a,b in Nat and n in PosInt, with a note; the integer multiplier k and congruence formula are unchanged.
- OLP-0016, orders.tex:78–79: the prefix order on A* is non-linear only when A has at least two distinct symbols. Empty and singleton alphabets give linear orders. French scopes the claim and discloses the small-alphabet cases, using genuine finite sequences distinguished by length as the first chapter's coding note already requires.
- OLP-0018, trees.tex:94: X in z∈X\B is undefined; the declared tree domain is A. French changes this occurrence to A and identifies the typo in a footnote. At lines 114–117 the prefix-closed subset must also be nonempty to qualify as a tree under the earlier definition requiring a root; French adds and discloses that hypothesis.
- OLP-0019, operations.tex, transitive-closure definition versus OLP-0016's strict-to-partial proposition: R+ has two different local meanings, reflexive closure and transitive closure. This is a notation collision, not a false formula. Both formulas are preserved and a reader note marks the change of meaning.

# Functions chapter: draft corrections, 8 September 2026 local

Paths are relative to frozen `content/sets-functions-relations/functions/`. Exact source/target identities and affected blocks are in ALIGNMENT.jsonl and FUNCTIONS_NEW_CONSTRUCTION_AUDIT.jsonl. These four new units are drafts, not yet part of the public reader. No upstream issue submitted.

- OLP-0023, functions-relations.tex:61–62 calls the graph a relation on A×B. Under the earlier definition that would mean a subset of (A×B)²; the displayed definition correctly gives a subset of A×B. French says a relation included in A×B. This is a precise prose correction, with unchanged graph formula, recorded in C170.
- OLP-0023, functions-relations.tex:81–89 and95–100 versus relations/operations.tex:28–29: function restriction selects only the first coordinate, whereas relation restriction intersects with C². The later claim that the notions agree is therefore qualified. For f(n)=n+1 on N and C={0}, the function restriction has graph {(0,1)} and the relation restriction is empty. Their graphs coincide exactly when f[C]⊆C. Both original definitions survive; a visible French footnote gives the distinction and counterexample. C171–C174 record the parameters, definition and repair.
- OLP-0024, inverses.tex:63–65 claims every injection has a left inverse. The proof at74 chooses a∈A, so it needs A nonempty unless B is also empty. The empty function ∅→{0} is injective but there is no function {0}→∅. French adds A nonempty to the proposition/proof and explicitly notes both the counterexample and the valid double-empty case. Yger PDF23/printed19 §1.9.4, proposition1.2, independently states the nonempty-domain convention. C183–C184 record the correction and fixed-element construction.

- OLP-0021, function-basics.tex:69–71: retaining only a positive square root omits zero although the stated domain Nat includes it. French says positive or zero, with a visible note; the displayed function and two-root example for strictly positive n are unchanged.
- OLP-0021, function-basics.tex:105–107: the input is called n and then x in the same calculation. French consistently uses x and identifies the typo in a note.
- OLP-0021, function-basics.tex:133–137: mutually exclusive cases are sufficient but not necessary for a piecewise function. The cases x≥0 and x≤0, both assigning x, define the identity on the reals despite their overlap at zero. French scopes the disjoint-case condition to this presentation and adds a note allowing compatible overlaps while retaining exhaustive coverage. The original pair/impair formulas are unchanged.

# Size-of-sets: four new draft observations

These drafts are not in public v0.3. Full evidence and target hashes: SIZE_FOUR_DRAFT_SOURCE_OBSERVATIONS.json; semantic review: SIZE_FOUR_DRAFT_SEMANTIC_REVIEW.md.

- content/sets-functions-relations/size-of-sets/zig-zag.tex:115: Exponent0 included although earlier product-power definition starts at1; explicit empty-tuple convention added.
- content/sets-functions-relations/size-of-sets/pairing.tex:34: Sum with strict bound is k(k−1)/2, not the stated k(k+1)/2; target uses inclusive bound.
- content/sets-functions-relations/size-of-sets/pairing.tex:108: General injective pairing inverse is defined only on its image, possibly a proper subset of Nat; target asks to construct enumeration from it, with empty case.
- content/sets-functions-relations/size-of-sets/pairing-alt.tex:21: Second pair must be(0,1), as in the table; corrected and disclosed.
- content/sets-functions-relations/size-of-sets/pairing-alt.tex:39: Second family must advance to(3,m), as in the table; corrected and disclosed.
- content/sets-functions-relations/size-of-sets/non-enumerability.tex:17: Parallel non-enumerability proof is at nen-alt; corrected and disclosed.
- content/sets-functions-relations/size-of-sets/non-enumerability.tex:26: Surjection from PosInt requires A nonempty; empty A is still countable. Nonempty condition added and disclosed.

## Inverses : existence et unicité, correction FR-FUN-001

OLP0024 inverses.tex, source149 attribue unique inverse à prop:bijection-inverse, qui énonce seulement existence aux lignes127–131. Prop:inverse-unique énonce et prouve unicité aux lignes167–174. Le texte français conserve existence et unicité, sépare leurs renvois, ajoute une note visible et conserve l’abus de notation suivant. Source anglaise gelée inchangée ; correction locale destinée à la prochaine édition.

## Réduction, équipotence et Cantor : nouveaux brouillons

Voir SIZE_REDUCTION_CANTOR_SOURCE_OBSERVATIONS.json pour les identités source/cible et les extraits.

- content/sets-functions-relations/size-of-sets/reduction.tex:52 : Undefined index k removed from characteristic sequence and disclosed.
- content/sets-functions-relations/size-of-sets/reduction.tex:97 : Finite n-zero word has wrong type for Bin^omega; completed by infinitely many ones with visible editorial note.
- content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:75 : Both empty-set branches must use f(x)=y; g is the enumeration in the nonempty branch. Corrected with notes.
- content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:91 : Both empty-set branches must use f(x)=y; g is the enumeration in the nonempty branch. Corrected with notes.
- content/sets-functions-relations/size-of-sets/comparing-size.tex:45 : Equivalence assumes a choice principle sufficient to provide Nat injection into an arbitrary infinite A. AC disclosed as sufficient, not claimed minimal.
- content/sets-functions-relations/size-of-sets/comparing-size.tex:88 : Final universal index in diagonal proof must range over A, not only diagonal subset. Corrected with visible note and two cases.

## Taille des ensembles — variantes finales

OLP0039 non-enumerability-alt.tex : le tableau annonce N0=Nat et N3={2,3,4,…}, mais omet N0 aux colonnes3/4/5 et N3 en colonne5. Quatre cellules rétablies avec note ; diagonale inchangée. Le renvoi conditionnel à card-opps omet une fermeture d’argument après la note : son troisième argument consomme end, malgré l’équilibre global des accolades. La structure cible est réparée. Les inversions d’indices s_n(m) et du second échange diagonal sont signalées dans le lecteur.

OLP0040 reduction-alt.tex : transfert par surjection complété par suppression des répétitions pour la définition bijective ; injectivité de l’application caractéristique vérifiée explicitement. Les commentaires conservés sont traduits et visibles avec provenance ; h(n), mot fini mal typé, est complété par une queue infinie de1 avec note. Le label red:prob:nat-nat en doublon reçoit red-alt dans cette seule variante. Voir la revue sémantique et les décisions C386–C436 pour les hypothèses, indices et autres précisions.
