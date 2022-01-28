from random import randint as r


x = r(1, 100)
user_num = 0
cnt = 0
print('Добро пожаловать в числовую угадайку')
while True:
    user_num = input("Я загадал число от 1 до 100 - угадай его: ")
    if not user_num.isnumeric():
        print("ШТА??? Некорректный ввод.")
        print("¯\_(ツ)_/¯")
        print()
        continue
    user_num = int(user_num)
    if user_num not in range(1, 101):
        print("Ваше число не входит в диапозон от 1 до 100.")
        print("¯\_(ツ)_/¯")
        print()
        continue
    cnt += 1
    if user_num == x:
        print(f"Правильно {user_num}. Ты угадал число за {cnt} попыток.")
        print("\(＾◡＾)/")
        print()
        y = input('Cыграем еще? "y|n": ')

        if y == "y":
            x = r(1, 100)
            cnt = 0
        else:
            if y == "n":
                print("Спасибо за игру. Еще увидимся...")
                break
            else:
                while True:
                    print("ШТА??? Некорректный ввод")
                    y = input('Cыграем еще? "y|n": ')
                    if y == "y":
                        cnt = 0
                        break
                    elif y == "n":
                        print("Спасибо за игру. Еще увидимся...")
                        exit()

    elif user_num > x:
        print(f"Мое число меньше {user_num}, попробуйте еще разок")
    else:
        print(f"Мое число больше {user_num}, попробуйте еще разок")