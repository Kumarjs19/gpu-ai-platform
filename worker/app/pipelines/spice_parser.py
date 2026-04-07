import re

def parse_spice_output(output:str):
    voltages = {}
    currents = {}

    for line in output.splitlines():
        # Parse node voltages
        if "v(" in line.lower():
            parts = line.split()
            if len(parts) >= 2:
                voltages[parts[0]] = float(parts[-1])

        # Parse currents (basic heuristic)
        if "i(" in line.lower():
            parts = line.split()
            if len(parts) >= 2:
                currents[parts[0]] = float(parts[-1])

    return {
        "voltages": voltages,
        "currents": currents
    }
