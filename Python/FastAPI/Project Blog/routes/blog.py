from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select

from database import SessionDep
from models import Blog, User
from auth import get_current_user

router = APIRouter(prefix="/blog", tags=["Blog"])


@router.post("/", response_model=Blog, status_code=201)
def create_blog(
    blog: Blog,
    session: SessionDep,
    user: User = Depends(get_current_user),
):
    session.add(blog)
    session.commit()
    session.refresh(blog)
    return blog


@router.get("/", response_model=list[Blog])
def read_blogs(session: SessionDep):
    return session.exec(select(Blog)).all()


@router.get("/{blog_id}", response_model=Blog)
def read_blog(blog_id: int, session: SessionDep):
    blog = session.get(Blog, blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog
