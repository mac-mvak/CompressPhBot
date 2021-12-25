import telebot
import os


bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello it's compress bot. Send me photo and I will compress it.")


@bot.message_handler(content_types=['photo'])
def work_with_photo(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
