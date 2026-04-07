from fastapi import APIRouter

router = APIRouter()

@router.get("/usage/me")
def usage():
    return {
        "total_requests": 10,
        "images": 4,
        "text": 6,
        "credits_used": 50
    }
