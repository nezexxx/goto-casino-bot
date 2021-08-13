import functools

from helpers import generate_keyboard
from config import token
from locations.bank_api import ask_money, verify_transaction, send_money
from locations.userr import users

import functools

temp = {}
spisok_of_payment = [100, 200, 300, 500]


def welcome(location_manager, user, users, bot):
    bot.send_message(user['id'], "Режим Баланс")
    send_menu(user, bot)


def send_menu(user, bot):
    keyboard = generate_keyboard(["100", "300", "500", "1000","Меню❌"])
    bot.send_message(user["id"], "Выберите на сколько  будете пополнять\nМаксимальный коэффицент  50", reply_markup=keyboard)


def check_payment(message, user, bot):
    try:
        payment = int(message.text)
    except:
        bot.send_message(user["id"], "некорректно введено число")
        return


    if int(message.text) in spisok_of_payment:
        pass
    else:
        bot.send_message(user["id"], "неверное значение\nвозможно вы ввели сторочку")
        return

    user["payment"] = payment
    print(user)


def ask_code(message, bot, user):
    print('1')
    bot.send_message(message.chat.id, "Пришли код подтверждения")
    print("22")
    next_func = functools.partial(process_code,user = user, bot = bot )
    bot.register_next_step_handler(message,  next_func)



def process_code(message, user, bot):
    print(" 222")
    try:
        code = int(message.text)
        print(999999)
    except:
        print('boba')
        ask_code(message, bot, user)
        print('biba')
        bot.send_message(user["id"], "неверный код, давай еще раз")
        return

    print("дошел до result ")
    print(code)
    result = verify_transaction(user["transaction_id"], code)
    print(code)
    print(result)

    if 'error' in result:
        print(555)
        send_menu(user, bot)
        bot.send_message(message.chat.id, "Не удалось пополнить баланс, банк вернул ошибку - {}.".format(result['error']))
    else:
        user["code"] = code
        bot.send_message(message.chat.id,"Операция одобрена")
        user["balance"] += user["payment"]
        bot.send_message(message.chat.id, "Возможность вывода средств доступна по достижению баланса >= 5000GT\n"
                                          "Приносим свои извения за неудобство\nЭти меры необходимы")
        bot.send_message(message.chat.id, "ваш баланс {}".format(user["balance"]))
        send_menu(user, bot)
        del user["payment"]
        del user["code"]




def process_pay(message, user, bot):
    amount = None

    if "100" in message.text:
        amount = 100
    elif "200" in message.text:
        amount = 200
    elif "300" in message.text:
        amount = 300
    elif "500" in message.text:
         amount = 500

    if amount:
        user["payment"] = amount
        transaction = ask_money(message.chat.id, amount, 'Зачисление в казино The Venetian Casino"')
        print(transaction)
        if 'transaction_id' not in transaction:
            send_menu(user, bot)
            bot.send_message(message.chat.id,"Не удалось пополнить баланс, банк вернул ошибку - {}.".format(transaction['error']))

        else:
            ask_code(message,bot, user)
            user["transaction_id"] = transaction['transaction_id']
    else:
        send_menu(user,bot)




def process_message(message, user, users,  bot, location_manager):
    print("я здесь")
    if ("payment" not in user) and ("code" not in user):
        print("я дошел до сюда")
        check_payment(message, user, bot)


    if("payment" in user) and ("code" not in user):
        print("я тут")
        process_pay(message, user, bot)


