import random
import sys
import messages
from time import sleep

max_attempts = 5
attempts = 0

#print(messages.welcome_message)
sleep(2)
print(messages.question_message)
sleep(2)

# Ввод границы x
while True:
    try:
        first_digit = int(input(messages.range_x_input_message))
        break
    except ValueError:
        print(messages.error_type_message)

# Ввод границы y
while True:
    try:
        second_digit = int(input(messages.range_y_input_message))
        break
    except ValueError:
        print(messages.error_type_message)


randNum = random.randint(first_digit, second_digit)
sleep(1)
print(f"Отлично! Мы угадываем число в диапазоне от {first_digit} до {second_digit}")

while attempts < max_attempts:
    try:
        num = int(input(messages.input_your_digit))
    except ValueError:
        print(messages.error_type_message)
        continue # Пропустить попытку, если была допущена ошибка

    if num == randNum:
        print(messages.correct_message)
        exit()
    else:
        print(messages.incorrect_message)
        print(f"У тебя осталось {max_attempts - attempts - 1} попыток")
        attempts += 1

if attempts == max_attempts:
    print(f"Загаданное число было {randNum}. Попробуйте ещё раз")
    exit()