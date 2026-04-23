import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:

    from dotenv import load_dotenv
    load_dotenv()
    DATABASE_URL = os.getenv("DATABASE_URL")

print(f"Connecting to: {DATABASE_URL}")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set in the environment!")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine

)



Base = declarative_base()
