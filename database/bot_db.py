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
        "CREATE TABLE IF NOT EXISTS menty"
        "(id INTEGER PRIMARY KEY,"
        "username TEXT,"
        "direction TEXT,"
        "grup FLOAT, "
        "problem TEXT,"
        "numberhw INT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        values = tuple(data.values())
        cursor.execute("INSERT INTO menty (username, direction, grup, problem, numberhw)"
                       " VALUES (?, ?, ?, ?, ?)", values)

        db.commit()
