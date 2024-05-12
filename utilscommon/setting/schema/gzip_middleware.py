from pydantic import BaseModel


class SchemaGZipMiddleware(BaseModel):
    MINIMUM_SIZE_IN_BYTE: int
