from sqlalchemy import BIGINT, VARCHAR
from enum import Enum as PyEnum
from sqlalchemy.orm import Mapped, mapped_column
from db import  Base
from db.utils import CreatedModel


class User(CreatedModel):
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, unique=True)
    tg_first_name: Mapped[str]
    username: Mapped[str] = mapped_column(VARCHAR, nullable=True)



metadata = Base.metadata
