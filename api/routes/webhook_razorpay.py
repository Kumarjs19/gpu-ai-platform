from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/razorpay/webhook")
async def webhook(req: Request):
    data = await req.json()
    # TODO: verify signature
    if data.get("event") == "payment.captured":
        # update user credits in DB
        pass
    return {"status":"ok"}
