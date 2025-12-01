## Worksheet Exercise: DNA to mRNA Transcription

1 Dec

#### Background

In molecular biology, **transcription** converts DNA to mRNA by swapping nucleotide bases:

| DNA Base     | mRNA Base    |
| ------------ | ------------ |
| A (Adenine)  | U (Uracil)   |
| T (Thymine)  | A (Adenine)  |
| G (Guanine)  | C (Cytosine) |
| C (Cytosine) | G (Guanine)  |

**Example:** DNA sequence `TCGTTCAGT` → mRNA sequence `AGCAAGUCA`

You will implement this same transcription using **three different approaches**, each demonstrating different Python techniques.

### Task 1: Using Conditionals (if/elif)

**Approach:** Loop through each character and use `if/elif` to determine the replacement.

This is the most explicit approach—easy to read and understand, but requires more code.

**Complete the function:**

```python
def transcription_if(input_sequence):
    '''DNA to mRNA transcription using conditionals'''
    output_sequence = ''
    
    for s in input_sequence:
        if s == 'A':
            l = ____
        elif s == ____:
            l = 'A'
        elif s == 'G':
            l = ____
        elif s == ____:
            l = 'G'
        output_sequence = __________________ + l
    
    return output_sequence

# Test
print(transcription_if('TCGTTCAGT'))  # Expected: AGCAAGUCA
```

**Questions:**

1. Why do we initialize `output_sequence = ''` before the loop?
2. What would happen if the input contained an invalid character like 'X'?

### Task 2: Using String `.replace()` Method

**Approach:** Use the string method `.replace(old, new)` to swap characters.

**⚠️ The Problem:** If you replace `C→G` and then `G→C`, the first replacements get overwritten!

**The Trick:** Use a temporary placeholder (`X`) for one of the swaps.

**Complete the function:**

```python
def transcription_replace(input_sequence):
    '''DNA to mRNA transcription using .replace()'''
    
    # Step 1: A -> U (straightforward)
    output_sequence = input_sequence.replace('A', ____)
    
    # Step 2: T -> A (straightforward)
    output_sequence = output_sequence.replace(____, 'A')
    
    # Step 3: Handle C <-> G swap using a placeholder
    # First: C -> X (temporary placeholder)
    output_sequence = output_sequence.replace('C', ____)
    # Then: G -> C
    output_sequence = output_sequence.replace(____, ____)
    # Finally: X -> G
    output_sequence = output_sequence.replace('X', ____)
    
    return output_sequence

# Test
print(transcription_replace('TCGTTCAGT'))  # Expected: AGCAAGUCA
```

**Questions:**

1. Why can't we simply do `.replace('C','G')` followed by `.replace('G','C')`?
2. What would the output be for input `'CCGG'` if we didn't use the placeholder trick?

### Task 3: Using `str.maketrans()` and `.translate()`

**Approach:** Python has a built-in method for character-by-character translation. This is the most elegant and efficient solution.

- `str.maketrans(from_chars, to_chars)` creates a translation table
- `.translate(table)` applies the translation to a string

**Complete the function:**

```python
def transcription_translate(input_sequence):
    '''DNA to mRNA transcription using str.translate()'''
    
    # Create translation table: 'ATCG' -> 'UAGC'
    translation_table = str.maketrans(________, ________)
    
    # Apply translation
    return input_sequence.____________(translation_table)

# Test
print(transcription_translate('TCGTTCAGT'))  # Expected: AGCAAGUCA
```

**Key insight:** The characters in the two strings correspond by position:

- Position 0: A → U
- Position 1: T → A
- Position 2: C → G
- Position 3: G → C

### Comparison: Test All Three Approaches

```python
test_sequences = ['TCGTTCAGT', 'ATGCTAGCAT', 'AAAA', 'GCGC']

for seq in test_sequences:
    print(f'\nDNA: {seq}')
    print(f'  if/elif:    {transcription_if(seq)}')
    print(f'  replace:    {transcription_replace(seq)}')
    print(f'  translate:  {transcription_translate(seq)}')
```

### Summary: When to Use Each Approach

| Approach         | Pros                       | Cons                               | Best For                            |
| ---------------- | -------------------------- | ---------------------------------- | ----------------------------------- |
| **if/elif**      | Clear logic, easy to debug | Verbose, slower for long sequences | Learning, complex conditional logic |
| **.replace()**   | Simple for basic swaps     | Tricky when swapping pairs (C↔G)   | Simple replacements                 |
| **.translate()** | Fast, elegant, one-liner   | Less obvious to beginners          | Production code, efficiency         |

### Extension Challenge

Modify `transcription_if()` to handle invalid characters gracefully by either:

- **Option A:** Skip invalid characters (don't add anything to output)
- **Option B:** Raise a `ValueError` with a helpful message

```python
def transcription_safe(input_sequence):
    '''DNA to mRNA transcription with error handling'''
    output_sequence = ''
    
    for s in input_sequence:
        if s == 'A':
            l = 'U'
        elif s == 'T':
            l = 'A'
        elif s == 'G':
            l = 'C'
        elif s == 'C':
            l = 'G'
        else:
            # Your error handling here
            ____________________
        output_sequence = output_sequence + l
    
    return output_sequence

# Test with invalid input
print(transcription_safe('ATXGC'))  # What should happen?
```