from ..utils.vm_finder import VMFinder

def get_vm_info(vm_name):
    with VMFinder(host, user, password) as finder:
        vms = finder.search_vms({'nom': vm_name})
        if not vms:
            return None
        # Supposons que search_vms retourne une liste de VMs, prenez la première
        vm = vms[0]
        return {
            'name': vm.name,
            'status': vm.runtime.powerState,
            # Ajoutez d'autres informations pertinentes ici
        }