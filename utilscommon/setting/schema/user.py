from pydantic import BaseModel


class SchemaUser(BaseModel):
    SECRET_KEY: str
