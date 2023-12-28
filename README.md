# template_vmapi

### Structure du projet

mon_api_vmware/  
├── app/  
│   ├── __init__.py  
│   ├── main.py            # Point d'entrée de l'application FastAPI  
│   ├── dependencies.py    # Dépendances (comme les connexions DB, etc.)  
│   ├── routers/           # Routers FastAPI pour différentes routes  
│   ├── models/            # Modèles de données (si nécessaire)  
│   ├── services/          # Logique métier  
│   │   ├── __init__.py  
│   │   ├── vmware.py      # Service VMware  
│   ├── utils/             # Utilitaires (connexion vCenter, gestion des exceptions, etc.)  
│   │   ├── __init__.py  
│   │   ├── vcenter.py     # Module de connexion au vCenter  
│   │   └── exceptions.py  # Module des exceptions personnalisées  
├── tests/                 # Tests unitaires  
├── config/  
│   ├── logging.ini        # Configuration de logging  
├── requirements.txt       # Dépendances du projet  
└── Dockerfile             # Dockerfile pour le déploiement  


## Recherche de VM

```python
# application/services/vmware.py

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
```
