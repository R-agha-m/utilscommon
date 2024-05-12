from pydantic import BaseModel


class Otp(BaseModel):
    resend_lock_duration_in_second: int
    validity_period_in_second: int
    number_of_characters: int
    allowed_characters: str
