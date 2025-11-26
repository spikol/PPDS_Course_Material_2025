# Week 2 Wednesday Worksheet - Answer Key

26 Nov 2025

## Problem 1: List Functions

**Part A:**

1. `len(five_senses)` prints: **4**
2. `sorted(five_senses)` prints: **['ears', 'eye', 'fingers', 'toes']**
3. Bug: **The variable is named `five_senses` but contains body parts, not senses (sight, hearing, taste, smell, touch)**

**Part B:**

```python
# Task 1
five_senses = ["sight", "hearing", "taste", "smell", "touch"]

# Task 2
body_parts = ["toes", "fingers", "eye", "ears", "nose"]
```

**Extension:** `sorted()` returns a NEW sorted list (original unchanged). `.sort()` modifies the original list and returns `None`.

## Problem 2: Age Classifier

**Part A - Code Tracing:**

| Input | Output   |
| ----- | -------- |
| 5     | Child    |
| 13    | Teenager |
| 17    | Teenager |
| 18    | Adult    |
| 59    | Adult    |
| 60    | Senior   |
| 85    | Senior   |

**Why 13 → Teenager:** The first condition `age < 13` is False (13 is not less than 13), so it checks the next condition `age < 18`, which is True.

**Part B:**

```python
if age < 3:
    print('Infant')
elif age < 6:
    print('Toddler')
elif age < 13:
    print('Child')
elif age < 18:
    print('Teen')
else:
    print('Adult')
```

**Part C - Two Bugs:**

1. Missing colon after `if age < 13`
2. `age` is a string (needs `int(input(...))`)

**Extension:**

```python
if age < 0 or age > 120:
    print('Invalid age')
```

## Problem 3: Loops

**Part A - Trace:**

| Iteration | `i`  | `words[i]` | Output |
| --------- | ---- | ---------- | ------ |
| 1st       | 0    | "hello"    | hello  |
| 2nd       | 1    | "how"      | how    |
| 3rd       | 2    | "are"      | are    |
| 4th       | 3    | "you"      | you    |

Loop stops when `i = 4` (not less than `len(words)` which is 4).

**Part B:**

```python
# Task 1
words = ["hello", "how", "are", "you"]
i = 0
while i < len(words):
    print(words[i])
    i = i + 1

# Task 2
for w in words:
    print(w)

# Task 3
for w in words:
    if w[:1] == "h":
        print(w)
```

**Part C:** Error is `IndexError`. Fix: use `w[:1]` instead of `w[0]`

**Part D:**

| Aspect                | `while` | `for` |
| --------------------- | ------- | ----- |
| Track index?          | Yes     | No    |
| Risk infinite loop?   | Yes     | No    |
| "Do until condition"? | Yes     | No    |
| "Do for each item"?   | No      | Yes   |

**Extension:** `count = 0` then `count = count + 1` inside the if block.

## Problem 4: Modules

**Exercise 1:**

```python
import random

def roll_dice(sides):
    return random.randint(1, sides)
```

**Exercise 2:**

```python
from random import randint

def roll_dice(sides):
    return randint(1, sides)
```

**Exercise 4 - Missing parts:**

```python
print("Player 1 wins!")
print("Player 2 wins!")
print("It's a tie!")
```