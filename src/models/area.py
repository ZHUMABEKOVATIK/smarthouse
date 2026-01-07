from src.database.base import Base

from sqlalchemy.orm import (
    Mapped, 
    mapped_column, 
    relationship
)

from sqlalchemy import (
    BigInteger, 
    String, 
    DateTime, 
    func, 
    Enum as SQLEnum,
    ForeignKey
)

from datetime import datetime
from enum import Enum

from src.models.users import Users

class Area(Base):
    __tablename__ = "area"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    users: Mapped[list["Users"]] = relationship(back_populates="area", lazy="selectin")