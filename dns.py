import requests
from bs4 import BeautifulSoup
import json
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import telegram
import datetime
import time
import re

bot_token = '1231763676:AAE-QQpkUxQQGZpFBCmF9KvQkj09uO1zi1I'
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

 
def start(update, context) :
    context.bot.send_message(chat_id=update.effective_chat.id, text= 'Принял. в 12.00 скину все товары',parse_mode=telegram.ParseMode.HTML)
    while True :
        message = ''
        with open('parser/sneakers_list.json', "r") as read_file:
            json_product = json.load(read_file)
        part = len(json_product)
        type_number = 0
        h = datetime.datetime.now()
        if h.hour == 12 :
            part = parser()
            while type_number < part:
                message += str(json_product[type_number]['title']) 
                message += '        <b>'
                message += str(json_product[type_number]['price'])
                message += '</b>\n'
                message += '\n'
                type_number += 1
                if type_number % 40 == 0 :
                    context.bot.send_message(chat_id=update.effective_chat.id, text= message ,parse_mode=telegram.ParseMode.HTML)
                    time.sleep(3)
                    message = ''
            context.bot.send_message(chat_id=update.effective_chat.id, text= 'Разъебано. Приходите завтра',parse_mode=telegram.ParseMode.HTML)
        time.sleep(600)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
