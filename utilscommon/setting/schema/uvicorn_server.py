from typing import Any

from pydantic import BaseModel
from ..enum import EnumLogLevel


class SchemaUvicornServer(BaseModel):
    def __init__(self, **data: Any):
        should_be_upper_list = ("log_level",)
        for i in should_be_upper_list:
            if i in data:
                data[i] = data[i].upper()

        super().__init__(**data)

    APP: str
    HOST: str
    PORT: int
    LOG_LEVEL: EnumLogLevel
    PROXY_HEADERS: bool
    FORWARDED_ALLOW_IPS: str
    RELOAD: bool
    LOOP: str
    WORKERS: int
    SERVER_HEADER: bool
