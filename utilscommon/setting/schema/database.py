from typing import Optional

from pydantic import BaseModel


class SchemaDatabase(BaseModel):
    CONNECTION_STRING: Optional[str]
    HOST: str
    PORT: int
    DATABASE: str
    USERNAME: Optional[str]
    PASSWORD: Optional[str]


class SchemaDatabaseWithAuthDb(BaseModel):
    CONNECTION_STRING: Optional[str]
    HOST: str
    PORT: int
    DATABASE: str
    USERNAME: Optional[str]
    PASSWORD: Optional[str]
    AUTHDB: Optional[str] = None
