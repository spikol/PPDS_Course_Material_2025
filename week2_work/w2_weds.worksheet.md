# Week 2 - Worksheet Wednesday

26 Nov 2025

## Problem 1: List Functions - `len()` and `sorted()`

- Use `len()` to find the number of items in a list
- Use `sorted()` to create an alphabetically sorted copy of a list
- Predict the output of code involving list functions
- Identify logical errors in code (variable naming vs. content)

#### Part A: Code Reading (5 minutes)

Examine the following code carefully:

```python
five_senses = ["toes", "fingers", "eye", "ears"]

print(len(five_senses))
print(sorted(five_senses))
```

**Questions:**

1. What will `len(five_senses)` print? Write your prediction: `____`
2. What will `sorted(five_senses)` print? Write your prediction: `____`
3. **Bug Hunt:** There is something wrong with this code that Python will NOT catch as an error. What is the problem?

#### Part B: Fix and Extend

**Task 1:** Fix the list so the variable name matches its contents. Create a list called `five_senses` that actually contains the five human senses.

```python
five_senses = [_________________________________________]

print(len(five_senses))      # Should print: ____
print(sorted(five_senses))   # What will this print?
```

**Task 2:** The original list contained body parts. Create a *new* variable with an appropriate name for those items, then add one more body part to make exactly 5 items.

```python
_____________ = ["toes", "fingers", "eye", "ears", _______]

print(len(_____________))
print(sorted(_____________))
```

#### Extension Challenge

What is the difference between `sorted()` and `.sort()`? Test with this code:

```python
animals = ["zebra", "ant", "monkey"]

# Method 1
result1 = sorted(animals)
print("Original after sorted():", animals)
print("Result:", result1)

# Method 2
result2 = animals.sort()
print("Original after .sort():", animals)
print("Result:", result2)
```

What do you observe? Which one modifies the original list?

## Problem 2: Chained Conditionals - Age Classifier

- Use `if`, `elif`, and `else` to create chained conditionals
- Convert user input to integers using `int()`
- Trace through conditional logic to predict which branch executes
- Understand that only ONE branch runs in a chained conditional

### Part A: Code Tracing (5 minutes)

Examine the following code:

python

```python
age = int(input('Please input an age: '))

if age < 13:
    print('Child')
elif age < 18:
    print('Teenager')
elif age < 60:
    print('Adult')
else:
    print('Senior')
```

**Trace the code:** For each input value, write which category is printed.

```
Input AgeOutput
5______
13______
17______
18______
59______
60______
85______
```

**Question:** Why does age 13 print "Teenager" and not "Child"? Explain in your own words.

### Part B: Complete the Code (5-10 minutes)

Write an age classifier that uses **different** age boundaries. Your program should classify people into these categories:

- **Infant**: 0-2 years
- **Toddler**: 3-5 years
- **Child**: 6-12 years
- **Teen**: 13-17 years
- **Adult**: 18 and above

Complete the scaffolding:

python

```python
age = int(input('Enter age: '))

if age < ____:
    print('Infant')
elif age < ____:
    print('________')
elif ___________:
    print('Child')
elif ___________:
    print('________')
else:
    print('________')
```

**Test your code** with ages: 1, 4, 10, 15, 25

### Part C: Bug Hunt

A student wrote this code, but it doesn't work correctly. Find and fix the TWO errors:

python

```python
age = input('Enter your age: ')

if age < 13
    print('Child')
elif age < 18:
    print('Teenager')
else:
    print('Adult')
```

**Hint:** One error is about data types, one is about syntax.

### Extension Challenge

Modify the original age classifier to handle invalid input as well. What happens if someone enters `-5` or `150`? Add conditions to print `'Invalid age'` for ages below 0 or above 120.

python

```python
age = int(input('Please input an age: '))

# Add your validation here first
if _______________:
    print('Invalid age')
elif age < 13:
    print('Child')
# ... continue the rest
```

**Key Takeaways:**

- In chained conditionals, only the FIRST true condition executes
- The order of conditions matters—put more specific conditions first
- `input()` returns a string; use `int()` to convert for numeric comparisons

## Problem 3: While Loops, For Loops, and Filtering

#### Learning Objectives

- Use a `while` loop to iterate through a list using an index
- Use a `for` loop to iterate directly over list elements
- Combine loops with conditionals to filter elements
- Understand the difference between indexing (`w[0]`) and slicing (`w[:1]`)

### Part A: Code Tracing (5 minutes)

**Given this list:**

```python
words = ["hello", "how", "are", "you"]
```

**Task 1:** Trace through this `while` loop. Write what prints on each iteration.

```python
i = 0
while i < len(words):
    print(words[i])
    i = i + 1
```

| Iteration | Value of `i` | `words[i]` | Output |
| --------- | ------------ | ---------- | ------ |
| 1st       | 0            | ________   | ______ |
| 2nd       | ___          | ________   | ______ |
| 3rd       | ___          | ________   | ______ |
| 4th       | ___          | ________   | ______ |

**Question:** What is the value of `i` when the loop stops? Why does it stop?

### Part B: Write the Loops (10 minutes)

Complete each task using the scaffolding provided.

**Task 1:** Create the list and write a `while` loop that prints each word.

```python
words = [____________________________________]

i = ____
while ________________:
    print(__________)
    ______________
```

**Task 2:** Write a `for` loop that does the same thing (much simpler!).

```python
for ____ in ______:
    print(_____)
```

**Task 3:** Write a `for` loop that prints ONLY words starting with "h".

```python
for w in words:
    if _______________:
        print(w)
```

### Part C: Bug Hunt - The Empty String Trap (5 minutes)

A student wrote this code, but it crashes. Run it in your head (or in Python) to find the problem.

```python
words = ["hello", "how", "are", "you", ""]  # Note the empty string!

for w in words:
    if w[0] == "h":
        print(w)
```

**Questions:**

1. What error do you get? ____________________
2. Why does this happen? ____________________
3. **Fix the bug** using slicing instead of indexing:

```python
for w in words:
    if w[___] == "h":    # Change this part
        print(w)
```

**Explanation:**

- `w[0]` on an empty string causes an `IndexError`
- `w[:1]` on an empty string returns `""` (no error!)

### Part D: Compare While vs For

Fill in the table comparing the two loop types:

| Aspect                           | `while` loop | `for` loop |
| -------------------------------- | ------------ | ---------- |
| Need to track index?             | Yes / No     | Yes / No   |
| Risk of infinite loop?           | Yes / No     | Yes / No   |
| Better for "do until condition"? | Yes / No     | Yes / No   |
| Better for "do for each item"?   | Yes / No     | Yes / No   |

### Extension Challenge

Modify the filtering loop to count how many words start with "h" instead of printing them:

```python
words = ["hello", "how", "are", "you", "hungry", "hippo"]

count = ____
for w in words:
    if w[:1] == "h":
        ______________

print(f"Words starting with 'h': {count}")
```

**Key Takeaways:**

- `while` loops need manual index management; `for` loops handle iteration automatically
- Always consider edge cases like empty strings in your data
- Use `w[:1]` instead of `w[0]` when strings might be empty—slicing never raises `IndexError`

## Worksheet Exercise: Modules and Functions - Dice Rolling

### Learning Objectives

- Import modules using `import module_name`
- Import specific functions using `from module import function`
- Use `random.randint(a, b)` to generate random integers
- Create and import your own custom module

### Part A: Using the `random` Module (10 minutes)

#### Exercise 1: Basic Dice Roll with `import`

1. Import the `random` module
2. Create a function called `roll_dice()` that takes a parameter `sides`
3. The function should `return` a random number between 1 and `sides`
4. Use `random.randint(a, b)` which returns a random integer from `a` to `b` (inclusive)
5. Test your function by printing the result

**Complete the scaffolding:**

```python
import ________

def roll_dice(sides):
    """Roll a dice with the given number of sides."""
    return random.________(__, _____)

# Test: Roll a 6-sided dice
print(roll_dice(6))

# Test: Roll a 20-sided dice (like in D&D!)
print(roll_dice(20))
```

**Expected output:** A random number between 1 and 6, then a random number between 1 and 20.

#### Exercise 2: Using `from ... import`

Rewrite the solution using `from random import randint` instead.

python

```python
from _______ import _______

def roll_dice(sides):
    """Roll a dice with the given number of sides."""
    return ________(1, sides)   # No need for random. prefix!

# Test it
print(roll_dice(6))
```

**Question:** What is the difference between `import random` and `from random import randint`?

### Part B: Create Your Own Module

#### Exercise 3: Build a Dice Module

**Step 1:** Create a new file called `dice_module.py` with this content:

python

```python
# dice_module.py
import random

def roll_die(minimum, maximum):
    """Roll a die with values from minimum to maximum."""
    return random.randint(minimum, maximum)
```

**Step 2:** Create a second file called `game.py` **in the same folder**:

python

```python
# game.py
import dice_module as dm

# Test the module
print("Rolling a 6-sided die:", dm.roll_die(1, 6))
print("Rolling a 12-sided die:", dm.roll_die(1, 12))
```

**Run `game.py`** and verify it works.

#### Exercise 4: Dice Battle Game

Add this game to your `game.py` file. Complete the missing parts:

python

```python
import dice_module as dm

def dice_battle():
    """Two players roll dice - highest roll wins!"""
    player_1 = dm.roll_die(1, 6)
    player_2 = dm.roll_die(1, 6)
    
    print(f"Player 1 rolled: {player_1}")
    print(f"Player 2 rolled: {player_2}")
    
    if player_1 > player_2:
        print("__________ wins!")
    elif player_2 > player_1:
        print("__________ wins!")
    else:
        print("__________!")

# Play the game
dice_battle()
```

### Quick Reference

```
Import StyleSyntaxUsage
Full moduleimport randomrandom.randint(1, 6)
With aliasimport random as rr.randint(1, 6)
Specific functionfrom random import randintrandint(1, 6)
```

**Key Takeaways:**

- `randint(a, b)` requires TWO arguments: minimum and maximum (both inclusive)
- Any `.py` file can be imported as a module
- Custom modules must be in the same directory (or Python path) to import them