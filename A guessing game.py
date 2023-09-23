import random
from time import sleep

# Сообщения с текстом
welcome_message = 'Привет. Это игра "Угадай число"'
range_x_input_message = 'Задай значение диапазона x (левая граница): '
range_y_input_message = 'Задай значение диапазона y (правая граница): '
question_message = 'Попробуешь угадать?'
input_your_digit = "Введите ваше число: "
incorrect_message = "Неправильно."
correct_message = "Ура! Ты угадал число"
error_type_message = "Неправильный тип данных. Введите целое число."

print(welcome_message)
sleep(2)
print(question_message)
sleep(2)

while True:
    try:
        first_digit = int(input(range_x_input_message))
        break
    except ValueError:
        print(error_type_message)

while True:
    try:
        second_digit = int(input(range_y_input_message))
        break
    except ValueError:
        print(error_type_message)


randNum = random.randint(first_digit, second_digit)
sleep(2)
print(f"Отлично! Мы угадываем число в диапазоне от {first_digit} до {second_digit}")

while True:
    try:
        num = int(input(input_your_digit))
        integer_value = int(num)
        break
    except ValueError:
        print(error_type_message)

if num == randNum:
    print(correct_message)
else:
    while num != randNum:
        print(incorrect_message)
        num = int(input(input_your_digit))
        if num == randNum:
            print(correct_message)
            break