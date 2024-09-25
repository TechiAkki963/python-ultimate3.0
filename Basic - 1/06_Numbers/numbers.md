# Numbers in Python

Python supports two primary numerical data types:

- Integers: Whole numbers without decimal points (e.g., 10, -5, 0).
- Floating-point numbers: Numbers with decimal points (e.g., 3.14, -2.5, 1.0).

### Arithmetic Operations

Python supports the following arithmetic operations:

- Addition: + (e.g., 5 + 3 = 8)
- Subtraction: - (e.g., 10 - 4 = 6)
- Multiplication: * (e.g., 2 * 7 = 14)
- Division: / (e.g., 15 / 3 = 5)
- Floor Division: // (returns the integer quotient, e.g., 17 // 5 = 3)
- Modulo: % (returns the remainder, e.g., 17 % 5 = 2)
- Exponentiation: ** (e.g., 2 ** 3 = 8)

## Code

```Python

x = 10
y = 3

# Arithmetic operations
result1 = x + y  # 13
result2 = x - y  # 7
result3 = x * y  # 30
result4 = x / y  # 3.3333333333333335
result5 = x // y  # 3
result6 = x % y  # 1
result7 = x ** y  # 1000

print(result1, result2, result3, result4, result5, result6, result7)

```

### Mathematical Functions

Python's math module provides various mathematical functions:

- ***math.sqrt(x)***: Calculates the square root of x.
- ***math.pow(x, y)***: Calculates x raised to the power of y.
- ***math.sin(x), math.cos(x), math.tan(x)***: Trigonometric functions.
- ***math.log(x)***: Calculates the natural logarithm of x.
- ***math.exp(x)***: Calculates e raised to the power of x.
- ***math.factorial(x)***: Calculates the factorial of x.
- ***math.ceil(x)***: Rounds x up to the nearest integer.
- ***math.floor(x)***: Rounds x down to the nearest integer.


---

```Python

import math

result = math.sqrt(25)  # 5
print(result)

```
---

### Number Conversion

You can convert between integers and floating-point numbers using the following functions:

- int(x): Converts x to an integer.
- float(x): Converts x to a floating-point number.