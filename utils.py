import math

from telebot import types


def generate_keyboard_from_list(data, columns=1, resize_keyboard=True):
    __kbd = types.ReplyKeyboardMarkup(resize_keyboard=resize_keyboard)
    for i in range(math.ceil(len(data) / columns)):
        __kbd.row(*data[i * columns:(i + 1) * columns])
    return __kbd
