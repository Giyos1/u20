# has_yomgir = bool(int(input('yomg\'ir yogyaptimi?(1-ha/0-yoq)')))  # 1 -> True , 0-> False
# print(has_yomgir)  # "1"-> 1 - [ error, True,1 ] "0"-> 0 - > [ error, True, False,0]

# if has_yomgir:
#     print('soyaboni oling')
# else:
#     print('shart emas soyabon')

ball = int(input('balingizni kiriting'))

if ball > 90:
    print('alo')
else:
    if ball > 70:
        print('yaxshi')
    else:
        if ball > 56:
            print('qoniqarli')
        else:
            print('yiqilding')

if ball > 90:
    print('alo')
elif ball > 70:
    print('yaxshi')
elif ball > 56:
    print('qoniqarli')
else:
    print('yiqilding')

age1 = 24
age2 = 16

if age2 <= 18 and age1 <= 18:
    print('osmir ikkalsi xam')
elif age2 <= 18 or age1 <= 18:
    print('biri katta 18 dan')
else:
    print('ikkalasi xam yosh bola')

summa = 0
mahsulotlar = []

salat_aytasizmi = input('salat aytasizmi?(ha/yoq)').lower()
osh_aytasizmi = input('osh aytasizmi?(ha/yoq)').lower()
choy_aytamizmi = input('choy aytasizmi?(ha/yoq)').lower()
cola_aytamizmi = input('cola aytasizmi?(ha/yoq)').lower()

if salat_aytasizmi == 'ha':
    summa += 15000
    mahsulotlar.append('salat')
    print('salat yozildi')

if osh_aytasizmi == 'ha':
    summa += 40000
    print('osh yozildi')
    mahsulotlar.append('osh')


if choy_aytamizmi == 'ha':
    summa+=10000
    print('choy yozildi')
    mahsulotlar.append('choy')


if cola_aytamizmi == 'ha':
    summa+=15000
    print('cola yozildi')
    mahsulotlar.append('cola')

print(f'{mahsulotlar} yozildi va narxi {summa} ga teng')


