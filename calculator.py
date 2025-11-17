"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b): return a + b

def mul(a, b): return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def exp(a, b): return a**b

def square_root(a):
    try:
        if a < 0: raise ValueError("Input of square root must be non-negative")
        return math.sqrt(a)
    except ValueError as e:
        print(f"Error: {e}")

def hypotenuse(a, b):
    return math.hypot(a, b)

def subtract(a, b):
    return a - b

def logarithm(a, b):
    if a <= 0 or b <= 0: raise ValueError("Base or input of logarithm has to be positive")
    return math.log(b, a)
