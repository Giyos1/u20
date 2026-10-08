# fayl = open('pi.txt')
# content = fayl.read()
# print(content)
# fayl.close()

# read
# try:
#     with open('pi.txt') as fayl:
#         content = fayl.readlines()
#         for i in content:
#             print(i.strip()) #1\n
#
# except FileNotFoundError as e:
#     print(e)

# # write modeda eski malumotlar butunlay ochib yangisini yozadi
# with open('pi.txt', mode='w') as f:
#     f.write('salom')
#
# # appemd modeda esa eskisini pastidan yozadi
# with open('pi.txt', mode='a') as f:
#     f.write('\nsalom')

# O'qish + yozish. Tarkib o'chadi!
# with open('pi2.txt', mode='w+') as f:
#     f.write('\nsalom')
#     f.seek(0)
#     print(f.read())


# pickle va json

# 1 pickle

import pickle


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# s1 = Student('Ali', 21)
# a = [1,2,3,5]
#
# with open('student.dat', 'wb') as f:
#     pickle.dump(s1, f)

# with open('student.dat', 'rb') as f:
#     student = pickle.load(f)
#
# print(student.name)
# print(student.age)
#
# import json
#
# bemor = {
#     "ism": "Alijon Valiyev",
#     "yosh": 30,
#     "dorilar": [
#         {"nomi": "Analgin", "miqdori": 0.5},
#         {"nomi": "Panadol", "miqdori": 1.2}
#     ]
# }
#
# # JSON faylga yozish
# with open('bemor.json', 'w') as fayl:
#     json.dump(bemor, fayl, indent=4)

# # JSON faylni o'qish
# with open('bemor.json') as fayl:
#     bemor = json.load(fayl)
#
# # print(bemor)
# print("Bemorning ismi:", bemor["ism"])
# print("Dorilar:", bemor["dorilar"])