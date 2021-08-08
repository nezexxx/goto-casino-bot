from helpers import generate_keyboard
import requests
from config import token
def welcome(user, users, bot, location_manager):
    keyboard = generate_keyboard(['Рулетка', 'Автоматы','Баланс'])
    bot.send_message(user['id'], "Выберите режим", reply_markup=keyboard)

def process_message(message, user, users, bot, location_manager):
    if "Автоматы" in message.text:
        location_manager.change_location(user, "slots", users, bot, location_manager)

    elif "Рулетка" in message.text:
        location_manager.change_location(user, "roulette", users, bot, location_manager)
