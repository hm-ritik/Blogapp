from fastapi import FastAPI
from app.model import post as model_post
from app.core.database import Base, engine
from app.api.routes import post as post_routes

app = FastAPI()

app.include_router(post_routes.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
async def health():
    return {"message": "API is running"}
