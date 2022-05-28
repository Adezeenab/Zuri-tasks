'''This python script, a simple Python CLI Calculator that can
perform addition, subtraction, division, multiplication 
and modulus operations. It can also accept user input.'''

# First user interaction interface
#print("Welcome to my Python CLI Calculator!\n")
username = input("Please enter your name: ")
print(f"Welcome, {username}", end="!")
print()

# Inform and user selects type of operations possible
print(f"What operation will {username} like to carryout?")
print("You may select from the following options")
print("For addition, enter 'A'")
print("For subtraction, enter 'B'")
print("For division, enter 'C'")
print("For multiplication, enter 'D'")
print("For modulus operation, enter 'E'\n")

operationChoice = input("Please enter your choice: ").upper()

# Collect user's operands
num1 = float(input("Please enter your first number:"))
num2 = float(input("Please enter the second number:"))

# Perform user's choice of operation
while operationChoice in ["A","B","C","D","E"]:
    if operationChoice == "A":
        result = (num1 + num2)
        print(f"The result of the operation ({num1} + {num2}) is: {result}" )
        break
    elif operationChoice == "B":
        result = (num1 - num2)
        print(f"The result of the operation ({num1} - {num2}) is: {result}" )
        break
    elif operationChoice == "C":
        result = (num1 / num2)
        print(f"The result of the operation ({num1} / {num2}) is: {result}" )
        break
    elif operationChoice == "D":
        result = (num1 * num2)
        print(f"The result of the operation ({num1} * {num2}) is: {result}" )
        break
    elif operationChoice == "E":
        result = num1 % num2
        print(f"The result of the operation ({num1} % {num2}) is: {result}" )
        break
else:
    print("You have not selected the right operation")
