# Source-target reverse-paraphrase samples

Method: the same translation agent reread the French passages and restated their meaning in English, then compared that restatement with the frozen original. This is not independent human or independent-model review.

1. OLP-0005-B06: “Two sets are equal exactly when each member of the first belongs to the second and conversely.” Both directions survive; no assertion that arbitrary property-defined sets exist is introduced.
2. OLP-0006-B11: “Restricted universal quantification abbreviates an implication inside ∀; restricted existential quantification abbreviates a conjunction inside ∃.” Both unchanged displayed formulas have the correct scope.
3. OLP-0007-B06: “The positive integers start at one, and Bin contains exactly the first two natural numbers, zero and one.” French strictement positif preserves exclusion of zero from PosInt.
4. OLP-0008-B07: “The union contains everything in A, in B, or in both.” Inclusive or is explicit in both languages.
5. OLP-0008-B21: “For a nonempty family, the intersection contains the objects in every member; for an empty family in a specified universe U, the result can be U.” The first qualification and universe note are disclosed source repairs, not claimed literal translation.
6. OLP-0009-B08: “Triples and longer tuples are encoded by repeatedly pairing on the left; the first component of the resulting pair is the previous tuple.” The nested formulas preserve that convention.
7. OLP-0010-B10–B11: “Assuming R belongs to itself makes it fail the defining property, hence it cannot belong; assuming it does not belong makes it satisfy the defining property, hence it belongs.” Neither negation nor either case is dropped.

Result: these seven samples preserve the English mathematical dependencies, apart from the explicitly identified correction in sample 5. Other text was reviewed directly in the paired block inspection; these samples do not prove complete semantic correctness.
