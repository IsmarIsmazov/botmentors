import sqlite3
from config import bot
import random


def sql_create_menty():
    global db, cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()

    if db:
        print('база данных менти подключен')
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


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM menty").fetchall()
    random_user = random.choice(result)
    await message.answer(f'{random_user[1]}, {random_user[2]}, {random_user[3]}\n'
                         f'{random_user[4]}, {random_user[5]}')


async def sql_command_all():
    return cursor.execute("SELECT * FROM menty").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM menty WHERE id = ?", (user_id,))
    db.commit()

