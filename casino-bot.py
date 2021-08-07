import telebot
from telebot import types
from config import token


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def cmd_start(message):
    user = message.chat.id

    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Рулетка"))
    keyboard.add(types.KeyboardButton(text="Покер"))

    bot.send_message(user, "В какую игру будете играть?", reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help(message):
    user = message.chat.id
    bot.send_message(user,
                     "Это бот-казино.Тут ты можешь поиграть в разные игры и выиграть goto-деньги.Напиши 'start',чтобы начать игру")


bot.polling(none_stop=True)
