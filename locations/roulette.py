
def welcome(user, users, bot, location_manager):
    pass

def process_message(message, user, users, bot, location_manager):

    if message.text == "Ставка":
        bot.send_message(user['id'], "Вы делаете ставку")
    else:
        bot.send_message(user['id'], "Вы в рулетке.Чтобы начать иру,вам над поставить ставку.Для этого вам надо написать 'Ставка'")