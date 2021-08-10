from helpers import generate_keyboard

kart={}

def welcome(user, users, bot, location_manager):
    keyboard = generate_keyboard(['Готовы', 'Пополнить баланс','Узнать сколько игроков сейчас',"❌ Меню"])
    bot.send_message(user['id'], "Выберите режим", reply_markup=keyboard)

def process_message(message, user, users, bot, location_manager):
    if "Пополнить балансланс" in message.text:
        location_manager.change_location(user, "balance", users, bot, location_manager)

def fack_user_who_wrote_readi(users,user, bot, location_manager):
    users+=1
    bot.send_message(user['id'], "Раздаются карты,ваши карты")




def a (user, users, bot, location_manager):
    keyboard = generate_keyboard(['Продолжить', 'Выйти',"❌ Меню"])
    bot.send_message(user['id'], "Если вы не будете больше играть, то нажмите Выйти", reply_markup=keyboard)
    # Когда нажимаешь на выйти users-=1