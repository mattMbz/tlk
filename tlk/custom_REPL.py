# Python utilities
import os, re
from dotenv import load_dotenv

# TLK imports
from tlk.bash import executeFile

load_dotenv()
PATH=os.getenv('PATH_TO_SCRIPT')
# TEST_PATH=os.getenv('PATH_TO_TEST')


menu='''
+====================================+
|  Qubik Hypervisor version 1.0.0    |
|  Author: Matias Barboza            |
+====================================+
|  Menu options:                     |
+====================================+
|  1. Create   VM                    |
|  2. Remove   VM                    |
|  3. Rename   VM                    |
|  4. Start    VM                    |
|  5. Shutdown VM                    |   
|  6. List     VM                    |
|  7. Monitor                        |
|  8. Exit                           |
+====================================+
'''


def custom_repl():
    while True:
        print(menu)
        
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
            print("Replacing virtual machine name ...")
            vm_name=input('Input VM name to replace >> ')
            new_vm_name=input('Input new VM name >> ')
            print()
            if(vm_name!='.abort'):
                executeFile(PATH, 'rename-vm.sh', vm_name, new_vm_name)

        elif option == "4":
            print("Starting virtual machine ...")
            vm_name=input('Input VM name >>')
            print()
            if(vm_name!='.abort'):
                executeFile(PATH, 'start-vm.sh', vm_name)

        elif option == "5":
            print("Shutting down virtual machine ...")
            vm_name=input('Input VM name >>')
            print()
            if(vm_name!='.abort'):
                executeFile(PATH, 'shutdown-vm.sh', vm_name)

        elif option == "6":
            print("Your virtual machines: ")
            print()
            executeFile(PATH, 'list-all.sh')

        elif option == "7":
            print("Hypervisor monitor :)")
            vm_name=input('Input VM name >>')
            print()
            if(vm_name!='.abort'):
                executeFile(PATH, 'run-monitor-vm.sh', vm_name)

        elif option == "8":
            print("Goodbye!")

        else:
            print("Invalid option, please enter a valid option !")

        response=input("Exit? (y/N): ")
        if(exit_repl(response)):
            break
        else:
            os.system('clear')
#End_of_def


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
#End_of_def


def parse_vm_name(vm_name):
    response=False
    vm_name=vm_name.lower()

    regex = r"^(?!.*\.{2,})[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*$"

    if re.match(regex, vm_name):
        response=True
    else:
        message(1)
    return response
#End_of_def


def message(code):
    if code==1:
        print('Invalid name, try without simbols!')
#End_of_def

## END
