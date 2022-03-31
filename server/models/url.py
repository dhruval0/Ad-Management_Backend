from pydantic import BaseModel
from server.utils.database import Base
from sqlalchemy import String, Integer, Column


class UrlPayload(BaseModel):
    id: int
    base_url: str

    class Config:
        orm_mode = True


class Url(Base):
    __tablename__ = 'url'
    id = Column(Integer, primary_key=True)
    base_url = Column(String(20))
