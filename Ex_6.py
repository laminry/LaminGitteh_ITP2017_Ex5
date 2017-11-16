def calculator(no1, no2, operator="+", outoption="float"):
    try:
        if operator == "+":
            result = no1 + no2
        elif operator == "-":
            result = no1 - no2
        elif operator == "*":
            result = no1 * no2
        elif operator == "/":
            result = no1 / no2

        if outoption == "float" or operator == "/":
            return float(result)
        elif outoption == "int":
            return round(result)

    except ValueError:
        return None

print(calculator(2, 3.0))
print(calculator(2, 3.0, outoption="int"))
print(calculator(2, 3.0, "/"))
print(calculator(2, 3.0, "/", "int"))