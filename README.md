# PyODMongo

![Image title](https://raw.githubusercontent.com/mauro-andre/pyodmongo/mkdocs/docs/assets/images/pyodmongo_Logo_BG_White.png)

[![PyPI - Version](https://img.shields.io/pypi/v/pyodmongo)](https://pypi.org/project/pyodmongo/)

`pyodmongo` is a Python library that serves as an Object-Document Mapper (ODM) for MongoDB. It is built on top of the popular `pydantic V2` library, making it easy to work with MongoDB documents in a Pythonic and efficient way.

With `pyodmongo`, you can seamlessly map your Python classes to MongoDB documents, allowing you to work with data in a more intuitive and Pythonic manner. It simplifies the process of defining and interacting with MongoDB collections, documents, and queries.

## Key Features

- **Integration with pydantic**: Leverage the power of pydantic's data validation and modeling capabilities while working with MongoDB data.

- **Automatic Schema Generation**: Define your MongoDB schema using pydantic models, and `pyodmongo` will automatically create the necessary MongoDB collections and ensure data consistency.

- **Query Builder**: Easily construct complex MongoDB queries using Python code, reducing the need for writing raw query strings.

- **Document Serialization**: Serialize and deserialize Python objects to and from MongoDB documents effortlessly.

- **Async Support**: Take advantage of asynchronous programming with `pyodmongo` to enhance the performance of your MongoDB operations.

- **Active Development**: `pyodmongo` is actively developed and maintained, with new features and improvements being regularly added.

## Installation

You can install `pyodmongo` using pip:

```bash
pip install pyodmongo
```

## Contributing

Contributions to `pyodmongo` are welcome! If you find any issues or have ideas for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/mauro-andre/pyodmongo).

## License
`pyodmongo` is licensed under the MIT License. See the [LICENSE file](https://github.com/mauro-andre/pyodmongo/blob/master/LICENSE) for more information.


## Async exemple

```python hl_lines="5"
from pyodmongo import AsyncDbEngine, DbModel
from typing import ClassVar
import asyncio

engine = AsyncDbEngine(mongo_uri='mongodb://localhost:27017', db_name='my_db')


class Product(DbModel):
    name: str
    price: float
    is_available: bool
    _collection: ClassVar = 'products'


box = Product(name='Box', price='5.99', is_available=True)


async def main():
    result = await engine.save(box)

asyncio.run(main())
```

## Sync exemple

```python hl_lines="4"
from pyodmongo import DbEngine, DbModel
from typing import ClassVar

engine = DbEngine(mongo_uri='mongodb://localhost:27017', db_name='my_db')


class Product(DbModel):
    name: str
    price: float
    is_available: bool
    _collection: ClassVar = 'products'


box = Product(name='Box', price='5.99', is_available=True)

result = engine.save(box)
```