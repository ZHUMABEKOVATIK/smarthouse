from src.database.base import Base
from typing import TYPE_CHECKING

from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship
)

from sqlalchemy import (
    BigInteger, 
    String
)

if TYPE_CHECKING:
    from src.models.users import Users

class City(Base):
    __tablename__ = "city"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    users: Mapped[list["Users"]] = relationship("Users", back_populates="city", lazy="selectin", passive_deletes=True)