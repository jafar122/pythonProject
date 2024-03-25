# my_list = [1,2,3,4]
# my_list.append(5)
# print(my_list)
#
# def print_gretting():
#     '''
#     Print Hello !
#     :return:None
#     '''
#     print('hello')
# print_gretting()
# help(print_gretting)

# def print_greeting_withName(name):
#     '''
#     : param name
#     : return: None
#     '''
#     print('Hello ' +name)
# print_greeting_withName('Jafar')
# help(print_greeting_withName)

#
# def sum_of_numbers(a = 6 , b = 8):
#     '''
#
#     '''
#     return a +b
#
#     :return:
# x = sum_of_numbers(1,6)
# print(x)

# def is_text(text):
#     if 'Hello' in text:
#         return  True
#     else:
#         return False
# print(is_text("How are yoiueorfpd Hello"))


# def cat_voice():
#     print('Meow')
# cat_voice()
# cat_voice()
#
# def dog_wois():
#     print('Woow')
# dog_wois()
# dog_wois()
# def get_text(text):
#    print(text + '!')


# def all_numbers(a,b):
#     all_list = []
#     all_list1 =[]
#     for c in range (a,b):
#         if c % 2 :
#             all_list.append(c)
#         elif c % 2 ==0:
#          print(all_list1)
#     print(all_list)
#
# all_numbers(1,8)
#
# all_numbers(1,10)





def all_numbers (a,b):
    plus_nUmbers = []
    mines_numbers = []
    for i in range(a,b):
        if i % 2 == 0:
            plus_nUmbers.append(i)
        else:
            mines_numbers.append(i)
    print(plus_nUmbers)
    print(mines_numbers)

all_numbers(1,10)
