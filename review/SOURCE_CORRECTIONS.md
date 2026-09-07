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

# Functions chapter: reviewed corrections, 8 September 2026 local

Paths are relative to frozen `content/sets-functions-relations/functions/`. Exact source/target identities and affected blocks are in ALIGNMENT.jsonl and FUNCTIONS_NEW_CONSTRUCTION_AUDIT.jsonl. These units now form part of the three-chapter public reader. No upstream issue submitted.

- OLP-0023, functions-relations.tex:61–62 calls the graph a relation on A×B. Under the earlier definition that would mean a subset of (A×B)²; the displayed definition correctly gives a subset of A×B. French says a relation included in A×B. This is a precise prose correction, with unchanged graph formula, recorded in C170.
- OLP-0023, functions-relations.tex:81–89 and95–100 versus relations/operations.tex:28–29: function restriction selects only the first coordinate, whereas relation restriction intersects with C². The later claim that the notions agree is therefore qualified. For f(n)=n+1 on N and C={0}, the function restriction has graph {(0,1)} and the relation restriction is empty. Their graphs coincide exactly when f[C]⊆C. Both original definitions survive; a visible French footnote gives the distinction and counterexample. C171–C174 record the parameters, definition and repair.
- OLP-0024, inverses.tex:63–65 claims every injection has a left inverse. The proof at74 chooses a∈A, so it needs A nonempty unless B is also empty. The empty function ∅→{0} is injective but there is no function {0}→∅. French adds A nonempty to the proposition/proof and explicitly notes both the counterexample and the valid double-empty case. Yger PDF23/printed19 §1.9.4, proposition1.2, independently states the nonempty-domain convention. C183–C184 record the correction and fixed-element construction.

- OLP-0021, function-basics.tex:69–71: retaining only a positive square root omits zero although the stated domain Nat includes it. French says positive or zero, with a visible note; the displayed function and two-root example for strictly positive n are unchanged.
- OLP-0021, function-basics.tex:105–107: the input is called n and then x in the same calculation. French consistently uses x and identifies the typo in a note.
- OLP-0021, function-basics.tex:133–137: mutually exclusive cases are sufficient but not necessary for a piecewise function. The cases x≥0 and x≤0, both assigning x, define the identity on the reals despite their overlap at zero. French scopes the disjoint-case condition to this presentation and adds a note allowing compatible overlaps while retaining exhaustive coverage. The original pair/impair formulas are unchanged.
