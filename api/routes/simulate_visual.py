from fastapi import APIRouter
from worker.app.pipelines.circuit_sim import run_spice
from worker.app.pipelines.spice_parser import parse_spice_output
from api.services.validator import detect_conflicts

router = APIRouter()

@router.post("/simulate-visual")
def simulate_visual(data: dict):
    netlist = data.get("netlist")

    raw = run_spice(netlist)
    parsed = parse_spice_output(raw.get("stdout",""))
    issues = detect_conflicts(parsed)

    return {
        "simulation": parsed,
        "issues": issues
    }
