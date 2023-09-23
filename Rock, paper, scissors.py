import random
from time import sleep
def choice_computer():
    """Выбор компьютера через рандом"""
    options = ['камень', 'ножницы', 'бумага']
    choice_computer = random.choice(options)
    return choice_computer

def determ_winner(player, computer):
    """Определение победителя в игре"""
    if player == computer:
        return "Ничья!"
    elif (player == "камень" and computer == "ножницы") or \
            (player == "ножницы" and computer == "бумага") or \
            (player == "бумага" and computer == "камень"):
        return "Вы победили!"
    else:
        return "Компьютер победил!"

# Модуль сообщений
welcome_message = 'Привет! Это игра "Камень, ножницы, бумага"'
player_choise = "Ваш выбор: Камень, ножницы или бумага?\n"
error_type_message = "Введено неверное значение"

print(welcome_message)
sleep(1)

while True:
    try:
        player = input(player_choise).lower()
    except ValueError:
        print(error_type_message)

    computer = choice_computer()

    print(f"Вы выбрали: {player}")
    print(f"Компьютер выбрал {computer}")

    result = determ_winner(player, computer)
    print(result)

    play_again = input("Хотите сыграть ещё раз? (да/нет)").lower()
    if play_again != "да":
        break