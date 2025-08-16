from typing import List, Optional 
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address

address = Address(
    street="123 Main St",
    city="Anytown",
    postal_code="12345"
)

user = User(
    id=1,
    name="John Doe",
    address=address
)

user_data = {
    "id": 1,
    "name": "John Doe",
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "postal_code": "12345"
    }
}

user_from_data = User(**user_data)
print(user_from_data)