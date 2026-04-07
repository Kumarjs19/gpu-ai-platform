from fastapi import APIRouter
from worker.app.pipelines.circuit_sim import run_spice

router = APIRouter()

@router.post("/simulate")
def simulate(data: dict):
    netlist = data.get("netlist")
    result = run_spice(netlist)
    return result
