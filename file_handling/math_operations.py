def add(a, b):
    return a * b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) # called as a recursive function

