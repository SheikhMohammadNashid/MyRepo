from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


# -------------------- Model --------------------

class Blog(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True, nullable=False)
    body: str = Field(nullable=False)
    published: bool = Field(default=False, nullable=False)


# -------------------- Database --------------------

DATABASE_URL = "postgresql+psycopg://sheikhn:strongpassword@localhost:5432/blog_db"

engine = create_engine(
    DATABASE_URL,
    echo=True,          # show SQL queries (dev only)
    pool_pre_ping=True  # avoids stale connections
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


# -------------------- FastAPI App --------------------

app = FastAPI(title="Blog API")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# -------------------- Routes --------------------

@app.post("/blog/", response_model=Blog, status_code=201)
def create_blog(blog: Blog, session: SessionDep):
    session.add(blog)
    session.commit()
    session.refresh(blog)
    return blog


@app.get("/blog/", response_model=list[Blog])
def read_blogs(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    statement = select(Blog).offset(offset).limit(limit)
    blogs = session.exec(statement).all()
    return blogs


@app.get("/blog/{blog_id}", response_model=Blog)
def read_blog(blog_id: int, session: SessionDep):
    blog = session.get(Blog, blog_id)
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog


@app.delete("/blog/{blog_id}", status_code=204)
def delete_blog(blog_id: int, session: SessionDep):
    blog = session.get(Blog, blog_id)
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    session.delete(blog)
    session.commit()
