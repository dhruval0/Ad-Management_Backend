from fastapi import FastAPI
from server.routes.ad_crud import router as adRouter
from server.routes.url_crud import router as urlRouter


app = FastAPI()


@app.get("/")
def news_scraper_home():
    return {"Welcome to": "postgres with fastapi"}


app.include_router(adRouter, tags=["ad"], prefix="/ad/v1")
app.include_router(urlRouter, tags=["url"], prefix="/url/v1")
