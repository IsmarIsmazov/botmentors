from aiogram import types, Dispatcher
from config import bot, dp, ADMINS


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
