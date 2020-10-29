from os import environ
from telegram.ext import MessageHandler, CommandHandler, Filters, Updater
import requests
import logging

from config import Config, Text

logging.basicConfig(level=logging.INFO)

SHORTNER_API = environ.get('SHORTNER_API', Config.SHORTNER_API)
SHORTNER_URL = environ.get('SHOERNER_URL', Config.SHORTNER_URL)
BOT_TOKEN = environ.get('BOT_TOKEN', Config.BOT_TOKEN)
WELCOME_TEXT = environ.get('WELCOME_TEXT', Text.WELCOME_TEXT)
HELP_TEXT = environ.get('HELP_TEXT', Text.HELP_TEXT)


def start(update, context):
	update.message.reply_text(WELCOME_TEXT)


def help(update, context):
	update.message.reply_text(HELP_TEXT)

def link_handler(update, context):
	long_link = update.message.text
	link = (SHORTNER_URL.format(SHORTNER_API, long_link))
	req = requests.get(link)
	data = req.json()
	short_link = data["shortenedUrl"]
	print(long_link, "---", data["shortenedUrl"])
	update.message.reply_text("Here is your shorten link: \n"+short_link+"\n\nThanks for using me!")

def main():
	updater = Updater(BOT_TOKEN, use_context=True)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(MessageHandler(Filters.text & ~Filters.command, link_handler))
	updater.start_polling()
	updater.idle()


if __name__ == "__main__":
	main()