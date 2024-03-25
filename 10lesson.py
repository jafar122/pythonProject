# for a in range(1,10+1):
#     for b in range(1,10+1 ):
#         print(a,'*',b,'=',a * b)
#     print()

# for row in range(6):
#     for col in range(6):
#         print(row  + col,end = ' ')
#     print()
#----------------------------------
#1
# for row in range(1,10):
#     for col in range(1,10):
#         print(row * col,end = '\t')
#     print()

#2
# number = int(input('Введите число:'))
# for a in range (0,number +1):
#     for b in range(0,number +1):
#         print(a + b, end= '\t')
#     print()

#3
# for number1 in range(0,10):
#     for number2 in range(10):
#         if number2 <= number1:
#             print(number1 - number2,end='\t')
#         else:
#             print(number1-number2,end='\t')
#     print()
#---------------------------------------------

# size =  int(input('Введите размер матрицы:'))
# for row in range(1,size +1):
#     for col in range(size +1):
#         if row % 2 == 0:
#             print(row, end = ' ')
#         else:
#             print(col,end=' ')
#     print()

# for row in range(20):
#     for col in range(50):
#         if row == 9 :
#             print('-',end= '')
#         elif col == 25:
#             print('|',end='')
#         else:
#             print(' ', end = '')
#     print()
#-----------------------------------------

#1
# size = int(input('Введите размер матрицы:'))
# for a in range(1,size+1):
#     for b in range(1,size +1):
#         if a % 2 == 0 :
#             print(a,end='\t')
#         else:
#             print(b,end = '\t')
#     print()

#2
# size = int(input('Введите размер матрицы:'))
# for a in range(1,size +1):
#     for b in range(1,size +1):
#         if b % 3 == 0:
#             print(b, end= '\t')
#         else:
#             print(a, end='\t')
#     print()
#---------------------------------------------------------

# size = int(input('Введите размер матрицы:'))
# for row in range(size):
#     for col in range(size):
#         if row < col:
#             print(0,end=' ')
#         elif row > col:
#             print(2,end= ' ')
#         else:
#             print(1,end = ' ')
#     print()
#

# for row in range(20):
#     for col in range(50):
#         if row == 9 :
#             print('-',end='')
#         elif col == row + 29:
#             print('\\',end= '')
#         elif col == -row + 19:
#             print('/',end='')
#         elif col == 24:
#             print('|',end='')
#         else:
#             print(' ',end='')
#     print()
#---------------------------------------------------------------
#1
# x_lim = 30
# y_lim = 20
#
# for y in range(y_lim):
#     for x in range(x_lim):
#         if y == 0 :
#             print('-',end ='')
#         elif x == 0 or x ==x_lim -1:
#             print('|',end='')
#         else:
#             print(' ',end='')
#     print()

#3
# n = int(input('Введите число:'))
# for y in range(n):
#     for x in range(n):
#         buf_x = (n - 1) -y
#         if buf_x > x:
#             print(0,end='\t')
#         elif buf_x == x:
#             print(1,end='\t')
#         else:
#             print(2,end='\t')
#     print()

#------------------------------------------------
# people = int(input('Введите кол-во людей:'))
# for hour in range(1,people +1):
#     print('Идет час:',hour)
#     for num in range(hour,people):
#         print('Номер в очереди',num)
# print('Очередь обслуженна !')

#
# numbers = int(input('Введите сколько чисел будут в последовательности ?'))
# wich_num = int(input('Какую цифру нам нужно считать '))
# while wich_num < 0 or wich_num >9 :
#     wich_num = int(input('Цифра должна быть в деапазоне от 0 до 9! Введите новую цифру: '))
# wich_numCount = 0
# for num in range(numbers):
#     print('Введите',num, '-e число:',end='')
#     number = int(input())
#     while number > 0 :
#         if number % 10 == wich_num:
#             wich_numCount +=1
#         number //= 10
# print('Цифр',wich_num,'В ПОСЛЕДОВАТЕЛЬНОСТИ:',wich_numCount)
#--------------------------------------------------------------------------------

#3
# numbers = int(input('Введите число N:'))
# for a in range(numbers +1):
#     for b in range(a,numbers + 1):
#         print(b,end='\t')
#     print()


#2
# number = int (input('Введите число:'))
# cipher_count = 0
# for _ in range(number):
#     new_number = int(input('Введите число'))
#     while new_number:
#         if new_number % 10 >5:
#             cipher_count +=1
#         new_number //= 10
# print(cipher_count)

#----------------------------------------
# while True:
#     for attemt in range(1, 4):
#         pincode = int(input('Введите пин-код:'))
#         if pincode == 1234:
#             print('Пин-код верный. Держите вашу зарплату! :)')
#             break
#         print('Неверный пин-код.Осталось попыток:', 3-attemt)
#     else:
#         print('\nВаша карта заблокирована')
#     print('Следующий клиент, добро пожаловать!')
#-------------------------------------------------------





#1
# for row in range(6):
#     for col in range(0,12,2):
#         print(row+col, end='\t')
#     print()

#2
# number = int(input('Введие число:'))
# for row in range(number):
#     for col in range(number):
#         if row >= col:
#             print(row,end='\t')
#     print()
#

#3
# height =int(input('Введите высоту Рамки:'))
# width = int(input('Введите ширину рамки:'))
# for size1 in range(height):
#     for size2 in range(width):
#         if size1 == 0 or size1 == height - 1:
#             print('-',end=(''))
#         elif size2 == 0 or size2 ==width - 1:
#             print('|',end=(''))
#         else:
#             print(' ',end='')
#     print()

#4

# max_num = int(input('Введите число: '))
# prime_num = 0
#
# for number in range(2, max_num+1):
#   is_prime = True
#   for interval_num in range(2, number):
#     if number % interval_num == 0:
#       is_prime = False
#       break
#   if is_prime:
#     prime_num += 1
# print(prime_num)

#5
# numbers = int(input('Сколько чисел будете вводить :'))
# total = 0
# maxnum = 0
# number_n = 0
#
# for _ in range(numbers):
#     x = int(input('Введите натуральные числа:'))
#     for summ in range(1,x + 1):
#         total += summ
#     if total > maxnum:
#         maxnum = total
#         number_n = x
#     total = 0
# print('Наибольше по сумме цифра:',number_n,'итог суммы:',maxnum)

#6
# height = int(input('Введите высоту треугольника:'))
# for row in range(height):
#     print(' '*(height-row-1) + '#' * (2*row+1))
#

#7
# height = int(input('Введите уровень пирамиды:'))
# number = 1
# for row in range(height):
#     for _ in range(height - row,0, -1):
#         print(end= '\t')
#     for col in range(row+1):
#         print(number,'  ',end='\t')
#         number +=2
#     print()

#8
# depth =int(input('Введите глубину ямы:'))
# for line in range(depth):#по строчкам
#     for lef_number in range(depth,depth-line-1, -1):
#         print(lef_number, end ='')
#     point_count = 2 * (depth -line -1)
#     print('.' * point_count, end = '')
#     for right_number in range (depth - line, depth+1):
#         print(right_number,end = '')
#     print()
#
#


            






  


