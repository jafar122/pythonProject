
# rain = int(input('На улице идет дождь?'))
# if rain == 1:
#     print('Пошел дождь . Возьмите зонтик')
# else:
#     print('Дождя нет хомело!')

#2
# russian = int(input('Введите количество баллов по руссокму языку:'))
# math = int(input('Введите количество баллов по математике:'))
# informatik = int(input('Введите количество баллов по информатике:'))
#
# total =russian+math+informatik
# if total >= 270:
#     print('Поздравляю,Ты поступил на бюджет')
# else:
#     print('К сожалению,ты не прошел на бюджет ')

#3
# new_number = int(input('Введите число:'))
# if new_number % 2 == 0:
#     print('Число Четное ')
# else:
#     print('Число не четное ')ди с

#4

# prado = int(input('Введите стоймость товара:'))
# guci = int(input('Введите стоймость товара:'))
# guess = int(input('Введите стоймость товара: '))
# total = prado + guci + guess
# if total > 10000:
#     print(((total *10) / 100),'Итоговая сумма к оплате')
# elif total <= 10000:
#     print('Сумма без скидки:',total)

#5
# number = int(input('Введите число:'))
# if number > 0 :
#     print(number)
# elif number < 0 :
#     number *= -1
#     print(number)

#6
# first_number = int(input('Введите число:'))
# second_number = int(input('Введите второе число :'))
# if first_number >= second_number:
#     a = first_number - second_number
#     print('Игрок платит',a)
# elif first_number <= second_number:
#     a = first_number + second_number
#     print('Сумма:',a)
#     print('Владелец Платит')
# print('Игра окончена')

#7

# hour = int(input('Введите отработанные часы:'))
# credit = int(input('Введите остаток по кредиту:'))
# food_money = int(input('Введите кол.во денег на еду:'))
# salary = ((200*hour) / 2 ** 3) + hour
# total = credit +food_money
# if salary < total:
#     print('Часов не хватает . Придется Работать еще больше')
# else:
#     print('Часов хватает')
# 8
# max1 = int(input('Введите число:'))
# max2 = int(input('Введите число:'))
# max3 = int(input('Введите число:'))
# if max1 > max2 and max1 > max3:
#     print(max1)
# elif max2 >max1 and max2 > max3:
#     print(max2)
# elif max3 > max1 and max3 > max2:
#     print(max3)
#-------------------------------------------------------------------------------------------------------------------------------

#1
# eneter_level = int(input('Введите количество уровня:'))
# level = 1
# if eneter_level <= 1000:
#     print('Ваш Уровень:', level)
# elif eneter_level < 2500:
#     level +=1
#     print('Ваш Уровень:', level)
# elif eneter_level < 5000:
#     level += 2
#     print('Ваш Уровень:', level)
# elif eneter_level > 5000 :
#     level += 3
#     print('Ваш Уровень:', level)

#2
# chislo_x = int(input('Введите число x:'))
# chislo_y = 0
# if chislo_x > 0:
#     chislo_y = chislo_x -12
# elif chislo_x == 0 :
#     chislo_y = 5
# elif chislo_x < 0:
#     chislo_y = chislo_x * chislo_x
#
# print(chislo_y)

#3
# place_in_list = int(input('Введите место в списке поступающих:'))
# if place_in_list <= 10:
#     total_mark = int(input('Введите кол.во баллов за экзамен'))
#     if total_mark > 290:
#         print('Поздравляем, вы поступили!')
#         print('Бонусом вам будет начислена стипендия')
#     if total_mark < 290:
#        print('Поздравляем, вы поступили!')
#        print('Но Вам не хватило балов на стипендию')
# else:
#     if place_in_list > 10:
#         print('К Сожалению вы не поступили ')

#4
# mark = int(input('Что получил по математике:'))
# if mark == 2:
#     print('Плохо.Марш учится !')
# elif mark == 3:
#     print('Плохо.Марш учится !')
# elif mark > 3:
#     print('Молодец, Можешь отдохнуть :)')

#5
# a =0
# b = 0
# c = 0
# first_number = int(input('Введите перове число: '))
# second_number = int(input('Введите второе число:'))
# third_number = int(input('Введите третье число:'))
# d = first_number,second_number,third_number
# e = second_number,third_number,
#
# if first_number == d :
#     a +=3
#     print(a)
# elif second_number == third_number and second_number == first_number:
#     b += 2
#     print(b)

#6
# ploshad = int(input('Введите площадь кв:'))
# cost = int(input('Введите стоймость кв:'))
# if ploshad < 100 and cost < 10000000:
#     print(ploshad,cost,'Подходит')
# else:
#     print('Не Подходит')

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