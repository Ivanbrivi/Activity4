from pydantic import BaseModel
from typing import Optional


class UserBO(BaseModel):
    id: Optional[int] = None
    username: str
    password: str
    mail: str
