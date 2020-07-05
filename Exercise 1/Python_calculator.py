import python_operators

class Calculator:

    def calculate(self):

        #This is to provide options for the user to perform calculator functions
        print("Select which operation would you like to proceed with.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Working out the remainder")
        print("6.Working out the area of a triangle")


        choiceof_operation = int(input("Please choose which of the operations you would like to proceed with  "))
        #This is allowing the user to enter one of the options

        # This is gather the input of the user to complete the calculator function
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter the second number: "))

        # These are if and else statements, finding the user's choice of calculation and completing it using the python
        # operators file.

        if choiceof_operation == 1:
            print(python_operators.adding_values(num1, num2))

        elif choiceof_operation == 2:
            print(python_operators.subtracting_values(num1,num2))

        elif choiceof_operation == 3:
            print(python_operators.multiplying_values(num1, num2))

        elif choiceof_operation == 4:
            print(python_operators.dividing_values(num1, num2))

        elif choiceof_operation == 5:
            print(python_operators.modulous_values(num1, num2))

        elif choiceof_operation == 6:
            print("The area of the triangle is")
            print(python_operators.area_of_triangle(num1, num2))

        else:
            print("An error has occurred, please try again.")

ultimatecalculator = Calculator()
ultimatecalculator.calculate()

