from aiogram import types, Dispatcher
from config import bot, dp, ADMINS
import random
from .constants import helps, infos
from keyboards.client_kb import start_markup


async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}!\n'
                                                 f'Вот команды которые у нас есть: \n'
                                                 f'/info : Информация о менторстве и GeekCoin \n'
                                                 f'/mentors : список менторов которые могут вам помочь \n'
                                                 f'/techmentors : список тех-менторов которые могут вам помочь \n'
                                                 f'/help : помощь вам с дз \n'
                                                 f'/helpmentors : заполняете анкету и через некоторое время вам напишет ментор\n',
                                                 reply_markup=start_markup)


async def register(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'/helpmentors : заполняете анкету и через некоторое время вам напишет ментор\n',
                           )


# async def mentors(message: types.message):
#     await bot.send_message(message.from_user.id, )
# async def teshmentors(message: types.Message):
#     await bot.send_message(message.from_user.id, )


async def help(message: types.Message):
    await bot.send_message(message.from_user.id,
                           helps)


async def info(message: types.Message):
    await bot.send_message(message.from_user.id, infos)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(info, commands=['info'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(register,commands=['register'])
