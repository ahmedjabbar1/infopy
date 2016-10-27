#info bot created by negative
#info bot created by negative
#info bot created by negative
#info bot created by negative
import telebot
from telebot import types
import sys
import json
reload(sys)
sys.setdefaultencoding("utf-8")

bot = telebot.TeleBot("257403510:AAG-aZaQ2LjNrZkrrw73m8Yw3sUZ29tToQk")

@bot.message_handler(commands=['start', 'help'])
def welcome(m):
    bot.reply_to(m, "Hello I'm ID bot \n\n Send : \n  /id or /me or /info   \n or all pm text \n\n get your id : \n /idme (just pv)")

@bot.message_handler(commands=['id', 'ids', 'info', 'me'])
def id(m):      # info menu
    cid = m.chat.id
    title = m.chat.title
    usr = m.chat.username
    f = m.chat.first_name
    l = m.chat.last_name
    t = m.chat.type
    d = m.date
    text = m.text
    p = m.pinned_message
    fromm = m.forward_from
#info text
    bot.send_chat_action(cid, "typing")
    bot.reply_to(m, "*ID from* : ```{}``` \n\n *Chat name* : ```{}``` \n\n\n *Your Username* : ```{}``` \n\n *Your First Name* : ```{}```\n\n *Your Last Name* : ```{}```\n\n *Type From* : ```{}``` \n\n *Msg data* : ```{}```\n\n *Your Msg* : ```{}```\n\n* pind msg * : ```{}```\n\n *from* : ```{}```".format(cid,title,usr,f,l,t,d,text,p,fromm), parse_mode="Markdown")

@bot.message_handler(commands=['contact'])
def c(m):
    uid = m.chat.id
    bot.send_chat_action(uid, 'typing')
    bot.send_contact(uid, phone_number="9647826296458", first_name="ahmedjabbar")


@bot.message_handler(commands=['about']) # copy right Taylor Team
def p(m):
    uid = m.chat.id
    bot.send_chat_action(uid, 'typing')
    bot.send_message(uid, "TeamTop development Telegram bot and web mastering \n\n developers : \n [negative](https://telegram.me/TeamTop) \n [Parham](https://telegram.me/DevTop)", parse_mode="Markdown")
    bot.send_photo(uid, open('IMG_٢٠١٦١٠٢٧_١٨٠٧٠٤.png'), caption="@TeamTop")

@bot.message_handler(func=lambda m: m.chat.type == 'private', commands=['idme'])
def test_handler(m):
    cid = m.chat.id
    fl = m.chat.first_name
    bot.send_message(cid, "*{}*  Your ID = ```{}```".format(fl,cid), parse_mode="Markdown")
    

@bot.message_handler(func=lambda message: True)  # on pv all pm / group /id /me pm created by negative
def id(m):      # info menu
    cid = m.chat.id #id from
    title = m.chat.title #group title
    usr = m.chat.username #username
    f = m.chat.first_name #First name
    l = m.chat.last_name #last name
    t = m.chat.type #type
    d = m.date #data
    text = m.text #msg text
    p = m.pinned_message #msg pined
    fromm = m.forward_from #from 
#info text  by negative , taylor team copy right
    bot.send_chat_action(cid, "typing")
    bot.reply_to(m, "*ID from* : ```{}``` \n\n *Chat name* : ```{}``` \n\n\n *Your Username* : ```{}``` \n\n *Your First Name* : ```{}```\n\n *Your Last Name* : ```{}```\n\n *Type From* : ```{}``` \n\n *Msg data* : ```{}```\n\n *Your Msg* : ```{}```\n\n* pind msg * : ```{}```\n\n *from* : ```{}```".format(cid,title,usr,f,l,t,d,text,p,fromm), parse_mode="Markdown")
    


bot.polling()
#end
