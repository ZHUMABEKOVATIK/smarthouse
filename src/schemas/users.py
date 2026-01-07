from pydantic import BaseModel, Field, ConfigDict

class UserSignUp(BaseModel):
    lastname: str = Field(..., title="Фамилия", description="Фамилия, например: Тест", example="Тест")
    firstname: str = Field(..., title="Имя", description="Имя, например: Тест", example="Тест")
    area_id: int = Field(..., title="Облость", description="Облость, например: Тест", example="Тест")
    city_id: int = Field(..., title="Город", description="Город, например: Нукус", example="Нукус")
    phone: str = Field(..., title="Телефон", description="Телефон, например: 1234567", example="1234567")

class UserSignUpOut(BaseModel):
    access_token: str = Field(..., examples=["Test Access Token"])
    refresh_token: str = Field(..., examples=["Test Refresh Token"])
    token_type: str = Field(..., examples=["Test Type Token"])