import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def power(base, exponent):
    return base ** exponent

def square_root(num):
    return math.sqrt(num)

def logarithm(num, base):
    return math.log(num, base)

def sine(angle):
    return math.sin(angle)

def cosine(angle):
    return math.cos(angle)

def tangent(angle):
    return math.tan(angle)

print("Select the operation you want to perform:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square Root")
print("7. Logarithm")
print("8. Sine")
print("9. Cosine")
print("10. Tangent")

choice = int(input("Enter your choice (1/2/3/4/5/6/7/8/9/10): "))

if choice in [1, 2, 3, 4, 5]:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == 2:
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == 3:
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == 4:
        print(num1, "/", num2, "=", divide(num1, num2))

    elif choice == 5:
        print(num1, "^", num2, "=", power(num1, num2))

elif choice in [6, 7, 8, 9, 10]:
    num = float(input("Enter the number: "))

    if choice == 6:
        print("Square root of", num, "=", square_root(num))

    elif choice == 7:
        base = float(input("Enter the base: "))
        print("Log", num, "with base", base, "=", logarithm(num, base))

    elif choice == 8:
        print("Sine of", num, "=", sine(num))

    elif choice == 9:
        print("Cosine of", num, "=", cosine(num))

    elif choice == 10:
        print("Tangent of", num, "=", tangent(num))

else:
    print("Invalid Input")
