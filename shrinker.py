from telegram.ext import MessageHandler, CommandHandler, Filters, Updater
import requests
import logging

logging.basicConfig(level=logging.INFO)

GP_API = "484c105293b3fa61508b7a81d3269d62b6b1cafc"
GP_URL = "https://gplinks.in/api?api={}&url={}"
TOKEN = "1311641915:AAEn-4Zkl35Y4FkJRsfVuOS6eI3nJ4qLGHQ"


def start(update, context):
	update.message.reply_text("Hi, I'm a GPLink Shortner bot!\nYou can short link using me.\nJust sent me your long URL")


def help(update, context):
	update.message.reply_text("Sent me any link!\n\n\nEnample:\nhttps://google.com\nhttps://bing.com")

def link_handler(update, context):
	long_link = update.message.text
	link = GP_URL.format(GP_API, long_link)
	req = requests.get(link)
	data = req.json()
	short_link = data["shortenedUrl"]
	print(long_link, "---", data["shortenedUrl"])
	update.message.reply_text("Here is your shorten link: \n"+short_link+"\n\nThanks for using me!")

def main():
	updater = Updater(TOKEN, use_context=True)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(MessageHandler(Filters.text & ~Filters.command, link_handler))
	updater.start_polling()
	updater.idle()


if __name__ == "__main__":
	main()