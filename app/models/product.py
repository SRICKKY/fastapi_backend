from typing import List
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description: str
    price: float

class ProductInDB(Product):
    id: str
