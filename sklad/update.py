from constant import ombor


def update():
    search_product = input("Yangilash uchun mahsulot nomini kiriting: ")
    if search_product not in ombor:
        print(f"'{search_product}' mahsuloti omborida topilmadi.")
        return

    print("""
    1 — Narxni yangilash
    2 — Sonini yangilash
    3 — Kirim qo'shish
    4 — Chiqim ayirish
    """)
    tanlov = input("Tanlang: ")

    if tanlov == "1":
        new_price = int(input("Yangi narxni kiriting: "))
        ombor[search_product]["narxi"] = new_price
        print(f"{search_product} narxi yangilandi.")
    elif tanlov == "2":
        new_n = int(input("Yangi sonini kiriting: "))
        ombor[search_product]["soni"] = new_n
        print(f"{search_product} soni yangilandi.")
    elif tanlov == "3":
        count_n = int(input("Qancha kirim qo'shmoqchisiz: "))
        ombor[search_product]["soni"] += count_n
        print(f"{search_product} soni {count_n} ta ortdi.")
    elif tanlov == "4":
        minus_n = int(input("Qancha chiqim ayirmoqchisiz: "))
        if minus_n <= ombor[search_product]["soni"]:
            ombor[search_product]["soni"] -= minus_n
            print(f"{search_product} soni {minus_n} ta azaldi.")
        else:
            print("Yetarli mahsulot yo'q!")
    else:
        print("Noto'g'ri tanlov!")
