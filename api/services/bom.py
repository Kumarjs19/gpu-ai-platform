# Simple BOM generator from SPICE netlist

def generate_bom(netlist: str):
    bom = {}

    lines = netlist.split("\n")
    for l in lines:
        parts = l.strip().split()
        if not parts:
            continue

        comp = parts[0]

        if comp.startswith("R"):
            val = parts[3] if len(parts) > 3 else "unknown"
            key = f"Resistor {val}"

        elif comp.startswith("C"):
            val = parts[3] if len(parts) > 3 else "unknown"
            key = f"Capacitor {val}"

        elif comp.startswith("V"):
            key = "Power Supply"

        else:
            key = "Other"

        bom[key] = bom.get(key, 0) + 1

    return bom
