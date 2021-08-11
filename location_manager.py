from locations import slots, roulette,menu,balance
from telebot import types

locations_managers = {
    "slots": slots,
    "menu": menu,
    "roulette": roulette,
    "balance": balance
}

def change_location(user, location, users, bot, location_manager):
    user['location'] = location
    locations_managers[location].welcome(user, users, bot, location_manager)