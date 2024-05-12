from pydantic import BaseModel


class SchemaCache(BaseModel):
    CACHE_FOR_DB_ACTIONS: bool
    CACHE_FOR_ROUTERS: bool
