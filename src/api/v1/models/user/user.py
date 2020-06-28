# Created by PyCharm Professional.
# User: romandemyanchuk
# Date: 6/25/20
# Time: 2:53 AM
# To change this template use File | Settings | File and Code Templates.

from typing import Union

from sqlalchemy.orm.exc import NoResultFound
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.api.models.user import UserInDB
from src.api.db.base import User
from src.api.db.queries.users import get_user_query


oauth2_token_scheme = OAuth2PasswordBearer(tokenUrl='api/v1/token')


class UserAuth:
    def __init__(self, user_model: UserInDB):
        self.user_model = user_model

    def get_user(self) -> Union[User or None]:
        try:
            user = get_user_query(user_model=self.user_model)
            return user
        except NoResultFound:
            return
