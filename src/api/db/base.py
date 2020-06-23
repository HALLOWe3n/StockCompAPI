# Created by PyCharm Professional.
# User: romandemyanchuk
# Date: 11.06.2020
# Time: 22:47
# To change this template use File | Settings | File and Code Templates.

from passlib.hash import bcrypt

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from src.api.core.settings import POSTGRES_URI

engine = create_engine(POSTGRES_URI, echo=True)
Base = declarative_base()


class User(Base):
    """
    SQLAlchemy ORM model, user table
    """
    __tablename__: str = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(length=30))
    fullname = Column(String(length=40))
    email = Column(String(length=254), unique=True)
    password = Column(String)

    def __init__(
        self,
        username: str,
        fullname: str,
        email: str,
        password: str,
    ):
        self.username = username
        self.fullname = fullname
        self.email = email
        self.password = bcrypt(password)

    def validate_password(self, password: str):
        return bcrypt.verify(password, self.password)

    def __repr__(self):
        return f'<User -> username: {self.username}, fullname: {self.fullname}, email: {self.email}>'


class StockSymbol(Base):
    __tablename__: str = 'stocks'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    symbol = Column(String(5))
    description = Column(String(100))

    def __init__(self, name, symbol, description):
        self.name = name
        self.symbol = symbol
        self.description = description

    def __repr__(self):
        return f'<Stock: name - {self.name}, symbol - {self.symbol}, description - {self.description}>'
