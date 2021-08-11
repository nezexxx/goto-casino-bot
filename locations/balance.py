
import requests
from config import token


host = 'https://bank.goto.msk.ru'
trading_token = token
from helpers import generate_keyboard


def welcome(user, users, bot, location_manager):
    keyboard = generate_keyboard(["Пополнить баланс", "❌ Меню"])
    bot.send_message(user["id"], f'баланс пользвоаптеля: {user["balance"]}', reply_markup=keyboard)


#def process_message(message, user, users, bot, location_manager,
#                    from_id, amount, description, trading_token,reply_to_user,val,process_code):
# удалил все аргумент , которыми функция не пользуеться

def process_message(message, user, users, bot, location_manager,process_code):
    user["id"] = message.chat.id
    keyboard = generate_keyboard(["Пополнить баланс", "❌ Меню"])
    bot.send_message('баланс пользвоаптеля: {user["id"]}: {user["balance"]}', reply_markup=keyboard)

    user["id"] = message.chat.id
    bot.send_message(user["id"],"Введите сумму,котрую хотите положить на баланс")
    if "Пополнить баланс" in message.text:
        summa=int(input,message.text)
        bot.send_message(user["id"], summa)
        # сумма - в ней лежит число переведённое на баланс
        msg = bot.send_message(message.chat.id, "Пришли код подтверждения...")# вставил ask_code сторчками
        bot.register_next_step_handler(msg, process_code)



# def ask_code(message,process_code):
#     msg = bot.send_message(message.chat.id, "Пришли код подтверждения...")
#     bot.register_next_step_handler(msg, process_code)


from telebot import TeleBot
from config import token
import location_manager

bot = TeleBot(token)

users = {}

def send_help(chat_id):
    bot.send_message(chat_id, "help")

#@bot.message_handler(content_types=['text'])
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

