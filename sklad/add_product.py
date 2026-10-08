from constant import ombor


def choose():
    name = input("Mahsulotni kiriting: ")
    if name in ombor:
        print(f"Bunday mahsulot bor")
        return
    narxi = int(input("Narxini kiriting: "))
    soni = int(input("Qanchaligi kiriting: "))
    ombor[name] = {"narxi": narxi, "soni": soni}
    print(f"{name} mahsuloti omborga qo'shildi.")
