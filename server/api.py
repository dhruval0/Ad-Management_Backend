from fastapi import FastAPI
from server.routes.crud import router as adRouter


app = FastAPI()


@app.get("/")
def news_scraper_home():
    return {"Welcome to": "postgres with fastapi"}


app.include_router(adRouter, tags=["ad"], prefix="/ad/v1")
