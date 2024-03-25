# salary = int(input('Введите сумму которую вы зарабатываете'))
#
# low_t = 10000
# high_t = 50000
#
# if salary < 0:
#     print('Доход не может быть отрицательным')
# elif salary < low_t:
#     print((salary*13) / 100)
# elif low_t <= salary < high_t:
#     print((salary * 20) / 100)
# elif salary >=50000:
#     print((salary*30) /100 )
#


# a = int(input('Введите сколько Илья Набрал Баллов по Экзамену'))
# b = int(input('Есть Медали'))
# if a >280 and b > 0:
#     print('Ты прошел')
# else:
#     print('Ты не прошел')


# temp = int(input('Введите температуру '))
# if temp < 0 or temp > 100:
#     print('Опасно')

# 1
# b = 0
# over_ALL = int(input('Введите количество опыта'))
# b = 1
# if over_ALL >= 1000:
#     b +=1
#
# if over_ALL >=2500:
#     b += 1
#
# if over_ALL >=5000:
#     b += 1
#     print('Your Level - ', b)


# 2
# x = int(input('Введите число икс'))
# if x > 0 :
#     y=x-12
#     print(y)
# elif x == 0 :
#     y = 5
#     print(y)
# elif x < 0 :
#     y = x ** 2
#     print(y)

# 3
# place_in_list = int(input('Введите место в списке поступающих: '))
#
# if place_in_list < 10:
#     total_score = int(input('Введите количество балоов за экзамен: '))
#     print('Поздравляю вы поступили ')
#
#     if total_score > 290:
#         print('Бонусом вам будет стипендия ')
#     else:
#         print('Вы не будете получать стипендию ')
# else:
#     print('Вы не поступили')


#4
# rating = int(input('Что получил по математике? '))
# if rating == 2 or  rating == 3:
#  print('Плохо. Марш учиться!')
#
#
# if rating == 4 or rating == 5:
#  print('Молодец! Можешь отдохнуть.')
#

#5
# count = 0
# first_number = int(input('Введите Пожалуйста  первое число '))
# second_number = int(input('Введите пожалуйста второе число '))
# third_number = int(input('Введите пожалуйста третье число '))
# if first_number == second_number:
#     count += 1
# if first_number == third_number:
#     count += 1
# if second_number == third_number:
#     count += 1
# print('Кол-во совп: ', count)

#6


# a = int(input('Стоймость кв '))
# b = int(input('Площадь кв '))
# if a  <= 7000000 and b <= 80:
#     print('Good Choice')
# else:
#     print('Bad Choice ')

#7

# hour = int(input('Введите время '))
# if (8 <= hour < 10 ) or (12 <= hour < 14 ) or (15 <= hour < 18 ) or ( 20 <= hour < 22) :
#     print('Можно заюрать посылку')
# else:
#     print('посылку получить нельзя')