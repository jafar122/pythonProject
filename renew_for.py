#1
# task = 0
# for number in range (1,11):
#     number += 0
#     print(number, '-ое число')
#     new_number = int(input('Введите 10.ть чисел:'))
#     if new_number > 0 and new_number % 2 == 0 : # два равно нужно чтобы проверялось является ли наше выражение четным и не остается ли остатка .То есть везде нужен ответ без остатка .
#         task +=1
# print(task,'-чисел являются одновременно четными и положительными')

#2

# total = 0
# count = 0
# for one in range(1,13):
#     one += 0
#     print(one, '-ый месяц:')
#     salary = int(input('Введите зарплату за один месяц:'))
#     total += salary
#     count +=1
# print('Средняя зп сосотавляет : ',total // count )
#

#3
# count = 1
# factory = int(input('Введите натуральное число:'))
# for number in range (1,factory +1 ):
#     count *= number
# print('Факториал числа',factory,'равен -',count)

# count_factory = 1
# new_factory = int(input('Введите новый факториял:'))
# for factory in range(1,new_factory +1):
#    count_factory *= factory
# print('Факториал числа',new_factory,'равен',count_factory)

#4
# tree = 0
# four = 0
# five = 0
# student = 0
# total_students = int(input('Введите сколько студентов в классе:'))
# for students in range (total_students):
#     student += 1
#     print(student, '-ый студент')
#     total_marks = int(input('Введите оценку каждого студента: '))
#     if total_marks == 3:
#         tree += 1
#     else:
#         if total_marks == 4:
#             four +=1
#         elif total_marks == 5:
#             five +=1
# print(tree,'-столько студентов получили тройки ')
# print(four,'-столько студентов получили четверки ')
# print(five,'-столько студентов получили пятерки')
# print('Just Practice Your self habibi :)')

#6

#7
# total_cards = int(input('Введите кол.во карт:'))
# Total_Sum = 0
# remaining_sum = 0
# for card in range(1,total_cards +1):
#     Total_Sum += card
# for card in range(total_cards - 1):
#     remainig_card = int(input('Номер Оставшейся карты:'))
#     Total_Sum -=remainig_card
# print('Номер потерявшейся карты:',Total_Sum)