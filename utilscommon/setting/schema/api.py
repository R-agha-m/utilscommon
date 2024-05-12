from pydantic import BaseModel


class SchemaApi(BaseModel):
    PATH: str
    API_KEY: str
