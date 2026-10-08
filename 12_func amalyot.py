# ombor = {}
#
# name = "olma"
# narxi = 15
# soni = 20
#
# # result {"olma":{"narxi":15,"soni":16}}
#
# ombor[name] = {"narxi": narxi, "soni": soni}
# ombor["gilos"] = {"narxi": 14, "soni": 29}
#
# ombor["gilos"]["narxi"]=26
#
# ombor.pop('gilos')
# print(ombor)

ombor = {}


def main():
    print("""========================================
   📦 OMBORXONA TIZIMI v1.0
========================================""")
    while True:
        tanlov = input("""
    1 — Mahsulot qo'shish
    2 — Barcha mahsulotlar
    3 — Qidirish
    4 — Yangilash (kirim/chiqim/narx)
    5 — O'chirish
    6 — Umumiy qiymat
    0 — Chiqish
    >>> Bo'limni tanlang: """)

        if tanlov == "1":
            pass

        elif tanlov == "2":
            pass
        elif tanlov == "3":
            pass
        elif tanlov == "4":
            pass
        elif tanlov == "5":
            pass
        elif tanlov == "6":
            pass

        else:
            print("👋 Dastur tugadi. Xayr!")
            break


main()