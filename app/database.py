import os

from sqlalchemy import create_engine
from sqlalchemy import sessionmaker,declarative_base

DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv("POSTGRES_HOST")}"
    f"{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

engine = create_engine (DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflash=False,
    bind=engine
)

Base = declarative_base()