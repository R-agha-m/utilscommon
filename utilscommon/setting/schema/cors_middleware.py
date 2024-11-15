from typing import (
    List,
    Optional,
)

from pydantic import BaseModel


class SchemaCorsMiddleware(BaseModel):
    ALLOW_ORIGINS: List[str] = ["*"]
    ALLOW_CREDENTIALS: bool = True
    ALLOW_METHODS: List[str] = ["*"]
    ALLOW_HEADERS: List[str] = ["*"]
    EXPOSE_HEADERS: List[str] = ["*"]
    ALLOW_ORIGIN_REGEX: Optional[str]= None
    MAX_AGE: int = 600
