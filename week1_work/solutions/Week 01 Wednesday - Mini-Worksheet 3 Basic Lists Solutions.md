# Week 01 Wednesday - Mini-Worksheet 3: Basic Lists Solutions

# Solutions

## Exercise 1 Solution

```python
# 1. Create a list of your 5 favorite fruits
fruits = ['apple', 'banana', 'orange', 'grape', 'mango']

# 2. Get the first fruit
first = fruits[0]

# 3. Get the last fruit using negative indexing
last = fruits[-1]

# 4. Get the middle fruit (index 2)
middle = fruits[2]

# 5. Change the second fruit to "mango"
fruits[1] = "mango"

# 6. Get the length of the list
length = len(fruits)

print(f"Fruits: {fruits}")
print(f"First: {first}, Last: {last}, Middle: {middle}")
print(f"Length: {length}")
```

## Exercise 2 Solution

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1. First three numbers
first_three = numbers[:3]  # or numbers[0:3]

# 2. Last three numbers
last_three = numbers[-3:]  # or numbers[7:]

# 3. Every second number (even indices)
evens = numbers[::2]

# 4. Every second number starting from index 1
odds = numbers[1::2]

# 5. Numbers from index 3 to 7
middle_section = numbers[3:7]

# 6. Reverse the entire list
reversed_list = numbers[::-1]

# 7. Numbers from index 2 to 8 with step 2
step_slice = numbers[2:9:2]

print(f"First 3: {first_three}")
print(f"Last 3: {last_three}")
print(f"Evens: {evens}")
print(f"Odds: {odds}")
print(f"Middle: {middle_section}")
print(f"Reversed: {reversed_list}")
print(f"Step slice: {step_slice}")
```

## Exercise 3 Solution

```python
# Start with an empty shopping cart
cart = []

# 1. Add "apple" to the cart
cart.append("apple")

# 2. Add "banana" to the cart
cart.append("banana")

# 3. Add multiple items
cart.extend(["milk", "eggs", "bread"])

# 4. Remove "banana" from the cart
cart.remove("banana")

# 5. Check how many items are in the cart
item_count = len(cart)

# 6. Check if "milk" is in the cart
has_milk = "milk" in cart

# 7. Sort the cart alphabetically
cart.sort()

# 8. Remove and return the last item
last_item = cart.pop()

print(f"Cart: {cart}")
print(f"Item count: {item_count}")
print(f"Has milk: {has_milk}")
print(f"Removed: {last_item}")
```

## Exercise 4 Solution

```python
# Strings are IMMUTABLE
word = "hello"
new_word = "H" + word[1:]
print(f"New word: {new_word}")

# Lists are MUTABLE
letters = ['h', 'e', 'l', 'l', 'o']
letters[0] = 'H'
print(f"Letters: {letters}")

# Convert between strings and lists
word = "Python"
# 1. Convert string to list
char_list = list(word)

# 2. Modify the list
char_list[0] = 'p'

# 3. Convert back to string
new_word = "".join(char_list)

print(f"Original: {word}")
print(f"Modified: {new_word}")
```

## Exercise 5 Solution

```python
# 1. Concatenate two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2

# 2. Repeat a list 3 times
pattern = [0, 1]
repeated = pattern * 3

# 3. Check membership
numbers = [10, 20, 30, 40, 50]
has_30 = 30 in numbers
has_25 = 25 in numbers

# 4. Compare lists
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = [1, 2, 4]
equal_ab = list_a == list_b
equal_ac = list_a == list_c

print(f"Combined: {combined}")
print(f"Repeated: {repeated}")
print(f"Has 30: {has_30}")
print(f"Has 25: {has_25}")
print(f"A equals B: {equal_ab}")
print(f"A equals C: {equal_ac}")
```

## Exercise 6 Solution

```python
numbers = [5, 2, 8, 1, 9, 3]

# 1. Use list.sort() method
numbers_copy1 = numbers.copy()
numbers_copy1.sort()
print(f"After sort(): {numbers_copy1}")

# 2. Use sorted() function
numbers_copy2 = numbers.copy()
sorted_numbers = sorted(numbers_copy2)
print(f"Original: {numbers_copy2}")
print(f"Sorted version: {sorted_numbers}")

# 3. Sort in descending order
numbers_copy3 = numbers.copy()
numbers_copy3.sort(reverse=True)
print(f"Descending: {numbers_copy3}")

# 4. Reverse the list
numbers_copy4 = numbers.copy()
numbers_copy4.reverse()
print(f"Reversed: {numbers_copy4}")

# 5. Reverse using slicing
reversed_slice = numbers[::-1]
print(f"Reversed (slice): {reversed_slice}")
```

## Exercise 7 Solution

```python
scores = [85, 92, 78, 90, 88, 95, 82, 89, 91, 87]

# 1. Calculate average
average = sum(scores) / len(scores)

# 2. Find highest
highest = max(scores)

# 3. Find lowest
lowest = min(scores)

# 4. Count high scorers
high_scorers = 0
for score in scores:
    if score >= 90:
        high_scorers += 1

# 5. Get top 3
sorted_scores = sorted(scores, reverse=True)
top_3 = sorted_scores[:3]

# 6. Get mid-range scores
mid_range = []
for score in scores:
    if 85 <= score <= 92:
        mid_range.append(score)

# 7. Remove failing scores
passing_scores = []
for score in scores:
    if score >= 80:
        passing_scores.append(score)

print(f"Average: {average:.2f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"High scorers (>=90): {high_scorers}")
print(f"Top 3: {top_3}")
print(f"Mid-range (85-92): {mid_range}")
print(f"Passing (>=80): {passing_scores}")
```

## Challenge Exercise Solution

```python
data_lines = [
    "# This is a comment",
    "# Another comment line",
    "2020,Male,Asian,5",
    "2020,Female,White,8",
    "2021,Male,Black,3",
    "# Final comment",
    "2021,Female,Asian,6"
]

# Task 1: Count comment lines
comment_count = 0
for line in data_lines:
    if line.startswith("#"):
        comment_count += 1

# Task 2: Total line count
total_lines = len(data_lines)

# Task 3: Data point count
data_point_count = total_lines - comment_count

# Task 4: Get last line and count columns
last_line = data_lines[-1]
columns = last_line.split(",")
column_count = len(columns)

# Task 5: Extract data lines
data_only = []
for line in data_lines:
    if not line.startswith("#"):
        data_only.append(line)

print(f"Comment lines: {comment_count}")
print(f"Total lines: {total_lines}")
print(f"Data points: {data_point_count}")
print(f"Columns: {column_count}")
print(f"\nData lines:")
for line in data_only:
    print(f"  {line}")
```