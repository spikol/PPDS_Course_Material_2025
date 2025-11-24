# Solution Key: Chinese Zodiac Calculator

**Course:** PPDS Week 2 Monday

## Part 1: Basic Solutions (Everyone)

### Task 1: Create a Zodiac Function

**Solution:**

```python
def get_zodiac(year):
    """Calculate the Chinese zodiac sign for a given year.
    
    Args:
        year (int): The year to calculate zodiac for
        
    Returns:
        str: The zodiac animal name
    """
    zodiacs = ['Rat', 'Ox', 'Tiger', 'Rabbit', 
               'Dragon', 'Snake', 'Horse', 'Goat',
               'Monkey', 'Rooster', 'Dog', 'Pig']
    
    index = (year - 1996) % 12
    zodiac = zodiacs[index]
    
    return zodiac

# Test cases
print(get_zodiac(1994))  # Dog
print(get_zodiac(2000))  # Dragon
print(get_zodiac(1996))  # Rat
```

**Key Points:**

- Function must have docstring
- Must use `return`, not `print()`
- List order: Rat first, Pig last
- Formula: `(year - 1996) % 12`

**Common Mistakes:**

- Using `% 13` instead of `% 12`
- Printing instead of returning
- Wrong list order

### Task 2: Interactive Program

**Solution:**

```python
def get_zodiac(year):
    """Calculate the Chinese zodiac sign for a given year."""
    zodiacs = ['Rat', 'Ox', 'Tiger', 'Rabbit', 
               'Dragon', 'Snake', 'Horse', 'Goat',
               'Monkey', 'Rooster', 'Dog', 'Pig']
    index = (year - 1996) % 12
    return zodiacs[index]

# Main program
birth_year = input('Please type in your birth year: ')
year = int(birth_year)
zodiac = get_zodiac(year)
print(f'Your Chinese zodiac sign is: {zodiac}')
```

**Alternative (Combined Conversion):**

```python
year = int(input('Please type in your birth year: '))
zodiac = get_zodiac(year)
print(f'Your Chinese zodiac sign is: {zodiac}')
```

**Expected Output:**

```
Please type in your birth year: 1994
Your Chinese zodiac sign is: Dog
```

**Common Mistakes:**

- Forgetting to convert input to int: `get_zodiac(birth_year)` 
- Missing f-string: `print('Your Chinese zodiac sign is: {zodiac}')` 
- Not capturing return value: `get_zodiac(year)` without assignment 



## Part 2: Advanced Solutions

### Challenge A: Count Zodiac Years (with loops)

**Solution 1: Complete Implementation**

```python
def zodiac_year_count(list_of_years, target_zodiac):
    """Count how many years in the list match the target zodiac.
    
    Args:
        list_of_years (list): List of year integers
        target_zodiac (str): Zodiac animal name to count
        
    Returns:
        int: Number of matching years
    """
    zodiacs = ['Rat', 'Ox', 'Tiger', 'Rabbit', 
               'Dragon', 'Snake', 'Horse', 'Goat',
               'Monkey', 'Rooster', 'Dog', 'Pig']
    
    count = 0
    for year in list_of_years:
        index = (year - 1996) % 12
        zodiac = zodiacs[index]
        if zodiac == target_zodiac:
            count += 1
    
    return count

# Test code
from random import sample
test_years = sample(range(1990, 2025), 10)
print(f"Years: {test_years}")
print(f"Dog years: {zodiac_year_count(test_years, 'Dog')}")
print(f"Dragon years: {zodiac_year_count(test_years, 'Dragon')}")
```

**Solution 2: Reusing get_zodiac() Function**

```python
def get_zodiac(year):
    """Calculate zodiac for a year."""
    zodiacs = ['Rat', 'Ox', 'Tiger', 'Rabbit', 
               'Dragon', 'Snake', 'Horse', 'Goat',
               'Monkey', 'Rooster', 'Dog', 'Pig']
    return zodiacs[(year - 1996) % 12]

def zodiac_year_count(list_of_years, target_zodiac):
    """Count matching zodiac years."""
    count = 0
    for year in list_of_years:
        if get_zodiac(year) == target_zodiac:
            count += 1
    return count
```

**Test Cases:**

```python
# Test 1: Known years
test1 = [1994, 2006, 2018]  # All Dog years
assert zodiac_year_count(test1, 'Dog') == 3

# Test 2: Mixed years
test2 = [1996, 1997, 1998]  # Rat, Ox, Tiger
assert zodiac_year_count(test2, 'Rat') == 1

# Test 3: No matches
test3 = [2000, 2012, 2024]  # All Dragon years
assert zodiac_year_count(test3, 'Dog') == 0
```

**Key Points:**

- Must use a for loop
- Initialize `count = 0` before loop
- Increment: `count += 1`
- Return after loop completes

### Challenge B: Error Handling (Edge Cases)

**Solution:**

```python
def get_zodiac_safe(year):
    """Calculate zodiac with error handling.
    
    Returns zodiac name or error message.
    """
    # Validation
    if year < 1900:
        return "Error: Year too old (before 1900)"
    if year > 2100:
        return "Error: Year too far in future (after 2100)"
    
    # Calculate zodiac
    zodiacs = ['Rat', 'Ox', 'Tiger', 'Rabbit', 
               'Dragon', 'Snake', 'Horse', 'Goat',
               'Monkey', 'Rooster', 'Dog', 'Pig']
    index = (year - 1996) % 12
    return zodiacs[index]

# Main program with try/except
year_input = input('Please type in your birth year: ')

try:
    year = int(year_input)
    result = get_zodiac_safe(year)
    
    if result.startswith("Error"):
        print(result)
    else:
        print(f'Your Chinese zodiac sign is: {result}')
        
except ValueError:
    print("Error: Please enter a valid number")
```

**Test Cases:**

```python
# Test 1: Valid year
print(get_zodiac_safe(1994))  # Dog

# Test 2: Too old
print(get_zodiac_safe(1800))  # Error: Year too old

# Test 3: Too far
print(get_zodiac_safe(2200))  # Error: Year too far

# Test 4: Non-numeric input (handled by try/except)
# Input: "hello" → "Error: Please enter a valid number"
```

**Key Points:**

-  Validate BEFORE calculating
- Use try/except for ValueError
- Check year range (1900-2100)
- Clear error messages



### Challenge C: Multiple Years with Loop

**Solution:**

```python
def get_zodiac(year):
    """Calculate the Chinese zodiac sign for a given year."""
    zodiacs = ['Rat', 'Ox', 'Tiger', 'Rabbit', 
               'Dragon', 'Snake', 'Horse', 'Goat',
               'Monkey', 'Rooster', 'Dog', 'Pig']
    return zodiacs[(year - 1996) % 12]

# Main program with while loop
print("Chinese Zodiac Calculator")
print("Type 'quit' to exit\n")

while True:
    year_input = input('Enter birth year (or "quit" to exit): ')
    
    if year_input.lower() == 'quit':
        print("Goodbye!")
        break
    
    try:
        year = int(year_input)
        zodiac = get_zodiac(year)
        print(f'Your Chinese zodiac sign is: {zodiac}\n')
    except ValueError:
        print("Please enter a valid number\n")
```

**Expected Output:**

```
Chinese Zodiac Calculator
Type 'quit' to exit

Enter birth year (or "quit" to exit): 1994
Your Chinese zodiac sign is: Dog

Enter birth year (or "quit" to exit): 2000
Your Chinese zodiac sign is: Dragon

Enter birth year (or "quit" to exit): quit
Goodbye!
```

**Key Points:**

- Use `while True:` for infinite loop
- Check for "quit" BEFORE converting to int
- Use `.lower()` for case-insensitive matching
- Use `break` to exit loop
- Handle ValueError for non-numeric input

