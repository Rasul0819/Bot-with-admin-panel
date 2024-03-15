from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

admins_menu = ReplyKeyboardMarkup(resize_keyboard=True)
admins_menu.add(KeyboardButton(text='Users'),KeyboardButton(text='Computers'))
admins_menu.add(KeyboardButton(text='Share adds'))

reg_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text='Registration'))
