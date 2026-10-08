from constant import ombor


def all_product():
    if not ombor:
        print("Omborda hozircha mahsulot yo'q.")
        return

    print("""
    ----------------------------------------
    MAHSULOT              NARXI    SONI
    ----------------------------------------
    """)
    for key, value in ombor.items():
        print(f"{key} {value['narxi']} {value['soni']}")
    print("----------------------------------------")


def search():
    search_product = input("Mahsulotni nomini kriting:")
    if not ombor:
        print("Mahsulotingiz yoq (")
        return
    if search_product in ombor:
        value = ombor[search_product]
        print(f"🔎 {search_product} narxi: {value['narxi']} soni: {value['soni']}")
    else:
        print(f"'{search_product}' mahsuloti omborida topilmadi.")


def all_count():
    son = 0
    for value in ombor.values():
        son += value["narxi"] * value["soni"]
    print(f"Umumiy qiymatlari: {son} so'm")
