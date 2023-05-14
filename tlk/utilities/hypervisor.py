import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('No se pudo conectar a hypervisor')
    exit(1)

# Nombre de la VM que deseamos monitorear
vm_name = 'nombre_vm'

# Buscar la VM por su nombre
vm = conn.lookupByName(vm_name)
if vm == None:
    print('No se pudo encontrar la VM')
    exit(1)