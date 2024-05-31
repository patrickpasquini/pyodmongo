from pyodmongo import AsyncDbEngine, DbModel, DbResponse
from typing import ClassVar
import asyncio

engine = AsyncDbEngine(mongo_uri="mongodb://localhost:27017", db_name="my_db")


class Product(DbModel):
    name: str
    price: float
    is_available: bool
    _collection: ClassVar = "products"


class User(DbModel):
    name: str
    email: str
    password: str
    _collection: ClassVar = "users"


obj_list = [
    Product(name="Box", price="5.99", is_available=True),
    Product(name="Ball", price="6.99", is_available=True),
    User(name="John", email="john@email.com", password="john_pwd"),
]


async def main():
    response: dict[str, DbResponse] = await engine.save_all(obj_list)


asyncio.run(main())
