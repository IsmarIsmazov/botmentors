import sqlite3
from config import bot
import random


def sql_create_mentors():
    global db, cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()

    if db:
        print('база данных подключен')
    db.execute(
        "CREATE TABLE IF NOT EXISTS mentors"
        "(id INTEGER PRIMARY KEY,"
        "username TEXT,"
        "direction TEXT,"
        "grup FLOAT, "
        "available INT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        values = tuple(data.values())
        cursor.execute("INSERT INTO mentors (username, direction, grup, available)"
                       " VALUES (?, ?, ?, ?)", values)

        db.commit()
