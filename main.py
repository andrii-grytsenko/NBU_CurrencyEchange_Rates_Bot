import telebot

import NBUCurrencyClasses as nbu
import actor
import command_processor as cmd_proc
import config
from state import STATES

bot = telebot.TeleBot(config.BOT_TOKEN)
cp = cmd_proc.CommandProcessor()
actor_list = actor.ActorList()


@bot.message_handler(commands=["start", "help"])
def cmd_start(message):
    _actor = actor_list.get_actor(message)
    print(" ".join(map(str, [_actor.get_state(), _actor.get_id()])))
    print(message.from_user.username)
    bot.reply_to(message, STATES["START"]["message"], reply_markup=STATES["STATE01"]["keyboard"])


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    _actor = actor_list.get_actor(message)
    print(" ".join(map(str, [_actor.get_state(), _actor.get_id()])))
    print(message.from_user.username)
    text = message.text.upper()
    if text == "START" or text == "HELP":
        cmd_start(message)
    elif text == "BACK":
        bot.send_message(message.chat.id, STATES["STATE01"]["message"], reply_markup=STATES["STATE01"]["keyboard"])
    elif text == "GET ALL CURRENCIES":
        get_currencies_list(message)
    elif len(text) != 3:
        bot.reply_to(message, "Unknown command.")
    else:
        get_currency_rate(message, text[:3])


def get_currency_rate(message, currency=""):
    currency_list = nbu.CurrencyRateList()
    if currency_list.update(currency):
        text = currency_list.get_currency_rate(currency)
    else:
        text = "Error"
    bot.send_message(message.chat.id, text, reply_markup=STATES["STATE01"]["keyboard"])


def get_currencies_list(message):
    bot.send_message(message.chat.id, STATES["STATE02"]["message"], reply_markup=STATES["STATE02"]["keyboard"])


def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
