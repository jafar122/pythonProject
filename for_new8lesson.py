# n = int(input('Введите число:'))
# for number in range(1,n//2 + 1):
#     number *= 2
#     print(number,'** 3 =',number ** 3)

# total_hours = int(input('Введите кол-во часов:'))
# cells = 1
# for hour in range(1,total_hours//3 +1):
#     cells *= 2
#     print('Прошло часов:',hour *3)
#     print('Кол-во клеток:',cells)
#     print('Осталось часов:',total_hours - hour *3)
#     print()
# print('Наблюдение завершено!')



# totall_hours = int(input('Введите кол-во часовЖ:'))
# cells = 1
# for hour in range(1,totall_hours //3 +1):
#     cells *=2
#     print('Прошло часов:',hour *3)
#     print('Кол-во клеток:',cells)
#     print('Осталось Часов:',totall_hours - hour *3)
#     print()
# print('Наблюдение завершено!')






# new_number = int(input('Введите число N:'))
# for number in range (1,new_number,2):
#     number =number * 2 -1
#     print(number,'**2 = ',number **2)


# wake_up = int(input('Введите во сколько просыпается Саша:'))
# calories_sum = 0
# water = 0
# for hour in range(wake_up,23,3):
#    water +=1
#    print('Пошли Есть в ',hour,'часов')
#    calories = int(input('Сколько Съел?'))
#    calories_sum +=calories
# print('Выпито литров воды:',water)
# print('Съедино калорий:',calories_sum)


# new_number = int(input('Введите число:'))
# summa = 0
# for number in range(1,new_number +1,5,):
#     number_of_chair = int(input('Введите номер стула:'))
#     summa +=number_of_chair
# print('Сумма:',summa)



# seconds = int(input('Введите кол-во секунд:'))
# for sec in range(seconds,-1,-1):
#     print('Микроволновка греет:',sec)
# print('Дзынь:')

# totalSoldiers = int(input('Кол-во солдат в шеренге:'))
# total_rules = int(input('Сколько правил в уставе?'))
# push_ups = 0
# for soldier in range(totalSoldiers,0,-4):
#     soldires_rules = int(input('Солдат,назови кол-во правил в уставе:'))
#     if total_rules != soldires_rules:
#         print('Неправильно!',10 *soldier,'отжимании!')
#         push_ups += 10 * soldier
# print('Общее кол-во отжимании:',push_ups)


# n = int(input('Введите четное число:'))
# even_n = n - n % 2
#
# for i in range (even_n,0,-2):
#     print(i)
# print('Я иду искать!')
#



# begin_number = int(input('Введите начальное число:'))
# end_number = int(input('Введите конечное число:'))
# step = int(input('Введите шаг:'))
#
# for number in range(begin_number,end_number + 1,step):
#     print(number,'** 2 = ',number ** 2)
#     step +=4
#     print(step)