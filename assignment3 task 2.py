import math

# 1. Ask the user for a number
num = float(input("Enter a number: "))

# 2. Use math module to calculate required values
square_root = math.sqrt(num)
natural_log = math.log(num)      # log base e
sine_value = math.sin(num)       # in radians

# 3. Display the results
print(f"Square root of {num} = {square_root}")
print(f"Natural logarithm of {num} = {natural_log}")
print(f"Sine of {num} (in radians) = {sine_value}")
