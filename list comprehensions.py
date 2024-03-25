
# squares = [x ** 2 for x in range(10)]
# print(squares)/


# def get_higher_price(percent, price):
#     return round(price ** (1 + percent / 100), 2)
#
# price_now = [1.76, 23.56, 57.86, 4.54, 7.78]
# first_precent = int(input('Повышение на первый год:'))
# second_precent = int(input('Повышение на второй год:'))
#
# prices_first = [get_higher_price(first_precent,i_price) for i_price in price_now]
# prices_second = [get_higher_price(second_precent,i_price) for i_price in prices_first]
#
# print('Сумма цен за каждый год:',round(sum(price_now), 2), round(sum(prices_first), 2), round(sum(prices_second), 2))

# 1

# left = int(input('Левая граница:'))
# right = int(input('Правая граница:'))
#
# cubes = [i ** 3 for i in range(left, right +1)]
# squares = [i ** 2 for i in range(left, right +1)]
#
# print(f'Список кубов чисел в диапазоне от', left, 'до', right, ':', cubes)
# print(f'Список кубов чисел в диапазоне от', left, 'до', right, ':',squares)

# 2
# text = input('Введите строку:')
# sym_bol = input('Введите дополнительный символ:')
#
# doubled_letters = [letter * 2 for letter in text]
# result_msg = [letter + sym_bol for letter in doubled_letters]
#
#
# print("Список удвоенных символов:", doubled_letters)
# print("Склейка с дополнительным символом:", result_msg)
#------------------------------------------------------------------

# squares = []
# for x in range(10):
#     if x % 2 != 0:
#         squares.append(x ** 2)
# print(squares)

# squares_odds = [x ** 2 for x in range(10) if x  % 2 != 0]
# squares_cube = [(x ** 2  if x  % 2 != 0 else x ** 3 for x in range(10))]
#
# print(squares_odds)
# print(squares_odds)



# По задаче у нас юнит либо выжил либо погиб.В этой задаче нужно
# выбрать какой элемент вставить.То есть будет блок else.
# Условная логика будет стоять в начале.
# import random
#
# squad_1 = [random.randint(50, 80) for _ in range(10) ] # random(10)- 10 штук
# squad_2 = [random.randint(30, 68) for _ in range(10) ]
# squad_condition = [('Погиб' if squad_1 [i_damage] + squad_2[i_damage] > 100
#                     else 'Выжил')
#                    for i_damage in range(10) ] # -i_damage - счетчик принимает значения от 0 до 9
#
# print('Урон первого отряда',squad_1)
# print('Урон первого отряда',squad_2)
# print('Урон первого отряда',squad_condition)
#--------------------------------------------------------------

# 1
# first_number = int(input('Первое число A:'))
# second_number = int(input('Второе число B:'))
#
# result = [number for number in range(first_number, second_number) if number % 2 == 0]
# print(result)

# 2
# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# new_price = [price if price > 0 else 0 for price in original_prices]
# print("Результат:\n\n", new_price, sep="")

#-----Срезы Списков----------------------------------------------------
# nums = [x for x in range(1, 101) if x % 10 == 0]
# new_nums = nums[:]     # -  копия [:]- срезы.
# new_nums[3] = 0
#
#
# print(new_nums [2:7])

# 1
# import random
# original_prices = [random.randint(-100, 100) for _ in range(10)]
# new_prices = original_prices[::]  # копирование можно реализовать и через срез
#
# for i in range(len(original_prices)):
#     if new_prices[i] < 0:
#         new_prices[i] = 0
# print("Мы потеряли:", abs(sum(original_prices) - sum(new_prices)))

# 2
# nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
# print("Результат:")
# print(nums[:5])
# print(nums[:-2])
# print(nums[::2])
# print(nums[1::2])
# print(nums[::-1])
# print(nums[::-2])

# 3
# import random
#
# n = int(input("Введите количество чисел N: "))
#
# numbers = [random.randint(-10, 10) for _ in range(n)]
# a = random.randint(0, len(numbers) -2)
# b = random.randint(a + 1, len(numbers) - 1)
# print(numbers, a, b)
# numbers = numbers[:a] + numbers[b +1:]
# print(numbers)

#-------Home Work-----------------------------------
# 1
# def find_vowel(letter):
#     vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
#     for symbol in vowels:
#         if symbol == letter:
#             return symbol
#
# text = (input('Введите текст:'))
#
# vowel_letter = [symbol for symbol in text if find_vowel(symbol)]
# result = len(vowel_letter)
# print('Список гласных букв:', vowel_letter)
# print('Длина списка:', result)

# 2
number = int(input('Введите длину списка '))

result = [1 if digit % 2 == 0 else digit % 5 for digit in range(number)]

print(result)





