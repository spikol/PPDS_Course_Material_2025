# Week 01 Wednesday - Mini-Worksheet 4: Simple File I/O

## Learning Objectives
By completing these exercises, you will:
- Open and close files properly using `open()` and `close()`
- Read files using `read()`, `readline()`, and `readlines()`
- Write to files using `write()` and `writelines()`
- Use the `with` statement for automatic file closing
- Process file contents line by line
- Handle file paths correctly

---

## Exercise 1: Reading a File - Three Ways
First, create a file named `sample.txt` with this content:
```
Line 1: Hello
Line 2: World
Line 3: Python
```

Now read it three different ways:

```python
# Method 1: Read entire file as one string
file = open("sample.txt", "r")
content = ___________
print("Method 1 - Full content:")
print(content)
file.close()

# Method 2: Read line by line
file = open("sample.txt", "r")
first_line = ___________
second_line = ___________
print("\nMethod 2 - First two lines:")
print(first_line)
print(second_line)
file.close()

# Method 3: Read all lines into a list
file = open("sample.txt", "r")
lines = ___________
print("\nMethod 3 - All lines as list:")
print(lines)
file.close()

# What do you notice about the \n characters?
```

---

## Exercise 2: The `with` Statement - Best Practice
Rewrite Exercise 1 using the `with` statement (automatically closes file):

```python
# Read entire file
with open("sample.txt", "r") as file:
    content = ___________

print("Content:")
print(content)

# Read all lines
with open("sample.txt", "r") as file:
    lines = ___________

print("\nLines:")
for i, line in enumerate(lines):
    print(f"{i+1}: {line.strip()}")  # strip() removes \n
```

**Why use `with`?**
- Automatically closes the file
- Works even if an error occurs
- Cleaner, more readable code

---

## Exercise 3: Writing to a File
Create a new file and write content to it:

```python
# Create a list of messages
messages = [
    "Welcome to Python!\n",
    "File I/O is easy.\n",
    "Keep practicing!\n"
]

# Write to a new file
with open("output.txt", "w") as file:
    ___________  # Write all messages at once

# Verify by reading it back
with open("output.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# Try appending to the file
with open("output.txt", "a") as file:
    ___________  # Write one more line

# Read again to see the appended line
with open("output.txt", "r") as file:
    print("\nAfter appending:")
    print(file.read())
```

---

## Exercise 4: Processing Lines - Remove Whitespace
Read a file and clean up each line:

```python
# Create a file with messy whitespace
with open("messy.txt", "w") as file:
    file.write("  hello  \n")
    file.write("\tworld\t\n")
    file.write("  python  \n")

# Read and clean each line
with open("messy.txt", "r") as file:
    lines = file.readlines()

clean_lines = []
for line in lines:
    cleaned = ___________  # Remove whitespace
    clean_lines.append(cleaned + "\n")

# Write cleaned lines to new file
with open("clean.txt", "w") as file:
    ___________

# Verify
with open("clean.txt", "r") as file:
    print("Cleaned content:")
    print(file.read())
```

---

## Exercise 5: Counting Lines and Words
Create a simple text analyzer:

```python
# Create a sample file
with open("story.txt", "w") as file:
    file.write("Python is awesome.\n")
    file.write("I love programming.\n")
    file.write("Data science rocks!\n")

# Analyze the file
with open("story.txt", "r") as file:
    content = ___________

# Count lines
lines = ___________
line_count = ___________

# Count words
words = ___________
word_count = ___________

# Count characters
char_count = ___________

print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Characters: {char_count}")
```

**Expected Output:**
```
Lines: 3
Words: 9
Characters: 62 (approximately, including newlines)
```

---

## Exercise 6: File Copy Program
This connects directly to Week 2 Monday worksheet!

```python
def copy_file(source_filename, target_filename):
    """
    Copy content from source file to target file
    """
    # Read from source
    with open(source_filename, "r") as source:
        content = ___________
    
    # Write to target
    with open(target_filename, "w") as target:
        ___________
    
    print(f"Copied {source_filename} to {target_filename}")

# Test it
with open("original.txt", "w") as file:
    file.write("This is the original file.\n")
    file.write("Let's copy it!\n")

copy_file("original.txt", "backup.txt")

# Verify the copy
with open("backup.txt", "r") as file:
    print("\nBackup content:")
    print(file.read())
```

---

## Exercise 7: Processing CSV-like Data
Work with comma-separated data (preparation for real CSV files):

```python
# Create a file with CSV-like data
with open("students.txt", "w") as file:
    file.write("Name,Age,Grade\n")
    file.write("Alice,20,A\n")
    file.write("Bob,21,B\n")
    file.write("Charlie,19,A\n")

# Read and process the data
with open("students.txt", "r") as file:
    lines = file.readlines()

# Get header (first line)
header = ___________
print(f"Header: {header}")

# Process data lines
students = []
for line in lines[1:]:  # Skip header
    # Split by comma
    parts = ___________
    name = parts[0]
    age = int(parts[1])
    grade = parts[2].strip()
    
    # Store as dictionary
    student = {
        "name": name,
        "age": age,
        "grade": grade
    }
    students.append(student)

# Display results
print("\nStudents:")
for student in students:
    print(f"  {student['name']}: Age {student['age']}, Grade {student['grade']}")
```

---



## Reflection Questions

1. What's the difference between `read()`, `readline()`, and `readlines()`?
2. Why should you use the `with` statement instead of manually calling `close()`?
3. What happens if you open a file in "w" mode when it already exists?
4. When would you use "a" (append) mode vs "w" (write) mode?
5. Why do we need to use `strip()` when processing lines from a file?

## Connection to Handin 1

**These exercises directly prepare you for Handin 1 Project:**
-  Reading file with `open()` and `read()` → stores in `file_content`
- Counting comment lines using `count("#")` → `comment_line_count`
-  Reading file with `readlines()` → stores in `list_of_lines`
-  Using `len()` to get total lines → `total_line_count`
- Calculating data points → `data_point_count`
- Using `list[-1]` and `split()` → get `column_count`

**The Challenge Exercise is EXACTLY what you need for Handin 1!** 

Practice these exercises thoroughly - they're the foundation of data file processing! 
