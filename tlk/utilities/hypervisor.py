import libvirt, os
import xml.etree.ElementTree as ET

from dotenv import load_dotenv
from tlk.utilities.bash import executeFile

load_dotenv()
PATH = os.getenv('PATH_TO_SCRIPT')
PATH_TO_STORAGE_POOL = os.getenv('PATH_TO_STORAGE_POOL')
#PATH=os.getenv('PATH_TO_TEST')


class Hypervisor:
    '''Implementing Libvirt functionalities form management virtual machines '''

    def __init__(self):
        self.conn = libvirt.open('qemu:///system')
        if self.conn == None:
            print('Hypervisor conection Failed!')
            exit(1)
    #End_def

    
    def createNewVirtualMachine(self, vmname):
       executeFile(PATH, 'clone-vm.sh', 'debian11-vm', vmname)
    #End_def


    def startVM(self, vmname):
        domain = self.conn.lookupByName(vmname)
        domain.create()
    #End_def
   

    def renameVM(self, oldname, newname):
        '''Rename some virtual machine ''' 
        domains = self.conn.listAllDomains()

        try:
            domain = self.conn.lookupByName(oldname)
            domain.rename(newname)
        except Exception as error:
            print("ERROR: ", type(error).__name__)
    #End_def

   
    def deleteVM(self, vmname):
        '''Delete some virtual machine if exists.'''
        domains = self.getVirtualMachineNames()
        
        if vmname in domains:
           '''vnmane Exists''' 
           domain = self.conn.lookupByName(vmname)

           if domain.state()[0] == 1: 
               print('The VM is running. Please Turn-off first !')
           else:
                domain = self.conn.lookupByName(vmname)
                domain.undefine()
                vdiskName = self.getVDiskName(vmname)
                storage_pool_path = PATH_TO_STORAGE_POOL
                storage_pool = self.conn.storagePoolLookupByTargetPath(storage_pool_path)
                storage_vol = storage_pool.storageVolLookupByName(vdiskName)
                storage_vol.delete(0)

        else:
            print('That VM  not exists !')    
    #End_def
    

    def getVDiskName(self, vmname):
        domain = self.conn.lookupByName(vmname)
        xml_desc = domain.XMLDesc()
        tree = ET.fromstring(xml_desc)
        disk_element = tree.find(".//disk[@device='disk']")
        disk_path = disk_element.find("source").get("file")
        disk_name = os.path.basename(disk_path)

        return disk_name
    #End_def


    def shutdownVM(self,vmname):
        ''' '''
        domain = self.conn.lookupByName(vmname)
        domain.shutdown()
    #End_def        


    def listVirtualMachines(self):
        ''' '''
        domains = self.conn.listAllDomains()
        vms = []
        
        for domain in domains:
            state = 'off'
            id = '-'
            
            if domain.state()[0]==1:
                state = 'Runnning' 
            
            if domain.ID() != -1:
                id = domain.ID() 
 
            vms.append({'id': id, 'vmname': domain.name(), 'state': state})
        
        return vms
    #End_def


    def getVirtualMachineNames(self):
        domains = self.conn.listAllDomains()
        onlynames = [] 
        for domain in domains:
            onlynames.append(domain.name())
        
        return onlynames
    #End_def
    
    
    def getNamesOfRunningVM(self):
        active_domains = self.conn.listDomainsID()
        only_actives = []
        for domain_id in active_domains:
            domain = self.conn.lookupByID(domain_id)
            only_actives.append(domain.name())

        if len(only_actives)==0:
            print('There are not Running Virtual Machine, press ENTER to exit!')
        
        only_actives.append('Cancel')
    
        return only_actives
    #End_def
            
    
    def getStoppedVM(self):
        defined_domains = self.conn.listDefinedDomains()
        only_stopped_vms = []
        print(defined_domains)

        return defined_domains
    #End_def


    def getHypervisorResources(self):
        pass
    #End_def

#End_class
