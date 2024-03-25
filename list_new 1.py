# b = [1, 4, 6, 7, 8]
# for _ in range (5):
#     a = int(input('Введите число:'))
#     b.append(a)
#     for number in b:
#         print(number, '** 2 =', number ** 2)

# books_Id = [50, 34, -1, -1, 2, 6]
# new_books_Id = []
# returned = 0
#
# for _ in range(10):
#     id = int(input('Введите Id книги:'))
#     books_Id.append(id)
#
# for id in books_Id:
#     if id == -1:
#         returned += 1
#     else:
#         new_books_Id.append(id)
# print('Новый список выданных книг', new_books_Id)
# print('Вернули за день:', returned)
#-------------Home Work par 1--------------------------

# numbers = [3,7,5]
# stop = 0
#
# while stop < 4:
#     number = int(input('Новое число:'))
#     stop += 1
#     numbers.append(number)
#     print('Текущий список:', numbers)
#
#     for _ in numbers:
#         print( _ ** 2, _ ** 3, _ ** 4)
#     print()
# print(f'Всего {stop} новых значении')

# 2

# numbers = []
# for number in range(100):
#     numbers.append(number)
# print(numbers)

# 3
# totall_people = int(input('Кол-во соотрудниковв офисе:'))
# employs = []
# for people in range(totall_people):
#
#     New_Id =int(input('ID сотрудника:'))
#     employs.append(New_Id)
#
# search = int(input('Какой ID ищем ?'))
# if search not in employs:
#     print('Сотрудник не работает!')
# else:
#     print('Сотрудник работает')

#--------------------------------------------------------------

# scores = [8, 5, 6, 9, 7]
# print(scores)
#
# scores[2] *= 2
# x = scores[4]
# x += 10
# print(x)
# print(scores)

# 2

# monster_count = int(input('Кол-во монстров:'))
# mage_index = int(input('Номер мага в списке:'))
#
# monster_damage = []
#
# for monster in range(monster_count):
#     print('Урон у', monster + 1, 'монстра', end=' ')
#     damage = int(input())
#     monster_damage.append(damage)
#
# for i_monster in monster_damage:
#     if monster_damage[i_monster] < 100 and i_monster != mage_index -1:
#         monster_damage[i_monster] += monster_damage[mage_index - 1]
#
#
#
# print('Итоговый урон монстров:', monster_damage)

#--------------Home Work---------------------------

# nums_list = []
#
# N = int(input('Кол-во чисел в списке: '))
#
# for _ in range(N):
#     num = int(input('Очередное число: '))
#     nums_list.append(num)
#
# if nums_list:
#     maximum = nums_list[0]
#     minimum = nums_list[0]
#
#     for i in nums_list:
#
#         if maximum < i:
#             maximum = i
#
#         if minimum > i:
#             minimum = i
#
#     print('Максимальное число в списке:', maximum)
#     print('Минимальное число в списке:', minimum)
# else:
#     print('В списке нету чисел')

# 2
# nums_list = []
#
# N = int(input('Кол-во чисел в списке: '))
#
# for i in range(1, N + 1):
#     print("Введите ", i, "число: ")
#     num = int(input())
#     nums_list.append(num)
#
# divider = int(input('Введите делитель: '))
# index = 0
# sum_indexes = 0
# for number in nums_list:
#     if number % divider == 0:
#         print("Индекс числа", number, ":", index)
#         sum_indexes += index
#     index += 1
#
# print("Сумма индексов:", sum_indexes)




#-------------------------------------------------
# nums_list = []
#
# N = int(input('Кол-во чисел в списке: '))
#
# for _ in range(N):
#     num = int(input('Очередное число: '))
#     nums_list.append(num)
#
# if nums_list:
#     maximum = nums_list[0]
#     minimum = nums_list[0]
#
#     minimum_index = 0
#     maximum_index = 0
#     for index, i in enumerate(nums_list):
#
#         if maximum < i:
#             maximum = i
#             maximum_index = index
#
#         if minimum > i:
#             minimum = i
#             minimum_index = index
#
#     print('Максимальное число в списке:', maximum)
#     print('Минимальное число в списке:', minimum)
#
#     print(nums_list)
#     nums_list[minimum_index], nums_list[maximum_index] = nums_list[maximum_index], nums_list[minimum_index]
#     print(nums_list)
# else:
#     print('В списке нету чисел')

#-----------------------------------------

# word = input('Введите слово:')
# replace_num =int(input('Номер символа для замены:'))
# replace_sym = input('Чем заменяем:')
#
# sym_list = list(word)
# sym_list[replace_num -1] = replace_sym
#
#
# for i in sym_list:
#     print(i, end='')

#---------------------------------------------------

# words_list = []
# counts = [0, 0, 0]
#
# for i in range(3):
#     print('Введите:', i + 1, 'слово', end=' ')
#     word = input()
#     words_list.append(word)
#
# text = input('Слово из текста:')
# while text != 'end':
#     for index in range(3):
#         if words_list[index] == text:
#             counts[index] += 1
#     text = input('Слово из текста:')
#
# print('\nПодсчет слов в тексте')
# for i in range(3):
#     print(words_list[i], ':', counts[i])

#--------Home Work----------------------------------------------

# user_msg = input("Введите строку: ")
# letters = list(user_msg)
# what_replace = ":"
# for_what_replace = ";"
# index = 0
# replace_count = 0
# for letter in letters:
#     if letter == what_replace:
#         letters[index] = for_what_replace
#         replace_count += 1
#     index += 1
#
# print("Исправленная строка:", end=' ')
# for letter in letters:
#     print(letter, end='')
#
# print("Кол-во замен:", replace_count)

# Аналогичное решение при помощи функции enumerate:

# user_msg = input("Введите строку: ")
# letters = list(user_msg)
# what_replace = ":"
# for_what_replace = ";"
# for index, letter in enumerate(letters):
#     if letter == what_replace:
#         letters[index] = for_what_replace
#
# for letter in letters:
#     print(letter, end='')
#--------------------------------------------
#2
# stroka = input('Введите строку:')
# number_of_symbol = int(input('Номер символа:')) - 1 # -сразу отнимаем 1
# letters = list(stroka)
# count = 0
# if number_of_symbol > 0:
#     print("Символ слева:", letters[number_of_symbol - 1])
#     if letters[number_of_symbol - 1] == letters[number_of_symbol]:
#         count += 1
# if number_of_symbol <len(letters) - 1:
#     count += 1
#
# if count == 0:
#     print("Таких же символов нет.")
# elif count == 1:
#     print("Есть ровно один такой же символ.")
# elif count == 2:
#     print("Таких символов два.")
#------------------------------------------------------

# 3
# words_list = []
# counts = [0, 0, 0] # - 0 это слова , 3 (0) означает 3 слова.
#
# for i in range(3):
#     print("Введите", i + 1, "слово", end=' ')
#     word = input()
#     words_list.append(word)
#
# text = input("Слово из текста: ")
# while text != "end":
#     for index in range(3):
#         if words_list[index] == text:
#             counts[index] += 1
#     text = input("Слово из текста: ")
#
# print("Подсчёт слов в тексте")
# for i in range(3):
#     print(words_list[i], ':', counts[i])
#----------------------------------------------------------

# scores = [8, 6, 7, 10, 6]
# scores[1] += len(scores)
# scores.append(0)
# scores[2] += len(scores)
# print(scores)
#---------------Home Work-------------------------------------------

# 1
# new_list = []
# numbers = int(input('Введите число:'))
# for number in range(1, numbers + 1):
#     if number % 2 != 0:
#         new_list.append(number)
#
# print(f'Список из нечетных чисел от одного до {numbers}: {new_list}')

# 2
# names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', ' Евгений', 'Женя', 'Захар']
# list_names = []
# for index, name in enumerate(names):
#     if index % 2 == 0:
#         list_names.append(name)
# print('Первый день:', list_names)

# 3
# list_of_old_cards = []
# video_cards = int(input('Кол-во видеокарт:'))
# for i in range(video_cards):
#     card = int(input(f'Видеокарта {i + 1}:'))
#     list_of_old_cards.append(card)
# print(f'Старый список видеокарт:{list_of_old_cards}')
#
# max_video_card = max(list_of_old_cards)
# list_of_old_cards.remove(max_video_card)
# print(f'Новый список видеокарт: {list_of_old_cards}')

# 4
# def add_favorite_films():
#     my_list = []
#     film_list = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов',
#                  'Аякс', 'Отступники', 'Деревня']
#     new_films = int(input('Сколько фильмов хотите добавить?'))
#
#     for _ in range(new_films):
#         new_film = input('Введите название фильма:')
#
#         if new_film in film_list:
#             my_list.append(new_film)
#         else:
#             print(f'Ошибка: Фильм {new_film} у нас нет :(')
#
#     print(f'Ваш список любимых фильмов: {my_list}')
#
#
# # Вызываем функцию
# add_favorite_films()

# 5
# list_containers = []
# totall_containers = int(input('Введите кол-во контейнеров:'))
#
# for container in range(totall_containers):
#     cont = int(input('Введите вес контейнера:'))
#     list_containers.append(cont)
#     if cont > 200:
#         print('все числа не должны превышать 200. ')
#
# new_container = int(input('Введите вес нового контейнера:'))
# position = 1
# for i in range(len(list_containers)):
#     if new_container <= list_containers[i]:
#         position = i + 1
#         break
#
# print(f'Номер, который получит новый контейнер: {position}')

# 6
# count = 0
# while count < 4:
#     a = [1, 2, 3, 4, 5]
#     sdig = int(input('Сдвиг:'))
#
#     # Проверка, что сдвиг не превышает длину списка
#     sdig %= len(a)
#
#     # Создаем новый список, в который будем помещать сдвинутые элементы
#     new_list = []
#
#     for i in range(len(a)):
#         new_index = (i + sdig) % len(a)
#         new_list.append(a[new_index])
#
#     print('Изначальный список:', a)
#     print('Сдвинутый список:', new_list)
#     count += 1

# def selection_sort(my_list):
#     i_mn = 0
#     for i_mn in range(len(my_list)):
#         for cuur in range(i_mn, len(my_list)):
#             if my_list[cuur] < my_list[i_mn]:
#                 my_list[cuur], my_list[i_mn] = my_list[i_mn], my_list[cuur]
#
# nums = [4, 9, 7, 6, 3, 2]
#
# selection_sort(nums)
# print(nums)

#----------------New Lesson 3 part----------------------------------------

# langs = ['Python', 'Java', 'JS', 'SQL']
# new_lang = input('После чего вставить:')
# i_lang = langs.index(new_lang)
#
# langs.insert(i_lang + 1, 'C++')
#
# print(langs)
#-------------------------------------------
# def is_film_exist(movie, film_list):
#     return movie in film_list
#
# films = [
#     'Крепкий Орешек', 'Назад в Будущее', 'Таксист',
#     'Леон', 'Богемская рапсодия', 'Город Грехов',
#     'Мементо', 'Отступники', 'Деревня',
#     'Проклятый Остров', 'Начало', 'Матрица'
# ]
#
# my_list = []
#
# while True:
#     print('\nВаш текущий топ филмов:', my_list)
#     new_movie = input('Название фильма:')
#     if is_film_exist(new_movie, films):
#         print('Команды: добавить, удалить, вставить')
#         command = input('Введите команду:')
#         if command.strip() == 'добавить':
#             my_list.append(new_movie)
#         elif command.strip() == 'удалить':
#             if is_film_exist(new_movie, my_list):
#                 my_list.remove(new_movie)
#             else:
#                 print('Такого фильма нет в вашем списке')
#         elif command.strip() == 'вставить':
#             index = int(input('На какое место:'))
#             my_list.insert(index - 1, new_movie)
#     else:
#         print('Такого фильма нет на сайте.')

#-------Home Work ----------------------------------------

# 1
# zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
# zoo.remove('elephant')
# zoo.insert(1, 'bear' )
# print('Зоопарк:', zoo)
#
# print('Лев сидит в клетке номер', zoo.index('lion') + 1)
# print("Обезьяна сидит в клетке номер", zoo.index('monkey') + 1)

# 2
# totall_employs = int(input('Кол-во сотрудников:'))
# list_employs = []
# for i_employ in range(totall_employs):
#     salary = int(input(f'Зарплата {i_employ + 1}:'))
#     if salary > 0:
#         list_employs.append(salary)
#
# print("Осталось сотрудников:", len(list_employs))
# print("Зарплаты:", list_employs)
# print(f' Минимальная зп {min(list_employs)}, Максимальная зп {max(list_employs)}')

# 3

#-------------3.rd part-------------------------------------

# my_list = ['Игра', 'Изгой', 'Таксист']
# your_list = ['Начало', 'Отсупники', 'Короле Лев']
#
# my_list.extend(your_list)
# for i_elem in my_list:
#     print(i_elem)

#-------------------------------------------------------------
# pack = []
# decode = []
# bad_packs = 0
#
# packs_amt = int(input('Кол-во Пакетов'))
#
# for i_pack_num in range(packs_amt):
#     print('\nПакет Номер', i_pack_num + 1)
#     for i_bit in range(4):
#         print(i_bit + 1, 'бит:', end=' ')
#         num = int(input())
#         pack.append(num)
#     if pack.count(-1) <= 1:
#         decode.extend(pack)
#     else:
#         print('Много ошибок в пакете.')
#         bad_packs += 1
#     pack = []
#
# print('\nПолученное сообщение:', decode)
# print('Кол-во ошибок в сообщении:', decode.count(-1))
# print('Кол-во потерянных пакетов:', bad_packs)

#-------Home Work------------------------------------------
# 1
# main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
# first_company = [0, 0, 0]
# second_company = [1, 0, 0, 1, 1, 0]
# third_company = [1, 1, 1, 0, 1]
#
# main.extend(first_company)
# main.extend(second_company)
# main.extend(third_company)
# print('Общий список задач:', main)
# print(f'Кол-во нерешенных задач: {main.count(0)}')

#  2
# first_message = input('Первое сообщение:')
# second_message = input('Второе Сообщение:')
#
# first_count = first_message.count('!') + first_message.count('?')
# second_count = second_message.count('!') + second_message.count('?')
# if first_count < second_count:
#     first_message, second_message = second_message, first_message
# print(first_message + second_message)

#-----------------4.ST Lesson----Вложенные списки-----------------------

# N = int(input('Кол-во участников:'))
# memebrs = []
# num = 1
# for _ in range(N // 3):
#     memebrs.append(list(range(num, num + 3)))
# print(memebrs)

# 2