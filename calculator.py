MENU_PROMPT = "\nSimple calculator program. Please select an option: \n1) Addition \n2) Subtraction \n3) Multiplication \n4) Division \n5) Exit Application\n"

def addition():

    add = int(input(f"Enter an integer: "))
    add2 = int(input(f"Enter another integer: "))

    print(f"The two integers added = {add+add2}")

def subtraction():

    minus = int(input(f"Enter an integer: "))
    minus2 = int(input(f"Enter another integer: "))

    print(f"The two integers subtracted = {minus-minus2}")

def multiplication():

    multiply = int(input(f"Enter an integer: "))
    multiply2 = int(input(f"Enter another integer: "))

    print(f"The two integers multiplied = {multiply*multiply2}")

def division():

    divide = int(input(f"Enter an integer: "))
    divide2 = int(input(f"Enter another integer: "))

    print(f"The two integers divided = {divide/divide2}")

# Used first class function 
user_options = {
    '1': addition,
    '2': subtraction,
    '3': multiplication,
    '4': division
}


def menu():

    selection = input(MENU_PROMPT)
    while selection != '5':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("Unknown command. Please try again.")

        selection = input(MENU_PROMPT)


menu()