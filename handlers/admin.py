from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot, dp, ADMINS
from database.bot_db_menty import sql_command_random, sql_command_delete, sql_command_all


async def delete_data(message: types.Message):
    if not message.from_user.id in ADMINS:
        await message.reply("Ты не мой босс!")
    else:
        users = await sql_command_all()
        for user in users:
            await bot.send_message(message.from_user.id, f'{user[1]}, {user[2]}, {user[3]}\n'
                                                         f'{user[4]}, {user[5]}',
                                   reply_markup=InlineKeyboardMarkup().add(
                                       InlineKeyboardButton(f"delete {user[1]}",
                                                            callback_data=f"delete {user[0]}")))


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace('delete ', ''))
    await call.answer(text="Удаленно с БД", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)


async def get_random_menty(message: types.Message):
    if not message.from_user.id in ADMINS:
        await message.reply("Ты не мой босс!")
    else:
        await sql_command_random(message)


async def ban(message: types.Message):
    if message.chat.type == 'group':
        if not message.from_user.id in ADMINS:
            await message.reply("Ты не мой босс!")
        elif not message.reply_to_message:
            await message.reply("Укажи кого кикнуть!")
        else:
            await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.answer(
                f"{message.from_user.first_name} братан кикнул пользователя "
                f"{message.reply_to_message.from_user.full_name}"
            )
    else:
        await message.answer("Пиши в группе!")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(get_random_menty, commands=['get_menty'])
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith('delete'))
