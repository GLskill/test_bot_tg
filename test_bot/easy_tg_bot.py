import telebot
from test_bot.token import key


bot = telebot.TeleBot(key)


@bot.message_handlers(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, "Hello, Hello Mather Fucker!")


bot.polling()
