from pydantic import BaseModel


class SchemaApiKey(BaseModel):
    HEADER_NAME: str
    SECRET_KEY: str
