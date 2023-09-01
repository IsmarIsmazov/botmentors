from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMINS


# from Database.bot_db import sql_command_insert
class FSMAdmin(StatesGroup):
    name = State()
    direction = State()
    group = State()
    problem = State()
    numberhw = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.name.set()
        await message.answer(f"привет, {message.from_user.first_name}\n"
                             f'Пожалуйста напишите ваше имя')
    else:
        await message.answer('Пиши в личку!')

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.from_user.username
        print(data)



def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['helpmentors'])
    dp.register_message_handler(load_name, state=FSMAdmin.name, content_types=['text'])