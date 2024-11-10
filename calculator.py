#calculator
number1 = eval(input("Enter first number: "))
number2 = eval(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /, %): ")

def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def divide(number1, number2):
    if number2 != 0:
        return number1 / number2
    else:
        return "Error! Division by zero."

def multiply(number1, number2):
    return number1 * number2

def modulus(number1, number2):
    if number2 != 0:
        return number1 % number2
    else:
        return "Error! Modulus by zero."

if operator == '+':
    result = add(number1, number2)
elif operator == '-':
    result = subtract(number1, number2)
elif operator == '*':
    result = multiply(number1, number2)
elif operator == '/':
    result = divide(number1, number2)
elif operator == '%':
    result = modulus(number1, number2)
else:
    result = "Invalid operator! Please use one of +, -, *, /, %."

print(f"Result: {result}")
