from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL = "postgresql+psycopg://sheikhn:strongpassword@localhost:5432/blog_db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
