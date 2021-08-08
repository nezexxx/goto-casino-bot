from threading import Thread

from telebot import types
import time
import random

options = list('🍒🍋🍐')

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


	if result in ['🍒🍒🍒', '🍋🍋🍋', '🍐🍐🍐']:
		bot.send_message(chat_id, "Вы выиграли")
	else:
		bot.send_message(chat_id, "ВЫ проиграли")

def send_menu(chat_id, bot):
	keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
	keyboard.add(types.KeyboardButton(text="💸 100"))
	keyboard.add(types.KeyboardButton(text="❌ Меню"))

	bot.send_message(chat_id, "Сделайте ставку", reply_markup=keyboard)

def run_animation(chat_id, result, bot):
	message = bot.send_message(chat_id, "...")
	t = Thread(target=animate, args=(chat_id, message.id, bot, result))
	t.start()

def process_message(message, user, users, bot):
	if "100" in message.text:
		if user['balance'] < 100:
			bot.send_message(user['id'], 'Недостаточно средств на балансе')
		else:
			combination = random.choice(options) + random.choice(options) + random.choice(options)
			run_animation(user['id'], combination, bot)


	else:
		send_menu(user['id'], bot)


