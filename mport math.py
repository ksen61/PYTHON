import math
rez = None
while True:
    try:
        x = v = int (input('Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n 5 Возведение в степень \n 6 Квадратный корень \n 7 Факториал \n 8 Синус \n 9 Косинус \n 10 Тангенс \n'))
    except ValueError:
        print("Неверный выбор операции. Попробуйте снова")
        continue

    if v == 1:
        try:
            a = float(input('Введите число 1: ')) 
            b = float(input('Введите число 2: ')) 
            rez = a + b
        except:
            print("Это не число")
    if v == 2:
        try:
            a = float(input('Введите число 1: ')) 
            b = float(input('Введите число 2: ')) 
            rez = a - b
        except:
            print("Это не число")
    if v == 3:
        try:
            a = float(input('Введите число 1: ')) 
            b = float(input('Введите число 2: ')) 
            if b == 0: 
                print('Делить на 0 нельзя')
                continue 
            rez = a / b
        except:
            print("Это не число")
    if v == 4:
        try:
            a = float(input('Введите число 1: ')) 
            b = float(input('Введите число 2: ')) 
            rez = a * b
        except:
            print("Это не число")
    if v == 5:
        try:
            a = float(input('Введите число 1: ')) 
            b = float(input('Введите степень: ')) 
            rez = a ** b
        except:
            print("Это не число")
    if v == 6:
        try:
            a = float(input('Введите число: ')) 
            if a < 0:
                print("Квадратный корень из отрицательного числа.")
                continue
            rez = math.sqrt(int(a))
        except:
            print("Это не число")
    if v == 7:
        try:
            a = float(input('Введите число: ')) 
            if a < 0:
                print("Факториал отрицательного числа не определен.")
                continue
            rez = math.factorial(int(a))
        except:
            print("Это не число")
    if v == 8:
        try:
            a = float(input('Введите число: ')) 
            rez = math.sin(int(a))
        except:
            print("Это не число")
    if v == 9:
        try:
            a = float(input('Введите число: ')) 
            rez = math.cos(int(a))
        except:
            print("Это не число")
    if v == 10:
        try:
            a = float(input('Введите число: ')) 
            rez = math.tan(int(a))
        except:
            print("Это не число")

    if rez != None:
        print ('Результат' ,rez)

            