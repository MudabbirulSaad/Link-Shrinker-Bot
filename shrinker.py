from os import environ
from telegram.ext import MessageHandler, CommandHandler, Filters, Updater
import requests
import logging

logging.basicConfig(level=logging.INFO)

SHORTNER_API = environ.get('SHORTNER_API')
SHORTNER_URL = environ.get('SHOERNER_URL')
BOT_TOKEN = environ.get('BOT_TOKEN')


def start(update, context):
	update.message.reply_text("Hi, I'm a GPLink Shortner bot!\nYou can short link using me.\nJust sent me your long URL")


def help(update, context):
	update.message.reply_text("Sent me any link!\n\n\nEnample:\nhttps://google.com\nhttps://bing.com")

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