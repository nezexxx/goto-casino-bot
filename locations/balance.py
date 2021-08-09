from helpers import generate_keyboard
else:
bot.send_message(user, answer["balance"])
keyboard = generate_keyboard(["balance"])
host = 'https://bank.goto.msk.ru'
trading_token = token


def ask_money(from_id, amount, description):
    bot.send_message(user,)
    answer = requests.post(host + '/api/ask', json={
        'token': trading_token,
        'account_id': from_id,
        'amount': amount,
        'description': description

    return answer.json()


ask_money(user['id'],answer, "ОПИСАНИЕ ПОКУПКИ" )