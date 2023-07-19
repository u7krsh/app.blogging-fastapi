from pydantic import BaseModel


class Token_Schema(BaseModel):
    access_token: str
    token_type: str
