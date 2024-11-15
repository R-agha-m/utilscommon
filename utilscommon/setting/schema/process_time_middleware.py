from typing import (
    List,
    Optional,
)

from pydantic import BaseModel


class SchemaProcessTimeMiddleware(BaseModel):
    ACTIVE: bool = True
