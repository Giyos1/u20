# # func takrorlash
#
# def bir_ni_qosh(num):
#     return num + 1
#
# func = bir_ni_qosh
# # print(type(bir_ni_qosh(12))) # int
# # print(type(func)) # function
#
# print(bir_ni_qosh(13))
# print(func(13))
#
#
# def plus_one(number):
#     def add_one(number):      # ICHKI funksiya
#         return number + 1
#
#     result = add_one(number) # 12+1 = 13
#     return result
#
# plus_one(12) #


# decorator

def title_name(func):
    def wrapper(name):
        result = func(name)
        return result.title()

    return wrapper


@title_name
def salom_ber(name):
    return f'salom {name}'


# f = title_name(salom_ber) #
# print(f('ALI')) #

# print(salom_ber('VALI'))
# print(salom_ber('ali'))

#
# def montiring(func):
#     def wrapper(*args,**kwargs):
#
#         result = func(*args,**kwargs)
#
#         return result
#     return wrapper
#
# @montiring
# def fo():
#     pass
#
# fo()
import time
import math


def taymer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # boshlangich vaqt
        result = func(*args, **kwargs)  # sfunc = sekin_funksiya() 999999
        end_time = time.time()
        print(f'funksiyamiz {end_time - start_time} shuncha vaqt ishladi')
        return result  # None

    return wrapper


@taymer
def sekin_funksiya():
    for i in range(10_000_000):
        pass
    print(i)


@taymer
def factorial_(number):  # 5 ! = 1*2*3*4*5
    return math.factorial(number)


print(factorial_(20))


def ikki_marta(func):
    def wrapper(*args, **kwargs):
        result1 = func(*args, **kwargs)
        result2 = func(*args, **kwargs)

        return result1 + '\n' + result2

    return wrapper


@ikki_marta
def salom_ber(name):
    return f'salom {name}'


print(salom_ber('ALi'))
"""
salom ALi
salom ALi
"""
