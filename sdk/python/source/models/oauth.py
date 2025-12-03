from pydantic import BaseModel
from dataclasses import dataclass


class OAuthToken(BaseModel):
    access_token: str
    expires_in: int


@dataclass
class Credentials:
    email: str
    client_name: str
    api_key: str
