from pydantic import BaseModel


class SchemaKavehNegar(BaseModel):
    API_KEY: str
    TEMPLATE_NAME: str
