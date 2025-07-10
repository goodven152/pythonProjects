import random
import time


def number_input(prompt="Введите число: "):
    return input(prompt)

class Player:
    def __init__(self):
        self.inventory = []
        self.balance = 1
    
    def open_case(self, case):
        if self.balance == 0:
            print("У тебя нет кейсов!")
            return None
        print("Открываем кейс...")
        time.sleep(1)
        self.balance -= 1
        drop = case.open()
        print(f"Тебе выпало: {drop}")
        
    def show_inventory(self):
        print(f"Твой инвентарь: {self.inventory}")
    

class Case:
    def __init__(self):
        self.items = ["knife", "ak-47", "gloves"]
        self.weights = [0.2, 0.5, 0.3]
    
    def open(self):
        drop = random.choices(self.items, weights=self.weights, k=1)[0]
        return drop

player = Player()
case = Case()
def main():

    while True:
        print("==== Добро пожаловать в симулятор кейсов ====")
        print("\n\n\n\n")
        print(f"У вас имеется {player.balance}, кейс(а)\n")
        print("Выберите, что вы хотите сделать:\n")
        print("1. Открыть кейс\t2.Посмотреть инвентарь\t3.Выйти\n")
        number = number_input()
        
        if number == "1":
            if player.balance != 0:
                player.open_case(case)
                print("1.Продать\t2.Оставить\n")
                number = number_input()
            
                if number == "1":
                    print("Вы продали предмет! Выберите следующее действие\n")
                    print("1. Вернуться на главную.\t2. Выйти")
                    number = number_input()
                    if number == "1":
                        continue
                    else:
                        exit()
            else:
                print("Выберите действие:\n")
                print("1. Вернуться на главную.\t2.Выйти")
                number = number_input()
                
        elif number == "2":
            print("Предмет в инвентаре! Выберите действие\n")
            print("1. Вернуться на главную\t2. Выйти")
            number = number_input()
            if number == "1":
                continue
            elif number == "2":
                break
            else:
                print("Введите число!")
                continue
    
        elif number == "2":
            print("Ваш инвентарь:\n")
            player.show_inventory()
            print("1.Вернуться назад.\t2.Выйти\n")
            number = number_input()
            continue
        elif number == "3":
            exit()
        else:
            print("Неверное число")
            break
        
if __name__ == "__main__":
    main()
