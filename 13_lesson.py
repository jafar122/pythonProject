# def calculate_tax(price,tax):
#     tax += 10
#     print(tax)
#     total = price + (price * tax / 100) # - считается
#     return total # - выводится, возвращается
#
# myPrice = int(input('Введите цену:')) # - нужные значения
# myTax = int(input('Введите налог (в %):')) # - нужные значения
#
# totalPrice = calculate_tax(myPrice, myTax) # - вызов функции,куда передаем эти значения в виде аргументов
#
# newTax = int(input('Введите новый налог (в %):')) # - нужные значения
# totalPrice = calculate_tax(totalPrice, newTax) # - вызов функции
#
# print('Итоговая цена:',totalPrice)
#--------------------------------------------------------------------------------------------------------------

# def numeral_count(number): # - принимает один аргумент , это число.
#     if number < 0 :
#         print('Число Отрицательное! Обнуляю.')
#         return 0
#     count = 0 # - алгоритм который будет считать кол-во цифр. Создадим новую переменнную
#     while count > 0:
#         number // 10 # - делим число
#         count += 1 # - увеличививаем на один
#
#     return  count
#
# firstTusk = int(input('Введите первое число:')) #-запрашиваем числа
# secondTusk = int(input('Введите второе число:'))
#
# firstNumeral = numeral_count(firstTusk) # - создаем новую пересенную , чтобы сравнить количество цифр в двух переменных.
# secondNumeral = numeral_count(secondTusk) #- создаем новую пересенную , чтобы сравнить количество цифр в двух переменных.

# if firstNumeral > secondNumeral:
#     print('Цифр больше в первом числе.')
# elif firstNumeral < secondNumeral:
#     print('Цифр Больше во втором числе.')
# else:
#     print('Равное кол-во цифр!')

#-----------------------------------------------------------------------------------------------------------------------

def ex1():
    a = 5
    b = 6
    c = (a + b) * 10
    print(c)

ex1()