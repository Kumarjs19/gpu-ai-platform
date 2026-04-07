from fastapi import APIRouter
from api.services.llm_generator import generate_netlist_llm

router = APIRouter()

@router.post("/generate-circuit-llm")
def generate(data: dict):
    prompt = data.get("prompt", "")
    netlist = generate_netlist_llm(prompt)
    return {"prompt": prompt, "netlist": netlist}
