try:
    a = 12 / 0
# except NameError:
#     print('xato')
# except ZeroDivisionError:
#     print("0 ga bolish mumkin emas")
except:
    print(f'xato')

# print('tugadi')

try:
    n = input("pozitiv son kiriting>>>")

    if not n.isdigit():
        raise ValueError('harf kiritilgan')
    n = int(n)
    if n < 0:
        raise ValueError("siz musbat son kiriting")
except ValueError as e:
    print(f'kiritilgan son da xatolik {e}')
else:
    print('else ishladi')
finally:
    print('finally ishladi')

print('salom')
print("salom3")
print('salom1')