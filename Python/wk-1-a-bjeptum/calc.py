#!/usr/bin/python3
# Basic calculator that can perform addition, subtraction, multiplication, and division.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

if __name__ == "__main__":
    operation = input("Enter the operation in the format 'a b operator' (e.g., 10 5 +): ").strip()
    a, b, operator = operation.split()
    a, b = int(a.strip()), int(b.strip())

    if operator == '+':
        result = add(a, b)
        print("{} + {} = {}".format(a, b, result))
    elif operator == '-':
        result = subtract(a, b)
        print("{} - {} = {}".format(a, b, result))
    elif operator == '*':
        result = multiply(a, b)
        print("{} * {} = {}".format(a, b, result))
    elif operator == '/':
        result = divide(a, b)
        print("{} / {} = {}".format(a, b, result))
    else:
        print("Invalid operator. Please use one of +, -, *, /.")
