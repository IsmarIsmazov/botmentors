from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database.bot_db_techmentors import sql_command_insert
from keyboards.client_kb import directions_markup


class FSMTMentor(StatesGroup):
    username = State()
    direction = State()
    grup = State()
    available = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMTMentor.username.set()
        await message.answer(f"привет, {message.from_user.first_name}\n"
                             f'Пожалуйста напишите ваше имя')
    else:
        await message.answer('Пиши в личку!')


async def load_username(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    await FSMTMentor.next()
    await message.answer('Какой у вас направление?', reply_markup=directions_markup)


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMTMentor.next()
    await message.answer('В какой вы группе?\n'
                         'пример: \n'
                         '22.1, 33.2, 39.3')


async def load_grup(message: types.Message, state: FSMContext):
    try:
        if not 10 < float(message.text) < 70:
            await message.answer('такой группы не существует')
            await state.finish()
            return
        async with state.proxy() as data:
            data['grup'] = message.text
        await FSMTMentor.next()
        await message.answer('какие месяца вы можете менторить?\n'
                             'пример: 4, 1, 5')
    except:
        await message.answer('пишите как было в примере')


async def load_available(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['available'] = message.text
        await message.answer(f'{data["username"]}, {data["direction"]}, {data["grup"]}\n'
                             f'{data["available"]}')
    await FSMTMentor.next()
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
        await message.answer(f'Вы зарегистрированны как ментор')
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer('Отменено')
    else:
        await message.answer('Не пон')


def register_handlers_fsm_mentor(dp: Dispatcher):
    dp.register_message_handler(cancel_help, state='*', commands=['cancel'])
    dp.register_message_handler(fsm_start, commands=['regteshmentor'])
    dp.register_message_handler(load_username, state=FSMTMentor.username)
    dp.register_message_handler(load_direction, state=FSMTMentor.direction)
    dp.register_message_handler(load_grup, state=FSMTMentor.grup)
    dp.register_message_handler(load_available, state=FSMTMentor.available)
    dp.register_message_handler(submit, state=FSMTMentor.submit)
