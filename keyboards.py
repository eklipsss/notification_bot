from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('Создать напоминание')
b2 = KeyboardButton('Текущие дела')
b3 = KeyboardButton('Выполненные дела')
b4 = KeyboardButton('Меню')
kb_start.add(b1).insert(b2).add(b3).insert(b4)



