# func

def greeting(name):
    """
    Bu funksiyamiz salomlashishga moljalangan

    :param name:
    :return:
    """
    print(f'hello {name}')


# greeting("Ali")
# greeting("vali")
# greeting("Ali")

def celsius_to_fahr(temp):
    return 9 / 5 * temp + 32


a = celsius_to_fahr(12)


# print(a)


def toliq_ism_yasa(ism, familiya):
    """Toliq ism qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism  # qiymatni qaytaramiz


talaba1 = toliq_ism_yasa('olim', 'hakimov')  # natija o'zgaruvchiga tushdi!
talaba2 = toliq_ism_yasa('hakim', 'olimov')


# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

#
# def kvadrat(x):
#     return x * x
#     print("Men hech qachon ishlamayman")  # return'dan keyingi kod o'lik!
#
#
#
# def kopaytma(sonlar: list) -> int:
#     pass
#
#
# kopaytma([1, 2, 3, 5])  # 30
#
# # def summa(sonlar: list) -> int:
# #     sum = 0
# #     for i in sonlar:
# #         sum += i
# #     return sum
#
#
# def summa(sonlar: list) -> int:
#     count = 0
#     for i in sonlar:
#         count += i
#     return count
#
# b = summa([1,2,3,4,5])
#
# def kopaytma(sonlar: list) -> int:
#     count1 = 0
#     for j in sonlar:
#         count1 *= j
#     return count1


def talaba(ism, yosh=18):  # yosh=15 — STANDART QIYMAT
    print(f"{ism}, {yosh} yosh")


# talaba("Ali", 20)  # 1) TO'G'RI TARTIBDA: ism="Ali", yosh=16
# talaba('ali', yosh=25)


# talaba(yosh=17, ism="Vali")  # 2) KALIT SO'Z bilan: tartib muhim emas!
# talaba("Laylo")


def summa(*args, **kwargs):
    sum = 0
    for i in args:
        sum += i

    for v in kwargs.values():
        sum += v
    return sum


# print(summa(12, 21, 32, 21, 34, 32, 43, a=12, b=18, c=14))

x = 10   # Global o'zgaruvchi

def change_x():
    global x       # globalni o'zgartirishga ruxsat so'raymiz
    x = 20         # Global x ni o'zgartiramiz

change_x()
print(x) # 10, 20, Error