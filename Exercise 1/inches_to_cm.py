import python_operators

class inch_to_cm:
    print("1. Inches to cm")
    print("2. Cm to inches")

    conversion_operation = int(input("Please enter the operation to continue "))
    num1 = int(input("Please enter a number "))

    if conversion_operation == 1:
        print(python_operators.inch_cm_values(num1))

    elif conversion_operation == 2:
        print(python_operators.cm_inch_values(num1))