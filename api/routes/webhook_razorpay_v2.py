from fastapi import APIRouter, Request
from api.services.credit import add_credits

router = APIRouter()

@router.post("/razorpay/webhook_v2")
async def webhook(req: Request):
    data = await req.json()

    if data.get("event") == "payment.captured":
        payment = data["payload"]["payment"]["entity"]
        user_id = payment.get("notes", {}).get("user_id")
        amount = payment.get("amount", 0) / 100
        credits = int(amount * 10)

        if user_id:
            add_credits(user_id, credits)

    return {"status": "ok"}
