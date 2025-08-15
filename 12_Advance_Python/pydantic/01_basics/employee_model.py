from pydantic import BaseModel, Field
from typing import Optional
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ..., # The ellipsis (...) indicates that this field is required
        min_length=2,
        max_length=10,
        description="Name of the employee",
        examples="Mohammed Saleh"
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge=10000,
        le=100000,
        description="Salary of the employee",
        examples=50000.0
    )

class User(BaseModel):
    email: str = Field(
        ...,
        regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        description="Email address of the user",
        examples="user@example.com"
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage for the user",
        examples=10.0
    )
