# bet =int(input('Введите сколько ставим? '))
# coefficient = float(input('Введите коэффициент? '))
#
# win = round(bet * coefficient,2)
# print('Потенциальный выйрыш:',2)
# print(win)

# height = float(input('Введите рост:'))
# weight = float(input('Введите вес:'))
#
# bmi = round(weight / height **2, 2)
# print('Ваш индекс массы тела:',bmi)
#
# if bmi < 18.5 :
#     print('У вас не достаточная масса тела')
# elif bmi < 25:
#     print('У вас нормальная масса тела')
# elif bmi < 30:
#     print('У вас избыточная масса тела')
# else:
#     print('У вас ожиренье')
# ------------------------------------------------------------------

# 1
# skoliko_stavim = int(input('Сколько ставим ?'))
# coefficent = float(input('Какой коэффициент ?'))
#
# win = round(skoliko_stavim * coefficent,2)
#
# print('Потенциальный выйгрыш:',win)

# 2
# age = int(input('Введите возраст:'))
# temperature = float(input('Введите температуру тела:'))
#
# total =float(round(age * temperature *1.5 , 2))
# print('Столько денег подарит отец сыну на день рождения:',total)

# 3

# height = float(input('Введите рост:'))
# weight = float(input('Введите вес:'))
#
# total = round(weight / height ** 2, 2)
# if total < 18.5:
#     print(total,'У вас не добор')
# elif total < 25:
#     print(total,'У вас все нормально ,не переживайте')
# elif total < 30:
#     print(total,'Идет избыток')
# else:
#     print(total,'Ожирение')
# -----------------------------------------------------------------
# while True:
#     force =float(input('Сила Удара:'))
#     force *= 10
#     print('Балл:',int(force))

# x = float(input('Расположение по горизонтали:'))
# y = float(input('Расположение по вертикали:'))
#
# xSquare = int(x * 10)
# ySquare = int(y * 10)
#
# print('Фигура находится в клетке:',xSquare,ySquare)
# ------------------------------------------------------------

# 1
# CR = 2200
# sheep = 0
# while sheep != 4:
#     number = int(input('Сколько чатлов?'))
#     convert = float(number / CR)
#     print('Это:',convert)
#     if convert > 0.5:
#         sheep +=2
#     elif  sheep == 4:
#         break
#     print('Можно Купить Кораблей:',sheep)

# 3
# x_coord = float(input("По горизонтали: "))
# y_coord = float(input("По вертикали: "))
# if 0 < x_coord < 0.8 and 0 < y_coord < 0.8:
#     x_number = int(x_coord * 10)
#     y_number = int(y_coord * 10)
#     print("Фигура находится в клетке (", x_number, ",", y_number, ")")
#     center_x = x_number / 10 + 0.05
#     center_y = y_number / 10 + 0.05
#     delta_x = round(center_x - x_coord, 3)
#     delta_y = round(center_y - y_coord, 3)
#     print("Поправьте положение фигуры на (", delta_x, ",", delta_y, ")")
# else:
#     print("Клетки с такой координатой не существует")
# ----------------------------------------------------------------------
# import  math
#
# x = int(input('Ввведите координату икс:'))
# y = int(input('Введите координату игрек:'))
#
# distance = math.sqrt(x ** 2 + y ** 2)
# print('Расстояние:',distance)

# import math
#
# distatnce = float(input('Введите расстояние до танка:'))
# angel = float(input('Введите угол в градусах:'))
#
# angel /= 57.2958
# x = math.cos(angel)  * distatnce
# y =math.sin(angel) *distatnce
# print('Координаты вражеского танка',x,',',y)

# ----------------------------------------------------------------------
# 1
# import math
# a = float(input('Введите сторону a:'))
# b = float(input('Введите сторону b:'))
# c = float(input('Введите сторону c:'))
#
# p = (a + b + c) / 2
#
# area_formula = math.sqrt(p * (p -a) * (p -b ) *(p - c))
# print('Площадь треугольника:',area_formula)

# 3
# import math
# user_number = float(input('Введите число:'))
# print(math.floor(user_number))
# print(math.ceil(user_number))
# print(math.sqrt(user_number))
# print(abs(user_number))
# print(math.exp(user_number))
# print(math.log(user_number))
# print(math.log2(user_number))
# print(math.log10(user_number))
# print(math.sin(user_number))
# print(math.cos(user_number))
# if user_number % 1 == 0:
#     print(math.factorial(int(user_number)))
# Home Work------------------------------------

# 1
# euro = float(input('Введите сумму сделанную в магазине:'))
# dollar = round(euro * 1.25, 2)
# rub = round(dollar * 60.87, 2)
# print('Сумма покупки:',rub)

# 2
# import math
# numbers = int(input('Введите кол-во чисел:'))
# for number in range(numbers):
#     num = float(input('Введите число:'))
#     if num > 0:
#         num = math.ceil(num)
#         print(math.log(num))
#     else:
#         num = math.floor(num)
#         print(math.exp(num))

# 3
# import math
#
# time = 0
# # download = int(input('Укажите размер для скачивания:'))
# # trafic = int(input('Какова скорость вашего соединения:'))
# download = 123
# traffic = 27
#
# for speed in range(traffic, download, traffic):
#     procent = (speed * 100) / download
#     time += 1
#     print(f'sec: {time}. Скачено {speed} из {download} Мб ({math.ceil(procent)}%)')
#
#     if speed + traffic >= download:
#         time += 1
#         print(f'sec: {time} Скачано {download} из {download} Мб (100%)')

#4
# number = float(input('Введите число:'))
#
# number = round(number % 1, 5)
# result = number
# result = result * 10 // 1
# print(int(result))

#5
# extra_planet = float(input('Введите радиус случайной планеты:'))
# earth = 10.8321 * (10 ** 11)
#
# v = (4/3) *3.141 * (extra_planet ** 3)
# comparison = round(earth / v, 3)
# if comparison > 1:
#     print(f'Объем плантеы Земля больше в: {comparison} раз')
# elif comparison < 1:
#     comparison =round(1 / comparison, 3)
#     print(f'Объем планеты земля меньше в: {comparison} раз')

#6
# x = float(input('Введите местонахождение коня по горизонтали:'))
# y = float(input('Введите местонахождение коня по вертикали:'))
#
# x_square = int(x * 10)
# y_square = int(y * 10)
#
# plase_x = float(input('Введите местоположение точки по горизонтали:'))
# plase_y = float(input('Введите местоположение точки по вертикали:'))
# move_x = int(plase_x * 10)
# move_y = int(plase_y * 10)
# print(f'Конь в клетке:{x_square} {y_square},Точка в клетке {move_x, move_y}')
#
# calculation_a = (10 -x_square) - (10 - move_x)
# calculation_b = (10 - move_y) - (10 - move_y)
# calculation_c = (calculation_a + calculation_b)
# if calculation_a == 0  or calculation_b == 0:
#     print('Конь не может ходить в эту точку.')
# elif calculation_c ==3 or calculation_c == -3:
#     print('Да,конь может ходить в эту точку.')
# else:
#     print('Конь не может ходить в эту точку')

#7
# number = int(input('Введите первое число:'))
# number2 = int(input('Введите второе число:'))
#
# summ1 = number + number2
# summ2 = number - number2
# max_number = (summ1 +abs(summ2)) / 2
#
# print(max_number)




# number_a = int(input('Введите число:'))
# number_b = int(input('Введите число:'))
#
# summ_a = number_a +number_b
# summ_b = number_a - number_b
# max_numm = (summ_a + abs(summ_b)) / 2
# print(max_numm)