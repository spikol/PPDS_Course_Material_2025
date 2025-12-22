### Bonus exercise (not NumPy)

The nucleotide sequence of RNA is translated to amino acids of protein, briefly as follows:

   - It works in a left-to-right direction
   - Translation starts when 3 consecutive nucleotides are detected with `AUG`
   - Then, every 3 consecutive nucleotides are translated to a certain protein
   - When 3 consecutive nucleotides are `UAA`, `UAG`, `UGA`, translation stops
Example:
   - `CCAUGCAAUCAUGACC` -> `CC[start][amino acid][amino acid][stop]CC`
   - Translated into a protein of 2 amino acids

Implement code for predicting the number of amino acids in the translated protein

**Task: Count the number of amino acids**

Implement an algorithm that automatically counts the  **number of amino acids** for any input **string of RNA sequence** 

- When translation never starts, return zero
- When translation starts but never stops, the remaining 1-2 nucleotides are counted as a new amino acid

- E.g. 
   - `CCACGCAAUCACGACC` -> returns 0
   - `UCAUGCAAUCAUGACC` -> `UC[start][amino acid][amino acid][stop]CC` returns 2
   - `AAAUGCAAUCAU` -> `AA[start][amino acid][amino acid]U` returns 2

**Hint**

- Match the first appearence of the `AUG` -> `str.find()`
- Use string slicing to get the subsequence starting with `AUG` 

- Initialize a variable for storing the count
- Loop over the subsequence with `step_size=3`
- Check if the 3 characters matches the end sign, otherwise increasing the count by 1
