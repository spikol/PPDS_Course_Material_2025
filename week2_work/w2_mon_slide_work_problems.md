# Worksheet - Week 2 Monday

24 Nov 2025



## Week 01 Recap Variables and Strings (variabler og strenge)

#### Part 1

Complete the following code to produce the expected output:

````python
python# TODO: Create a variable called 'student_name' with your name
student_name = 

# TODO: Create a variable 'age' with value 20
age = 

# TODO: Create a variable 'grade_average' with value 8.5
grade_average = 

# TODO: Create a variable 'is_passing' with value True
is_passing = 

# TODO: Print a message combining all variables:
# Expected output: "Alice is 20 years old, has average 8.5, and passing status: True"
print(

# TODO: Now change 'age' to be a string "twenty" and print it
age = 
print("Age as string:", age)

# TODO: Convert grade_average to an integer and store in 'grade_rounded'
grade_rounded = 
print("Rounded grade:", grade_rounded)
```

### Expected Output:
```
Alice is 20 years old, has average 8.5, and passing status: True
Age as string: twenty
Rounded grade: 8
````

#### Part 2

Given the following string, extract the specified parts:

````python
pythontext = "Python Programming"

# TODO: Extract "Python" (first word)
first_word = text[

print("First word:", first_word)

# TODO: Extract "Programming" (second word)
second_word = text[

print("Second word:", second_word)

# TODO: Extract every other character from the entire string
every_other = text[

print("Every other char:", every_other)

# TODO: Reverse the entire string
reversed_text = text[

print("Reversed:", reversed_text)

# TODO: Extract the last 4 characters using negative indexing
last_four = text[

print("Last four:", last_four)

# TODO: Extract "gram" from the middle of "Programming"
middle_part = text[

print("Middle part:", middle_part)
```

### Expected Output:
```
First word: Python
Second word: Programming
Every other char: Pto rgamn
Reversed: gnimmargorP nohtyP
Last four: ming
Middle part: gram
````

### Hints:

- Remember: `text[start:end]` extracts from start up to (but not including) end
- Negative indices count from the end: `-1` is the last character
- Use `[::-1]` to reverse a string
- Use `[::2]` to get every other character

## Section 1: Functions (Moduł og Funktioner)

### Exercise 1.1: Simple Greeting Function

Create a function called `say_hello` that prints "Hej fra Python!".

```python
# Write your function here




# Test your function
say_hello()
```

**Expected output:**

```
Hej fra Python!
```

### Exercise 1.2: Function with One Parameter

Create a function called `triple` that takes a single number and returns it multiplied by 3.

```python
# Write your function here




# Test your function
print(triple(5))    # Should print: 15
print(triple(10))   # Should print: 30
```



## Section 2: Loops (Løkker)

### Exercise 2.1: Print Numbers with a While Loop

Write a while loop that prints the numbers from 1 to 4.

```python
# Write your while loop here
```

**Expected output:**

```
1
2
3
4
```

### Exercise 2.2: Print List Items with For Loop

Given the list `animals = ["cat", "dog", "bird"]`, write a for loop that prints each animal.

```python
animals = ["cat", "dog", "bird"]

# Write your for loop here
```

**Expected output:**

```
cat
dog
bird
```



## Section 3: Combining Functions and Loops

### Exercise 3.1: Using Modulo

Write code that prints the remainder when dividing numbers 10 through 15 by 3.

```python
# Write your code here
```

**Expected output:**

```
10 % 3 = 1
11 % 3 = 2
12 % 3 = 0
13 % 3 = 1
14 % 3 = 2
15 % 3 = 0
```

### Exercise 3.2: Count Specific Items

Given the list below, count how many times the number 5 appears.

```python
numbers = [5, 3, 5, 8, 5, 2, 5]

# Write your code to count 5s here





print(f"The number 5 appears {count} times")
```

**Expected output:**

```
The number 5 appears 4 times
```



## Bonus Challenge (Valgfri)

Create a function called `count_letter` that takes a list of words and a letter, then returns how many words start with that letter.

```python
def count_letter(word_list, letter):
    # Write your code here
    
    
    
    

# Test it
words = ["apple", "banana", "avocado", "cherry"]
print(count_letter(words, "a"))  # Should print: 2
```



## Self-Check (Selv-tjek)

Check off each skill you feel confident with:

- [ ] I can write a simple function with `def`
- [ ] I can write a function that takes a parameter
- [ ] I can write a function that returns a value
- [ ] I can write a while loop with a counter
- [ ] I can write a for loop to go through a list
- [ ] I understand how the modulo operator `%` works
- [ ] I can count specific items in a list using a loop