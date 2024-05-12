from pydantic import BaseModel


class Emta(BaseModel):
    url: str
    api_url: str
    client_id: str
    client_secret: str
    callback_url: str
