import math

def fact():
    try:
        return math.factorial(int(input("Enter number:\n")))
    except ValueError:
        return None

print(fact())