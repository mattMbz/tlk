# Python utilities
import os
from dotenv import load_dotenv

# TLK imports
from tlk.bash import executeFile

load_dotenv()
PATH=os.getenv('PATH_TO_SCRIPT')
# TEST_PATH=os.getenv('PATH_TO_TEST')

qubik='''
+====================================+
|  Qubik Hypervisor version 1.0.0    |
|  Author: Matias Barboza            |
+====================================+
'''

def custom_repl():
    while True:
        print(qubik)
        # Display the menu options
        print("Menu options:")
        print("1. Create VM")
        print("2. Remove VM")
        print("3. Rename VM")
        print("4. Monitor")
        print("5. Exit")
    
        # Ask the user to input an option
        option = input("Enter an option: ")
        print()
    
        # Evaluate the user's input
        if option == "1":
            print("Creatring new virtual machine")
            vm_name=input('Input your virtual machine name >> ')
            executeFile(PATH, 'clone-vm.sh', 'debian11-vm', vm_name)

        elif option == "2":
            print("Removing virtual machine")
            vm_name=input('Input your virtual machine name >> ')
            executeFile(PATH, 'remove-vm.sh', vm_name)
        
        elif option == "3":
            print("This feature is not implemented yet! =(")

        elif option == "4":
            print("This feature is not implemented yet! =(")

        elif option == "5":
            print("Goodbye!")

        else:
            print("Invalid option, please enter a valid option.")

        response=input("Exit? (y/N): ")
        if(exit_repl(response)):
            break
        else:
            os.system('clear')
## End custom_repl

def exit_repl(response):
    ex=True
    response=response.lower()
    if response=='n' or response =='no':
        ex=False
    return ex
## End exit_repl function