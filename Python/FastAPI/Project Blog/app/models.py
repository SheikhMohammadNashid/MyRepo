from sqlmodel import Field, SQLModel


class Blog(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True, nullable=False)
    body: str = Field(nullable=False)
    published: bool = Field(default=False)


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, nullable=False)
    email: str = Field(index=True, unique=True, nullable=False)
    hashed_password: str
    is_active: bool = Field(default=True)
