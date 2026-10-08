def sana(n):
    print(n)
    if n <= 1:
        return
    else:
        sana(n - 1)

#
# sana(10)  # 10 -> sana(9), 8-sana(8), 7 - sana(7) .... 1-sana(1)


def factorial(n):
    print(n)
    if n == 0:  # Bazaviy holat: 0! = 1
        return 1
    else:
        return n * factorial(n - 1)  # Rekursiv chaqiruv


print(factorial(5))
