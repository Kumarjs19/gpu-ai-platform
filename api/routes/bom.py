from fastapi import APIRouter
from api.services.bom import generate_bom
from api.services.cost import estimate_cost

router = APIRouter()

@router.post("/bom")
def bom(data: dict):
    netlist = data.get("netlist", "")
    bom = generate_bom(netlist)
    cost = estimate_cost(bom)

    return {
        "bom": bom,
        "estimated_cost": cost
    }
