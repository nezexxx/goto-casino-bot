import random
import time
from threading import Thread

from helpers import generate_keyboard

options = list('🍒🍋🍋🍐🍐🍐')


def send_menu(chat_id, bot):
  keyboard = generate_keyboard(["Ввети ставку", "❌ Меню"])
  bot.send_message(chat_id, "Сделайте ставку", reply_markup=keyboard)


def animate(chat_id, message_id, bot, result, val):
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

  if result in ['🍒🍒🍒']:
    bot.send_message(chat_id, "Вы выиграли", val*2)
  elif result in [ '🍋🍋🍋']:
    bot.send_message(chat_id, "Вы выиграли", val * 1.6)
  elif result in ['🍐🍐🍐']:
    bot.send_message(chat_id, "Вы выиграли", val * 1.3)
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
    bot.send_message(user['id'],'Ваша ставка', val)
    return
  if user['balance'] < val:
    bot.send_message(user['id'], 'Недостаточно средств на балансе')
    send_menu(user['id'], bot)
  else:
    nacheslenie(user, bot, val)

def nacheslenie(user, bot, val):
  combination = random.choice(options) + random.choice(options) + random.choice(options)
  run_animation(user['id'], combination, bot,val)

  if combination in ['🍒🍒🍒', '🍋🍋🍋', '🍐🍐🍐']:
    user['balance'] += val * 1.3
  else:
    user['balance'] -=val
