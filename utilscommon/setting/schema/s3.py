from pydantic import BaseModel


class S3(BaseModel):
    endpoint_url: str
    aws_access_key_id: str
    aws_secret_access_key: str
    signature_version: str
    region_name: str
    bucket_name: str
    folder_name: str
    server_address: str
