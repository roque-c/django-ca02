#Menu-Driven Calculator-Script 
import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    print("Welcome to 11th grade's calculator")

    choices = input("""
          Please choose an operation by typing the number:
          1.Addition
          2.Subtraction
          3.Multiplication
          4.Division
          5.Exit
          -> """)
    try: 
        first_arg = float(input("Please enter a number: "))
        second_arg = float(input("Please enter a second number: "))
    except ValueError:
        print("Please enter a correct number.")
        continue


    if (choices == '1'):
        def addition(numA, numB):
            return numA + numB
        result = addition(first_arg, second_arg)
        operation = "adding"
        
    elif (choices == '2'):
        def subtraction(numA, numB):
            return numA - numB
        result = subtraction(first_arg, second_arg)
        operation = "subtracting"

    elif (choices == '3'):
        def multiplication(numA, numB):
            return numA * numB
        result = multiplication(first_arg, second_arg)
        operation="mulitplying"

    elif (choices == '4'):
        def division(numA, numB):
            try:
                return numA / numB
            except ZeroDivisionError:
                return ("Unable to divide by zero")
                
        result = division(first_arg, second_arg)
        operation="dividing"

    elif (choices == '5'):
        break

    clear_screen()
    print(f"{operation}  {first_arg} and {second_arg} equals {result}\n")

 
