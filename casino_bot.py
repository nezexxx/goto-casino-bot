from telebot import TeleBot
import location_manager
import os

try:
    from config import token
except:
    token = os.environ['S3_SECRET']

from locations.userr import users

bot = TeleBot(token)



# users = {}

def send_help(chat_id):
    bot.send_message(chat_id, "help")

@bot.message_handler(content_types=['text'])
def process_message(message):
    chat_id = message.chat.id

    if chat_id not in users:
        users[chat_id] = {
            "balance": 400,
            "id": chat_id,
            "location": "menu"
        }
        location_manager.change_location(users[chat_id], "menu", users, bot, location_manager)

    user = users[chat_id]
    if "/help" in message.text:
        send_help(chat_id)
    elif "Меню" in message.text:
        location_manager.change_location(user, "menu", users, bot, location_manager)
    else:
        location = user['location']
        manager = location_manager.locations_managers[location]
        manager.process_message(message, user, users, bot, location_manager)

bot.polling(none_stop=True)