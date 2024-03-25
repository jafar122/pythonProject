# b = [1, 5, 6, -8, 9]
# for _ in range(5):
#     a = int(input('Enter Number:'))
#     b.append(a)
# for number in b:
#     print(number, '** 2 =', number ** 2)
#---------------------------------------------
# books_id = [50 ,34, -1, 2, 23, -1]
# new_books_id = []
# returned = 0
#
# for _ in range(10):
#     id = int(input('Введите ID книги:'))
#     books_id.append(id)
#
# for id in books_id:
#     if id == -1:
#         returned += 1
#     else:
#         new_books_id.append(id)
# print('Новый список выданных книг:', new_books_id)
# print('Вернули за день', returned)
#------------------------------------------------------

#1
# numbers = [3,7,5]
# count = 0
# while count < 5:
#     number = int(input('Введите новое число:'))
#     count += 1
#     numbers.append(number)
#     print(f'Текущий список {numbers}')
#
#     for i in numbers:
#
#         print(i ** 2, i ** 3, i ** 4,count)
#     print('Все',count)
#     print()

#2
    # numbers = []
    # for number in range(100):
    #     numbers.append(number)
    # print(numbers)

#3
# count_of_workers = int(input("Кол-во сотрудников в офисе: "))
# workers_id = []
# for _ in range(count_of_workers):
#     worker_id = int(input("ID сотрудника: "))
#     workers_id.append(worker_id)
#
# search_id = int(input("Какого сотрудника ищем? "))
#
# if search_id not in workers_id:
#     print("Сотрудник не работает!")
# else:
#     print("Сотрудник работает!")
#----------------------------------------------------------------

#1
# scores = [8, 5, 10, 5, 7]
# print(scores)
#
# scores[1] *= 3
# x = scores[4]
# x += 10
#
# print(x)
# print(scores)

#2
# monsters_count = int(input('Кол-во монстров:'))
# mage_index = int(input('Номер мага в списке:'))
# monsters_damage = []
#
# for monster in range(monsters_count):
#     print('Урон у', monster +1, 'Монстра', end=' ')
#     damage = int(input())
#     monsters_damage.append(damage)
#
#     for i_monster in range(monsters_count):
#         if monsters_damage[i_monster] < 100 and i_monster !=mage_index -1:
#             monsters_damage[i_monster] += monsters_damage[mage_index - 1]
#
# print('Итоговый урон монстров:', monsters_damage)

#-------------------------------------------------------------------

#1
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

#2
# new_list = []
# totall_numbers = int(input('Кол-во чисел в списке:'))
# for numbers in range(1,totall_numbers + 1):
#     print('Введите', numbers, ' Число:')
#     num = int(input())
#     new_list.append(num)
#
# divider = int(input('Введите делитель:'))
# index = 0
# sum_indexes = 0
# for number in new_list:
#     if number % divider == 0:
#         print('Индекс числа', number, ':', index)
#         sum_indexes += index
#     index += 1
# print('Сумма инедксов:', sum_indexes)

# 2 способ
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

#---------------------------------------------------------

#1
# word =input('Введите слово:')
# replace_num = int(input('Номер символа для замены:'))
# replace_sum = input('Чем заменяем:')
#
# sym_list = list(word)
#
# sym_list[replace_num - 1] = replace_sum
#
#
# for i in sym_list:
#     print(i, end='')
#2
# words_list = []
# counts = [0, 0, 0]
#
# for i in range(3):
#     print('Введите', i + 1, 'слово:', end=' ')
#     word = input()
#     words_list.append(word)
#
# text = input('Слово из текста: ')
# while text != 'end':
#     for index in range(3):
#         if words_list[index] ==text:
#             counts[index] +=1
#         text = input('Слово из текста:')
#
# print('\nПодсчет слов в тексте')
# for i in range(3):
#     print(words_list[i], ':', counts[i])
#---------------------------------------------------------------

#1
# user_msg = input('Введите строку:')
# letters = list(user_msg)
# what_replace = ':'
# for_what_replace = ';'
# index = 0
# replace_count = 0
# for letter in letters:
#     if letter == what_replace:
#         letters[index] = for_what_replace
#         replace_count += 1
#     index += 1
#
# print('Исправленная строка:', end=' ')
# for letter in letters:
#     print(letter, end='')
#
# print(f'\nКол-во замен: {replace_count}')

#2
# string = input('Введите строку:')
# index_of_letter = int(input('Номер символа: ')) -1
# letters = list(string)
# count = 0
# if index_of_letter > 0:
#     print('Символ слева:', letters[index_of_letter -1])
#     if letters[index_of_letter -1] ==letters[index_of_letter]:
#         count += 1
#     if index_of_letter < len(letters) -1 :
#         print('Симворл справа:', letters[index_of_letter +1])
#         if letters[index_of_letter +1] == letters[index_of_letter]:
#             count +=1
# if count == 0:
#     print('Таких же сиволов нет.')
# elif count == 1:
#     print('Есть ровно один такой же сивол.')
# elif count == 2:
#     print('Таких сиволов два.')

#3
# words_list = []
# counts = [0, 0, 0]
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

#--------------------------------------


# scores = [8, 6, 7, 3, 9]
# scores[1] += len(scores)
# scores.append(0)
# scores[2] += len(scores)
# print(scores)

#-----------------Home Work----------------------

#1

# number_one = []
# numbers = int(input('Введите число:'))
# for number in range(1,numbers +1, 2):
#     number_one.append(number)
# print(f'Список из нечетных чисел от одного до N: {number_one}')

# or
# Number = int(input('Введите число:'))
# odd_numbers_list = list(range(1, Number + 1, 2))
# print("Список из нечетных чисел от одного до N:", odd_numbers_list)

# or
# def odd_number(N):
#     odd_number_list = list(range(1, N + 1 , 2))
#     return odd_number_list
#
#
# N = int(input('Введите число !'))
#
# odd_number(N)
# print("Список из нечетных чисел от одного до N:", odd_number(N))

#--------------------------------------------------------------------------
#2
# participants = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
#
# # Используем цикл for для прохода по элементам списка с чётными индексами
#
# first_day_participants = []
# for i in range(0, len(participants), 2): # len - длина списка participants.
#     first_day_participants.append(participants[i])
#
# # Выводим результат
# print("Первый день:", first_day_participants)
#-------------------------------------------------------------------
#
# totall_cards = int(input('Количество видеокарт:'))
# graphics_cards = []
#
# # Заполнение списка видеокартами.
# for i in range(1, totall_cards +1):
#     card_model = int(input(f'Видеокарта {i}:'))
#     graphics_cards.append(card_model)
#
# print('Старый список видеокарт:', graphics_cards)
#
# # Находим максимальное значение в списке
# max_value = max(graphics_cards)
#
# # Удаляем все вхождения максимального значения из списка
# # delete - переменная . 1 - ая переменная delete нужна для указания на то что мы хотим включить каждое значение из списка graphics_cards в новый список , ( одним словом  это имя которое мы берем из списка graphics_cards.Отдельный элемент из списка)
# # delete - переменная . 2 -ая переменная delete нужна для временное имя , которое мы выбираем для представления этих значении внутри этого выражения. (То есть это просто имя которое мы даем этому элементу в процессе использования в генераторе списка)
# graphics_cards = [delete for delete in graphics_cards if delete !=max_value]
#
# print("Новый список видеокарт:", graphics_cards)

#---------------------------------------------------------------

#4

# films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
# new_films = int(input('Сколько фильмов хотите добавить?'))
# favorite_films = []
# for _ in range(new_films):
#     name_of_film = input('Введите название фильма:')
#     if name_of_film in films:
#         favorite_films.append(name_of_film)
#     else:
#         print(f'Ошибка: {name_of_film}, у нас нет :(')
#
# print('Ваш список любимых фильмов:', favorite_films)

# 5
# totall_list = []
# count_of_containers = int(input('Введите кол-во контейнеров:'))
# for container in range(count_of_containers):
#     each_container = int(input('Введите вес контейнера:'))
#     totall_list.append(each_container)
#
# # новый контейнер
# new_container = int(input('Введите вес нового контейнера:'))
#
# # находим место для вставки нового контейнера
#
# insert_position = 0
# for i in range(len(totall_list)):
#     if new_container <= totall_list[i]:
#         insert_position = i + 1
#         break
#     else:
#         insert_position += 1
# print(f'Номер, который получит новый контейнер: {insert_position + 1}')

#7




