# Created by PyCharm Professional.
# User: romandemyanchuk
# Date: 11.06.2020
# Time: 19:43
# To change this template use File | Settings | File and Code Templates.

import os
import sys
import logging

import psycopg2
from dotenv import load_dotenv

ENV = load_dotenv('.env')
LOCALHOST = 'localhost'
DEBUG = sys.gettrace()

# MARK:
# ----
# logger
logger = logging.getLogger(__name__)
formatter = logging.Formatter(fmt='%(asctime)s:%(levelname)s:%(name)s:%(message)s', datefmt='%Y-%m-%d %H:%M:%S')

try:
    file_handler = logging.FileHandler('logs/settings.log')
except FileNotFoundError:
    os.mkdir('logs')
    file_handler = logging.FileHandler('logs/settings.log')

file_handler.setFormatter(formatter)

logger.setLevel(logging.INFO)
logger.addHandler(file_handler)

# MARK:
# ----
# POSTGRES
POSTGRES_CONFIG = {
    'POSTGRES_DB': os.getenv('POSTGRES_DB'),
    'POSTGRES_USER': os.getenv('POSTGRES_USER'),
    'POSTGRES_PASSWORD': os.getenv('POSTGRES_PASSWORD'),
    'POSTGRES_HOST': os.getenv('POSTGRES_HOST'),
    'POSTGRES_PORT': os.getenv('POSTGRES_PORT')
}

POSTGRES_URI = f'postgresql://{POSTGRES_CONFIG["POSTGRES_USER"]}:{POSTGRES_CONFIG["POSTGRES_PASSWORD"]}@' \
               f'{POSTGRES_CONFIG["POSTGRES_HOST"] if not DEBUG else LOCALHOST}/{POSTGRES_CONFIG["POSTGRES_DB"]}'

try:
    psycopg2.connect(
        database=POSTGRES_CONFIG['POSTGRES_DB'],
        user=POSTGRES_CONFIG['POSTGRES_USER'],
        password=POSTGRES_CONFIG['POSTGRES_PASSWORD'],
        host=POSTGRES_CONFIG['POSTGRES_HOST'],
    )
    logger.info('Connection to database is successfully')
except psycopg2.OperationalError:
    logger.error('Database isn\'t connect, check POSTGRES URI or POSTGRES constants', )
