import random

def play_game(slot, bet):
    winning_slot = random.randint(1, 30)
    if slot == winning_slot:
        return 2 * bet
    else:
        return -1 * bet

def game_result(money):
    if money > 1000:
        print("Вы выиграли! Ваш капитал: ${}".format(money))
    elif money < 1000:
        print("Вы проиграли! Ваш капитал: ${}".format(money))
    else:
        print("Ничья! Ваш капитал: ${}".format(money))
