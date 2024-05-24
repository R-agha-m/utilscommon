from pydantic import BaseModel


class SchemaMinIo(BaseModel):
    ROOT_USER: str
    ROOT_PASSWORD: str
    DEFAULT_BUCKETS: str
    SERVER_PORT: int
    DASHBOARD_PORT: int
