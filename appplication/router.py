from . import logger
from . import app

from ..services.vmware import get_vm_info


@app.get("/vm-state/{vm_name}")
async def read_vm_state(vm_name: str):
    vm_info = get_vm_info(vm_name)
    if vm_info is None:
        raise HTTPException(status_code=404, detail="VM not found")
    return vm_info