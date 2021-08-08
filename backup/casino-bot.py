import telebot
from telebot import types
from config import token


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def cmd_start(message):
    user = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Одиночная игра"))
    keyboard.add(types.KeyboardButton(text="Многопольовательская игра"))
    bot.send_message(user,"Приветсвую тебя,мажорчик.Это бот-казино.Тут ты можешь поиграть в разные игры и выиграть goto-деньги.Для этого тебе надо выбрать режим и игру ",reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def process_text_message(message):
    user = message.chat.id
    if message.text == 'Одиночная игра':
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        keyboard.add(types.KeyboardButton(text="Рулетка"))
        keyboard.add(types.KeyboardButton(text="Покер"))
        keyboard.add(types.KeyboardButton(text="Назад"))
    elif message.text == 'Многопольовательская игра':
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        keyboard.add(types.KeyboardButton(text="Рулетка"))
        keyboard.add(types.KeyboardButton(text="Покер"))
        keyboard.add(types.KeyboardButton(text="Назад"))
    bot.send_message(user, "В какую игру будете играть?",reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def process_text_message(message):
    user = message.chat.id
    if message.text == 'Назад':
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        keyboard.add(types.KeyboardButton(text="Одиночная игра"))
        keyboard.add(types.KeyboardButton(text="Многопольовательская игра"))




bot.polling(none_stop=True)
