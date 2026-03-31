from sqlalchemy import Integer , Column  , String , DateTime
from app.core.database import Base
from datetime import datetime

class Post(Base):
    __tablename__='post'

    id=Column(Integer , primary_key=True , index=True)
    title=Column(String , nullable=False)
    content=Column(String, nullable=False)
    created_at=Column(DateTime, default=datetime.utcnow)

