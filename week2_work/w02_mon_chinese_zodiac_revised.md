# Main Worksheet: Chinese Zodiac Calculator

24 Nov 2025

## Background

Chinese zodiac years are represented by 12 animals. Each Chinese lunar year in the repeating zodiac cycle of 12 years is represented by a zodiac animal.

**The order of animals:** Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog, Pig.

The **Reference year:** 1996 is a Rat year (index 0 in our list). We use this as our base year for calculations.



![chinese-zodiac](/Users/zfp165/Documents/DIKU TEACHING/Python B2/2025-2026 Course/images/chinese-zodiac.png)



## Part 1: Basic Function (Everyone - 15 minutes)

### Task 1: Create a Zodiac Function

Write a function `get_zodiac(year)` that:

- Takes a birth year as input (integer)
- Returns the Chinese zodiac sign as a string
- Includes a docstring explaining what it does

**Expected behaviour:**

```python
print(get_zodiac(1994))  # Should return: 'Dog'
print(get_zodiac(2000))  # Should return: 'Dragon'
```

**Hints:**

- Create a list of all 12 zodiac animals in order
- Use modulo `%` to calculate the index: `(year - 1996) % 12`
- 1996 is a Rat year, so it's at index 0

**Starter code:**

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
    
    # TODO: Calculate index and return the zodiac
    
    return zodiac

# Test your function
print(get_zodiac(1994))  # Should print: Dog
print(get_zodiac(2000))  # Should print: Dragon
```

### Task 2: Interactive Program

Create a main program that:

- Prompts the user for their birth year
- Calls your `get_zodiac()` function
- Prints the result in this format: `Your Chinese zodiac sign is: Dog`

**Expected output:**

```
Please type in your birth year: 1994
Your Chinese zodiac sign is: Dog
```



## Part 2: Need more Challenges 

Choose ONE of the following challenges:

### Challenge A: Count Zodiac Years (Uses Loops)

Write a function `zodiac_year_count(list_of_years, zodiac)` that:

- Takes a list of years and a target zodiac name
- Returns how many years in the list match that zodiac
- Uses a **for loop** to iterate through the years

**Starter code:**

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
    # TODO: Use a for loop to check each year
    
    return count

# Test code
from random import sample
test_years = sample(range(1990, 2025), 10)
print(f"Years: {test_years}")
print(f"Dog years: {zodiac_year_count(test_years, 'Dog')}")
```

### Challenge B: Error Handling (Edge Cases)

Improve your `get_zodiac()` function to handle edge cases:

**Edge cases to handle:**

1. User enters text instead of a number
2. User enters a negative year
3. User enters an unrealistic year (before 1900 or after 2100)

**Strategy:**

```python
def get_zodiac_safe(year):
    """Calculate zodiac with error handling.
    
    Returns error messages for invalid inputs.
    """
    zodiacs = ['Rat', 'Ox', 'Tiger', 'Rabbit', 
               'Dragon', 'Snake', 'Horse', 'Goat',
               'Monkey', 'Rooster', 'Dog', 'Pig']
    
    # TODO: Add validation checks here
    # Check if year is in reasonable range (1900-2100)
    # Return error message if invalid
    
    index = (year - 1996) % 12
    return zodiacs[index]

# Main program with error handling
year_input = input('Please type in your birth year: ')

try:
    year = int(year_input)  # This might raise ValueError
    result = get_zodiac_safe(year)
    print(f'Your Chinese zodiac sign is: {result}')
except ValueError:
    print("Error: Please enter a valid number")
```

### Challenge C: Multiple Years with Loop

Modify your program to:

- Keep asking for years until the user types "quit"
- Calculate and display the zodiac for each year
- Use a **while loop**

**Example output:**

```
Enter birth year (or 'quit' to exit): 1994
Your Chinese zodiac sign is: Dog

Enter birth year (or 'quit' to exit): 2000
Your Chinese zodiac sign is: Dragon

Enter birth year (or 'quit' to exit): quit
Goodbye!
```

**Hint:** Use `while True:` and `break` when user types "quit"

## Testing Your Solution

Make sure your solution works for these test cases:

- 1996 → Rat (our reference year)
- 1994 → Dog (shown in example)
- 2000 → Dragon (millennium year)
- 2024 → Dragon (current year)

## Additional Information

### Why 1996 as a Reference?

We chose 1996 as the reference year because:

- It's a Rat year (the first animal in the cycle)
- It corresponds to index 0 in our list
- The modulo calculation `(year - 1996) % 12` gives us the correct index directly

**How the math works:**

- 1996 - 1996 = 0 → 0 % 12 = 0 → Rat ✓
- 1997 - 1996 = 1 → 1 % 12 = 1 → Ox ✓
- 1994 - 1996 = -2 → -2 % 12 = 10 → Dog ✓

(Python's modulo handles negative numbers correctly!)

### Edge Case Strategies

When writing robust code, consider these edge cases:

| Edge Case         | Problem            | Strategy                    |
| ----------------- | ------------------ | --------------------------- |
| Non-numeric input | User types "abc"   | Use `try/except ValueError` |
| Negative year     | User enters -500   | Check if `year < 1900`      |
| Future year       | User enters 3000   | Check if `year > 2100`      |
| Empty input       | User presses Enter | Check if `len(input) == 0`  |

**Error handling pattern:**

```python
try:
    year = int(user_input)
    if year < 1900 or year > 2100:
        print("Please enter a year between 1900-2100")
    else:
        # Process valid year
except ValueError:
    print("Please enter a valid number")
```