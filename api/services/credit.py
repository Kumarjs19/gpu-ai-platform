from api.db import SessionLocal
from api.models import User

def deduct_credits(user_id, cost):
    db = SessionLocal()
    user = db.query(User).filter(User.id==user_id).first()
    if not user or user.credits < cost:
        return False
    user.credits -= cost
    db.commit()
    return True

def add_credits(user_id, credits):
    db = SessionLocal()
    user = db.query(User).filter(User.id==user_id).first()
    if user:
        user.credits += credits
        db.commit()
