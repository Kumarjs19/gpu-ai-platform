from fastapi import APIRouter
from passlib.context import CryptContext
from jose import jwt
import uuid

router = APIRouter()
pwd = CryptContext(schemes=["bcrypt"])
SECRET = "secret"

users = {}

@router.post("/signup")
def signup(data: dict):
    uid = str(uuid.uuid4())
    users[data["email"]] = {
        "id": uid,
        "password": pwd.hash(data["password"]),
        "credits": 0
    }
    return {"msg": "created"}

@router.post("/login")
def login(data: dict):
    user = users.get(data["email"])
    if not user or not pwd.verify(data["password"], user["password"]):
        return {"error": "invalid"}

    token = jwt.encode({"user_id": user["id"]}, SECRET, algorithm="HS256")
    return {"token": token}
