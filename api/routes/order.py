from fastapi import APIRouter
from api.services.bom import generate_bom
from api.services.cost import estimate_cost
from api.services.supplier import place_supplier_order

router = APIRouter()

@router.post("/order")
def create_order(data: dict):
    netlist = data.get("netlist","")
    bom = generate_bom(netlist)
    cost = estimate_cost(bom)

    supplier_resp = place_supplier_order(bom)

    return {
        "bom": bom,
        "cost": cost,
        "supplier": supplier_resp
    }
