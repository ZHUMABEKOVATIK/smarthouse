from src.database.base import Base

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)
from sqlalchemy import (
    BigInteger,
    Enum as SQLEnum,
    DateTime,
    String,
    func
)
from sqlalchemy.dialects.postgresql import UUID
from enum import Enum
from datetime import datetime

class TransactionState(str, Enum):
    created = "CREATED"
    performed = "PERFORMED"
    cancelled = "CANCELLED"

class PaymeTransactions(Base):
    __tablename__ = "payme_transactions"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    payme_transaction_id: Mapped[str] = mapped_column(UUID(as_uuid=True), unique=True, nullable=False)
    account_order_id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True)
    amount: Mapped[int] = mapped_column(BigInteger, nullable=False)
    state: Mapped[TransactionState] = mapped_column(SQLEnum(TransactionState, name = "transaction_state_type"), default=TransactionState.created)
    create_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    perform_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    cancel_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    reason: Mapped[str | None] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())