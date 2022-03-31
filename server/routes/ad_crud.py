from fastapi import APIRouter, status, HTTPException
from server.utils.database import SessionLocal
from server.models.ads import Payload
from server.models.ads import Item

router = APIRouter()
db = SessionLocal()


@router.get('/ads', status_code=200)
def get_all_ads():
    items = db.query(Item).all()

    return {"data": items, "status": 200, "message": "Ads get successfully"}


@router.get('/ads/{item_id}', status_code=status.HTTP_200_OK)
def get_an_ad(item_id: int):
    item = db.query(Item).filter(Item.id == item_id).first()

    return {"data": item, "status": 200, "message": "Ads retrive successfully"}


@router.post('/ads', status_code=status.HTTP_201_CREATED)
def create_ad(payload: Payload):

    db_item = db.query(Item).filter(Item.id == payload.id).first()

    if db_item is not None:
        raise HTTPException(status_code=400, detail="Ad already exists")

    new_item = Item(
        id=payload.id,
        ad_id=payload.ad_id,
        status=payload.status,
        created_at=payload.created_at,
        updated_at=payload.updated_at
    )

    db.add(new_item)
    db.commit()

    return {"status": 200, "message": "Ad added successfully"}


@router.put('/ads/{item_id}', status_code=status.HTTP_200_OK)
def update_an_ad(item_id: int, item: Payload):

    item_to_update = db.query(Item).filter(Item.id == item_id).first()
    item_to_update.id = item.id
    item_to_update.ad_id = item.ad_id,
    item_to_update.created_at = item.created_at,
    item_to_update.updated_at = item.updated_at,
    item_to_update.status = item.status

    db.commit()

    return {"status": 200, "message": "Ad updated successfully"}


@router.delete('/ads/{item_id}')
def delete_ad(item_id: int):
    item_to_delete = db.query(Item).filter(Item.id == item_id).first()

    if item_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Ad not found")

    db.delete(item_to_delete)
    db.commit()

    return {"data": item_to_delete, "status": 200, "message": "Ad delete successfully"}
