from pydantic import BaseModel


class SchemaOtp(BaseModel):
    RESEND_LOCK_DURATION_IN_SECOND: int
    VALIDITY_PERIOD_IN_SECONDS: int
    NUMBER_OF_CHARACTERS: int
    ALLOWED_CHARACTER: str
