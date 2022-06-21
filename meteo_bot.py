import telebot
import random

bot = telebot.TeleBot('5536436535:AAGUeNnG4FUb7Oc_DBHd2bT2-txLWri7TNE')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start" or message.text == "Температура, вологість та тиск":
        t = random.uniform(27, 30)
        h = random.uniform(50, 60)
        p = random.uniform(1049, 1050)
        info = ''
        info += 'Температура °C - '
        info += "%.2f" % t
        info += '\n Вологість  - '
        info += "%.2f" % h
        info += '\n Атмосферний тиск hPa -'
        info += "%.2f" % p
        bot.send_message(message.chat.id, info)
    else:
        bot.send_message(message.chat.id, "Невідома команда")


bot.polling(none_stop=True, interval=0)