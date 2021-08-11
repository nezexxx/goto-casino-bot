from helpers import generate_keyboard
# from balance import *
import random
from helpers import *
from locations.userr import users





def send_menu(chat_id, bot):
    keyboard = generate_keyboard(["❌ Меню"])
    bot.send_message(chat_id, "Напишите вашу ставку", reply_markup=keyboard)


def welcome(users, user,  bot, location_manager):
    send_menu(users['id'], bot)





def choose_bet(user, message, bot):
    balance = user["balance"]
    money = balance
    bet = message.text

    if "Меню" in message.text:
        del user["bet"]
        del user["color"]
        del user["number"]

    try:
        bet = int(message.text)
    except:
        bot.send_message(message.from_user.id, "это не число")
        return
    try:
        balance > 0
    except:
        bot.send_message(message.from_user.id, "баланес ниже 0,пополните баланс")
        return

    if int(bet) > int(balance):
        bot.send_message(user["id"],"слишком большая ставка для тебя\nпопоробуй меньше)")
        return
    else:
        bot.send_message(user["id"], "ваша ставка:{}".format(bet))

        bet = message.text
        user["bet"] = bet
        user["balance"] = int(user["balance"]) - int(user["bet"])

        bot.send_message(message.chat.id,"напишите цвет: красный,черный,зеленый\n\nкоэффицент выиграша на зеленое 50🥵🥵\nкоэффицент выиграша на красное 25💵💵\nкоэффицент выиграша на черное 25💰💰\n\nУдачи🍀🍀🍀🍀")

    if "Меню" in message.text:
        del user["bet"]
        del user["color"]
        del user["number"]





def colors_of(message,bot,user):
    spisok_of_colors = ["зеленый", "красный", "черный"]

    if "Меню" in message.text:
        del user["color"]
        del user["bet"]
        del user["number"]

    if message.text in spisok_of_colors:
        colors = message.text
        color = colors
        bot.send_message(message.chat.id, "Отлично\nОсталось выбрать число")
        bot.send_message(message.chat.id,"Введите число от 1 до 37\n18 черных🖤, 18 красных🍎, 1 зеленых💚")
        user["color"] = color
    else:
        bot.send_message(message.chat.id, "введен неверный цвет\nЕсли вы решили выйти из игры, дабавив ставку\nвам нужно доиграть, потому что с вас списалась ставка")
        return

    if "Меню" in message.text:
        del user["color"]
        del user["bet"]
        del user["number"]


def number_of(message,bot,user):
    spisok_of_numbers = list(range(1, 38))
    spisok_of_colors = ["зеленый", "красный", "черный"]
    print("I am here")

    if "Меню" in message.text:
        del user["number"]
        del user["color"]
        del user["bet"]

    if int(message.text) in spisok_of_numbers:
        number = message.text
        user["number"] = number
        print('u', user)
        print("I am here")
    else:
        bot.send_message(user["id"],"некорректное число\nвведите число в диапозоне от 1 до 37")

    random_number_black = random.randint(1, 19)
    random_number_red = random.randint(19, 36)
    random_number_green = random.randint(1, 37)

    if "Меню" in message.text:
        del user["number"]
        del user["color"]
        del user["bet"]




def process_message(message, user, users, bot, location_manager):
    # balance = user["balance"]
    #
    # money = balance
    # spisok_of_numbers = list(range(1, 38))
    #
    # spisok_of_colors = ["зеленый", "красный", "черный"]
    print(user)
    if ('bet' not in user) and ("number" not in user) and ("color" not in user) :
        print('choosing bet')
        choose_bet(user, message, bot)

    elif('bet' in user) and ("color" not in user) and ("number" not in user):
        print('choosing color')
        colors_of(message,bot, user)

    elif ('bet' in user) and ("color" in user) and ("number" not in user):
        print('choosing number')
        number_of(message, bot, user)
        print("i am alive")
        print('u2', user)
        #он почему-то здесь останавливается и ждет второго сообщения
    if 'bet' in user and ("color" in user) and ("number" in user):
        print("game")
        game123(message, user, users, bot, location_manager)


def game123(message, user, users, bot, location_manager):
    print(user )

    balance = user["balance"]
    bet = user["bet"]
    color = user["color"]
    number = user ["number"]

    random_number_black = random.randint(1, 19)
    random_number_red = random.randint(19, 36)
    random_number_green = random.randint(1, 37)

    if color == "черный":
        print("я дошел до game 123 черное")
        # если рандомное число совпадает с числом, которое загадал человек он выиграл
        if number == random_number_black:
            print("я дошел до game 123 черное рандом")
            balance += bet * 25
            bot.send_message(message.chat.id, "вы выиграли")
            print("я дошел до сюда")
            bot.send_message(message.chat.id,"выпало{}\nпоздравляю с победой\n ваш коэффицент 2.5\nсейчас ваш баланс{}".format(random_number_black, (int(balance) + int(bet)) * 25))
            del user["bet"]
            del user["color"]
            del user["number"]
            send_menu(user["id"], bot)
        else:
            print("Я дошел до else *проигрешь*")
            bot.send_message(message.chat.id, "вы проиграли\nваш баланс{}".format(balance))
            del user["bet"]
            del user["color"]
            del user["number"]
            print("удалил bet, color, number")
            send_menu(user["id"], bot)

    elif color == "красный":
        if number == random_number_red:
            balance += bet * 25
            bot.send_message(message.chat.id, "вы выиграли")
            bot.send_message(message.chat.id,"выпало{}\nпоздравляю с победой\n ваш коэффицент 2.5\nсейчас ваш баланс{}".format(random_number_red, (int(balance) + int(bet)) * 25))
            del user["bet"]
            del user["color"]
            del user["number"]
            send_menu(user["id"], bot)

        else:
            bot.send_message(user['id'], "вы проиграли\nваш баланс{}".format(user["balance"]))
            del user["bet"]
            del user["color"]
            del user["number"]
            send_menu(user["id"], bot)

    elif user["color"] == "зеленый":
        print("я в зеленом")
        if number == random_number_red:
            balance += bet * 25
            bot.send_message(message.chat.id, "вы выиграли")
            bot.send_message(message.chat.id,"выпало{}\nпоздравляю с победой\n ваш коэффицент 2.5\nсейчас ваш баланс{}".format(random_number_red, (int(balance) + int(bet)) * 25))
            del user["bet"]
            del user["color"]
            del user["number"]
            send_menu(user["id"], bot)

        else:
            bot.send_message(user['id'], "вы проиграли\nваш баланс{}".format(user["balance"]))
            del user["bet"]
            del user["color"]
            del user["number"]
            send_menu(user["id"], bot)







