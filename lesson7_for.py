# for takrorlanuvchi operator

# range() ->  range(1,101) -> 1,2,3,..., 100

# for i in range(1, 5): # 1,2,3,4
#     print(i) # 1,2,3,4


# for i in [12,7,8,10,26]:
#     print(i) #
#     if i == 8:
#         break

# for i in ['Ali', 'vali', 'gani', 'azamat']:
#     if i == 'gani':
#         continue
#     print(f'{i} mashqlarni bajaring')


# list va for

# mevalar = ['olma','gilos','banan','nok','anor','kivi'] # ketm

# print(mevalar[0])
# print(mevalar[1])
# print(mevalar[2])
# print(mevalar[3])
# print(mevalar[4])

# for i in mevalar:
#     print(i)

# son = int(input('nechi karani chiqarmoqchisiz>>>'))  # 3

# kara jadval
"""
1*1=1
1*2=2
1*3=3
1*4=4
1*5=5
.
.
.
1*10=10
"""

# for i in range(1, 11):
#     print(f'{son} * {i} = {i * son}')


# soni = int(input('mahsulotlar sonini kiriting>>>'))  # 5
# mahsulotlar = []
#
# for i in range(soni):
#     mahsulot = input(f'{i + 1} - mahsulotingizni ayting>>')
#     mahsulotlar.append(mahsulot)
#
# print(mahsulotlar)

"""
karra jadval 1 -> 10 karagacha

1 * 1 = 1    2 * 1 = 2    3 * 1 = 3  4 * 1 = 4 ..... 10 * 1 = 10 
1 * 2 = 2
1 * 3 = 3
.
.
.
1 * 10 = 10
"""

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} X {j} = {i * j}')
    print('\n\n')


users = {"admin": "1234", "ali": "qwerty", "zebo": "python"}
print("admin" in users.keys()) # True
print(users.values()) #