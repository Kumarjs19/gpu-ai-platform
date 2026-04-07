# Simple cost estimator

PRICE_DB = {
    "Resistor": 2,
    "Capacitor": 5,
    "Power Supply": 100,
    "Other": 20
}

def estimate_cost(bom: dict):
    total = 0

    for item, qty in bom.items():
        base = item.split()[0]
        price = PRICE_DB.get(base, 10)
        total += price * qty

    return total
