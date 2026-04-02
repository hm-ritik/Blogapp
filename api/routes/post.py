from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schema.design import PostCreate, PostResponse
from app.crud.post import (
    create_post,
    get_posts,
    get_post,
    update_post,
    delete_post
)

router = APIRouter(prefix="/posts", tags=["Posts"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=PostResponse)
def create(post: PostCreate, db: Session = Depends(get_db)):
    return create_post(db, post)


@router.get("/", response_model=list[PostResponse])
def read_all(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return get_posts(db, skip, limit)


@router.get("/{post_id}", response_model=PostResponse)
def read_one(post_id: int, db: Session = Depends(get_db)):
    post = get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.put("/{post_id}", response_model=PostResponse)
def update(post_id: int, post: PostCreate, db: Session = Depends(get_db)):
    updated = update_post(db, post_id, post)
    if not updated:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated


@router.delete("/{post_id}")
def delete(post_id: int, db: Session = Depends(get_db)):
    deleted = delete_post(db, post_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted"}