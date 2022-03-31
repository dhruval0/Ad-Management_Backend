from fastapi import APIRouter, status, HTTPException
from server.utils.database import SessionLocal
from server.models.url import UrlPayload
from server.models.url import Url

router = APIRouter()
db = SessionLocal()

@router.post('/url', status_code=status.HTTP_201_CREATED)
def create_url(payload: UrlPayload):

    db_item = db.query(Url).filter(Url.id == payload.id).first()

    if db_item is not None:
        raise HTTPException(status_code=400, detail="url already exists")

    new_item = Url(
        id=payload.id,
        base_url=payload.base_url
    )

    db.add(new_item)
    db.commit()

    return {"status": 200, "message": "Base_url added successfully"}

@router.get('/url', status_code=200)
def get_all_urls():
    items = db.query(Url).all()

    return {"data": items, "status": 200, "message": "urls get successfully"}