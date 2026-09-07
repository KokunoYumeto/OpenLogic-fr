# Source observations, first sets chapter

Authority: OpenLogicProject/OpenLogic, revision 9620cc73f9c8e0ad003c514a5d3748f29611c4c0. Source files remain byte-for-byte unchanged under upstream/.

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
