# Python utilities
import os, re
from dotenv import load_dotenv

# TLK imports
from tlk.bash import executeFile
from tlk.virtualMachines import monitor

load_dotenv()
PATH=os.getenv('PATH_TO_SCRIPT')
GLOBALS_PATH=os.getenv('PATH_TO_GLOBAL')
# TEST_PATH=os.getenv('PATH_TO_TEST')


menu='''
+====================================+
|  Qubik Hypervisor version 1.0.0    |
|  Author: Matias Barboza            |
+====================================+
|  Menu options:                     |
+====================================+
|  1. Create VM                      |
|  2. Remove Vm                      |
|  3. Rename Vm                      |   
|  4. Monitor                        |
|  5. Exit                           |
+====================================+
'''

def custom_repl():
    while True:
        print(menu)
        executeFile(GLOBALS_PATH, 'globals.sh')
        # Ask the user to input an option
        option = input("Enter an option: ")
        print()
    
        # Evaluate the user's input
        if option == "1":
            print("Creating new virtual machine")
            vm_name=input('Input the name of new VM name >> ')
            print()
            if(vm_name!='.abort'):
                if parse_vm_name(vm_name):
                    executeFile(PATH, 'clone-vm.sh', 'debian11-vm', vm_name)

        elif option == "2":
            print("Removing virtual machine")
            vm_name=input('Input VM name to remove >> ')
            print()
            if(vm_name!='.abort'):
                executeFile(PATH, 'remove-vm.sh', vm_name)
        
        elif option == "3":
            print("This feature has not been implemented yet! =(")
            vm_name=input('Input VM name>> ')
            print()
            if(vm_name!='.abort'):
                executeFile(PATH, 'scr01.sh')

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
    default_regex = r"^(\s+)?$"
    response=response.lower()
    if re.match(default_regex, response):
        ex=False
    else:
        if response=='n' or response =='no':
            ex=False
        elif response=='y' or response == 'yes':
            ex=True
        else:
            ex=False
        
    return ex
## End of exit_repl()


def parse_vm_name(vm_name):
    response=False
    vm_name=vm_name.lower()

    regex = r"^(?!.*\.{2,})[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*$"

    if re.match(regex, vm_name):
        response=True
    else:
        message(1)
    return response
## End of parse_vm_name()


def message(code):
    if code==1:
        print('Invalid name, try without simbols!')
## End of parse_vm_name()
