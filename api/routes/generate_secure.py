from fastapi import APIRouter, Depends, HTTPException
from api.deps import get_user_id
from api.services.credit import deduct_credits

router = APIRouter()

@router.post("/generate_secure")
def generate(data: dict, user_id: str = Depends(get_user_id)):
    cost = 5
    if not deduct_credits(user_id, cost):
        raise HTTPException(status_code=402, detail="Insufficient credits")

    return {"status": "job accepted", "user": user_id}
