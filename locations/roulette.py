# from casino-bot.py import
def welcome(user, users, bot, location_manager):
    pass

def process_message(message, user, users, bot, location_manager):

    chat_id = message.chat.id

    balance = 400
    money = balance
    balance = users["balance"]
    spisok_of_numbers = list(range(1, 38))

    spisok_of_colors = ["зеленый", "красный", "черный"]

    def main(message):
        bot.send_message(user, "напишите ставку: ")
        bot.register_next_step_handler(message, choose_type)

    def choose_type(message):

        bet = message.text
        int(bet)
        if int(message.text) > 0 and int(message.text) < 100000:

            if balance > 0:
                print(bet)

                bot.send_message(message.from_user.id, "ваша ставка:{}".format(bet))

                bet = message.text
                money = balance
                money -= int(bet)

                bot.send_message(message.chat.id,
                                 "напишите цвет на который ставите варианты: красный,черный,зеленый:")
                bot.register_next_step_handler(message, colors_of)
            else:
                bot.send_message(message.chat.id,
                                 "у вас нуливой или отрицательный баланс\nПополните баланс чтобы поиграть))")

                print("")

            if int(bet) > int(money):
                bet = money
                bet = message.text
                money = balance
                money -= int(bet)
            else:
                print("")

    def colors_of(message):
        if message.text in spisok_of_colors:
            color = message.text
            bot.send_message(message.chat.id, "Отлично\nОсталось выбрать число")
            bot.send_message(message.chat.id,
                             "Введите число от 1 до 37\n1-18 черные, 19-37 красные, 1-37 зеленые\nПистать нужно так: черный,красный,зеленый")
            bot.register_next_step_handler(message, number_of)
        else:
            bot.send_message(message.chat.id, "введен неверный цвет")
            bot.register_next_step_handler(message, number_of)
            return

    def number_of(message):
        print("I am here")
        if int(message.text) in spisok_of_numbers:
            number = message.text
            print("I am here")
            bot.register_next_step_handler(message, win_or_lose)
        else:
            bot.send_message(message.chat.id, "некорректно введено число")
            bot.register_next_step_handler(message, win_or_lose)

    random_number_black = random.randint(1, 19)
    random_number_red = random.randint(19, 36)
    random_number_green = random.randint(1, 37)

    def win_or_lose(number_of, colors_of, choose_type):
        if color == "черный":
            # если рандомное число совпадает с числом, которое загадал человек он выиграл
            if number == random_number_black:
                money += bet * 2.5
                win += 1
                bot.send_message(message.chat.id, "вы выиграли")
                bot.send_message(message.chat.id,"выпало{}\nпоздравляю с победой\n ваш коэффицент 2.5\nсейчас ваш баланс{}".format(random_number_black, int(balance) * 2.5))
            else:
                # иначе — увеличиваем количество проигрышей
                loose += 1
                bot.send_message(message.chat.id, "вы проиграли")

        if color == "красный":
            if number == random_number_red:
                money += bet * 2.5
                win += 1
                bot.send_message(user['id'], "вы выиграли")
                bot.send_message(user['id'],"выпало{}\nпоздравляю с победой\n ваш коэффицент 2.5\nсейчас ваш баланс{}".format(random_number_red, int(balance) * 2.5))
            else:
                loose += 1
                bot.send_message(user['id'], "вы проиграли\nваш баланс{}".format(money))

        if color == 'зелёный':
            if color == random_number_green:
                money += bet * 100
                win += 1
                bot.send_message(user['id'], "вы выиграли")
                bot.send_message(user['id'],"выпало{}\nпоздравляю с победой\n ваш коэффицент 2.5\nсейчас ваш баланс{}".format(trandom_number_green, int(balance) * 100))
            else:
                loose += 1
                bot.send_message(user['id'], "вы проиграли")

    #
    # if message.text == "Ставка":
    #     bot.send_message(user['id'], "Вы делаете ставку")
    # else:
    #     bot.send_message(user['id'], """Вы в рулетке.Чтобы начать игру,
    #     вам над поставить ставку.Для этого вам надо написать 'Ставка'""")