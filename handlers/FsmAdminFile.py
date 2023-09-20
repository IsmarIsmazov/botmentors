from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.client_kb import directions_markup
from database.bot_db import sql_command_insert
class FSMAdmin(StatesGroup):
    username = State()
    direction = State()
    grup = State()
    problem = State()
    numberhw = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.username.set()
        await message.answer(f"привет, {message.from_user.first_name}\n"
                             f'Пожалуйста напишите ваше имя')
    else:
        await message.answer('Пиши в личку!')


async def load_username(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    await FSMAdmin.next()
    await message.answer('Какой у вас направление?', reply_markup=directions_markup)


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer('В какой вы группе?\n'
                         'пример: \n'
                         '22.1, 33.2, 39.3')


async def load_grup(message: types.Message, state: FSMContext):
    try:
        if not 20 < float(message.text) < 40:
            await message.answer('такой группы не существует')
            await state.finish()
            return
        async with state.proxy() as data:
            data['grup'] = message.text
        await FSMAdmin.next()
        await message.answer('какие у вас проблемаы? попытайтесь описать его')
    except:
        await message.answer('пишите как было в примере')


async def load_problem(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['problem'] = message.text

    await FSMAdmin.next()
    await message.answer('Какой это по счёту домашняя работа?')


async def load_numberhw(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['numberhw'] = message.text
        await message.answer(f'{data["username"]}, {data["direction"]}, {data["grup"]}\n'
                             f'{data["problem"]}, {data["numberhw"]}')
    await FSMAdmin.next()
    await message.answer('Всё верно?')


async def cancel_help(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('отменено')


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await sql_command_insert(state)
        await state.finish()
        await message.answer('Сообщение было отправленно Старшему Ментору вашего направление\n'
                             'Скоро вам напишут ментор')
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer('Отменено')
    else:
        await message.answer('Не пон')


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_help, state='*', commands=['cancel'])
    dp.register_message_handler(fsm_start, commands=['helpmentors'])
    dp.register_message_handler(load_username, state=FSMAdmin.username)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_grup, state=FSMAdmin.grup)
    dp.register_message_handler(load_problem, state=FSMAdmin.problem)
    dp.register_message_handler(load_numberhw, state=FSMAdmin.numberhw)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
