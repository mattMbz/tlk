# Python utilities
import os
from dotenv import load_dotenv

# Import TLK Functionalities
from tlk.bash import executeFile

## Write your custom repl
def repl():
    while True:
        # Display the menu options
        print("Menu options:")
        print("1.Option 1")
        print("2.Option 2")
        print("3.Option 3")
        print("3.Exit")

        # Ask the user to input an option
        option = input("Enter an option: ")

        # Evaluate the user's input
        if option == "1":
            print("You selected Option 1")
        elif option == "2":
            print("You selected Option 2")
        elif option == "3":
            print("You selected Option 2")
        elif option == "4":
            print("Goodbye!")
        else:
            print("Invalid option, please enter a valid option.")

        response=input("Exit? (y/N): ")
        if(exit_repl(response)):
            break
        else:
            os.system('clear')
## End of repl function


def exit_repl(response):
    go_out=True
    response=response.lower()
    if response=='n' or response =='no':
        go_out=False
    return go_out
## End exit_repl function

repl()