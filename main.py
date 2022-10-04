import os
import telebot

API_KEY = os.getenv("API_KEY")

bot = telebot.TeleBot(API_KEY, parse_mode="HTML")

@bot.message_handler(commands=['start'])
def start(message):

    bot.send_message(message.chat.id, "<b>Hi there! I am online 🤖</b>")
    
bot.infinity_polling()
