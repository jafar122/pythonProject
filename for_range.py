# text = 'Python !'
# for word in range(5):
#     print(text )
#     print(word)


# total_month = int(input('Введите сколько Месяцев будет копить  Алексей:'))
# summ = 0
# for month in range (total_month):
#     print('Месяц:',month)
#     money = int(input('Сколько рублей откладываем ?:'))
#     summ += money
# print('За', total_month,'месяцев ты накопишь',summ,'рублей')
#

# 1
# for a in range (10):
#     a **= 2
#     print(a)

#2
# hour = int(input('Который час?:'))
# for a in range(hour):
#     print('Ку-Ку!')

# begin_number =int(input('Введите начальное число:'))
# end_number = int(input('Введите конечное число:'))
# for number in range(begin_number,end_number):
#     print(number ** 2)

# wake_up = int(input('Введите во сколько Саша проснулся: '))
# awake_hours = 0
# calories_sum = 0
# for hour in range (wake_up,23):
#     print('Сейчас:',hour,'часов')
#     calories = int(input('Сколько съел за час?'))
#     calories_sum += calories
#     awake_hours +=1
#     if calories_sum > 2000:
#         print('Хорошо Поел, Можно и поспать')
#         break
#     print('Съедино колорий за день:',calories_sum)
#     print('Часов не спал:',awake_hours)


# for number in range (1,10):
#     print(number ** 3)



# first_number = int(input('Введите перове число: '))
# second_number = int(input('Введите второе число: '))
# summa = 0
# for number in range(first_number,second_number +1) :
#     summa +=numberы
# print(summa)


# prostoe_chislo = int(input('Ввведите простое число: '))
# isPrime = True
# for divider in range(2, prostoe_chislo):
#     if prostoe_chislo % divider == 0:
#         isPrime = False
#         break
# if isPrime:
#     print('Число простое')
# else:
#     print('Числое составное')