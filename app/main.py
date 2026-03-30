from fastapi import FastAPI
from app.model import post
from app.core.database import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/health")
async def health():
    return {"message": "API is running"}
