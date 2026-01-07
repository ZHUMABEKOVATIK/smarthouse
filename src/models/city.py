from src.database.base import Base

from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship
)

from sqlalchemy import (
    BigInteger, 
    String
)

from src.models.users import Users

class City(Base):
    __tablename__ = "city"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    users: Mapped[list["Users"]] = relationship(back_populates="city")