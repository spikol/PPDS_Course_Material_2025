# Week 01 Wednesday - Mini-Worksheet 3: Basic Lists

## Learning Objectives
By completing these exercises, you will:
- Create and manipulate lists
- Master list indexing with positive and negative indices
- Practice list slicing for extracting sublists
- Apply essential list methods (append, extend, remove, sort)
- Understand the difference between lists and strings (mutability)

---

## Exercise 1: Creating and Indexing Lists
Practice basic list operations:

```python
# 1. Create a list of your 5 favorite fruits
fruits = ___________

# 2. Get the first fruit
first = ___________

# 3. Get the last fruit using negative indexing
last = ___________

# 4. Get the middle fruit (index 2)
middle = ___________

# 5. Change the second fruit to "mango"
___________

# 6. Get the length of the list
length = ___________

print(f"Fruits: {fruits}")
print(f"First: {first}, Last: {last}, Middle: {middle}")
print(f"Length: {length}")
```

**Expected Output (example):**
```
Fruits: ['apple', 'mango', 'orange', 'banana', 'grape']
First: apple, Last: grape, Middle: orange
Length: 5
```

---

## Exercise 2: List Slicing Mastery
Given the list `numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`, extract:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1. First three numbers
first_three = ___________

# 2. Last three numbers
last_three = ___________

# 3. Every second number (even indices: 0, 2, 4, ...)
evens = ___________

# 4. Every second number starting from index 1 (odd indices)
odds = ___________

# 5. Numbers from index 3 to 7 (inclusive of 3, exclusive of 7)
middle_section = ___________

# 6. Reverse the entire list
reversed_list = ___________

# 7. Numbers from index 2 to 8 with step 2
step_slice = ___________

print(f"First 3: {first_three}")      # Expected: [0, 1, 2]
print(f"Last 3: {last_three}")        # Expected: [7, 8, 9]
print(f"Evens: {evens}")              # Expected: [0, 2, 4, 6, 8]
print(f"Odds: {odds}")                # Expected: [1, 3, 5, 7, 9]
print(f"Middle: {middle_section}")    # Expected: [3, 4, 5, 6]
print(f"Reversed: {reversed_list}")   # Expected: [9, 8, 7, ..., 0]
print(f"Step slice: {step_slice}")    # Expected: [2, 4, 6, 8]
```

---

## Exercise 3: List Methods Practice
Complete the following list manipulations:

```python
# Start with an empty shopping cart
cart = []

# 1. Add "apple" to the cart
___________

# 2. Add "banana" to the cart
___________

# 3. Add multiple items: ["milk", "eggs", "bread"]
___________

# 4. Remove "banana" from the cart
___________

# 5. Check how many items are in the cart
item_count = ___________

# 6. Check if "milk" is in the cart
has_milk = ___________

# 7. Sort the cart alphabetically
___________

# 8. Remove and return the last item
last_item = ___________

print(f"Cart: {cart}")
print(f"Item count: {item_count}")
print(f"Has milk: {has_milk}")
print(f"Removed: {last_item}")
```

**Expected Output (example):**
```
Cart: ['apple', 'bread', 'eggs']
Item count: 4 (before last removal)
Has milk: True
Removed: milk
```

---

## Exercise 4: Lists vs Strings - Mutability
Understand the difference between mutable lists and immutable strings:

```python
# Strings are IMMUTABLE
word = "hello"
# Try to change the first letter - this will cause an error!
# word[0] = "H"  # Uncomment to see the error

# But you can create a new string
new_word = "H" + word[1:]
print(f"New word: {new_word}")  # "Hello"

# Lists are MUTABLE
letters = ['h', 'e', 'l', 'l', 'o']
# Change the first letter - this works!
letters[0] = 'H'
print(f"Letters: {letters}")  # ['H', 'e', 'l', 'l', 'o']

# Convert between strings and lists
word = "Python"
# 1. Convert string to list of characters
char_list = ___________

# 2. Modify the list
char_list[0] = 'p'

# 3. Convert back to string
new_word = ___________

print(f"Original: {word}")
print(f"Modified: {new_word}")
```

---

## Exercise 5: List Operations
Practice list operators:

```python
# 1. Concatenate two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = ___________

# 2. Repeat a list 3 times
pattern = [0, 1]
repeated = ___________

# 3. Check membership
numbers = [10, 20, 30, 40, 50]
has_30 = ___________
has_25 = ___________

# 4. Compare lists
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = [1, 2, 4]
equal_ab = ___________
equal_ac = ___________

print(f"Combined: {combined}")          # Expected: [1, 2, 3, 4, 5, 6]
print(f"Repeated: {repeated}")          # Expected: [0, 1, 0, 1, 0, 1]
print(f"Has 30: {has_30}")              # Expected: True
print(f"Has 25: {has_25}")              # Expected: False
print(f"A equals B: {equal_ab}")        # Expected: True
print(f"A equals C: {equal_ac}")        # Expected: False
```



## Reflection Questions

1. What's the difference between `list.sort()` and `sorted(list)`?
2. Why can you modify a list but not a string?
3. When would you use `append()` vs `extend()`?
4. How is `list[::-1]` different from `list.reverse()`?
5. What does `list[-1]` give you?

## Connection to Handin 1

These exercises directly prepare you for:
- **Handin 1.3:** Using `split()` to create a list from a string
- **Handin 1 Project:** 
  - Reading file into list with `readlines()`
  - Using list indexing `list[-1]` to get last element
  - Using `len()` to count list elements
  - Splitting lines and counting columns

The Challenge Exercise is almost identical to what you'll do in Handin 1!
