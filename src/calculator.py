#add function to add a & b
def add(a, b):
    return a + b

#subtract b from a, subtract function
def subtract(a, b):
    return a - b

#divide function, handling edge case
def divide(a, b):
    if b == 0:
        raise ValueError("impossible to divide by 0")
    return a / b
