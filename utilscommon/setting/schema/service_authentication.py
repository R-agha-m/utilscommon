from typing import Optional

from pydantic import BaseModel


class ServiceAuthentication(BaseModel):
    hash_salt: Optional[str] = None
    hash_method_name: str
