from helpers import generate_keyboard
from Coloda import caloda
from location_manager import *
import random


def button_1( user, bot):
    keyboard = generate_keyboard(['Готовы', 'Пополнить баланс','Узнать сколько игроков сейчас',"❌ Меню"])
    bot.send_message(user['id'], "Выберите режим", reply_markup=keyboard)

def process_message(message, user, users, bot, location_manager):
    if "❌ Меню" in message.text:
        location_manager.change_location(user, "menu", users, bot, location_manager)
    elif "Пополнить баланс" in message.text:
        location_manager.change_location(user, "balance", users, bot, location_manager)
    elif "Узнать сколько игроков сейчас" in message.text:
        bot.send_message(user['id'],"Сейчас в покере {} человек".format(filter(lambda x:x['location'] == 'rulette', users)))
    elif "Готовы" in message.text:
        ready(user,users, bot,plaer,location_manager)

def waiting_room():
    pass
def button_2(user,bot):
    keyboard = generate_keyboard(['Туториал','Узнать сколько игроков сейчас',"❌ Меню"])
    bot.send_message(user['id'], "Выберите режим", reply_markup=keyboard)

def ready(bot,message):
    # Если есть люди в этой локации, то им идёт приглашение сыграть,
    # кроме людей которые играют.А человек нажавший попадает в комнату ожидания
    chat_id = message.chat.id
    user = chat_id and locations_managers
    if user==pocer:
        user+=1
        if user > 1:
            waiting_room()
        else:
            bot.send_message(user['id'], "Извини, сейчас никого нет, позови друзей и возращайся")
            bot.send_message(user['id'], "Отправляйся в Меню")
            locations_managers[location].welcome(user, users, bot, location_manager)
            location_manager.change_location(user, "menu", bot)

def karta(bot,message):# вытащить одну карту из калоды
    chat_id = message.chat.id
    user = chat_id and locations_managers
    random.shuffle(caloda)
    random_kart = random.choice(caloda)
    bot.send_message(user['id'],random_kart)
    caloda.remove(random_kart)  # удалить карту из колоды
#bot.send_message(user['id'], "Раздаются карты,ваши карты")



