from fastapi import FastAPI

from database import create_db_and_tables
from routes import users, blog

app = FastAPI(title="Blog API")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(users.router)
app.include_router(blog.router)
