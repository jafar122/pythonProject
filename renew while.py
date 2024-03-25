#1
# while True:
#     number = int(input('Введите число:'))
#     print(number ** 3)

#2
# print('Василий Ваша Задолжность составляет 100  рублей')
# while True:
#     how_much_pay = int(input('Сколько рублей вы внесете прямо сейчас, чтобы ее погасить?'))
#     if how_much_pay < 100:
#         print('Маловато,Василий.Давайте еще раз')
#     else:
#         if how_much_pay > 100:
#             print('Отлично,Василий! Вы погасили долг.Спасибо.')
#             break

#3
# count = 0
# while count < 10:
#     numbers = int(input('Введите число:'))
#     count += 1
# print('Вы ввели: -',count,'раз')
#4
# positive_number = 0
# negative_number = 0
# while True:
#     number = int(input('Введите число:'))
#     if number > 0:
#         positive_number += 1
#     else:
#         if number < 0:
#             negative_number += 1
#     if number == 0:
#         break
# print('Кол.во положительных чисел:',positive_number)
# print('Кол.во отрицательных чисел:',negative_number)

#5
# wife = False
# total_task = 0
# hour = 1
# print('Начался восьмичасовой рабочий день.')
# while hour <= 8:
#     print(hour, '- й час')
#     hour += 1
#     task = int(input('Сколько задач решил Максим?'))
#     total_task += task
#     calling_wife = int(input('Звонит жена. Взять Трубку? (1-да, 0-нет):'))
#     if calling_wife == 1:
#         wife = True
# if wife:
#     print('Нужно Зайти в Магазин')
# print('Рабочий день закончился. Всего выполнено задча:', total_task)

#7
# count = 0
# while True:
#     number = int(input('Введите число:'))
#     if number < 7:
#         print('Число Меньше чем нужно.Попробуйте еще раз!')
#         count += 1
#     else:
#         if number > 7:
#             print('Число больше,чем нужно.Попробуйте еще раз!')
#         elif number ==7:
#          break
# print('Вы угадали! Число попыток:',count)



