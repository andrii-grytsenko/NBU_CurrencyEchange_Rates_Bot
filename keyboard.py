from telebot import types

import NBUCurrencyClasses as nbu
import utils

kbd_main_screen = types.ReplyKeyboardMarkup(resize_keyboard=True)
kbd_main_screen.row('USD', 'EUR')
kbd_main_screen.row('GBP', 'CHF')
kbd_main_screen.row('Get all currencies')

kbd_all_currencies = kbd_main_screen
currency_list = nbu.CurrencyRateList()
if currency_list.update():
    text = sorted(currency_list.get_currencies_list())
    kbd_all_currencies = utils.generate_keyboard_from_list(text, 10)
    kbd_all_currencies.row("back")
