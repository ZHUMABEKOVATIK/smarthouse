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

class ChatTypeEnum(Enum):
    private = "PRIVATE"
    group = "GROUP"

class Chats(Base):
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    chat_type: Mapped[ChatTypeEnum] = mapped_column(SQLEnum(ChatTypeEnum, name="chat_type_enum"))
    title: Mapped[str] = mapped_column(String(100), nullable=True)
    created_by: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id", ondelete="SET NULL"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    creator: Mapped["Users"] = relationship(back_populates="chats")