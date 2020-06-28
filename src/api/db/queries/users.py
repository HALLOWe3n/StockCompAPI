# Created by PyCharm Professional.
# User: romandemyanchuk
# Date: 6/27/20
# Time: 2:19 AM
# To change this template use File | Settings | File and Code Templates.

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from ..base import engine, User
from src.api.models.user import UserInDB


def get_user_query(user_model: UserInDB) -> User:
    session = Session(bind=engine)
    user = session.query(User).filter(User.username == user_model.username)

    if not user:
        raise NoResultFound

    return user.first()
