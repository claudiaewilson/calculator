def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference between x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y. Raise ValueError if dividing by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def sqrt(x):
    """Returns the square root of x. Raise ValueError if x is < 0"""
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return (x)**0.5