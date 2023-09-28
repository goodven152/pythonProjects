import random
from time import sleep
import sys

# Сообщения с текстом
welcome_message = 'Привет. Это игра "Угадай число"\nУ тебя будет 5 попыток, чтобы угадать число'
range_x_input_message = 'Задай значение диапазона x (левая граница): '
range_y_input_message = 'Задай значение диапазона y (правая граница): '
question_message = 'Попробуешь угадать?'
input_your_digit = "Введите ваше число: "
incorrect_message = "Неправильно."
correct_message = "Ура! Ты угадал число"
error_type_message = "Неправильный тип данных. Введите целое число."

max_attempts = 5
attempts = 0

print(welcome_message)
sleep(2)
print(question_message)
sleep(2)

# Ввод границы x
while True:
    try:
        first_digit = int(input(range_x_input_message))
        break
    except ValueError:
        print(error_type_message)

# Ввод границы y
while True:
    try:
        second_digit = int(input(range_y_input_message))
        break
    except ValueError:
        print(error_type_message)


randNum = random.randint(first_digit, second_digit)
sleep(1)
print(f"Отлично! Мы угадываем число в диапазоне от {first_digit} до {second_digit}")

while attempts < max_attempts:
    try:
        num = int(input(input_your_digit))
    except ValueError:
        print(error_type_message)
        continue # Пропустить попытку, если была допущена ошибка

    if num == randNum:
        print(correct_message)
        exit()
    else:
        print(incorrect_message)
        print(f"У тебя осталось {max_attempts - attempts - 1} попыток")
        attempts += 1

if attempts == max_attempts:
    print(f"Загаданное число было {randNum}. Попробуйте ещё раз")
    exit()