from os import environ
from telegram.ext import MessageHandler, CommandHandler, Filters, Updater
from telegram import Update, ParseMode
import requests
import logging

from config import Config, Text

logging.basicConfig(level=logging.INFO)

SHORTNER_API = Config.SHORTNER_API
SHORTNER_URL = Config.SHORTNER_URL
BOT_TOKEN = Config.BOT_TOKEN
WELCOME_TEXT = Text.WELCOME_TEXT
HELP_TEXT = Text.HELP_TEXT
MAINTAINER = Text.MAINTAINER


def start(update, context):
	update.message.reply_text(WELCOME_TEXT, parse_mode="Markdown")


def help(update, context):
	update.message.reply_text(HELP_TEXT, parse_mode="Markdown")

def link_handler(update, context):
	long_link = update.message.text
	link = (SHORTNER_URL.format(SHORTNER_API, long_link))
	req = requests.get(link)
	data = req.json()
	short_link = data["shortenedUrl"]
	if short_link:
	    update.message.reply_text(f" *Here is your short* [link]({short_link})!\n\n*You can copy this link too!*\n`{short_link}`\n\n*Tnx for using me!*\n*Made with ❤ by @MudabbirulSaad*\n*Bot maintained by {MAINTAINER}*", parse_mode="Markdown")
	else:
	    update.message.reply_text("*You entered invalid url!*", parse_mode="Markdown")

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
