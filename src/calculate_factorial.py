

def calculate_factorial(n):
    """Returns the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
