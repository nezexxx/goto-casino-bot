from helpers import generate_keyboard
import requests
from config import token

user = message.chat.id
host = 'https://bank.goto.msk.ru'
trading_token = token
bot.send_message(user, "text=Введите сумму")
if text==[1,100000]:
    def ask_money(from_id, amount, description):
        answer = requests.post(host + '/api/ask', json={
            'token': trading_token,
            'account_id': from_id,
            'amount': amount,
            'description': description
        })

        return answer.json()


     ask_money(user, СУММА, "Пополнить счет в казино")
else:
bot.send_message(user, "Неправильный ввод,попробуйте еще раз")