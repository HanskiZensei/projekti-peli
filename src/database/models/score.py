from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class Score(Base):
    __tablename__ = "score"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(256))

    score: Mapped[int]

    def __repr__(self) -> str:
        return f"Score(id={self.id!r}, name={self.question!r}, score={self.difficulty!r})"
