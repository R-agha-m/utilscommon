from pydantic import (
    BaseModel,
    conbytes,
)


class SchemaPassword(BaseModel):
    MINIMUM_LENGTH: int
    SALT: conbytes(
        min_length=16,
        max_length=16,
    )
