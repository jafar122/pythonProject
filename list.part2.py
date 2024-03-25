# langs = ['Python', 'Java', 'JS', 'SQL']
# langs.insert(2, 'c++')
#
# print(langs)

#------------------------------------------------------

# 2
# langs = ['Python', 'Java', 'JS', 'SQL']
# user_lang = input('После чего вставить:')
# i_lang = langs.index(user_lang)
#
# langs.insert(i_lang + 1, 'c++')
#
# print(langs)
#------------------------------------------------------

# 3
# films = [
#     'Крепкий орешек', 'Назад в будущее', 'Таксист',
#     'Леон', 'Богемская рапсодия', 'Город грехов',
#     'Мементо', 'Отступники', 'Деревня',
#     'Проклятый остров', 'Начало', 'Матрица'
# ]
#
# n = int(input("Сколько фильмов выбрать? "))
# your_films = []
# for i in range(n):
#     print("Ваш текущий топ фильмов:", your_films)
#     film_name = input("Имя фильма: ")
#     print("Команды: добавить, вставить, удалить")
#     command = input("Введите команду: ")
#     if film_name not in your_films:
#         if command == "добавить":
#             your_films.append(film_name)
#         elif command == "вставить":
#             insert_index = int(input("Введите индекс для вставки "))
#             insert_index %= len(your_films)  # ограничим индекс списка, чтобы он не вылезал за границу списка
#             your_films.insert(insert_index, film_name)
#     else:
#         if command == "удалить":
#             your_films.remove(film_name)
#         elif command == "добавить" or command == "вставить":
#             print("Этот фильм уже есть в вашем списке.")
#
# print("Ваш текущий топ фильмов:", your_films)

#1
# zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
# zoo.insert(1, 'bear')
# zoo.remove('elephant')
#
# print("Зоопарк:", zoo)
#
# print("Лев сидит в клетке номер", zoo.index('lion') + 1)
# print("Обезьяна сидит в клетке номер", zoo.index('monkey') + 1)

#2
# count = 0
# total_emaploys = int(input('Кол-во сотрудников:'))
# wages_of_works = []
# for i in range(total_emaploys):
#     wages = int(input(f"Зарплата {i + 1} сотрудника:"))
#     if wages > 0:
#         wages_of_works.append(wages)
#
# print("Осталось сотрудников:", len(wages_of_works))
# print("Зарплаты:", wages_of_works)

#or Можно сперва собрать все зарплаты, затем "удалить" их, собрав подходящие элементы в новый список

# numbers_of_workers = int(input('Кол-во сотрудников:'))
# wages_of_works = [] # -пустой список
# for i in range(numbers_of_workers):
#     wage = int(input(f"Зарплата {i} сотрудника:"))
#     wages_of_works.append(wage)
#
# print("Осталось сотрудников:", len(wages_of_works))
# print("Зарплаты:", wages_of_works)

#--------------------------------------------------------------------
#
# my_list = ['Игра', 'Изгой', 'Таксист']
# your_liyst = ['Начало', 'Отступник', 'Корол Лев']
#
# my_list.extend(your_liyst)
# my_list.extend('alladin')
#
# for i_lem in my_list:
#     print(i_lem)
#
#------------------------------------------------------------------
# pack = []
# decode = []
# bad_packs = 0
#
# packs_ant = int(input('Кол-во пакетов:'))
#
# for i_pack_num in range(packs_ant):
#     print('\nПакет номер',i_pack_num + 1)
#     for i_bit in range(4):
#         print(i_bit +1, 'Бит:', end= ' ')
#         num =int(input())
#         pack.append(num)
#     if pack.count(-1) <= -1:
#         decode.extend(pack)
#     else:
#         print('Много ошибок в пакете.')
#         bad_packs += 1
#     pack = []
#
# print('\nПолученное сообщение:', decode)
# print('Кол-во ошибок в сообщении:', decode.count(-1))
# print('Кол-во потерянных пакетов:', bad_packs)

#-----------------------------------------------------------
# 1
# main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
# first_company = [0, 0, 0]
# second_company = [1, 0, 0, 1, 1]
# third_company = [1, 1, 1, 0, 1]
#
# main.extend(first_company)
# main.extend(second_company)
# main.extend(third_company)
# print("Общий список задач:", main)
# print("Кол-во невыполненных задач:", main.count(0))
#------------------------------------------------------------
#  2
# first_word = input("Первое сообщение: ")
# second_word = input("Первое сообщение: ")
# first_count = first_word.count("!") + first_word.count("?")
# second_count = second_word.count("!") + second_word.count("?")
# if first_count < second_count:
#     first_word, second_word = second_word, first_word  # пусть первым словом будет то, в котором больше знаков
#
# print(first_word + second_word)
#-------------------------------------------------------------------
# 1
# numbers = []
# N = int(input('Кол-во участников: '))
# members = []
# num = 1
# for _ in range(N // 3):
#     members.append(list(range(num, num +3)))
#     num += 3
#
# print(members)
#--------------------------------------------------------------

# 1
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in matrix:
#     for j in i:
#         print(j, end=' ')
#     print('\n')

# 2
# human_count = int(input('Кол-во участников:'))
# team_count = int(input('Кол-во человек в команде:'))
# if human_count % team_count == 0:
#     teams = []
#     teammate_number = 0
#     for _ in range(human_count // team_count):
#         new_team = []
#         for _ in range(team_count):
#             teammate_number += 1
#             new_team.append(teammate_number)
#         teams.append(new_team)
#     print(teams)
# else:
#     print(human_count, 'невозможно поделить на команды по', team_count, "человек!" )

# 3
# goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
#
# new_fruit_name = input("Новый фрукт: ")
# new_fruit_price = int(input("Цена: "))
#
# goods.append([new_fruit_name, new_fruit_price])
#
# print("Новый ассортимент:", goods)
#
# for good in goods:
#     good[1] = round(good[1] * 1.08, 2)
#
# print("Новый ассортимент с увел. ценой:", goods)

#---Home Work---------------------------------------------------------------------

# 1
# first_lst = [1, 5, 3]
# second_lst = [1, 5, 1, 5]
# third_lst = [1, 3, 1, 5, 3, 3]
#
# first_lst.extend(second_lst)
# search = first_lst.count(5)
# print('Кол-во цифр 5 при первом объединении:', search)
#
# for i in first_lst:
#     if i == 5:
#         first_lst.remove(i)
#
# first_lst.extend(third_lst)
# search = first_lst.count(3)
# print('Кол-во цифр 3 при втором объединении:', search)
# print('Итоговый список:', first_lst)

# 2
# list1 = [1, 3, 5, 7, 9]
# list2 = [2, 4, 5, 6, 8, 10]
# new = []
# new.extend(list1)
# new.extend(list2)
# print(new)

# 3
# shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
#         ['педаль', 100], ['седло', 1500], ['рама', 12000],
#         ['обод', 2000], ['шатун', 200], ['седло', 2700]]
#
# name = input('Название детали: ')
#
# count = 0
# price = 0
#
# for i in shop:
#     if i[0] == name:
#         count += 1
#         price += i[1]
#
# print('Кол-во деталей -', count)
# print('Общая стоимость -', price)

# 4
# def check_lst(my_lst, person):
#     for i in my_lst:
#         if i == person:
#             return False
#     return True
#
#
# guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
#
# while True:
#     print('Сейчас на вечеринке', len(guests), 'человек', guests)
#     question = input('\nГость пришел или ушел? ').lower()
#
#     if question == 'пора спать':
#         print('Вечеринка закончилась, все легли спать.')
#         break
#
#     name = input('Имя Гостья: ')
#
#     if question == 'пришел':
#         if len(guests) >= 6:
#             print('Прости,', name, 'но мест нет.')
#         elif check_lst(guests, name) and len(guests) < 6:
#             guests.append(name)
#
#     elif question == 'ушел':
#         if check_lst(guests, name) == False:
#             guests.remove(name)

# 5
# violator_songs = [
#     ['World in My Eyes', 4.86],
#     ['Sweetest Perfection', 4.43],
#     ['Personal Jesus', 4.56],
#     ['Halo', 4.9],
#     ['Waiting for the Night', 6.07],
#     ['Enjoy the Silence', 4.20],
#     ['Policy of Truth', 4.76],
#     ['Blue Dress', 4.29],
#     ['Clean', 5.83]
# ]
#
# play_time = 0
# number_of_songs = int(input('Сколько песен выбрать:'))
# for song in range(1, number_of_songs + 1):
#     songs = input(f'Введите название {song} песни:')
#     for i2 in violator_songs:
#         if songs == i2[0]:
#             play_time += i2[1]
#
#
# print('Общее время звучания песен:', round(play_time), 'минут')

# 6
# def generator_lst(digit):
#     my_list = []
#     for i in range(digit):
#         size = int(input(f'Размер {i + 1} пары:'))
#         my_list.append(size)
#     return  my_list
#
#
# number = int(input('Кол-во коньков:'))
# skate_size = generator_lst(number)
# people_num = int(input('Кол-во людей:'))
# members = generator_lst(people_num)
# count = 0
#
# for i in skate_size:
#     for i2 in members:
#         if i >= i2:
#             count += 1
#             members.remove(i2)
#             break
# print('Наибольшее кол-во людей, которые могут взять ролики:', count)

# 7

# members = int(input('Кол-во человек:'))
# nums = list(range(1, members + 1))
# shift_count = int(input('Какое число в считалке? '))
# print('Значит, выбыбает каждый', shift_count, 'человек')
#
# index = 0
# number = len(nums) - 1
#
# while len(nums) != 1:
#     if index == number:
#         index = 0
#     number = len(nums) -1
#
#     print('\nТекущий круг людей:', nums)
#     print('Начало счёта с номера', nums[index])
#
#     for i in range(shift_count):
#         if index == number:
#             index = 0
#         elif i > 0:
#             index += 1
#         print('Выбывает человек под номером', nums[index])
#         nums.pop(index)
# print('Остался человек под номером', * nums)

# 8
# def is_palicondrome(num_list):
#     reverse_lst = []
#     for i_num in range(len(num_list) -1, -1,-1):
#         reverse_lst.append(num_list[i_num])
#     if num_list == reverse_lst:
#         return True
#     else:
#         return False
#
#
# digit = int(input('Кол-во чисел:'))
# nums = []
# for i in range(digit):
#     num_for_lst = int(input(f'число {i + 1}:'))
#     nums.append(num_for_lst)
# number = []
# answer = []
#
# for i in range(len(nums)):
#     for i2 in range(i , len(nums)):
#         number.append(nums[i2])
#     if is_palicondrome(number):
#         for i3 in range(0, i):
#             answer.append(nums[i3])
#         answer.reverse()
#         break
#     number = []
# print('Последовательность: ', nums)
# print('Нужно приписать чисел:', len(answer))
# print('Сами числа:', answer)


