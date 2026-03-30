from sqlalchemy import Integer , Column  , String , DateTime
from app.core.database import Base
from datetime import datetime

class Post(Base):
    __tablename__='post'

    id=Column(Integer , primary_key=True , index=True)
    title=Column(String , nullable=False)
    Content=Column(String, nullable=False)
    Created_at=Column(DateTime, default=datetime.utcnow)

