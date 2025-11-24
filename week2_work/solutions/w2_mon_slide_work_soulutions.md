# Mini-Exercise Sheet - ANSWER KEY

24 Nov 2025

## Week 01 Recap Variables and Strings (variabler og strenge)

#### Part 1

Complete the following code to produce the expected output:

```python
python# Solution
student_name = "Alice"
age = 20
grade_average = 8.5
is_passing = True

# Print message combining all variables
print(f"{student_name} is {age} years old, has average {grade_average}, and passing status: {is_passing}")

# Change age to string
age = "twenty"
print("Age as string:", age)

# Convert grade_average to integer
grade_rounded = int(grade_average)
print("Rounded grade:", grade_rounded)

### Output:
Alice is 20 years old, has average 8.5, and passing status: True
Age as string: twenty
Rounded grade: 8
```

#### Part 2

Given the following string, extract the specified parts:

```python
text = "Python Programming"

# Extract "Python" (first word)
first_word = text[0:6]  # or text[:6]
print("First word:", first_word)

# Extract "Programming" (second word)
second_word = text[7:]
print("Second word:", second_word)

# Extract every other character
every_other = text[::2]
print("Every other char:", every_other)

# Reverse the entire string
reversed_text = text[::-1]
print("Reversed:", reversed_text)

# Extract last 4 characters using negative indexing
last_four = text[-4:]
print("Last four:", last_four)

# Extract "gram" from the middle
middle_part = text[10:14]
print("Middle part:", middle_part)

### Expected Output:
First word: Python
Second word: Programming
Every other char: Pto rgamn
Reversed: gnimmargorP nohtyP
Last four: ming
Middle part: gram
```

### Hints:

- Remember: `text[start:end]` extracts from start up to (but not including) end
- Negative indices count from the end: `-1` is the last character
- Use `[::-1]` to reverse a string
- Use `[::2]` to get every other character





## Section 1: Functions

### Exercise 1.1: Simple Greeting Function

```python
def say_hello():
    print("Hej fra Python!")

# Test your function
say_hello()
```

### Exercise 1.2: Function with One Parameter

```python
def triple(num):
    return num * 3

# Test your function
print(triple(5))    # Prints: 15
print(triple(10))   # Prints: 30
```

**Common mistakes:**

- Using `print()` instead of `return`
- Forgetting to include the parameter in the function definition
- Writing `return 3 * num` works equally well

**Alternative solution:**

```python
def triple(num):
    result = num * 3
    return result
```



## Section 2: Loops

### Exercise 2.1: Print Numbers with a While Loop

```python
counter = 1
while counter <= 4:
    print(counter)
    counter = counter + 1
```

**Common mistakes:**

- Starting counter at 0 (would print 0, 1, 2, 3)
- Forgetting to increment the counter (infinite loop!)
- Using `counter++` or `counter += 1` before they've learned it (both valid but not yet introduced)

**Alternative solution:**

```python
counter = 1
while counter < 5:
    print(counter)
    counter = counter + 1
    
```

### Exercise 2.2: Print List Items with For Loop

```python
animals = ["cat", "dog", "bird"]

for animal in animals:
    print(animal)
```

**Common mistakes:**

- Trying to use indices: `for i in animals` then `print(animals[i])` - works but overcomplicated
- Forgetting the colon `:`
- Not indenting the print statement



## Section 3: Combining Functions and Loops

### Exercise 3.1: Using Modulo

```python
for number in range(10, 16):
    remainder = number % 3
    print(f"{number} % 3 = {remainder}")
```

**Alternative solution (more beginner-friendly):**

```python
number = 10
while number <= 15:
    print(f"{number} % 3 = {number % 3}")
    number = number + 1
```

**Teaching notes:**

- Students might not format the output exactly as shown - that's okay
- Key learning: understanding that `%` gives the remainder
- Connection to zodiac exercise: year % 12 gives zodiac position

------

### Exercise 3.2: Count Specific Items

```python
numbers = [5, 3, 5, 8, 5, 2, 5]

count = 0
for num in numbers:
    if num == 5:
        count = count + 1

print(f"The number 5 appears {count} times")
```

**Common mistakes:**

- Not initializing `count = 0` before the loop
- Using `count = 1` instead of `count = 0`
- Using `=` instead of `==` in the if statement
- Forgetting to increment count

**Advanced alternative:**

```python
numbers = [5, 3, 5, 8, 5, 2, 5]
count = numbers.count(5)
print(f"The number 5 appears {count} times")
```



## Bonus Challenge

```python
def count_letter(word_list, letter):
    count = 0
    for word in word_list:
        if word[0] == letter:
            count = count + 1
    return count

# Test it
words = ["apple", "banana", "avocado", "cherry"]
print(count_letter(words, "a"))  # Prints: 2
```

**Common mistakes:**

- Checking if `letter in word` instead of `word[0] == letter` (would count "banana" for letter "a")
- Not initializing count to 0
- Using print instead of return

