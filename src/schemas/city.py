from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class CreateCity(BaseModel):
    name: str = Field(
        ...,
        title="Название города",
        description="Введите название города, например: Нукус",
        example="Нукус"
    )

class CityOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., examples=[1])
    name: str = Field(..., examples=["Nukus"])
    created_at: datetime = Field(..., examples=["2026-01-07T12:34:56"])