from os import getenv
import os
from dotenv import load_dotenv

load_dotenv('.env')


class Bot:
    TOKEN = os.getenv("TOKEN")
    ADMIN = os.getenv("ADMIN")


class DB:
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")

    DB_URL = f"postgresql+asyncpg://postgres:1@{DB_HOST}:5432/{DB_NAME}"


class Env:
    bot = Bot()
    db = DB()
