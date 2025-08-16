from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address (BaseModel):
    street: str
    city: str
    zip_code: str

class User (BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:$S")
        }
    )


user = User(
    id=1,
    name="Hitesh",
    email="h@hitesh.ai",
    createdAt=datetime(2024, 3, 15, 14, 30),
    address=Address(
        street="123 Main St",
        city="Anytown",
        zip_code="12345"
    ),
    tags=["developer", "python"],
    is_active=False
)

# https://docs.pydantic.dev/latest/concepts/serialization/#modelmodel_dump
python_dict = user.model_dump()
print(user)
print("=" * 40)
print(python_dict)


# https://docs.pydantic.dev/latest/concepts/serialization/#modelmodel_dump_json
json_str = user.model_dump_json()
print('=' * 40)
print(json_str)