from pydantic import BaseModel, Field
from datetime import datetime

class PostCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=40)
    content: str = Field(..., min_length=5)


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

    class Config:
        orm_mode = True


class PostListResponse(BaseModel):
    page: int
    size: int
    data: list[PostResponse]

