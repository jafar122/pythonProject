#  1
# toral_number = int(input('Введите число:'))
# number = 0
# while number != toral_number:
#     number += 1
#     summ = number
#     summ **= 3
#     print(summ)
# 2
# while True:
#     print('Василий, ваша задолженность составляет 100 рублей')
#     money = int(input('Сколько рублей вы внесете прямо сейчас, чтобы ее погасить ? '))
#     if money < 100 :
#         print('Маловато, Василий. Давайте еще раз.')
#     else:
#         print('Отлично.Василий! Вы погасили долг.Спасибо! ')
#         break

# 3
# number = int(input('Введите число:'))
# iteration = 0
# while number != 0:
#     last_number = number % 10
#     number //= 10
#     iteration +=1
# decimal_digit = iteration // 10
# print('Десятичных цифр:',decimal_digit)

# 4
# plus_number = 0
# mines_number = 0
# while True:
#     all_number = int(input('Введите число : '))
#     if all_number > 0:
#         plus_number += 1
#     else:
#         if all_number < 0:
#             mines_number += 1
#         elif all_number == 0:
#             print('Кол-во положительных чисел: ', plus_number)
#             print('Кол-во отрицательных чисел ', mines_number)
#             break

# 5
# print('Начался восьмичасовой рабочий день.')
#
# calling_wife = True
# total_hour = 0
# total_ex = 0
# while True:
#     hour = int(input('Какой час:'))
#     hour += total_hour
#     print(hour, '-й час')
#     exercises = int(input('Сколько задач решит Максим?'))
#     total_ex += exercises
#     calling_wife = int(input('Звонит Жена. Взять трубуку?(1-Да,0-Нет):'))
#     if calling_wife == 1:
#         calling_wife = False
#     if hour == 8:
#         break
# print(total_ex)
# if not calling_wife:
#     print('Нужно зайти в магазин срочно.')


# 7

# all_count = 0
# while True:
#     all_count += 1
#     number_new = int(input('Введите число '))
#     number = 7
#     if number_new < number:
#         print('Число меньше чем нужно.Попробуйте еще раз!')
#     else:
#         if number_new > number:
#             print('Число больше чем нужно. Попробуйте еще раз!')
#         else:
#             if number_new == number:
#                 print('Вы угадали ! Число поппыток:', all_count)
#                 break

# 8
# N = (100 + 1) // 2
# while True:
#     print('Твое число равно , больше или меньше числа:',N,'?')
#     answer = int(input('1 -равно , 2-больше, 3-меньше :'))
#     if answer ==1:
#         print('Я угадал !')
#         break
#     elif answer ==1:
#         N -= 1
#     else:
#         N+=1

