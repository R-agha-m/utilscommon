from pydantic import BaseModel


class SchemaPagination(BaseModel):
    PAGE_SIZE: int
