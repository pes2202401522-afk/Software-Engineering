"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b


def multiply(a, b):
    """Multiply two numbers with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    
    print(f"Multiplying {a} × {b}")  # Added logging
    result = a * b
    print(f"Result: {result}")
    return result

def divide(a, b):
    """Divide a by b with enhanced error handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero - division by zero is undefined")
    
    print(f"Dividing {a} ÷ {b}")  # Added logging
    result = a / b
    print(f"Result: {result}")
    return result

def power(base, exponent):
    """Raise base to the power of exponent"""
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if exponent < 0:
        raise ValueError("Negative exponents are not supported in this implementation")
    return base ** exponent

def square_root(number):
    """Calculate the square root of a number"""
    if not isinstance(number, (int, float)):
        raise TypeError("Argument must be a number")
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return number ** 0.5

# TODO: Students will add multiply, divide, power, sqrt functions

if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")