from ..pydantic_mod.main import BaseModel


class ResponsePaginate(BaseModel):
    current_page: int
    page_quantity: int
    docs_quantity: int
    docs: list
