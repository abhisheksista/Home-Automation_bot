
from telegram.ext import Updater, MessageHandler, Filters
from Adafruit_IO import Client
aio=Client('Abhishek_sista', 'aio_dCmg60c2XwzMvhcVw23CSDaXVECJ')

def demo1(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Okay, light is turned on')
  aio.send('light',1)

def demo2(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Okay, light is turned off')
  aio.send('light',0)

def demo3(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Okay, fan is turned on')
  aio.send('fan',2)

def demo4(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Okay, fan is turned off')
  aio.send('fan',0)

def main(bot,update):
  a= bot.message.text.lower()
  if a =="turn on light":
    demo1(bot,update)
  elif a =="turn off light":
    demo2(bot,update)
  elif a =="turn on fan":
    demo3(bot, update)
  elif a =="turn off fan":
    demo4(bot, update)
bot_token = '1944629476:AAE5dX_4jdxs0lgXyEgC6Lfd6_LpZDUZ-NY'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()

