# file = open('pi.txt')
# try:
#     content = file.read()
#     print(content)
#     a = 12 / 0
# finally:
#     file.close()
#     print(file.closed)


# with open('pi.txt') as f:
#     content = f.read()
#     print(content)
#     a = 12 / 0

# ctrl+ALT+L


import time


class Taymer:
    def __enter__(self):  # with boshlanganda
        self.boshi = time.time()
        print("⏱ Taymer yoqildi")
        return self

    def __exit__(self, xato_turi, xato, iz):  # with tugaganda (xatoda ham!)
        vaqt = time.time() - self.boshi
        print(f"⏱ Tugadi: {vaqt:.2f} soniya")


with Taymer():
    for i in range(10_000_000):
        pass
