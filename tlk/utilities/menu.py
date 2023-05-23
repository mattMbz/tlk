# Python utilities
import os, re, inquirer
from prettytable import PrettyTable

# TLK imports
from tlk.utilities.hypervisor import Hypervisor


class CustomMenu():

    def __init__(self) -> None:
        self.input = MenuInput()
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
            
            #Write your code here ...
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
            if response == 'n' or response == 'no':
                ex=False
            elif response == 'y' or response == 'yes':
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
        self.qubik = Hypervisor()
        self.keyword = '.cancel'
    #End_def

    def run(self, option):

        # Option 1 is when we want create new virtual machine
        if option == "1":
            print("Creating new virtual machine")
            questions = [inquirer.Text('input', message="Input the name of new VM")]
            answers = inquirer.prompt(questions)
            vm_name = answers['input']
            
            if(vm_name != self.keyword.lower()):
                if self.parse_vm_name(vm_name):
                    self.qubik.createNewVirtualMachine(vm_name)

            self.output.starts(vm_name)
        
        elif option == "2":
            print("Removing virtual machine")
            print(self.qubik.getVirtualMachineNames())
            questions = [inquirer.Text('input', message="Input VM name to remove")]
            
            answers = inquirer.prompt(questions)
            vm_name = answers['input']
            print()
            if(vm_name!=self.keyword.lower()):
                self.qubik.deleteVM(vm_name)
                #executeFile(PATH, 'remove-vm.sh', vm_name)
        
        elif option == "3":
            print("Replacing virtual machine name ...")
            questions = [
                inquirer.Text('vm_name', message="Input VM name to replace"),
                inquirer.Text('new_vm_name', message="Input new VM name")
            ]
            answers = inquirer.prompt(questions)
            vm_name = answers['vm_name']
            new_vm_name = answers['new_vm_name']
            print()

            if(vm_name != self.keyword.lower()):
                self.qubik.renameVM(self)


        elif option == "4":
            print("Starting virtual machine ...")
            choiceValues = self.qubik.getStoppedVM()
            choiceValues.append(self.keyword)
            questions = [
                inquirer.List(
                    'option',
                    message="Select any option",
                    choices=choiceValues
                )
            ]
            answers = inquirer.prompt(questions)
            vm_name = answers['option']
            print()
            print(f'has seleccionado {vm_name}')

            if(vm_name != self.keyword.lower()):
                #executeFile(PATH, 'start-vm.sh', vm_name)
                self.qubik.startVM(vm_name)

        elif option == "5":
            print("Shutting down virtual machine ...")
            choiceValues = self.qubik.getNamesOfRunningVM()
            choiceValues.append(self.keyword)
            questions = [
                inquirer.List(
                    'option',
                    message="Select any option",
                    choices=choiceValues
                ),
            ]
            answers = inquirer.prompt(questions)
            selected_options = answers['option']
            
            print()
            if(selected_options != self.keyword.lower()):
                #executeFile(PATH, 'shutdown-vm.sh', selected_options)
                self.qubik.shutdownVM(selected_options)
                
        elif option == "6":
            print("Your virtual machines: ")
            print()
            self.qubik = Hypervisor()
            vm_list =  self.qubik.listVirtualMachines()
            table = PrettyTable()
            table.field_names = ["Id","Virtual Machine","State"]
            for vm in vm_list:
                table.add_row([value for value in vm.values()])
            print(table)
            only_names = self.qubik.getVirtualMachineNames()

        elif option == "7":
            questions = [
                inquirer.List(
                    'resource', 
                    message="Select any option",
                    choices=['RAM', 'CPU', self.keyword ]
                ),
                inquirer.List(
                    'vm',
                    message="Select your virtual machine",
                    choices=['Debian11-vm', 'vm01', 'guarani3.16', self.keyword]
                )
            ]

            answers = inquirer.prompt(questions)
            resource = answers['resource']
            vmToConfig= answers['vm']

            if resource == 'RAM':
                choiceValues = ['512M','768M','1G', '2G']
            elif resource == 'CPU':
                choiceValues = ['1 vCPU', '2 vCPU', '4 vCPU']

            if (resource != self.keyword.lower()) and (vmToConfig != self.keyword.lower()):
                questions = [
                    inquirer.List(
                        'option',
                        message=f'Select {resource}',
                        choices=choiceValues
                    )
                ]
                answers = inquirer.prompt(questions)
                selected = answers['option']
                print(f'Values {vmToConfig} -> {selected}')
                #executeFile(PATH, f'config-{resource}.sh', vmToConfig, selected.split(' ')[0])

        elif option == "8":
            print("Hypervisor monitor :)")
            questions = [inquirer.Text('input', message="Input VM name")]
            answers = inquirer.prompt(questions)
            vm_name = answers['input']
            print()

            if(vm_name != self.keyword.lower()):
                pass
                #executeFile(PATH, 'run-monitor-vm.sh', vm_name)

        elif option == "9":
            print("Goodbye!")
        
        else:
            print("Invalid option, please enter a valid option !")
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
#####End_class


class MenuOutput():

    def __init__(self) -> None:
        pass
    #End_def

    def starts(self, option):
        print(f'The output was: {option}')
    #End_def
#####End_Class

## END
