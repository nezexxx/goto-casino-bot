from helpers import generate_keyboard
import kart
import location_manager

def welcome(user, users, bot, location_manager):
    keyboard = generate_keyboard(['Готовы', 'Пополнить баланс','Узнать сколько игроков сейчас',"❌ Меню"])
    bot.send_message(user['id'], "Выберите режим", reply_markup=keyboard)

def process_message(message, user, users, bot, location_manager):
    if "❌ Меню" in message.text:
        location_manager.change_location(user, "menu", users, bot, location_manager)
    elif "Пополнить баланс" in message.text:
        location_manager.change_location(user, "balance", users, bot, location_manager)
    elif "Узнать сколько игроков сейчас" in message.text:
        bot.send_messag
    elif "Готовы" in message.text:
        ready(users,user, bot)

def ready(users,user, bot):
    users+=1
    bot.send_message(user['id'], "Раздаются карты,ваши карты")
def a (user, users, bot, location_manager):
    keyboard = generate_keyboard(['Продолжить', 'Выйти',"❌ Меню"])
    bot.send_message(user['id'], "Если вы не будете больше играть, то нажмите Выйти", reply_markup=keyboard)
    # Когда нажимаешь на выйти users-=1