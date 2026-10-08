from sklad.add_product import choose
from sklad.delete import delet as d
from sklad.show_products import all_product, search, all_count
from sklad.update import update


# ombor["olma"]={}
# ombor["olma"]["narxi"]=15000
# ombor["olma"]["soni"]=140

def main():
    print("========================================")
    print("   📦 OMBORXONA TIZIMI v1.0")
    print("========================================")
    while True:
        tanglash = input("""
    1 — Mahsulot qo'shish
    2 — Barcha mahsulotlar
    3 — Qidirish
    4 — Yangilash (kirim/chiqim/narx)
    5 — O'chirish
    6 — Umumiy qiymat
    0 — Chiqish
    >>> Bo'limni tanlang: """)

        if tanglash == "1":
            choose()
        elif tanglash == "2":
            all_product()
        elif tanglash == "3":
            search()
        elif tanglash == "4":
            update()
        elif tanglash == "5":
            d()
        elif tanglash == "6":
            all_count()
        elif tanglash == "0":
            print("👋 Dastur tugadi. Xayr!")
            break
        else:
            print("Noto'g'ri tanlov!")


main()