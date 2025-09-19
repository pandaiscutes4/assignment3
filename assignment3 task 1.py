def factorial(n):
    """Calculate factorial of n using a loop"""
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Call the function with a sample number
number = 5
print(f"The factorial of {number} is {factorial(number)}")
