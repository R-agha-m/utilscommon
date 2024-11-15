from typing import Optional,Any

from pydantic import BaseModel, field_validator


class SchemaDatabase(BaseModel):
    CONNECTION_STRING: Optional[str] = None
    HOST: Optional[str] = None
    PORT: Optional[int] = None
    DATABASE: Optional[str] = None
    USERNAME: Optional[str] = None
    PASSWORD: Optional[str] = None
    AUTHDB: Optional[str] = None


class SchemaDatabaseWithAuthDb(SchemaDatabase):
    pass
