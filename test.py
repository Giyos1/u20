ombor = {}

def qoshish():
    nom = input("Mahsulot nomi: ")

    if nom in ombor:
        print("Bu mahsulot allaqachon bor")
    else:
        narx = int(input("Narxi: "))
        soni = float(input("Soni (dona) yoki vazni (kg): "))

        ombor[nom] = {
            "narx": narx,
            "soni": soni
        }

        print("Mahsulot qo'shildi")

def korish():
    if len(ombor) == 0:
        print("Ombor bo'sh!")
    else:
        for nom in ombor:
            print("Mahsulot:", nom)
            print("Narxi:", ombor[nom]["narx"], "so'm")
            print("Soni:", ombor[nom]["soni"])
            print()


def qidirish():
    nom = input("Mahsulot nomi: ")

    if nom in ombor:
        print("Mahsulot:", nom)
        print("Narxi:", ombor[nom]["narx"], "so'm")
        print("Soni:", ombor[nom]["soni"])
    else:
        print("Bunday mahsulot topilmadi!")

def yangilash():
    nom = input("Mahsulot nomi: ")

    if nom in ombor:
        print("1 - Kirim")
        print("2 - Chiqim")
        print("3 - Narxni o'zgartirish")

        amal = input("Tanlang: ")

        if amal == "1":
            soni = float(input("Kirim miqdori: "))
            ombor[nom]["soni"] = ombor[nom]["soni"] + soni
            print("Kirim qo'shildi")

        elif amal == "2":
            soni = float(input("Chiqim miqdori: "))

            if soni <= ombor[nom]["soni"]:
                ombor[nom]["soni"] = ombor[nom]["soni"] - soni
                print("Chiqim qilindi")
            else:
                print("Omborda yetarli mahsulot yo'q!")

        elif amal == "3":
            narx = int(input("Yangi narx: "))
            ombor[nom]["narx"] = narx
            print("Narx o'zgartirildi")

        else:
            print("Noto'g'ri tanlov")

    else:
        print("Bunday mahsulot topilmadi!")
def ochirish():
    nom = input("O'chiriladigan mahsulot: ")

    if nom in ombor:
        javob = input("O'chirishni xohlaysizmi? (ha/yo'q): ")

        if javob == "ha":
            del ombor[nom]
            print("Mahsulot o'chirildi")
        else:
            print("O'chirish bekor qilindi")
    else:
        print("Bunday mahsulot topilmadi!")
def umumiy_qiymat():
    jami = 0

    for nom in ombor:
        narx = ombor[nom]["narx"]
        soni = ombor[nom]["soni"]

        jami = jami + narx * soni

    print("Umumiy qiymat:", jami, "so'm")







def kam_qolgan():
    for nom in ombor:
        if ombor[nom]["soni"] < 5:
            print("Mahsulot:", nom)
            print("Soni:", ombor[nom]["soni"])



def main():
    print("""========================================
   OMBORXONA TIZIMI v1.0
========================================""")

    while True:
        tanlov = input("""
    1 - Mahsulot qo'shish
    2 - Barcha mahsulotlar
    3 - Qidirish
    4 - Yangilash (kirim/chiqim/narx)
    5 - O'chirish
    6 - Umumiy qiymat
    7 - Kam qolgan mahsulotlar
    8 - Eng qimmat mahsulot
    0 - Chiqish
    >>> Bo'limni tanlang: """)

        if tanlov == "1":
            qoshish()

        elif tanlov == "2":
            korish()

        elif tanlov == "3":
            qidirish()

        elif tanlov == "4":
            yangilash()

        elif tanlov == "5":
            ochirish()

        elif tanlov == "6":
            umumiy_qiymat()

        elif tanlov == "7":
            kam_qolgan()

        elif tanlov == "8":
            eng_qimmat()

        elif tanlov == "0":
            print("Dastur tugadi. Xayr!")
            break

        else:
            print("Noto'g'ri tanlov")
main()