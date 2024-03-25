# 1
# all_grecha = 100
# moth_grecha = 0
# for grecha in range(0,all_grecha +1,4):
#     moth_grecha +=1
#     print(moth_grecha, '-ый месяц:')
#     print(grecha)
#

# 2
# enter_dolzhnik = int(input('Введите кол-во должников:'))
# total_dolzhnik = 0
# for dolzhnik in range(0,enter_dolzhnik,5):
#     print('Должник с номером:', dolzhnik)
#     much_pay = int(input('Сколько Должны :'))
#     total_dolzhnik +=much_pay
# print('Общая Сумма долга:',total_dolzhnik)


# 3


# 4
# a = int(input('Введите первое число:'))
# b = int(input('Введите второе число:'))
# c = int(input('Введите третье число:'))
#
# sum_numbers = 0
# count_numbers = 0
#
# for number in range(a, b + 1):
#     if number % c == 0:
#         sum_numbers += number
#         count_numbers += 1
# if count_numbers > 0:
#     avarage = sum_numbers / count_numbers
#     print(f'Среднее арифметическое чисел {a} до {b} , кратных {c}, равно : {avarage}')
# else:
#     print(f'В указаном отрезке нет чисел,кратных: {c}')


# 5
# start = int(input('Введите начала отрезка:'))
# stop = int(input('Введите конец отрезка:'))
# step = int(input('Введите шаг:'))
# for range_num in range(stop, start - 1, step):
#     print('num: ', range_num)
#     result = (range_num ** 3) + (2 * (range_num ** 2))- (4 * range_num) +1
#     print(result)

# 6
# educational_grand = 10000
# expenses = 12000
# total = 0
# for month in range(1,11):
#     total += expenses - educational_grand
#     print(month, '.месяц траты', round(expenses,1), 'не хватает', round(total, 2))
#     formula = (expenses * 3) / 100
#     expenses += formula


# 7

# first_number = int(input('Введите N:'))
# summ = 0
#
# for number in range(0, first_number):
#     result = (-1 ** number) * (1 / (2 ** number))
#
#     if number % 2 == 0:
#         result = -result
#
#     summ += result
#
# print(summ)
#

#8

# boys = int(input('Введите кол-во мальчиков:'))
# girls = int(input('Введите кол-во девочек:'))
# answer = '' #- где будем хранить ответ -пустая строка
# if (boys > 2 * girls) or (girls >  2 * boys ):
#     print('Нет Решения.')
# elif boys >= girls:
#     k = boys - girls
#     for bgb in range (k):
#         answer += 'BGB'
#     for bg in range(girls - k):
#         answer += 'BG'
# else:
#     k = girls - boys
#     for gbg in range(k):
#         answer += 'GBG'
#     for bg in range(girls - k):
#         answer += 'GB'
# print(answer)
