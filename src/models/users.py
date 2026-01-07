from src.database.base import Base
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, String, DateTime, func, ForeignKey
from datetime import datetime

if TYPE_CHECKING:
    from .area import Area
    from .city import City

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    lastname: Mapped[str | None] = mapped_column(String(100), nullable=True)
    firstname: Mapped[str] = mapped_column(String(100), nullable=False)
    area_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("area.id", ondelete="SET NULL"), nullable=True)
    city_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("city.id", ondelete="SET NULL"), nullable=True)
    phone: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    area: Mapped["Area"] = relationship(back_populates="users")
    city: Mapped["City"] = relationship(back_populates="users")
