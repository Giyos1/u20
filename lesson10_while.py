# while

num = 1

# while num <= 5:
#     print(num) # 1,2....5
#     num += 1  # num : 2,3..,6

# 1,2,3,4,5,6

# i = 2
# while i <= 3:
#     print(i)
#     i += 1
# else:
#     print("Tsikl tugadi va shart bajarilmadi.")

# while True:
#     print('Namlang. Ko\'piklang. Chaying. TAKRORLANG.')

# n = 5
# while n > 0:  # 5 < 0
#     print('Lather')  # ko'piklang
#     print('Rinse')  # chaying
#     n -= 1 # toxtash shart
# print('Dry off!')

users = [
    {
        "login": "ali",
        "password": '12'
    },
    {
        "login": "vali",
        "password": '123'
    },
    {
        "login": "gali",
        "password": '125'
    },
]

stop = False
#
# while True:
#     login = input('login kiriting>>')
#     parol = input('parol kiriting>>')
#
#     for i in users:
#         if i['login'] == login and i["password"] == parol:
#             print('muvaffaqiyatli tizimga kirdingiz')
#             stop = True
#             break
#
#     if stop:
#         break
#     else:
#         print("qayta urinib koring")

qalinlik = 0.0001
masofa = 384400000
sanoq = 0

while qalinlik < masofa:
    qalinlik *= 2
    sanoq += 1

# print(f"Qog'ozni {sanoq} marta buklash kerak. {int(qalinlik/1000)} km")


# qogoz = 0.0001          # m
# oy = 384400000 # m
# buklash = 0
#
# while qogoz < oy:
#     qogoz = qogoz * 2
#     buklash += 1
#
# print(buklash)

import random

number_to_guess = random.randint(1, 10)
guess = 0

while guess != number_to_guess:
    guess = int(input("1 dan 10 gacha son kiriting: "))
    if guess < number_to_guess:
        print("Ko'proq kiriting.")
    elif guess > number_to_guess:
        print("Kamroq kiriting.")
    else:
        print("To'g'ri topdingiz!")
       