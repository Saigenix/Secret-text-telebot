from cryptography.fernet import Fernet
from boto.s3.connection import S3Connection
import os
import telebot


API_KEY = S3Connection(os.environ['API_KEY'])

print ("bot started")

bot = telebot.TeleBot(API_KEY, parse_mode=None)

wlctext = """
Hello !

✨To make Secret message use
/encrypt

✨To decrypt Secret message use
/decrypt

✨ For Help & More use
/help

❤️ Share this bot with your friends to start secret messaging !
@secretextbot

🧡 Made by @saigenix

 """
helptxt = """

This bot is very easy to use !

✨ To convert simple Text into secret text just use
 /encrypt command after that send your text !

✨ To convert encrypted text into normal text simply you have to use /decrypt command then send encrypted text
after that bot will send you normal text !

where to use?
You can use this bot to share personal or secret information secretly with anyone.

Note : Only this bot can decrypt secret messages , so sender and receiver both have to use this bot

❤️ Share this bot with your friends to start secret messaging !
@secretextbot

🧡 made by @saigenix
"""

enctext = """ Send a text which you want to convert into secret text """
dectext = """ Send a Secret or encrypted text which you want to convert into Normal text """

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, wlctext)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, helptxt)


@bot.message_handler(commands=['encrypt'])
def send_welcome(message):
    bot.reply_to(message, enctext)

    def check_msg2(msg4):
         if "*$^?" in msg4.text:
            return False
         else :
             return True
    @bot.message_handler(func=check_msg2 , content_types=['text'])
    def send_enc(msg) :
        txt = msg.text

        print(msg.from_user.first_name)
        print(msg.from_user.username)
        print(txt)
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encMessage = fernet.encrypt(txt.encode())
        send_txt = f"{key.decode()}*$^?{encMessage.decode()}"
        bot.send_message(msg.chat.id, send_txt)


@bot.message_handler(commands=['decrypt'])
def send_welcome(message):
    bot.reply_to(message, dectext)

    def check_msg(msg3):
         if "*$^?" in msg3.text:
            return True
         else :
            return False


    @bot.message_handler(func=check_msg , content_types=['text'])
    def send_enc(msge) :

        if "*$^?" in msge.text :
            dectxt = msge.text
            split_txt = dectxt.split("*$^?")
            key = split_txt[0].encode()
            fernet = Fernet(key)
            enctxt2 =split_txt[1].encode()
            decMessage = fernet.decrypt(enctxt2).decode()
            bot.send_message(msge.chat.id, decMessage)
        else :
             bot.send_message(msge.chat.id, "plz send valid text!")


bot.infinity_polling()
