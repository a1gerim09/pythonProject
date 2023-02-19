import os
from decouple import config
from casino import play_game, game_result


def play_casino():
    MY_MONEY = int(config('MY_MONEY'))
    money = MY_MONEY
    while True:
        slot = int(input("На какой слот хотите сделать ставку (1-30)? "))
        if slot < 1 or slot > 30:
            print("Введите число от 1 до 30!")
            continue
        bet = int(input("Сколько денег хотите поставить? "))
        if bet > money:
            print("У вас нет столько денег!")
            continue
        result = play_game(slot, bet)
        money += result
        game_result(money)
        play_again = input("Хотите сыграть еще раз? (y/n) ")
        if play_again.lower() != 'y':
            break
    game_result(money)
