import random

def generate_random(start: int, end: int) -> int:
    """
    Generate a random non-zero integer between start and end.

    Args:
        start (int): The lower bound of the number range.
        end (int): The upper bound of the number range.

    Returns:
        int: A randomly generated non-zero integer.
    """
    num = 0
    while num == 0:
        num = random.randint(start, end)
    return num

def generate_equation(start: int, end: int, mode: str) -> tuple:
    """
    Generates a linear equation of the form ax + b = c and returns all values.

    In "Basic" mode, x is an integer.  
    In "Expert" mode, x is a rounded decimal (float with 2 decimal places).

    Args:
        start (int): The lower bound of the number range.
        end (int): The upper bound of the number range.
        mode (str): Either "Basic" or "Expert", determines solution type.

    Returns:
        tuple: A tuple containing four values:
            a (int): Coefficient of x.
            b (int): Constant term.
            c (int or float): The result of ax + b.
            x (int or float): The solution for equation.
    """
    a = generate_random(start, end)
    b = generate_random(start, end)
    x = generate_random(start, end)
    c = a * x + b
    if mode == "Expert":
        x = round(random.uniform(start, end), 2)
        c = round(a * x + b, 2)
    return a, b, c, x
