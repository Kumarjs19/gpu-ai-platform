from fastapi import APIRouter

router = APIRouter()

# Simple rule-based AI generator (can upgrade to LLM later)

def generate_netlist(prompt: str):
    prompt = prompt.lower()

    if "water level" in prompt:
        return """* Water level controller (basic)
V1 1 0 DC 12
R1 1 2 10k
R2 2 0 10k
R3 2 3 1k
Q1 3 2 0 NPN
.op
.end"""

    if "voltage divider" in prompt:
        return """* Voltage Divider
V1 1 0 DC 10
R1 1 2 1k
R2 2 0 1k
.op
.end"""

    return """* Default resistor
V1 1 0 DC 5
R1 1 0 1k
.op
.end"""

@router.post("/generate-circuit")
def generate(data: dict):
    prompt = data.get("prompt","")
    netlist = generate_netlist(prompt)

    return {
        "prompt": prompt,
        "netlist": netlist
    }
