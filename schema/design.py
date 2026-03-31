from pydantic import BaseModel
from datetime import datetime 
#schema define their own structure 

class PostCreate(BaseModel):  #request body
    title:str
    content:str

class PostResponse(BaseModel):
    id:int
    title:str
    content:str
    created_at: datetime

    class Config:
         orm_mode = True

