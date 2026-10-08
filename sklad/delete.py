from constant import ombor

def delet():
    search = input("Mahsulotni kiriting olib tashlash uchun:")
    if search not in ombor:
        print(f"'{search}' mahsuloti omborida topilmadi.")
        return
    ombor.pop(search)
    print(f"🗑️ {search} ombordan o'chirildi.")