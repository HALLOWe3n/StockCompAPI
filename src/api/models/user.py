# Created by PyCharm Professional.
# User: romandemyanchuk
# Date: 13.06.2020
# Time: 23:47
# To change this template use File | Settings | File and Code Templates.

from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    username: str
    email: EmailStr
    password: str
