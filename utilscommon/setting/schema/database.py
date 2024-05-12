from typing import Optional

from pydantic import BaseModel


class SchemaDatabase(BaseModel):
    HOST: str
    PORT: int
    DATABASE: str
    USERNAME: Optional[str]
    PASSWORD: Optional[str]


class SchemaDatabaseWithAuthDb(BaseModel):
    HOST: str
    PORT: int
    DATABASE: str
    USERNAME: Optional[str]
    PASSWORD: Optional[str]
    AUTHDB: Optional[str] = None
