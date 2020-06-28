# Created by PyCharm Professional.
# User: romandemyanchuk
# Date: 13.06.2020
# Time: 23:47
# To change this template use File | Settings | File and Code Templates.

from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    joined: datetime = datetime.now()
    disabled: bool = False


class UserInDB(UserModel):
    password: str
