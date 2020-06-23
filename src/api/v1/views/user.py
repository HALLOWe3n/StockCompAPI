# Created by PyCharm Professional.
# User: romandemyanchuk
# Date: 13.06.2020
# Time: 23:51
# To change this template use File | Settings | File and Code Templates.

from fastapi import APIRouter

from src.api.models.user import UserModel

router = APIRouter()


@router.get('/profile/')
async def profile():
    """
    :return:
    """
    pass


@router.get('/user/create/')
async def create_user(user: UserModel):
    """
    ---
    \f
    :param user: pydantic model user
    :return:
    """
    pass
