import asyncio

from aiogram.utils import executor
from config import dp
import logging
from handlers import client, callback, extra, admin, FsmMenty, notifications, inline, FsmMentor
from database.bot_db_menty import sql_create_menty
from database.bot_db_mentors import sql_create_mentors


async def on_startup(_):
    # asyncio.create_task(notifications.scheduler())
    sql_create_menty()
    sql_create_mentors()


admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
FsmMenty.register_handlers_fsm_menty(dp)
FsmMentor.register_handlers_fsm_mentor(dp)

extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
