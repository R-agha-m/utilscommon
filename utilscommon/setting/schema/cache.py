from typing import Optional

from pydantic import BaseModel


class SchemaCache(BaseModel):
    CACHE_FOR_DB_ACTIONS: bool
    CACHE_FOR_ROUTERS: bool
    TIME_INTERVAL_TO_CLEAR_CACHE_IN_HOUR: Optional[int] = None
