import telebot
import os


bot = telebot.TeleBot("5071959034:AAEUpOaKFOvKHQ2EzfyD1EB9uwa2y1xdfbo")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Worst bot ever seen.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
