from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='О каких городах ты знаешь?')]], 
                            resize_keyboard=True,
                            input_field_placeholder="Выберите пункт меню...")

abis = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Достопримечательности'),
                                      KeyboardButton(text='Маршруты')],
                                    [KeyboardButton(text='Выбрать другой город')]],
                            resize_keyboard=True,
                            input_field_placeholder="Выберите пункт меню...")

cities = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Москва', callback_data='moscow')],
        [InlineKeyboardButton(text='Астана', callback_data='astana')],
        [InlineKeyboardButton(text='Нью-Йорк', callback_data='newyork')]])