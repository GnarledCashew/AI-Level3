num1 = float(input("Enter First Value: "))  # Float 1
num2 = float(input("Enter Second Value: "))  # Float 2
operation = str( #Provides the user with the different arithematic operations available
    input(
        "What would you like to do with your numbers?\n"
        "A) Addition\n"
        "B) Subtraction\n"
        "C) Division\n"
        "D) Multiplication\n"
        "Select an option: " 
    )
).lower() # Forces the answer provided to be in lowercase

if operation not in ["a", "b", "c", "d"]: # error handling to ensure a valid input
    print("That wasn't a valid input")
elif operation == "a":
    print("Your total is " + str(num1 + num2)) #Addition operation
elif operation == "b":
    print("Your total is " + str(num1 - num2)) #Subtraction operation
elif operation == "c":
    if num2 == 0:
        print("Cannot divide by zero") #Division error handling
    else:
        print("Your total is " + str(num1 / num2)) #Division operation
elif operation == "d":
    print("Your total is " + str(num1 * num2)) #Multiplication operation