from telebot import TeleBot
from config import token
from locations import slots, roulette

bot = TeleBot(token)

users = {}

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

        bot.send_message(chat_id, "Hello from joy casino")
        return
    user = users[chat_id]
    if "/help" in message.text:
        send_help(chat_id)
    elif "Рулетка" in message.text:
        user['location'] = 'roulette'
    elif "Автоматы" in message.text:
        user['location'] = 'slots'
    elif "Меню" in message.text:
        user['location'] = 'menu'
    else:
        if user['location'] == 'slots':
            slots.process_message(message, user, users, bot)
        elif user['location'] == 'roulette':
            roulette.process_message(message, user, users, bot)




bot.polling(none_stop=True)