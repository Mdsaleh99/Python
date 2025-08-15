from pydantic import BaseModel

# Always use type annotations
class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True # Default value is True


product_one = Product(id=1, name="Laptop", price=19.99, in_stock=True)
product_two = Product(id=2, name="Smartphone", price=9.99)
# product_three = Product(name="Tablet")