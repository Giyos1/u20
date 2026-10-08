class Avto:
    def __init__(self, model, narx, rang='oq', egasi=None):
        self.model = model
        self.narx = narx
        self.rang = rang
        self.egasi = egasi

    def __repr__(self):
        return self.get_info()

    def get_info(self):
        if self.egasi is None:
            return f'🚗 {self.rang} {self.model} — {self.narx}$ (sotuvda)'
        else:
            return f'🚗 {self.rang} {self.model} — {self.narx}$ (egase:{self.egasi.name})'


class ElectroAvto(Avto):
    def __init__(self, model, narx, zaryad_km, rang='oq', egasi=None):
        super().__init__(model, narx, rang, egasi)
        self.zaryad_km = zaryad_km

    def get_info(self):
        if self.egasi is None:
            return f'⚡ {self.rang} {self.model} — {self.narx}$ | zaryad: {self.zaryad_km} km (sotuvda)'
        else:
            return f'⚡ {self.rang} {self.model} — {self.narx}$ | zaryad: {self.zaryad_km} km (egasi: {self.egasi.name})'


class Client:
    def __init__(self, name, tel):
        self.name = name
        self.tel = tel


class Salon:
    def __init__(self, name):
        self.name = name
        self.__avtolar = []

    def add(self, avto):
        self.__avtolar.append(avto)

    def hammasi(self):
        return self.__avtolar

    def sotuvda(self):
        s = []
        for i in self.__avtolar:
            if i.egasi is None:
                s.append(i)
        return s


m1 = Client("Alijon", "+99890...")
a1 = Avto('Nexia', 10000)
a1.egasi = m1
a2 = Avto('Matiz', 10000, 'qora')
e1 = ElectroAvto('Matiz', 10000, '1200')

salon = Salon('DR')
salon.add(a1)
salon.add(a2)
salon.add(e1)

# print(salon.hammasi())
# print(salon.sotuvda())
# print(a1.get_info())
# print(a2.get_info())
# print(e1.get_info())




while True:
    print()
    print(f"===== {salon.name} | avtolar: {len(salon.hammasi())} =====")
    print("1. Avto qo'shish")
    print("2. Elektromobil qo'shish")
    print("3. Hammasini ko'rish")
    print("4. Sotish")
    print("5. Eng qimmat avto")
    print("6. Faylga saqlash")
    print("7. Fayldan yuklash")
    print("0. Chiqish")
    tanlov = input("Tanlang: ")

    if tanlov == "1" or tanlov == "2":
        model = input("Model: ")
        try:
            narx = int(input("Narx ($): "))
        except ValueError:
            print("Xato: Son kiriting!")
            continue
        rang = input("Rang (Enter = oq): ")
        if tanlov == "1":
            if rang == "":
                salon.add(Avto(model, narx))            # default rang ishlaydi
            else:
                salon.add(Avto(model, narx, rang))
        else:
            try:
                zaryad = int(input("Zaryad masofasi (km): "))
            except ValueError:
                print("Xato: Son kiriting!")
                continue
            if rang == "":
                salon.add(ElectroAvto(model, narx, zaryad))
            else:
                salon.add(ElectroAvto(model, narx, zaryad, rang))
