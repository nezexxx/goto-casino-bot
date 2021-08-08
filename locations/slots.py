
def process_message(message, user, users, bot):
    if "Запуск" in message.text:
        bot.send_message(user['id'], "ВЫ дергаете ручку")
    else:
        bot.send_message(user['id'], "You are in slots")