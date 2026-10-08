# mevalar = ["olma","banan","gilos"]
m1 = 'olma'
m2 = 'banan'

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]  # matnlar ro'yxati
narhlar = [12000, 18000, 10900, 22000]  # sonlar ro'yxati
# sonlar = ['bir', 'ikki', 3, 4, 5]  # aralash ro'yxat
# ismlar = []

# print(bool(ismlar))  # True
# a = ""
# print(bool(a))
# raqam = 0
# print(bool(raqam))

zal = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22, 23, 24],
]

# print(zal[1][3])

countries = ["USA", "Canada", "India"]

# print(countries[1])
# print(countries[-2])

# print(countries[3])

# print(len(countries)) # 3

sonlar =  [0,1,2,3,4,5]

# print(sonlar[1:4])
# print(sonlar[:4])
# print(sonlar[2:])
#
# print(sonlar[:])

sonlar2=sonlar[:]  # [0,1,2,3,4,5]

# print(sonlar2)
# sonlar.append(12)
# # print(sonlar)
# print(sonlar2) #  [0,1,2,3,4,5]

countries[1] = 'UK'
# print(countries)

# del countries[1]
# countries.remove('UK')
# uk = countries.pop(1)
# print(uk)
# print(countries)

countries.append('Algeria')
# print(countries)
countries.insert(0,'Uzbekistan')
# print(countries)

countries = countries+["Japan","Korea"]
# print(countries)

# countries.sort(reverse=True)
# print(countries)
# sonlar.sort()
# print(sonlar)

# countries.reverse()
# print(countries)

# print(countries)
# print(sorted(countries))
# print(countries)

# print(countries)
# countries.sort()
# print(countries)
# print(countries)


sonalar = list(range(0,100,2))
print(sonalar)

toys = ('bus', 'car', 'bear', 'dino')
print(toys[0])    # o'qish mumkin ✅
toys[3] = 'dragon'