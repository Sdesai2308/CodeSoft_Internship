#Basic calculator
print("Choose 1 for addition")
print("Choose 2 for subtraction")
print("Choose 3 for multiplication")
print("Choose 4 for division")
print("Choose 5 for Exit!!!!!")

def getInput():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return num1 , num2
flag = True
while(flag):
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        num1, num2 = getInput()
        print(f"addition of {num1} and {num2} is {num1+num2}")
    elif(choice == 2):
        num1, num2 = getInput()
        print(f'subtraction of {num1} from {num2} is {num2 - num1}')
    elif(choice == 3):
        num1, num2 = getInput()
        print(f'multiplication of {num1} and {num2} is {num1*num2}')
    elif(choice == 4):
        num1, num2 = getInput()
        print(f'division of {num1} by {num2} is {num1 / num2}')
    elif(choice == 5):
        flag = False
    else:
        print('Wrong Choice')
        

    
