import random
import time

items = ["knife", "ak-47", "gloves"]
inventory = []
case_balance = 1

def open_case():
    global case_balance
    print("Открываем кейс...")
    case_balance -= 1
    time.sleep(5)
    drop = random.choice(items)
    print("\n")
    print("\n")
    print("\n")
    print(f"Выпал предмет {drop}\n")
    print(f"У вас осталось {case_balance} кейса(ов)")
    return drop


def main():
    while True:
        print("==== Добро пожаловать в симулятор кейсов ====")
        print("\n\n\n\n")
        print(f"У вас имеется {case_balance}, кейс(а)\n")
        print("Выберите, что вы хотите сделать:\n")
        print("1. Открыть кейс\t2.Посмотреть инвентарь\t3.Выйти\n")
        number = input("Введите цифру:")
        if number == "1":
            if case_balance != 0:
                drop = open_case()
                print("1.Продать\t2.Оставить\n")
                number = input("Введите число:")
                if number == "1":
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
                        break
                    else:
                        print("Введите число!")
                else:
                    print("Введите число!")
            else:
                print("У вас нет кейсов!")
                continue
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
            break