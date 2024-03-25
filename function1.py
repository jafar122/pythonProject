# 1
# def countFood():
#     fruits = int(input('Введите кол-во фруктов ?'))
#     vegetables = int(input('Сколько овощей?'))
#     print('Всего:',fruits + vegetables)

# print('Обезьяны')
# countFood()
# print('\nЖирафы')
# countFood()
# print('\nСлоны')
# countFood()

# 2
# def triangle():
#     stars = 1
#     for line in range(5):
#         print(' ' * (5 - line -1), end = '')
#         stars += 2
# def rectangle():
#     for line in range(5):
#         if line == 0 or line == 4:
#             print('*' * 5)
#         else:
#             print('*' + ' ' * 3 + '*')
#
# choice = int(input('Что рисуем? 1 - треугольник, 2 - прямоугольник'))
# if choice == 1:
#     triangle()
# elif choice == 2:
#     rectangle()
# else:
#     print('Ошибка ввода !!!')

# ---------------------------------------------------------------------
# 1
# def greeting():
#     Count_Yes = 0
#     Count_No = 0
#     people = 0
#     while True:
#         question = input('Зайдете?Да/Нет:')
#         if question == 'Да':
#             print('Добро Пожаловать !')
#             Count_Yes += 1
#             print('Следующий')
#         elif question == 'Нет':
#             print('Следующий!')
#             Count_No += 1
#         people +=1
#         if people == 5:
#             break
#     print(f'Всего зашли:{Count_Yes}')
#     print(f'Всего не зашли:{Count_No}')
#
# greeting()

# 2

# def countFood():
#     a = int(input())
#     b = int(input())
#     print("Всего", a + b, "шт.")
#
#
# print("Сколько мешков рыбы и мяса?")
# countFood()
# print("Сколько буханок белого и чёрного хлеба?")
# countFood()
# print("Сколько вёдер воды и молока?")
# countFood()
#


# def information():
#     surname = input('Фамилия:')
#     name = input('Имя:')
#     street = input('Улица:')
#     house = input('Дом:')
#
#
# information()
# print('\n')
# information()
# print('\n')
# information()
# --------------------------------------------------------------


# def myAdress(name):
#     print('Фамилия: Иванов')
#     print('Имя: ',name)
#     print('Улица: Пушкина')
#     print('Дом: 32')
#     print()
#
# myAdress('Василий')
# myAdress('Игорь')
# myAdress('Алена')
#

# --------------------------------

# import  math
# def func(x):
#     if  - 5 <= x <= 5:
#         print('x =', x,'y =', math.exp(x))
#     elif x <  -5:
#         print('x =', x, 'y =', 2 * abs(x) - 1)
#     else:
#         print('x =', x, 'y =', 2 * x)
#
#
# for x in range (-10, 11):
#     func(x)

# ---------------------------------

# def monye(price):
#     print('Название: КлирВотер')
#     print('Производитель: ВодЗавод')
#     print('Цена:',price)
#     print()
#
# monye(25)
# monye(30)
# monye(40)

# или
import math


# def about_water(price):
#     print("Название: КлирВотер\n"
#           "Производитель: ВодЗавод\n"
#           f"Цена: {price}")
#
# for _ in range(3):
#     price_of_water = int(input('Введите цену:'))
#     about_water(price_of_water)
#     print()

# -------------------------------------------------

# def sphere_area(radius):
#     print(4 * math.pi *radius ** 2)
#
# def sphere_volume(radius):
#     print(4 / 3 * math.pi * radius ** 3)
#
# radius_of_planet = float(input('Введите радиус планеты:'))
# sphere_area(radius_of_planet)
# sphere_volume(radius_of_planet)

# -----------------------------------------

# def is_prime(number):
#     for i in range(2,int(number **0.5) +1):
#         if number % i == 0:
#             return False
#         return True
#
# n = int(input('Введие количество чисел в последовательности:'))
# for i in range (n):
#     new_number = int(input('Введите число:'))
#     is_prime(new_number)

# ----------------------------------------------

# def myAdress(name,house_number):
#     print('Фамилия: Иванов')
#     print('Имя: ',name)
#     print('Улица: Пушкина')
#     print('Дом:',house_number)
#     print()
#
# myAdress('Василий',43)
# myAdress('Игорь',34)
# myAdress('Алена',22)

# -----------------------------------------------
# import math
#
# def myDistance(x , y):
#     distance = math.sqrt(x ** 2 + y ** 2)
#     print(distance)
#
# def betweenDistance(x_1, y_1, x_2, y_2):
#     distance = math.sqrt((x_2 - x_1) ** 2 + (y_2 -y_1) **2)
#     print(distance)
#
#
#
# choice = int(input('1 - Расстояние от точки: 2 - расстояние между двумя точками: '))
# if choice == 1:
#     x = float(input('Введите координату икс'))
#     y = float(input('Введите координату игрек'))
#     myDistance(x, y)
# elif choice == 2:
#     x_1 = float(input('Введите координату икс первой точки'))
#     y_1 = float(input('Введите координату игрек первой точки'))
#     x_2 = float(input('Введите координату икс второй точки'))
#     y_2 = float(input('Введите координату игрек второй точки'))
#     betweenDistance(x_1, y_1, x_2, y_2)
# else:
#     print('Ошибка ввода')
# ----------------------------------------------------
# def number(left,right):
#     number = (left + right) / 2
#     print(number)
#
#
# left = int(input('Введите левую границу:'))
# right = int(input('Введите правую границу:'))
#
# number(left,right)

# ------------------------------------------------------
# def information(surname, name, country, place_of_state , city, street, number_of_house, number_of_flat):
#     information(surname,name,country,place_of_state,city,street,number_of_house,number_of_flat)
# for all in range(3):
#     print()
#     surname = input('Введите Фамилию:')
#     name = input('Введите Имя:')
#     country = input('Введите Страну:')
#     city = input('Введите город проживания:')
#     street = input('Введите улицу:')
#     number_of_house = input('Введите номер дома:')
#     number_of_flat = input('Введите номер кв')
#     print()
#     print(surname, name, country, city, street, number_of_house, number_of_flat)
#
# ----------------------------------------------
# def print_all_information(surname, name, country, city, street, houese, flat):
#     print('Фамилия',surname)
#     print('Имя',name)
#     print('Страна проживания',country)
#     print('Город',city)
#     print('Улица',street)
#     print('Номер Дома',houese)
#     print('Номер Кв',flat)
#
# def print_all_info_hard(surname, name, country, city, street, house, flat):
#     print(f"Фамилия: {surname}\n"
#           f"Имя: {name}\n"
#           f"Страна: {country}\n"
#           f"Город: {city}\n"
#           f"Улица: {street}\n"
#           f"Дом: {house}\n"
#           f"КВ: {flat}\n")
#
# user_surname = input('Введите Фамилию:')
# user_name = input('Введите Имя:')
# user_street = input('Введите Улицу:')
# user_house = input('Введите Дома:')
#
# for _ in range(3):
#     user_surname = input('Введите Фамилию:')
#     user_name = input('Введите Имя:')
#     user_country = input('Введите Страну:')
#     user_city = input('Введите город:')
#     user_street = input('Введите Улицу:')
#     user_house = input('Введите Дома:')
#     user_flat = input('Введите Дом:')
#
#     print_all_information(user_surname, user_name, user_country, user_city, user_street, user_house, user_flat)

# -----------------------------------------------------------------------------------------

# def mainMenu():
#     print('1 - сделать что то плохое')
#     print('2 -  сделать что то хорошее')
#
#     choise = int(input('Введите номер действия: '))
#
#     if choise == 1:
#         good()
#     elif choise == 2:
#         bad()
#     else:
#         print('Ошибка ввода:нужно ввести 1 или 2')
#         mainMenu()
#
# def good():
#     print('Все хорошо.')
#     input('Нажмите любую кномпу чтобы вернуться в меню:')
#     mainMenu()
#
# def bad():
#     print('Все плохо.')
#
#
# mainMenu()
# ---------------------------------------------------------------------------------------------

# def myAdress(name,house_number):
#     print('Фамилия: Иванов')
#     print('Имя:',name)
#     print('Улица: Пушкина')
#     print('Дом:',house_number)
#     print()
#
# myAdress('Игорь',32)
# myAdress('Василий',45)
# myAdress('Алена',67)

# 2
# import math
# def my_distance(x,y):
#     distance = math.sqrt(x ** 2 + y ** 2)
#     print(distance)
#
#
# def betweenDistance(x_1, y_1, x_2, y_2):
#     distance = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
#     print(distance)
#
# choise = int(input('1 - расстояние до точки, 2 - расстояние между двумя точками:'))
# if choise ==1:
#     x = float(input('Введите координтау икс:'))
#     y = float(input('Введите координату игрик:'))
#     my_distance(x,y)
# elif choise == 2:
#     x_1 = float(input('Введите координтау первой точки икс:'))
#     y_1 = float(input('Введите координату первой точки игрик:'))
#     x_2 = float(input('Введите координтау второй точик икс:'))
#     y_2 = float(input('Введите координату второй точки игрик:'))
#     betweenDistance(x_1, y_1, x_2, y_2)
# else:
#     print('Ошибка Ввода.')
# ---------------------------------------------------------------------------
# Home Work---------------------------------------------------------------

# 1
# def mean_calc(x,y):
#     print('Среднее:',round(x +y) / 2)
#
# a = int(input('Введите a:'))
# b = int(input('Введите b:'))
# if a < b:
#     a,b = b,a
# elif a > b:
#     print(f'Ошибка число: {a} должно быть меньше числа {b}.Попробуй еще раз!!!')
#
# mean_calc(a,b)

# 2
# def all_information(name, surname, Country, Place, City, Street, NumberFlat):
#     print(f"Фамилия:{surname}\n"
#           f"Имя:{name}\n"
#           f"Страна:{Country}\n"
#           f"Проживание:{Place}\n"
#           f"Город:{City}\n"
#           f"Улица:{Street}\n"
#           f"Номер Кв:{NumberFlat}\n")
#     print()
#
#
# all_information('Jafar', 'Sabri', 'Kazakhstan', 'Almaty', 'Almaty', 'Zhandosova', '32')
# all_information('Oralbek', 'Saparaly', 'Kazakhstan', 'Almaty', 'Almaty', 'Tole-Bi', '52')
# all_information('Maksat', 'Inkar', 'Kazakhstan', 'Almaty', 'Almaty', 'Sairan', '89')

# -----------------------------------------------------------------------------------------
# def mainmenu():
#     print('1. Cделать что то хорошее')
#     print('2. Сделать что то плохое')
#     choice = int(input('Введите номер действия:'))
#     if choice == 1:
#         good()
#     elif choice == 2:
#         bad()
#     else:
#         print('Ошибка ввода:нужно ввести 1 или 2.')
#         mainmenu()
#
# def good():
#     print('Все хорошо ')
#     input('Нажмите любую кнопку чтобы вернутся в меню.')
#     mainmenu()
#
# def bad():
#     print('Все плохо.')
#
#
# mainmenu()

# ----Home Work --------------------------------------------------------------------------------------

# 1
# def summa_n():
#     result = 0
#     new = int(input('Введите число:'))
#     for number in range(1, new + 1):
#         result += number
#     return result
#
# print(summa_n())
# ---------------------------------------------------------------------------------------------------

# 2
# def test():
#     number = int(input('Введите целое число:'))
#     if number < 0:
#         negative()
#     elif number >= 0:
#         positive()
#
# def positive():
#     print('Положительное :)')
#
# def negative():
#     print('Отрицательное:(')
#
#
# test()
# -------------------------------------------------------------------------------------------------------

# 3
# def main():
#     while True:
#         one_number = (int(input('Введите число:')))
#         choise = int(input('Что нужно сделать с числом ? 1 - Ввывести сумму его цифр, 2 - максимум, 3- минимальную: '))
#         result = 0
#         if choise == 1:
#             result = summa(one_number=one_number, choise=choise)
#         elif choise == 2:
#             result = max_number(number=one_number)
#         elif choise == 3:
#             result = min_number()
#         else:
#             print('Ошибка Ввода БАРАН')
#         print(result)
#
#
# def summa(choise, one_number):
#     result = 0
#     for number in range(1, one_number + 1):
#         result += number
#     return result
#
#
# def max_number(number):
#     return number
#
#
# def min_number():
#     return 0
#
#
# main()
#-----------------------------------------------------------------------------------------------------------------

#4
# def uppend_number(digit):
#     flip_number = 0
#     count = 0
#     duplication = digit
#     while duplication // 1 != 0:
#         count += 1
#         duplication //= 10
#
#     multiplier = 1
#     for i in range(count - 1):
#         multiplier *= 10
#
#     while digit // 1 !=0:
#         flip_number +=digit % 10 * multiplier
#         multiplier //= 10
#         digit //= 10
#     print('Число наоборот:',flip_number)
#
# while True:
#     digit = int(input('\nВведите число:'))
#     if digit == 0:
#         print('Программа остановлена !')
#         break
#     uppend_number(digit)
#-----------------------------------------------------------------------------------------------------------------------

#5
# def count_letters():
#     text = input('Введите текст:')
#     letter = input('Какую букву мы ищем?')
#     number = input('Какую цифру мы ищем?')
#     count_letter = 0
#     count_number = 0
#     for check in (text):
#         if check == letter:
#             count_letter += 1
#         elif check == number:
#             count_number += 1
#     print('Кол-во цифр', number, ':', count_number)
#     print('Кол-во букв', text, ':', count_letter)
#
# count_letters()
#-----------------------------------------------------------------------------------------------------------------------

#  6
# def dividesrs():
#     number1 = int(input('Введите число:'))
#     number2 = int(input('Введите число:'))
#     max_div = 0
#     for summ in range(1, number1 + 1):
#         if number1 % summ == 0:
#             if number2 % summ == 0:
#                 max_div = summ
#     print('Наибольший общий делитель:', max_div)
#
# dividesrs()
#-----------------------------------------------------------------------------------------------------------------------



