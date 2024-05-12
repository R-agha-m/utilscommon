from pydantic import BaseModel


class SchemaGeneral(BaseModel):
    IS_PRODUCTION: bool
    APPLICATION_NAME: str
    APPLICATION_DESCRIPTION: str
    APPLICATION_VERSION: str
