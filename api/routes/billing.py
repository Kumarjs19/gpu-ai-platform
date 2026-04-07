from fastapi import APIRouter

router = APIRouter()

PLANS = {
  "free": {"credits": 50},
  "pro": {"credits": 1000},
  "team": {"credits": 10000}
}

@router.get("/plans")
def plans():
    return PLANS

@router.post("/subscribe")
def subscribe(data: dict):
    # TODO: integrate Razorpay subscription
    return {"status":"subscribed", "plan": data.get("plan")}
