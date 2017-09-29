def add(num1, num2):
    """Return num1 + num2."""
    return num1+num2

def sub(num1, num2):
    """Return num1-num2"""
    return num1 - num2

def mul(num1, num2):
    """Return num1 * num2"""
    return num1 * num2

def div(num1, num2):
    """Return num1 / num2"""
    return num1 / num2

def runoperation(operation, num1, num2):
    """Operation s based on input"""
    if (operation == 1 or operation == '+'):
        print(add(num1, num2))
    elif (operation == 2 or operation == '-'):
        print(sub(num1, num2))
    elif (operation == 3 or operation == '*'):
        print(mul(num1, num2))
    elif (operation == 4 or operation == '/'):
        print(div(num1, num2))
    else:
        print("I don't understand")

def main():

    user_continue = True

    while user_continue:
        validinput = False
        while not validinput:
            try:
                num1 = int(input("Enter 1st number :: "))
                num2 = int(input("Enter 2nd number :: "))
                operation = int(input("What do you want to do? "
                                      "(Type 1 for add, Type 2 for sub, Type 3 for mul, Type 4 for div) :: "))
                validinput = True
            except:
                print("Invalid Input Try Again")

            runoperation(operation,num1,num2)

        user_choice = input("Would you like to continue? (Y for yes and any other key to continue) : : ")
        if(user_choice != 'y'):
            user_continue = False
            break
        else:
            continue

if __name__ == '__main__':
    main()