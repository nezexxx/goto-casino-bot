from helpers import *
def welcome(user, users, bot, location_manager):
	keyboard = generate_keyboard([])
	bot.send_message(user['id'], "баланс")