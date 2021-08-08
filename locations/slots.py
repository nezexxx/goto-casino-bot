import random
import time
from threading import Thread

from telebot import types

options = list('🍒🍋🍐')

stav_50 = 0
stav_100 = 0
stav_200 = 0
stav_500= 0

def animate(chat_id, message_id, bot, result):
	time.sleep(0.5)
	old_frame = ""
	for i in range(1, 12):
		new_frame = random.choice(options) + random.choice(options) + random.choice(options)
		if new_frame != old_frame:
			bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=new_frame)
			old_frame = new_frame
		time.sleep(0.5)
	bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="...")
	time.sleep(0.5)
	bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=result)
	send_menu(chat_id, bot)




def send_menu(chat_id, bot):
	keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	stav_50 = types.KeyboardButton(text="💸 50")
	keyboard.add(stav_50)
	stav_100 = types.KeyboardButton(text="💸 100")
	keyboard.add(stav_100)
	stav_200 = types.KeyboardButton(text="💸 200")
	keyboard.add(stav_200)
	stav_500 = types.KeyboardButton(text="💸 500")
	keyboard.add(stav_500)

	keyboard.add(types.KeyboardButton(text="❌ Меню"))

	bot.send_message(chat_id, "Сделайте ставку", reply_markup=keyboard)


def run_animation(chat_id, result, bot):
	message = bot.send_message(chat_id, "...")
	t = Thread(target=animate, args=(chat_id, message.id, bot, result))
	t.start()

def raschet(user, users, bot):
	combination = random.choice(options) + random.choice(options) + random.choice(options)
	run_animation(user['id'], combination, bot)

	if combination in ['🍒🍒🍒', '🍋🍋🍋', '🍐🍐🍐']:
		bot.send_message(user['id'], "Вы выиграли")
		user['balance'] += stav_50 * 1.3
		user['balance'] += stav_100 * 1.3
		user['balance'] += stav_200 * 1.3
		user['balance'] += stav_500 * 1.3
	else:
		bot.send_message(user['id'], "ВЫ проиграли")
		user['balance'] -= stav_50
		user['balance'] -= stav_100
		user['balance'] -= stav_200
		user['balance'] -= stav_500
def process_message(message, user, users, bot):
	if "50" in message.text:
		if user['balance'] < 50:
			bot.send_message(user['id'], 'Недостаточно средств на балансе')
		else:
			raschet(user, users, bot)
	elif "100" in message.text:
		if user['balance'] < 100:
			bot.send_message(user['id'], 'Недостаточно средств на балансе')
		else:
			raschet(user, users, bot)
	elif "200" in message.text:
		if user['balance'] < 200:
			bot.send_message(user['id'], 'Недостаточно средств на балансе')
		else:
			raschet(user, users, bot)
	elif "200" in message.text:
		if user['balance'] < 200:
			bot.send_message(user['id'], 'Недостаточно средств на балансе')
		else:
			raschet(user, users, bot)
	else:
		send_menu(user['id'], bot)
