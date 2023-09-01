import sqlite3
from config import bot
import random


def sql_create():
    global db, cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()

    if db:
        print('база данных подключен')
    db.execute(
        "CREATE TABLE IF NOT EXISTS anketa"
        "(id INTEGER PRIMARY KEY, fullname TEXT,"
        "direction TEXT, age INTEGER, grup TEXT)"
    )
    db.commit()