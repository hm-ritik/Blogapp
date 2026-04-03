from sqlalchemy.orm import Session 
from app.model.post import Post 
from app.schema.design import PostCreate

def create_post(db:Session , post:PostCreate):
    new_post=Post(
        title=post.title ,
        content=post.content
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_post(db:Session , post_id:int):
    return db.query(Post).filter(Post.id==post_id).first()

def get_posts(db:Session , skip: int = 0, limit: int = 10):
    return db.query(Post).offset(skip).limit(limit).all()

def  update_post(db:Session , post_id: int , post:PostCreate):
    existing_post=db.query(Post).filter(Post.id==post_id).first()

    if not existing_post:
        return None
    
    existing_post.title=post.title
    existing_post.content=post.content

    db.commit()
    db.refresh(existing_post)
    return existing_post

def delete_post(db:Session , post_id:int ):
    delete_user=db.query(Post).filter(Post.id==post_id).first()

    if not delete_user:
        return None
    
    db.delete(delete_user)
    db.commit()
    return delete_user





