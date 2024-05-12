from pydantic import BaseModel


class SchemaToken(BaseModel):
    VALIDITY_PERIOD_IN_DAYS: int
    ALGORITHM: str
    SECRET_KEY: str
    HEADER_KEY_NAME: str
