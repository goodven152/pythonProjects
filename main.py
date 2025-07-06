import random
import time

items = ["knife", "ak-47", "gloves"]
inventory = []

while True:
    print("==== Добро пожаловать в симулятор кейсов ====")
    print("\n\n\n\n")
    print("Выберите, что вы хотите сделать:")
    print("1. Открыть кейс\t2.Посмотреть инвентарь\t3.Выйти\n")
    number = input("Введите цифру:")
    if number == "1":
        print("Открываем кейс...")
        time.sleep(5)
        drop = random.choice(items)
        print("\n")
        print("\n")
        print("\n")
        print(f"Выпал предмет {drop}\n")
        print("1.Продать\t2.Оставить\n")
        number = input("Введите число:")
        if number == "1":
            drop = 0
            print("Вы продали предмет! Выберите следующее действие\n")
            print("1. Вернуться на главную.\t2. Выйти")
            number = input("Введите число: ")
            if number == "1":
                continue
            else:
                exit()
        elif number == "2":
            inventory.append(drop)
            print("Предмет в инвентаре! Выберите действие\n")
            print("1. Вернуться на главную\t2. Выйти")
            number = input("Введите число: ")
            if number == "1":
                continue
            elif number == "2":
                exit()
            else:
                print("Введите число!")
        else:
            print("Введите число!")
    elif number == "2":
        print("Ваш инвентарь:\n")
        print(inventory)
        print("1.Вернуться назад.\t2.Выйти\n")
        number = input("Введите число: ")
        continue
    elif number == "3":
        exit()
    else:
        print("Неверное число")
        exit()