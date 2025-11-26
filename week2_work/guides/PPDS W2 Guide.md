# PPDS W2 Guide

## Quick Guide Random Module

~~~python

## Basic Random Numbers
- `random.random()` - Random float between 0.0 and 1.0
- `random.uniform(a, b)` - Random float between a and b
- `random.randint(a, b)` - Random integer between a and b (inclusive)
- `random.randrange(start, stop, step)` - Random integer from range

## Random Choices
- `random.choice(seq)` - Pick one random element from sequence
- `random.choices(seq, k=n)` - Pick n elements with replacement
- `random.sample(seq, k=n)` - Pick n unique elements without replacement

## Shuffling & Seeding
- `random.shuffle(list)` - Shuffle list in place
- `random.seed(n)` - Set random seed for reproducibility

## Common Use Cases
```python
# Roll a dice (1-6)
random.randint(1, 6)

# Flip a coin
random.choice(['Heads', 'Tails'])

# Pick lottery numbers (6 unique from 1-49)
random.sample(range(1, 50), 6)

# Random probability (30% chance)
random.random() < 0.3
```
~~~

```python
import random

# Basic random numbers
print("random():", random.random())                    # 0.0 to 1.0
print("uniform(1, 10):", random.uniform(1, 10))       # Float between 1 and 10
print("randint(1, 6):", random.randint(1, 6))         # Integer 1-6 (inclusive)
print("randrange(0, 10, 2):", random.randrange(0, 10, 2))  # Even numbers 0-8

# Random choices
colors = ['red', 'blue', 'green', 'yellow']
print("\nchoice:", random.choice(colors))              # Pick one
print("choices (k=3):", random.choices(colors, k=3))  # Pick 3 with replacement
print("sample (k=2):", random.sample(colors, k=2))    # Pick 2 unique

# Shuffle
deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print("\nShuffled deck:", deck)
```

## Math Module

```python
import math

# Constants
math.pi        # 3.141592653589793
math.e         # 2.718281828459045
math.inf       # Infinity
math.nan       # Not a Number

# Rounding & Absolute
math.ceil(4.3)      # 5 - Round up
math.floor(4.8)     # 4 - Round down
math.trunc(4.8)     # 4 - Remove decimals
abs(-5)             # 5 - Absolute value
round(4.567, 2)     # 4.57 - Round to n decimals

# Powers & Roots
math.pow(2, 3)      # 8.0 - Power (2³)
math.sqrt(16)       # 4.0 - Square root
math.exp(2)         # 7.389... - e^x

# Trigonometry (radians)
math.sin(math.pi/2)    # 1.0
math.cos(0)            # 1.0
math.tan(math.pi/4)    # 1.0
math.radians(180)      # Convert degrees to radians
math.degrees(math.pi)  # Convert radians to degrees

# Logarithms
math.log(10)        # 2.302... - Natural log (base e)
math.log10(100)     # 2.0 - Log base 10
math.log2(8)        # 3.0 - Log base 2

x=4
# Other Useful
math.factorial(5)   # 120 - 5!
math.gcd(48, 18)    # 6 - Greatest common divisor
math.isnan(x)       # Check if NaN
math.isinf(x)       # Check if infinite
```

### Common Uses

1. **Rounding up/down for real-world quantities**
   ```python
   math.ceil(2.1)   # 3 people needed (can't have 2.1 people)
   math.floor(4.9)  # 4 complete hours worked
   ```

2. **Calculate distance/area (Pythagorean theorem)**
   ```python
   distance = math.sqrt(x**2 + y**2)  # Distance between points
   ```

3. **Financial calculations with compound interest**
   ```python
   amount = principal * math.pow(1 + rate, years)
   ```

4. **Convert angles for graphics/rotation**
   ```python
   radians = math.radians(45)  # Convert 45° to radians for rotation
   ```

5. **Scientific calculations with natural log**
   ```python
   growth_rate = math.log(final_value / initial_value)
   ```