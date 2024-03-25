# password = int(input('Введите пароль: '))
# while password != 235:
#     print('password not correct')
#     password = int(input('Еще раз пароль: '))
# print( 'Пароль Правильный', password)

# balance = int(input('Введите сколько  пришло на карту '))
# while balance > 5000:
#     product_cost = int(input('Сколько стоит продукт : '))
#     balance -= product_cost
# print('Внимание на карте осталось мало денег Хватит')
# print('Баланс счета ', balance)

#
# number = int(input('Введите число:'))
# summ = 1
#
# while number != 0:
#     summ += number
#     number = int(input('Введите  число: '))
# print(summ)
#

# a = 0
# while a <= 105 :
#     a += 7
#     print(a)


# a = 0
# while a <=105:
#     a += 7
#     print(a, end = ' ')
# print()

# degree =int(input('Сколько Градусов на улице ?'))
# meters = 0
# while degree > 15:
#     meters += 20
#     degree -= 2
#     if degree <= 15:
#         break
#     meters += 10
#
# print('Прйдено Метров:', meters)

# number = int(input('Введите число'))
# summ = 0
# while number != 0:
#     last_num = number % 10
#     print(last_num)
#     if last_num == 5:
#         print('Обнаружен Разрыв')
#         break
#     summ += last_num
#     number //= 10
# print('СУММА', summ)

# numbers = int(input('Введите числа'))
# number = 0
# while numbers >0:


# all_money = int(input('Введите начальное количество денег'))
# b = 500
# while all_money < 10000:
#     kubik_number = int(input('Введите сколько выпало на кубике от 1-6'))
#     if kubik_number == 3:
#         print('Вы проиграли все')
#         break
#
#     elif kubik_number >= 1 and 2 and 4 and 5:
#         all_money += b
#         print('Вы выйграли ',b, 'Рублей' ,'Сумма -',all_money  )

# current_number = 0
# count = 0
# while True:
#     current_number = int(input('Введите число:'))
#     if current_number < 0:
#         print('Найдено Отрицательное число')
#         print('Введенных чисел, не учитывая отрицательное = ',count)
#         break
#     count += 1

# rate_check =False
# while True:
#     active = int(input('Продолжаем работать ? 1/0:'))
#     if active == 0:
#         print('Приложение Закрывается... ')
#         break
#     rate = int(input('Поставили ли вы оценку приложению ? 1/0:'))
#     if rate == 1:
#         rate_check = True
#     if rate_check :
#         print('Пользователь Поставил оценку :)')
#     print('Работа завершена !')

#1
# count = 10
#
# while count >= 0:
#
#     if count == 0:
#         print('Время Вышло')
#         count -= 1
#     else:
#         print(count)
#         count -= 1

# password = False
# while True :
#     print('Компьютер заблокирован. Вернешь скейт - скажу код разблокировки !')
#     new_code = int(input('Введите код :'))
#         if new_code == 550:
#          break
#     print('Код верный,завершаю работу')

