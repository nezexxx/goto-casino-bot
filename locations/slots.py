import random
import time
from threading import Thread
from time import sleep
from helpers import generate_keyboard
from telebot import types


options = list('🍒🍋🍐🍒🍋🍐🍒🍋🍐')


def send_menu(chat_id, bot):
	keyboard = generate_keyboard(["Ввети ставку", "❌ Меню"])
	bot.send_message(chat_id, "Ваша ставка", reply_markup=keyboard)


def reference(bot):
	bot.send_message(["Привет , есть рэйтинг ставок, чем ставка больше,тем вы вышеше вы в рэйтенге"])
	sleep(1)
	bot.send_message(["За первые 3 места вам начисляються проценты от всех ставок 1-й 3%,2-й 2%,3-й 1%"])
	sleep(1)
	bot.send_message(["Куш разный за разные фрукты, за 🍒 х3,🍋 х2,🍐 х2"])
	sleep(1)
	bot.send_message(["Чтобы узнать кто в топе, нажми узнать"])
def animate(chat_id, message_id, bot, result, val):
	time.sleep(0.4)
	old_frame = ""
	for i in range(1, 13):
		new_frame = random.choice(options) + random.choice(options) + random.choice(options)
		if new_frame != old_frame:
			bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=new_frame)
			old_frame = new_frame
		time.sleep(0.5)
	bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="...")
	time.sleep(0.6)
	bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=result)

	if result in ['🍒🍒🍒']:
		bot.send_message(chat_id, "Вы выиграли")
	elif result in ['🍋🍋🍋']:
		bot.send_message(chat_id, "Вы выиграли")
	elif result in ['🍐🍐🍐']:
		bot.send_message(chat_id, "Вы выиграли")
	else:
		bot.send_message(chat_id, "Вы проиграли")

	send_menu(chat_id, bot)


def run_animation(chat_id, result, bot, val):
	message = bot.send_message(chat_id, "...")
	t = Thread(target=animate, args=(chat_id, message.id, bot, result, val))
	t.start()


def welcome(user, users, bot, location_manager):
	send_menu(user['id'], bot)


def process_message(message, user, users, bot, location_manager):
	if "Назад" in message.text:
		location_manager.change_location(user, "menu", users, bot, location_manager)

	txt = message.text
	val = 0
	try:
		val = int(txt)
	except:
		return

	if user['balance'] < val:
		bot.send_message(user['id'], "Недостаточно средств на балансе")
		send_menu(user['id'], bot)
	elif val <= 0:
		bot.send_message(user['id'], "Некоректная ставка")
		return
	else:
		nacheslenie(user, bot, val)


def nacheslenie(user, bot, val):
	combination = random.choice(options) + random.choice(options) + random.choice(options)
	run_animation(user['id'], combination, bot, val)

	if combination in ['🍒🍒🍒']:
		val = val * 4
		bot.send_message(user['id'], "Вы выиграли", val)
		user['balance'] += val
	elif combination in ['🍋🍋🍋']:
		val = val * 3
		bot.send_message(user['id'], "Вы выиграли", val)
		user['balance'] += val
	elif combination in ['🍐🍐🍐']:
		val = val * 3
		bot.send_message(user['id'], "Вы выиграли", val)
		user['balance'] += val
	else:
		user['balance'] -= val
