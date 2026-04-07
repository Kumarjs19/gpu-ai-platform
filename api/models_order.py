from sqlalchemy import Column, String, Integer, DateTime
from api.db import Base
import uuid, datetime

class Order(Base):
    __tablename__ = "orders"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String)
    status = Column(String, default="created")
    total_cost = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    order_id = Column(String)
    component = Column(String)
    quantity = Column(Integer)
