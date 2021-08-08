
def process_message(message, user, users, bot):
    if message.text == "Ставка":
        bot.send_message(user['id'], "Вы делаете ставку")
    else:
        bot.send_message(user['id'], "You are in roulette")