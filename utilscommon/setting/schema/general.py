from typing import Annotated

from pydantic import (
    BaseModel,
    StringConstraints,
)


class SchemaGeneral(BaseModel):
    IS_PRODUCTION: bool
    APPLICATION_NAME: str
    PYTHONIC_APPLICATION_NAME: str
    APPLICATION_DESCRIPTION: str
    APPLICATION_VERSION: str
    DOCS_URL: Annotated[str, StringConstraints(pattern=r'^/.+$')] = "/docs"
    REDOCS_URL: Annotated[str, StringConstraints(pattern=r'^/.+$')] = "/redocs"
    HOST: Annotated[str, StringConstraints(pattern=r'^(http|https)://.+/$')] = "http://127.0.0.1:8000/"
