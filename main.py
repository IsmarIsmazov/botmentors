import asyncio

from aiogram.utils import executor
from config import dp
import logging
from handlers import client, callback, extra, admin, FsmAdminFile, notifications, inline
from database.bot_db import sql_create

# async def on_startup(_):
#     # asyncio.create_task(notifications.scheduler())
#     sql_create()
#
extra.register_handlers_extra(dp)
admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
FsmAdminFile.register_handlers_fsm_anketa(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
