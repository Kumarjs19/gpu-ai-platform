import subprocess
import tempfile
import json

# Simple ngspice runner

def run_spice(netlist:str):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".cir") as f:
        f.write(netlist.encode())
        path = f.name

    cmd = ["ngspice", "-b", path]
    result = subprocess.run(cmd, capture_output=True, text=True)

    return {
        "stdout": result.stdout,
        "stderr": result.stderr
    }
