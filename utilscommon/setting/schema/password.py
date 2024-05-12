from pydantic import (
    BaseModel,
    conbytes,
)


class SchemaPassword(BaseModel):
    minimum_length: int
    salt: conbytes(
        min_length=16,
        max_length=16,
    )
