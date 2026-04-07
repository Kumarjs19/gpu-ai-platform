def detect_conflicts(data):
    issues = []

    voltages = data.get("voltages", {})
    currents = data.get("currents", {})

    # Simple rules
    for k,v in voltages.items():
        if abs(v) > 50:
            issues.append(f"High voltage risk at {k}: {v}V")

    for k,i in currents.items():
        if abs(i) > 1:
            issues.append(f"High current risk at {k}: {i}A")

    if not voltages:
        issues.append("No voltage detected (possible open circuit)")

    return issues
