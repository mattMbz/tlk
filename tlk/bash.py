import subprocess, os


def welcome():
    print("TLK is an interface. You can use TLK to communicate python with Linux OS, through Bash, Ansible or gRPC")
## end welcome


def version():
    print("version 0.1")
## end version


## Run bash files
def executeAllPath(path):
    pass
## end executeAllPath


def executeFile(path, filename, *params):
    path_script = os.path.join(path, filename)
        
    command=['bash', path_script]
    for param in params:
        command.append(param)

    print(f'Input command: {command}')
    
    subprocess.run(command)
## end executeFile