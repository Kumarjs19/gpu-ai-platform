from fastapi import Header, HTTPException
from jose import jwt

SECRET = "secret"

def get_user_id(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing token")
    try:
        data = jwt.decode(authorization, SECRET, algorithms=["HS256"])
        return data["user_id"]
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
