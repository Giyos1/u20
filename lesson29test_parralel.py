# # # import unittest
# # #
# # #
# # # def kvadrat(a):
# # #     return a * a
# # #
# # #
# # # # a = kvadrat(12)  # 144
# # #
# # # assert 144 == kvadrat(12)
# # # assert 12 != kvadrat(12)
# # # print("Hammasi to'g'ri ✅")
# #
# #
# # def chegirma(narx, foiz):
# #     if not 0 <= foiz <= 100:
# #         raise ValueError("Foiz 0..100")
# #     return narx - narx * foiz / 100  # 100-100*1.1 = -10
# #
# #
# # # 100 20 foiz => 80
# #
# # import unittest
# #
# #
# # class ChegirmaTest(unittest.TestCase):
# #
# #     def test_oddiy_chegirma(self):
# #         self.assertEqual(chegirma(100, 20), 80)
# #
# #     def test_invalid_chegirma(self):
# #         with self.assertRaises(ValueError):
# #             chegirma(100, 110)
#
# # threading va proccing
#
# import time, threading
#
#
# def yukla(nom):
#     print(f"⬇️ {nom} yuklanmoqda...")
#     time.sleep(1)  # internetni kutish (requests.get kabi)
#     print(f"✅ {nom} tayyor")
#
#
# fayllar = ["rasm.png", "video.mp4", "musiqa.mp3"]
#
# # --- Ketma-ket ---
# # t = time.time()
# # for f in fayllar:
# #     yukla(f)
# # print(f"⏱ {time.time() - t:.1f} s")
#
# # --- threading ---
# t = time.time()
# t1 = threading.Thread(target=yukla, args=(fayllar[0],))
# t2 = threading.Thread(target=yukla, args=(fayllar[1],))
# t3 = threading.Thread(target=yukla, args=(fayllar[2],))
#
# t1.start()
# t2.start()
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()
#
# # oqimlar = [t1, t2, t3]
#
# # for o in oqimlar:
# #     o.start()  # ishga tushir — kutmasdan keyingisiga
# #
# # for o in oqimlar:
# #     o.join()  # hammasi tugashini kut
# print(f"⏱ {time.time() - t:.1f} s")


import time, threading, multiprocessing


def ogir_hisob(n):  # CPU 100% band
    s = 0
    for i in range(n):
        s += i * i
    return s


N = 10_000_000

if __name__ == "__main__":  # multiprocessing uchun SHART (ayniqsa Windows)
    # t = time.time()
    #
    # # for _ in range(3):
    # ogir_hisob(N)
    # ogir_hisob(N)
    # ogir_hisob(N)
    #
    # print(f"ketma-ket:       "
    #       f"{time.time() - t:.1f} s")

    # t = time.time()
    # oqimlar = [threading.Thread(target=ogir_hisob, args=(N,)) for _ in range(3)]

    # t1 = threading.Thread(target=ogir_hisob, args=(N,))
    # t2 = threading.Thread(target=ogir_hisob, args=(N,))
    # t3 = threading.Thread(target=ogir_hisob, args=(N,))
    #
    # oqimlar = [t1, t2, t3]
    # for o in oqimlar: o.start()
    # for o in oqimlar: o.join()
    #
    # print(f"threading:   "
    #       f"    {time.time() - t:.1f} s")

    t = time.time()
    # jarayonlar = [multiprocessing.Process(target=ogir_hisob, args=(N,)) for _ in range(3)]

    p1 = multiprocessing.Process(target=ogir_hisob, args=(N,))
    p2 = multiprocessing.Process(target=ogir_hisob, args=(N,))
    p3 = multiprocessing.Process(target=ogir_hisob, args=(N,))

    # jarayonlar = [p1, p2, p3]

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    # for j in jarayonlar: j.start()
    # for j in jarayonlar: j.join()
    print(f"multiprocessing: {time.time() - t:.1f} s")

print('salpom')