# Week 01 Wednesday - Mini-Worksheet 1: Strings -Solutions




## Exercise 1 Solution

```python
message = "DataScience"

# 1. Get the first character
first_char = message[0]

# 2. Get the last character using negative indexing
last_char = message[-1]

# 3. Get the 5th character (index 4)
fifth_char = message[4]

# 4. Get the second-to-last character
second_last = message[-2]

print(f"First: {first_char}, Last: {last_char}")
print(f"Fifth: {fifth_char}, Second-last: {second_last}")
```

## Exercise 2 Solution

```python
code = "PythonProgramming"

# 1. Extract "Python" (first 6 characters)
lang = code[0:6]  # or code[:6]

# 2. Extract "Programming" (from index 6 to end)
activity = code[6:]

# 3. Extract every second character from the entire string
every_second = code[::2]

# 4. Reverse the entire string
reversed_code = code[::-1]

# 5. Get the last 4 characters
last_four = code[-4:]

print(f"Language: {lang}")
print(f"Activity: {activity}")
print(f"Every second: {every_second}")
print(f"Reversed: {reversed_code}")
print(f"Last four: {last_four}")
```

## Exercise 3 Solution

```python
sentence = "  hello world  "
data = "apple,banana,cherry"
filename = "report_2024.txt"

# 1. Remove leading and trailing spaces from sentence
clean_sentence = sentence.strip()

# 2. Convert clean_sentence to uppercase
uppercase_sentence = clean_sentence.upper()

# 3. Split data into a list using comma as delimiter
fruit_list = data.split(",")

# 4. Replace ".txt" with ".pdf" in filename
new_filename = filename.replace(".txt", ".pdf")

# 5. Check if "world" is in the original sentence
contains_world = "world" in sentence

print(f"Clean: '{clean_sentence}'")
print(f"Uppercase: '{uppercase_sentence}'")
print(f"Fruits: {fruit_list}")
print(f"New filename: {new_filename}")
print(f"Contains 'world': {contains_world}")
```

## Exercise 4 Solution

```python
# 1. Convert the integer 42 to a string
age = 42
age_str = str(age)

# 2. Convert the string "123" to an integer
num_str = "123"
num_int = int(num_str)

# 3. Convert the string "45.67" to a float
price_str = "45.67"
price_float = float(price_str)

# 4. Create a formatted message using variables
name = "Alice"
score = 95
message = f"{name} scored {score} points"
# Alternative: message = name + " scored " + str(score) + " points"

print(f"Age as string: {age_str} (type: {type(age_str)})")
print(f"Number as int: {num_int} (type: {type(num_int)})")
print(f"Price as float: {price_float} (type: {type(price_float)})")
print(message)
```

