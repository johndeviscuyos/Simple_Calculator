import pyfiglet

#Ask the user if the operation is Addition, Subtraction, Multiplication and Division.
print("Welcome to the Simple Calculator")
print("This calculator will help you in simple Addition, Subtraction, Multiplication or Division")
#Ask the user to type the letter of the corresponding operation eg. A for Addition, S for Subtraction, M for Multiplication and D for Division.
while True:
    try:
        operation = str(input("Type A for Addition, S for Subtraction, M for Multiplication or D for Division: "))
        if operation in ('A', 'S', 'M', 'D'):
            #Ask the user to enter the first number
            first_number = float(input("Enter the first number: "))
            #Ask the user to enter the second number
            second_number = float(input("Enter the second number: "))
            #show the result
            if operation == 'A':
                result = first_number + second_number
                print ("The result is: ", result)
                art_text = pyfiglet.figlet_format(text=str(result),
                                                  font="slant")

                print(art_text)
            if operation == 'S':
                result = first_number - second_number
                print ("The result is:", result)
                art_text = pyfiglet.figlet_format(text=str(result),
                                                  font="slant")

                print(art_text)
            if operation == 'M':
                result = first_number * second_number
                print ("The result is:", result)
                art_text = pyfiglet.figlet_format(text=str(result),
                                                  font="slant")

                print(art_text)
            if operation == 'D':
                result = first_number / second_number
                print("The result is ", result)
                art_text = pyfiglet.figlet_format(text=str(result),
                                                  font="slant")

                print(art_text)
        else:
            print("Invalid input please try again")
    #Show an exception if user inputs an integer.
    except ValueError:
        print("Invalid input please try again")
    except ZeroDivisionError:
        print("You are dividing by zero")

    # Ask the user if he/she wants to try it again.

    try_again = str(input("Do you want to try again? Y/N: "))
    if try_again != 'Y':
        break


