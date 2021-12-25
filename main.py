import telebot
import os
from PIL import Image


bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))


@bot.message_handler(commands='start')
def send_welcome(message):
    bot.reply_to(message, "Hello it's compress bot."
                          " Send me photo and I will compress it.")


@bot.message_handler(commands='help')
def work_with_help(message):
    bot.reply_to(message, "Send me photo and I will compress it.")


@bot.message_handler(content_types=['photo'])
def work_with_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    image = open("image1.jpg", "wb")
    image.write(downloaded_file)
    photo = Image.open("image1.jpg")
    compressed = photo.resize((photo.size[0]//10, photo.size[1]//10))
    photo = compressed.resize(photo.size)
    photo.save("image1.jpg")
    file = open("image1.jpg", "rb")
    bot.send_photo(message.chat.id, file)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Not a photo!")


bot.infinity_polling()
