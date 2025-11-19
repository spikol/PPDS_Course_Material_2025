# Week 01 Wednesday - Mini-Worksheet 2: Numerics & Booleans Solutions



## Exercise 1 Solution

```python
# 1. Calculate: 15 + 3 * 2
result1 = 15 + 3 * 2  # 21 (multiplication first!)

# 2. Calculate: (15 + 3) * 2
result2 = (15 + 3) * 2  # 36 (parentheses change order)

# 3. Integer division: 17 // 5
result3 = 17 // 5  # 3

# 4. Regular division: 17 / 5
result4 = 17 / 5  # 3.4

# 5. Modulo (remainder): 17 % 5
result5 = 17 % 5  # 2

# 6. Exponentiation: 2 ** 10
result6 = 2 ** 10  # 1024

print(f"1. {result1}")
print(f"2. {result2}")
print(f"3. {result3}")
print(f"4. {result4}")
print(f"5. {result5}")
print(f"6. {result6}")
```

## Exercise 2 Solution

```python
x = 10
print(f"Start: x = {x}")

x += 5    # x = 15
print(f"After += 5: x = {x}")

x *= 2    # x = 30
print(f"After *= 2: x = {x}")

x //= 7   # x = 4 (30 // 7 = 4)
print(f"After //= 7: x = {x}")

x **= 2   # x = 16 (4 ** 2 = 16)
print(f"After **= 2: x = {x}")

x %= 10   # x = 6 (16 % 10 = 6)
print(f"After %= 10: x = {x}")
```

## Exercise 3 Solution

```python
a = 15
b = 20
c = 15

# 1. Is a less than b?
result1 = a < b  # True

# 2. Is a equal to c?
result2 = a == c  # True

# 3. Is b not equal to c?
result3 = b != c  # True

# 4. Is a greater than or equal to c?
result4 = a >= c  # True

# 5. Is (a + c) greater than b?
result5 = (a + c) > b  # True (30 > 20)

print(f"1. a < b: {result1}")
print(f"2. a == c: {result2}")
print(f"3. b != c: {result3}")
print(f"4. a >= c: {result4}")
print(f"5. (a+c) > b: {result5}")
```

## Exercise 4 Solution

```python
# Given conditions
is_student = True
has_id = True
age = 20
grade = 85

# 1. Can enter campus? (must be student AND have ID)
can_enter = is_student and has_id

# 2. Is adult? (age >= 18)
is_adult = age >= 18

# 3. Passed course? (grade >= 60)
passed = grade >= 60

# 4. Gets discount? (is student OR age < 18)
gets_discount = is_student or (age < 18)

# 5. Can vote? (is adult AND is student)
can_vote = is_adult and is_student

# 6. Failed course? (NOT passed)
failed = not passed

print(f"Can enter: {can_enter}")
print(f"Is adult: {is_adult}")
print(f"Passed: {passed}")
print(f"Gets discount: {gets_discount}")
print(f"Can vote: {can_vote}")
print(f"Failed: {failed}")
```

## Exercise 5 Solution

```python
# 1. Convert float to int (truncates decimal part!)
price = 19.99
price_int = int(price)  # 19

# 2. Convert int to float
quantity = 5
quantity_float = float(quantity)  # 5.0

# 3. Convert True to int
bool_val = True
bool_as_int = int(bool_val)  # 1

# 4. Convert 0 to bool
zero = 0
zero_as_bool = bool(zero)  # False

# 5. Convert non-zero to bool
non_zero = 42
non_zero_as_bool = bool(non_zero)  # True

print(f"Price as int: {price_int}")
print(f"Quantity as float: {quantity_float}")
print(f"True as int: {bool_as_int}")
print(f"Zero as bool: {zero_as_bool}")
print(f"42 as bool: {non_zero_as_bool}")
```

