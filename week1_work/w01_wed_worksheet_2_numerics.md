# Week 01 Wednesday - Mini-Worksheet 2: Numerics & Booleans

## Learning Objectives
By completing these exercises, you will:
- Perform arithmetic operations with the proper order of operations
- Use assignment operators as shortcuts
- Apply comparison and logical operators
- Convert between numeric types
- Combine Boolean expressions for decision-making

---

## Exercise 1: Arithmetic Operations


Calculate the following expressions. Try to predict the answer before running the code!

```python
# 1. Calculate: 15 + 3 * 2
result1 = ___________

# 2. Calculate: (15 + 3) * 2
result2 = ___________

# 3. Integer division: 17 // 5
result3 = ___________

# 4. Regular division: 17 / 5
result4 = ___________

# 5. Modulo (remainder): 17 % 5
result5 = ___________

# 6. Exponentiation: 2 ** 10
result6 = ___________

print(f"1. {result1}")  # Expected: 21
print(f"2. {result2}")  # Expected: 36
print(f"3. {result3}")  # Expected: 3
print(f"4. {result4}")  # Expected: 3.4
print(f"5. {result5}")  # Expected: 2
print(f"6. {result6}")  # Expected: 1024
```

---

## Exercise 2: Assignment Operators Trace
Trace through the code and predict the value of `x` after each operation:

```python
x = 10
print(f"Start: x = {x}")

x += 5    # x = ?
print(f"After += 5: x = {x}")

x *= 2    # x = ?
print(f"After *= 2: x = {x}")

x //= 7   # x = ?
print(f"After //= 7: x = {x}")

x **= 2   # x = ?
print(f"After **= 2: x = {x}")

x %= 10   # x = ?
print(f"After %= 10: x = {x}")

# What is the final value of x?
# Work through this mentally first, then run the code!
```

**Expected Output:**
```
Start: x = 10
After += 5: x = 15
After *= 2: x = 30
After //= 7: x = 4
After **= 2: x = 16
After %= 10: x = 6
```

---

## Exercise 3: Comparison Operators
Predict whether each comparison is True or False:

```python
a = 15
b = 20
c = 15

# 1. Is a less than b?
result1 = ___________

# 2. Is a equal to c?
result2 = ___________

# 3. Is b not equal to c?
result3 = ___________

# 4. Is a greater than or equal to c?
result4 = ___________

# 5. Is (a + c) greater than b?
result5 = ___________

print(f"1. a < b: {result1}")        # Expected: True
print(f"2. a == c: {result2}")       # Expected: True
print(f"3. b != c: {result3}")       # Expected: True
print(f"4. a >= c: {result4}")       # Expected: True
print(f"5. (a+c) > b: {result5}")    # Expected: True
```

---

## Exercise 4: Boolean Operations
Complete the boolean expressions:

```python
# Given conditions
is_student = True
has_id = True
age = 20
grade = 85

# 1. Can enter campus? (must be student AND have ID)
can_enter = ___________

# 2. Is adult? (age >= 18)
is_adult = ___________

# 3. Passed course? (grade >= 60)
passed = ___________

# 4. Gets discount? (is student OR age < 18)
gets_discount = ___________

# 5. Can vote? (is adult AND is student)
can_vote = ___________

# 6. Failed course? (NOT passed)
failed = ___________

print(f"Can enter: {can_enter}")      # Expected: True
print(f"Is adult: {is_adult}")        # Expected: True
print(f"Passed: {passed}")            # Expected: True
print(f"Gets discount: {gets_discount}")  # Expected: True
print(f"Can vote: {can_vote}")        # Expected: True
print(f"Failed: {failed}")            # Expected: False
```

---

## Exercise 5: Type Conversion Practice
Practice converting between numeric types:

```python
# 1. Convert float to int (truncates decimal part!)
price = 19.99
price_int = ___________

# 2. Convert int to float
quantity = 5
quantity_float = ___________

# 3. Convert True to int
bool_val = True
bool_as_int = ___________

# 4. Convert 0 to bool
zero = 0
zero_as_bool = ___________

# 5. Convert non-zero to bool
non_zero = 42
non_zero_as_bool = ___________

print(f"Price as int: {price_int}")           # Expected: 19
print(f"Quantity as float: {quantity_float}") # Expected: 5.0
print(f"True as int: {bool_as_int}")          # Expected: 1
print(f"Zero as bool: {zero_as_bool}")        # Expected: False
print(f"42 as bool: {non_zero_as_bool}")      # Expected: True
```

---

## Reflection Questions

1. Why does `17 / 5` give `3.4` but `17 // 5` gives `3`?
2. What's the difference between `=` and `==`?
3. Why is `0` considered `False` but any other number `True`?
4. When should you use parentheses in boolean expressions?
5. Why does `int(19.99)` give `19` and not `20`?

## Connection to Handin 1

These exercises prepare you for:
- **Handin 1 Part 1:** Understanding type conversions
- **Handin 1 Part 2:** Using arithmetic for data analysis
- **Counting & calculations** with numeric operations

Keep practicing! Math is the foundation of data science! 🔢
