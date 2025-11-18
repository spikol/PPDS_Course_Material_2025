# Week 01 Wednesday - Mini-Worksheet 1: Strings

## Learning Objectives
By completing these exercises, you will:
- Master string indexing with positive and negative indices
- Practice string slicing with different step sizes
- Apply string methods for text manipulation
- Convert between strings and other data types

---

## Exercise 1: Basic String Indexing
Write code to extract specific characters from the string `message = "DataScience"`.

```python
message = "DataScience"

# 1. Get the first character
first_char = ___________

# 2. Get the last character using negative indexing
last_char = ___________

# 3. Get the 5th character (index 4)
fifth_char = ___________

# 4. Get the second-to-last character
second_last = ___________

print(f"First: {first_char}, Last: {last_char}")
print(f"Fifth: {fifth_char}, Second-last: {second_last}")
```

**Expected Output:**
```
First: D, Last: e
Fifth: S, Second-last: c
```

---

## Exercise 2: String Slicing Practice
Given the string `code = "PythonProgramming"`, extract the following substrings:

```python
code = "PythonProgramming"

# 1. Extract "Python" (first 6 characters)
lang = ___________

# 2. Extract "Programming" (from index 6 to end)
activity = ___________

# 3. Extract every second character from the entire string
every_second = ___________

# 4. Reverse the entire string
reversed_code = ___________

# 5. Get the last 4 characters
last_four = ___________

print(f"Language: {lang}")
print(f"Activity: {activity}")
print(f"Every second: {every_second}")
print(f"Reversed: {reversed_code}")
print(f"Last four: {last_four}")
```

**Expected Output:**
```
Language: Python
Activity: Programming
Every second: PtoPormig
Reversed: gnimmargorPnohtyP
Last four: ming
```

---

## Exercise 3: String Methods Mastery
Complete the following string manipulations:

```python
sentence = "  hello world  "
data = "apple,banana,cherry"
filename = "report_2024.txt"

# 1. Remove leading and trailing spaces from sentence
clean_sentence = ___________

# 2. Convert clean_sentence to uppercase
uppercase_sentence = ___________

# 3. Split data into a list using comma as delimiter
fruit_list = ___________

# 4. Replace ".txt" with ".pdf" in filename
new_filename = ___________

# 5. Check if "world" is in the original sentence
contains_world = ___________

print(f"Clean: '{clean_sentence}'")
print(f"Uppercase: '{uppercase_sentence}'")
print(f"Fruits: {fruit_list}")
print(f"New filename: {new_filename}")
print(f"Contains 'world': {contains_world}")
```

**Expected Output:**
```
Clean: 'hello world'
Uppercase: 'HELLO WORLD'
Fruits: ['apple', 'banana', 'cherry']
New filename: report_2024.pdf
Contains 'world': True
```

---

## Exercise 4: Type Conversion Challenge
Practice converting between strings and other types:

```python
# 1. Convert the integer 42 to a string
age = 42
age_str = ___________

# 2. Convert the string "123" to an integer
num_str = "123"
num_int = ___________

# 3. Convert the string "45.67" to a float
price_str = "45.67"
price_float = ___________

# 4. Create a formatted message using variables
name = "Alice"
score = 95
message = ___________  # "Alice scored 95 points"

print(f"Age as string: {age_str} (type: {type(age_str)})")
print(f"Number as int: {num_int} (type: {type(num_int)})")
print(f"Price as float: {price_float} (type: {type(price_float)})")
print(message)
```

**Expected Output:**
```
Age as string: 42 (type: <class 'str'>)
Number as int: 123 (type: <class 'int'>)
Price as float: 45.67 (type: <class 'float'>)
Alice scored 95 points
```


---

## Reflection Questions

1. Why does Python use 0-based indexing instead of 1-based?
2. What's the difference between `strip()`, `lstrip()`, and `rstrip()`?
3. When would you use negative indices vs positive indices?
4. Why do we need to convert types (e.g., `str()`, `int()`) when working with mixed data?

## Connection to Handin 1

These exercises directly prepare you for:
- **Handin 1.1:** String syntax and print statements
- **Handin 1.2:** String manipulation and file output
- **Handin 1.3:** `strip()` and `split()` methods for data cleaning

Keep practicing! String manipulation is fundamental to data science! 🐍
