
# a: int = 5
# b: int = a
#
#
# def fuu2(number: int):
#     number += 1
#     return number
#
#
# fuu2(b)
# print(a)
# print(b)
# print(fuu2(number=b))


def rec(value):
    print(value)
    if value < 4 :
        rec(value + 1)
    print(value)

rec(1)
