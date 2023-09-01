from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

start_button = KeyboardButton('/start')
info_batton = KeyboardButton('/info')

start_markup.add(start_button, info_batton).add()

directions_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)
direction_a = KeyboardButton('Backend')
direction_b = KeyboardButton('Frontend')
direction_c = KeyboardButton('Android')
direction_d = KeyboardButton('IOS')
direction_e = KeyboardButton('UX/UI')

directions_markup.add(direction_a, direction_b, direction_c, direction_d, direction_e)
cancel_button = KeyboardButton('/cancel')
