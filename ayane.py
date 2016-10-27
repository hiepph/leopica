from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
import logging

updater = Updater(token=open('telegram.token').read().rstrip())
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s \
                    - %(levelname)s - %(message)s', level=logging.INFO)


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Konnichiwa. Ayane desu~")

def ping(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Pong")

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

ping_handler = CommandHandler('ping', ping)
dispatcher.add_handler(ping_handler)

echo_handler = MessageHandler([Filters.text], echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
