from helpers import generate_keyboard
import requests
from config import token
from Bank_API import ask_money, verify_transaction, send_money
temp = {}

def send_menu(chat_id, bot, message):
    chat_id = message.chat.id
    keyboard = generate_keyboard(["100💷", "200💷", "300💶","500💶", "Меню❌"])
    bot.send_message(chat_id, "Сделайте ставку", reply_markup=keyboard)

    if "Меню" in message.text:
        location_manager.change_location(user, "menu", users, bot, location_manager)
    payment = int(message.text)
    global payment


def ask_code(message, bot):
    msg = bot.send_message(message.chat.id, "Пришли код подтверждения...")
    bot.register_next_step_handler(msg, process_code)



def process_code(message, bot):
    try:
        code = int(message.text)
    except:
        ask_code(message)
        return


    result = verify_transaction(temp[message.chat.id], code)

    if 'error' in result:
        bot.send_message(message.chat.id, "Не удалось сделать ставку, банк вернул ошибку - {}.".format(result['error']))
        send_menu(message)
    else:
        balance = payment
        bot.send_message(message.chat.id, "Операция одобрена\nПополнение зачислено\nваш баланс сейчас{}".format("balance"))




















list_of_payment = list(range(1, 10000))



host = 'https://bank.goto.msk.ru'
trading_token = token


def ask_money(from_id, amount, description):
    answer = requests.post(host + '/api/ask', json={
        'token': trading_token,
        'account_id': from_id,
        'amount': amount,
        'description': description
    })

    return answer.json()


    ask_money(user, payment, "Пополнить счет в казино")

def payment_processing(message,bot):
    user = message.chat.id
    if  payment in  list_of_payment:
        ask_money(user, payment, "Пополнить счет в казино")
    elif payment < 10000:
        bot.send_message(user, "Максимальная сумма пополнения 10000\nПопробуйте меньше")