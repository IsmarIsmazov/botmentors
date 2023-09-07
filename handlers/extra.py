from aiogram import types, Dispatcher
from config import bot, dp


async def echo(message: types.Message):
    username = f'@{message.from_user.username}' \
        if message.from_user.username is not None else message.from_user.full_name
    bad_words = ['блятт', 'бля', 'дурак', "глупый", "черт", "блять", "сука", "гандон", "пидр", "бидр",
                 "негр", "нэгр", 'лох', "чмо", "пизда", "похуй"]
    for word in bad_words:
        if word in message.text.lower():
            await bot.delete_message(message.chat.id, message.message_id)
            await message.answer(
                f'Не матерись {username}'
            )


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)