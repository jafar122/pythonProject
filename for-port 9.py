# password = input('Введите пароль:')
# while password !='Питон123':
#     print('Не верный пароль!')
#     password = input('Введите еще раз пароль ')
# print('Пароль верный.Добро пожаловать !')

# total_2 = 0
# for student in range(5):
#     question = input('Кто написал произведение Евгений Онегин ?')
#     if question == 'Пушкин' or question =='пушкин':
#         print('Молодец так держать !')
#         break
#     print('Не правильно:2')
#     total_2 += 1
# print('Кол-во 2:',total_2)

#---------------------------------------------------------------------------

#2
# how_much = 0
# Basice = input('Выполнил ли ты задания:')
# while Basice != 'Да':
#     print('Подумай еще раз !')
#     Basice = input('Выполнил ли ты задания:')
#     if Basice == 'Да':
#         break
#     how_much += 1
# print('Всего попыток:',how_much)
# print('Молодец')

#3
# count = 0
# bye_elephant = input('Как тебя зовут ?')
# print(bye_elephant,'Купи Слона ! :)')
# while True:
#     bye_elephant = input("\n")
#     print('Все говорят',bye_elephant + ",",'а ты купи слона')
#     count += 1
#     if bye_elephant == 'Надоел куплю':
#         break
# print(count,'-Столько раз вы спрашивали:')
# print('Молодец Ха -ХА')

#------------------------------------------------------------------------------

# phrase = input('Введите фразу:')
# for symbol in phrase:
#     print(symbol * 5)
#     print('=' *10)

# text = input('Введите текст:')
# first_sym = input('Введите первую букву:')
# second_sym = input('Введите вторую букву:')
# first_letter = 0
# second_letter = 0
#
# for symbol in text:
#     if symbol == first_sym:
#         first_letter += 1
#     elif symbol == second_sym :
#         second_letter += 1
#
# print('Кол-во букв:',first_sym,'=',first_letter)
# print('Кол-во букв:',second_sym,'=',second_letter)


#--------------------------------------------------------------------------------------


#1
# word = input('Введите слово:')
# for letter in word:
#     print(letter)

#2
# word = input('Введите слово:')
# for letter in word:
#     print(letter * 3)

#3
# text = input('Ввведите текст:')
# small = 'ы'
# big = 'Ы'
# big_letter = 0
# small_letter = 0
# for symbol in text:
#         big_letter += 1
#         small_letter += 1
# print('Кол-во малегьких букв ы:',small_letter)
# print('Кол-во больших букв ы:',big_letter)

#----------------------------------------------------------------------------------------

# phrase = input('Введите \n фразу:')
# new_phrase = ''
# for symbol in phrase:
#     print(symbol,end = '\n@@')

# number = int(input('Введите первое число:'))
# step = int(input('Введите шаг:'))
# summ = 0
#
# print('\nIP-адрес:',end = ' ')
# for count in range(3):
#     print(number,end = '.')
#     summ +=number
#     number += step
# print

#--------------------------------------------------------------------------------------
#1
# print("-" * 10)
# for i in range(10):
#     if i == 0 or i == 9:
#         print("|", end="")
#     else:
#         print("0", end="")
# print()
# for i in range(10):
#     if i == 0 or i == 9:
#         print("|", end="")
#     else:
#         print("0", end="")
# print()
# for i in range(10):
#     if i == 0 or i == 9:
#         print("|", end="")
#     else:
#         print("0", end="")
# print()
# for i in range(10):
#     if i == 0 or i == 9:
#         print("|", end="")
#     else:
#         print("0", end="")
# print()
# print("-" * 10)

#2
# print("-" * 10)
# for new in range(4):
#     for i in range(10):
#         if i == 0 or i == 9:
#             print("|", end= " ")
#         else:
#             print("0",end="")
#     print()
# print("-" *10)

#3
# first_elem= int(input('Введите первый элемент:'))
# delta = int(input('Введите  разность:'))
# print(first_elem, end='.')
# last_sum = first_elem
# for summ in range(2):
#     first_elem += delta
#     last_sum += first_elem
#     print(first_elem,end= '.')
# print(last_sum)

#4
# n=int(input('Введите число:'))
# print("-=-", end= " ")
# for i in range(0,n+1,10):
#     print(i,end=" -=- ")

#-----------------------------------------------------------------
# text =input('Введите текст:')
# summ = 0
# print('\nОтфилтрованный текст', end = ' ')
# for symbol in text :
#     if symbol == '1' or symbol == '9':
#         summ += int(symbol)
#     else:
#         print(symbol,end = '')
# print('\nСумма:',summ)

# string = input('Ведите строку:') #aabc
# prevSym =''
# equalSym = False
# for letter in string:
#     if prevSym == letter:
#         equalSym = True
#         break
#     else:
#         prevSym = letter
#
# if equalSym:
#     print('Есть две одинаковые буквы подряд')
# else:
#     print('Нет двух одинаковых букв подряд')

#-----------------------------------------------------------------------------
#HomeWork

#1
# count = 0
# new_word = 0
# just_word = 'Карамба'
# for word in range(1,10+1):
#     new_word += 1
#     print(new_word, 'слово')
#     Our_Word = input('Введите слова:')
#     if Our_Word == just_word :
#         count += 1
# print('Всего похожих на слово:', just_word, count)

#2
# count = 0
# text = 'Приве*т как дела'
# for _ in text:
#     count += 1
#     if _ == '*':
#         break
# print('* стоит на позиции:',count)

#3
# print('Задача 4. Театр')
# row = int(input('Введите кол-во рядов: '))
# place = int(input('Введите кол-во сидений ряду: '))
# distance = int(input('Введите кол-во метров между рядами: '))
#
# for _ in range(row):
#   print('='* place, '*' * distance, '='* place)

#4
# lenght = 8
# width = 10
# while True:
#     operator = input('Оператор:').lower()
#     if operator == 'w' and lenght != 0:
#         lenght -= 1
#     elif operator == 's' and lenght != 15:
#         lenght += 1
#     elif operator == 'a' and lenght != 0:
#         width -= 1
#     elif operator == 'd' and lenght != 20:
#         width +=1
#     print('Марсоход находится на позиции',lenght,width,'Введите команду:')

#5
# word = 0
# long_word = 0
# text = input('Введите текст:')
# for _ in text:
#     if _ != ' ':
#         word +=1
#     elif word >= long_word:
#         long_word = word
#         word = 0
#     else:
#         word = 0
# if long_word >= word:
#     print('Длина самого длинного слова:',long_word)
# else:
#     print('Длина самого длинного слова',word)

#6
# srting = input('Введите строку из 10 символов: ')
# milk = 0
# manufacture = 0
#
# for symbol in srting:
#   if symbol == 'a':
#     manufacture += 2
#     milk += manufacture
#   elif symbol == 'b':
#     manufacture += 2
# print('Всего произведено',milk,'литров молока')

#7
# cipher = input('Ввведите зашифрованное сообщение:')
# begin = ''
# end = ''
# number = 0
# for symbol in cipher:
#     number += 1
#     if number % 2 == 1:
#         begin = begin + symbol
#     else:
#         end = symbol +end
# word = begin + end
# print(word)

