import telebot
import json

with open('config.json', 'r') as f:
    config = json.load(f)

bot = telebot.TeleBot(config['telegram_bot_token'])

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Grass Farm Bot!")

@bot.message_handler(commands=['status'])
def send_status(message):
    # Implement status checking logic here
    bot.reply_to(message, "All systems are operational!")

def send_message(chat_id, text):
    bot.send_message(chat_id, text)

def start_bot():
    bot.polling()
