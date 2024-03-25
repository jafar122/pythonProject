# 1
# plus_number = 0
# for number in range(1, 11):
#     new_number = int(input('Введите 10.цифр:'))
#     # print(number, '-число')
#     if new_number % 2 == 0 and new_number > 0:
#         plus_number += 1
#
# print(plus_number)
#

#2
# month = 0
# total = 0
# count = 0
# for month in range(1, 13):
#     month_salary = int(input('Введите запрлату сотрудника за каждый месяц:'))
#     month += 0
#     print(month, 'месяц')
#     total +=month_salary
#     count += 1
# print('Средняя зарабатная зарплата:=', total // count)

#3
# count_factory = 1
# new_factory = int(input('Введите новый факториял:'))
# for factory in range(1,new_factory +1):
#    count_factory *= factory
# print('Факториал числа',new_factory,'равен',count_factory)

#4
# five = 0
# four = 0
# three = 0
# count = 0
# all_class_students = int(input('Введите сколько студентов в классе:'))
# for student in range(1, all_class_students + 1):
#     print(student, '.')
#     marks = int(input('Введите какие оценки получили ученика начиная с 3 и заканичиваним 5:'))
#     if marks == 3:
#         three += 1
#     elif marks == 4:
#         four += 1
#     elif marks == 5:
#         five += 1
#     else:
#         print("unknown garde")
# print(four, '- Хорошист')
# print(three, '- Трошник')
# print(five ,'- Отличникиков')

#5

# number_a = int(input('Введите пожалуйста число a:'))
# number_b = int(input('Введите пожалуйста число b:'))
# for number in range(number_a,number_b +1):
#
#     print()

#6

#7
# total = 0
# tottal_cards = int(input('Введите количество карточек:'))
# for cards in range(1,tottal_cards+1):
#     # number_of_card +=0
#     total +=cards
# for cards in range(1,tottal_cards -1):
#     number_of_card = int(input('Введите номер карт:'))
#     total -= number_of_card
# print(total)


# total = 0
# n = int(input('Введите количество карточек:'))
# for number in range(1, n + 1):
#     total += number
# for number in range(1, n):
#     number1 = int(input('Введите карту '))
#     total -= number1
#     print(total)

# minimum = 0
# maximum = 0
# total = 0
# srednee = 0
# total_number = 0
# print('Введите 5 цифр')
# for number in range (1, 6):
#     all_number = int(input('Введите цифру:'))
#     total += all_number
#     if minimum == 0 or all_number < minimum:
#         minimum = all_number
#     if maximum == 0 or all_number > maximum:
#         maximum = all_number
#     total_number += 1
# print(total /total_number)
# print(maximum)
# print(minimum)
# print(total)







# all_numbers = int(input('Введите числа:'))
# for number in range(1, all_numbers + 1):
#     total +=number
# print(total)
# # all_numbers = int(input('Введите числа :'))
# # for number in range(1,all_numbers,1):
#
# #     all_numbers = int(input('Введите числа:'))
# # for number in range(1,all_numbers +1):
#

# all_hours = input('Введите часы:')
# all_money_rate = input('Введите ставку за час:')
#
# hours_pay = float(all_hours)
# money_rate = float(all_money_rate)
#
# if hours_pay <= 40:
#     gross_pay = hours_pay * money_rate
# else:
#     regular_time = 40
#     overtime_hours = hours_pay - 40
#     gross_pay = (regular_time * money_rate) + (overtime_hours * 1.5 * money_rate)
#
# print(gross_pay)


# while True:
#     a = (input('Введите число:'))
#     count += 1
#     if a == 'Done':
#         break
# print(count)

count = 0
minimum = None

while True:
    num = input("Enter the number: ")
    if num == "done":
        break
    try:
        int_num = int(num)
    except:
        print("Invalid input")
        continue

    if minimum == 0 or minimum > int_num:
        minimum = int_num
    count = count + 1


print("Count", count)
print("Minimum", minimum)
