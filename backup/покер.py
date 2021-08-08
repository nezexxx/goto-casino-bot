bot.message_handler(commands=['start'])
def cmd_start(message):
    user = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text="0"))
    keyboard.add(types.KeyboardButton(text="250"))
    keyboard.add(types.KeyboardButton(text="500"))
    bot.send_message(user,"Выбери ставку",reply_markup=keyboard)

bot.polling(none_stop=True)