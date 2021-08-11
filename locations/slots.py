import random
import time
from threading import Thread
from telebot import types
from helpers import generate_keyboard

options = list('🍒🍋🍐')

stav_100 = 0
stav_200 = 0

def send_menu(chat_id, bot):
    keyboard = generate_keyboard(["💸 100", "💸 200", "❌ Меню"])
    bot.send_message(chat_id, "Сделайте ставку", reply_markup=keyboard)

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

    if result in ['🍒🍒🍒', '🍋🍋🍋', '🍐🍐🍐']:
        bot.send_message(chat_id, "Вы выиграли")
    else:
        bot.send_message(chat_id, "ВЫ проиграли")

    send_menu(chat_id, bot)



def run_animation(chat_id, result, bot):
    message = bot.send_message(chat_id, "...")
    t = Thread(target=animate, args=(chat_id, message.id, bot, result))
    t.start()


def welcome(user, users, bot, location_manager):
    send_menu(user['id'], bot)


def process_message(message, user, users, bot, location_manager):
    if "Назад" in message.text:
        location_manager.change_location(user, "menu", users, bot, location_manager)

    elif "100" in message.text:
        if user['balance'] < 100:
            bot.send_message(user['id'], 'Недостаточно средств на балансе')
        else:
            combination = random.choice(options) + random.choice(options) + random.choice(options)
            run_animation(user['id'], combination, bot)

            if combination in ['🍒🍒🍒', '🍋🍋🍋', '🍐🍐🍐']:
                user['balance'] += stav_100 * 1.3
                user['balance'] += stav_200 * 1.3
            else:
                user['balance'] -= stav_100
                user['balance'] -= stav_200

    else:
        send_menu(user['id'], bot)


from helpers import generate_keyboard
import random
import time
from threading import Thread
from telebot import types

options = list('🍒🍋🍐')

stav_50 = 0
stav_100 = 0
stav_200 = 0
stav_500= 0
def send_menu(chat_id, bot):
    keyboard = generate_keyboard(["❌ Меню","💸 50","💸 100","💸 200", "💸 500"])
    bot.send_message(chat_id, "Сделайте ставку", reply_markup=keyboard)

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

    if result in ['🍒🍒🍒', '🍋🍋🍋', '🍐🍐🍐']:
        bot.send_message(chat_id, "Вы выиграли")
    else:
        bot.send_message(chat_id, "ВЫ проиграли")

    send_menu(chat_id, bot)



def run_animation(chat_id, result, bot):
    message = bot.send_message(chat_id, "...")
    t = Thread(target=animate, args=(chat_id, message.id, bot, result))
    t.start()


def welcome(user, users, bot, location_manager):
    send_menu(user['id'], bot)


def process_message(message, user, users, bot, location_manager):
    if "Назад" in message.text:
        location_manager.change_location(user, "menu", users, bot, location_manager)
    elif "100" in message.text:
        if user['balance'] < 100:
            bot.send_message(user['id'], 'Недостаточно средств на балансе')
        else:
            combination = random.choice(options) + random.choice(options) + random.choice(options)
            run_animation(user['id'], combination, bot)

            if combination in ['🍒🍒🍒', '🍋🍋🍋', '🍐🍐🍐']:
                user['balance'] += stav_100 * 1.3
                user['balance'] += stav_200 * 1.3
            else:
                user['balance'] -= stav_100
                user['balance'] -= stav_200

    else:
        send_menu(user['id'], bot)