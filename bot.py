import logging
import datetime
from typing import Text 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Привет, пользователь!")

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY) #создание бота и передача ему ключа для авторизации на сервере в телеграм

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user)) #Командуем боту начать входить в Telegram за сообщениями
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot activated")
    logging.info(datetime.datetime.now())    
    mybot.start_polling() #запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()
        
if __name__ == "__main__":
    main()        