from pydantic import BaseModel
from server.utils.database import Base
from sqlalchemy import String, Boolean, Integer, Column, DateTime


class Payload(BaseModel):  # serializer
    id: int
    ad_id: str
    status: bool
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    ad_id = Column(String(20), nullable=True)
    status = Column(Boolean, default=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
