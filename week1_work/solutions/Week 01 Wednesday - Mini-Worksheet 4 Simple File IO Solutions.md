# Week 01 Wednesday - Mini-Worksheet 4: Simple File I/O Solutions

## Exercise 1 Solution

```python
# Method 1: Read entire file
file = open("sample.txt", "r")
content = file.read()
print("Method 1 - Full content:")
print(content)
file.close()

# Method 2: Read line by line
file = open("sample.txt", "r")
first_line = file.readline()
second_line = file.readline()
print("\nMethod 2 - First two lines:")
print(first_line)
print(second_line)
file.close()

# Method 3: Read all lines into list
file = open("sample.txt", "r")
lines = file.readlines()
print("\nMethod 3 - All lines as list:")
print(lines)
file.close()
```

## Exercise 2 Solution

```python
# Read entire file
with open("sample.txt", "r") as file:
    content = file.read()

print("Content:")
print(content)

# Read all lines
with open("sample.txt", "r") as file:
    lines = file.readlines()

print("\nLines:")
for i, line in enumerate(lines):
    print(f"{i+1}: {line.strip()}")
```

## Exercise 3 Solution

```python
messages = [
    "Welcome to Python!\n",
    "File I/O is easy.\n",
    "Keep practicing!\n"
]

# Write to file
with open("output.txt", "w") as file:
    file.writelines(messages)

# Verify
with open("output.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# Append
with open("output.txt", "a") as file:
    file.write("This is appended!\n")

# Read again
with open("output.txt", "r") as file:
    print("\nAfter appending:")
    print(file.read())
```

## Exercise 4 Solution

```python
# Create messy file
with open("messy.txt", "w") as file:
    file.write("  hello  \n")
    file.write("\tworld\t\n")
    file.write("  python  \n")

# Read and clean
with open("messy.txt", "r") as file:
    lines = file.readlines()

clean_lines = []
for line in lines:
    cleaned = line.strip()
    clean_lines.append(cleaned + "\n")

# Write cleaned
with open("clean.txt", "w") as file:
    file.writelines(clean_lines)

# Verify
with open("clean.txt", "r") as file:
    print("Cleaned content:")
    print(file.read())
```

## Exercise 5 Solution

```python
# Create file
with open("story.txt", "w") as file:
    file.write("Python is awesome.\n")
    file.write("I love programming.\n")
    file.write("Data science rocks!\n")

# Analyze
with open("story.txt", "r") as file:
    content = file.read()

lines = content.split("\n")
line_count = len([l for l in lines if l])  # Non-empty lines

words = content.split()
word_count = len(words)

char_count = len(content)

print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Characters: {char_count}")
```

## Exercise 6 Solution

```python
def copy_file(source_filename, target_filename):
    # Read from source
    with open(source_filename, "r") as source:
        content = source.read()
    
    # Write to target
    with open(target_filename, "w") as target:
        target.write(content)
    
    print(f"Copied {source_filename} to {target_filename}")

# Test
with open("original.txt", "w") as file:
    file.write("This is the original file.\n")
    file.write("Let's copy it!\n")

copy_file("original.txt", "backup.txt")

with open("backup.txt", "r") as file:
    print("\nBackup content:")
    print(file.read())
```

## Exercise 7 Solution

```python
# Create CSV file
with open("students.txt", "w") as file:
    file.write("Name,Age,Grade\n")
    file.write("Alice,20,A\n")
    file.write("Bob,21,B\n")
    file.write("Charlie,19,A\n")

# Read and process
with open("students.txt", "r") as file:
    lines = file.readlines()

header = lines[0].strip().split(",")
print(f"Header: {header}")

students = []
for line in lines[1:]:
    parts = line.strip().split(",")
    name = parts[0]
    age = int(parts[1])
    grade = parts[2]
    
    student = {
        "name": name,
        "age": age,
        "grade": grade
    }
    students.append(student)

print("\nStudents:")
for student in students:
    print(f"  {student['name']}: Age {student['age']}, Grade {student['grade']}")
```