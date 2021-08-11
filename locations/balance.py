# import requests
# from config import token
# '''  host = 'https://bank.goto.msk.ru'
# trading_token = token '''
# from location_manager import *
# from helpers import generate_keyboard
#
# def change_location(user,bot,message):
#     user["id"] = message.chat.id
#     keyboard = generate_keyboard(["Пополнить баланс", "❌ Меню"])
#     bot.send_message(user["id"],user["balance"], reply_markup=keyboard)
'''
    def process_message(message, user, users, bot, location_manager,from_id, amount, description):
      if "Пополнить баланс" in message.text:
          bot.send_message(user_id, "Введите сумму,котрую хотите положить на баланс")
          answer = requests.post(host + '/api/ask', json={
              'token': trading_token,
              'account_id': from_id,
              'amount': amount,
              'description': description
                         

          return answer.json()

          ask_money(user, bet, "Закинуть в казино")

      elif "Меню" in message.text:
          location_manager.change_location(user, "menu", users, bot, location_manager)
'''
