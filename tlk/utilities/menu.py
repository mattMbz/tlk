# Python utilities
import os, re
from dotenv import load_dotenv

# TLK imports
from tlk.bash import executeFile

load_dotenv()
#PATH=os.getenv('PATH_TO_SCRIPT')
PATH=os.getenv('PATH_TO_TEST')


class CustomMenu():

    def __init__(self) -> None:
        self.input = MenuInput()
        self.output = MenuOutput()
    #End_def

    def show(self, header, items):
        '''Create the option menu'''

        while True:
            # Print the menu header
            print("+====================================+")

            for i in range(len(header)):
                print(f"| {header[i]:34} |")

            print("+====================================+")
            print("|  Menu options:                     |")
            print("+====================================+")

            # Print the menu items
            for i in range(len(items)):
                print(f"|  {i+1}. {items[i]:30} |")

            print("+====================================+")
            
            self.input.starts()

            response=input("Confirm exit? (y/N): ")
            if(self.exit(response)):
                break
            else:
                os.system('clear')
    #End_def

    def exit(self, response):
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

#End_class


class MenuInput():
    def __init__(self) -> None:
        self.process = Process()
    
    def starts(self):
        option = input("Enter an option: ")
        self.process.run(option)

#End_Class


class Process():

    def __init__(self) -> None:
        self.output = MenuOutput()
    #End_def

    def run(self, option):

        # Option 1 is when we want create new virtual machine
        if option == "1":
            print("Creating new virtual machine")
            vm_name=input('Input the name of new VM name >> ')
            self.output.starts(vm_name)
            if(vm_name!='.cancel'):
                if self.parse_vm_name(vm_name):
                    executeFile(PATH, 'clone-vm.sh', 'debian11-vm', vm_name)
    #End_def

    def parse_vm_name(self, vm_name):
        response=False
        vm_name=vm_name.lower()

        regex = r"^(?!.*\.{2,})[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*$"

        if re.match(regex, vm_name):
            response=True
        else:
            self.message(1)
        return response
    #End_def

    def message(self, code):
        if code==1:
            print('Invalid name, try without simbols!')
    #End_def

#End_class


class MenuOutput():

    def __init__(self) -> None:
        pass
    #End_def

    def starts(self, option):
        print(f'The output was: {option}')
    #End_def
#End_Class

## END
