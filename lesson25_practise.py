import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')


# ---------- 1-BOSQICH: Avto klassi (class, __init__, default) ----------
class Avto:
    __jami = 0  # 6-bosqich: klass atributi

    def __init__(self, model, narx, rang="oq"):
        self.model = model
        self.narx = narx
        self.rang = rang
        self.egasi = None  # 3-bosqich: hali sotilmagan
        Avto.__jami += 1

    def get_info(self):
        holat = f"egasi: {self.egasi.ism}" if self.egasi else "sotuvda"
        # logging.debug(holat)
        return f"🚗 {self.rang} {self.model} — {self.narx}$ ({holat})"

    # ---------- 5-BOSQICH: dunderlar ----------
    def __str__(self):
        return self.get_info()

    # ---------- 6-BOSQICH: taqqoslash + classmethod ----------
    def __gt__(self, other):
        return self.narx > other.narx

    @classmethod
    def jami_yaratilgan(cls):
        return cls.__jami


# ---------- 2-BOSQICH: Meros — ElektroAvto ----------
class ElektroAvto(Avto):
    def __init__(self, model, narx, zaryad_km, rang="oq"):
        super().__init__(model, narx, rang)
        self.zaryad_km = zaryad_km

    def get_info(self):  # override — polimorfizm!
        holat = f"egasi: {self.egasi.ism}" if self.egasi else "sotuvda"
        return f"⚡ {self.rang} {self.model} — {self.narx}$ | zaryad: {self.zaryad_km} km ({holat})"


# ---------- 3-BOSQICH: Mijoz (obyekt ichida obyekt) ----------
class Mijoz:
    def __init__(self, ism, tel):
        self.ism = ism
        self.tel = tel


# ---------- 4-BOSQICH: Salon (inkapsulyatsiya) ----------
class Salon:
    def __init__(self, nom):
        self.nom = nom
        self.__avtolar = []  # private!

    def add(self, avto):
        if not isinstance(avto, Avto):
            logging.critical(f'{type(avto)} Avto classidan olingan obyektni bermayapsiz')
            raise ValueError('siz Avto classidan olingan obyektni bermayapsiz')
        self.__avtolar.append(avto)
        logging.info(f'{avto} qoshildi')
        print(f"✅ Salonga qo'shildi: {avto.get_info()}")

    def hammasi(self):
        return self.__avtolar[:]

    def sotuvda(self):
        return [a for a in self.__avtolar if a.egasi is None]

    # ---------- 5-BOSQICH: dunderlar ----------
    def __len__(self):
        return len(self.__avtolar)

    def __getitem__(self, index):
        return self.__avtolar[index]

    # ---------- 6-BOSQICH: eng qimmat (max + __gt__) ----------
    def eng_qimmat(self):
        if len(self.sotuvda()) == 0:
            return None
        return max(self.sotuvda())

    # ---------- 7-BOSQICH: sotish ----------
    def sot(self, raqam, mijoz):
        try:
            avto = self.__avtolar[raqam - 1]
        except IndexError as e:
            print("Bunday raqamli avto yo'q!")
            logging.error(f'Bunday raqamli avto yo\'q [{e}] ')
            return
        if avto.egasi is not None:
            logging.warning(f'Afsus, bu avto allaqachon sotilgan ({avto.egasi.ism} ga).')
            print(f"Afsus, bu avto allaqachon sotilgan ({avto.egasi.ism} ga).")
        else:
            avto.egasi = mijoz
            print(f"🎉 SOTILDI! {avto.model} endi {mijoz.ism} niki (tel: {mijoz.tel})")

    # ---------- 8-BOSQICH: fayl bilan ishlash ----------
    def saqla(self, fayl_nomi="salon.txt"):
        with open(fayl_nomi, "w") as fayl:
            for avto in self.__avtolar:
                fayl.write(avto.get_info() + "\n")
        print(f"💾 {len(self)} ta avto faylga saqlandi.")


def yukla(fayl_nomi="salon.txt"):
    try:
        with open(fayl_nomi) as fayl:
            print("💾 Saqlangan salon:")
            for qator in fayl:
                print("  " + qator.strip())
    except FileNotFoundError:
        print("Hali saqlangan salon yo'q.")


# ---------- 7-BOSQICH: asosiy menyu ----------
salon = Salon("Ustudy Motors")

while True:
    print()
    print(f"===== {salon.nom} | avtolar: {len(salon)} =====")
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
                salon.add(Avto(model, narx))  # default rang ishlaydi
            else:
                salon.add(Avto(model, narx, rang))
        else:
            try:
                zaryad = int(input("Zaryad masofasi (km): "))
            except ValueError:
                print("Xato: Son kiriting!")
                continue
            if rang == "":
                salon.add(ElektroAvto(model, narx, zaryad))
            else:
                salon.add(ElektroAvto(model, narx, zaryad, rang))

    elif tanlov == "3":
        for i, avto in enumerate(salon, 1):  # __getitem__ tufayli!
            print(f"{i}. {avto}")  # __str__ tufayli!
        print(f"Jami yaratilgan avtolar: {Avto.jami_yaratilgan()} ta")

    elif tanlov == "4":
        try:
            raqam = int(input("Nechanchi avtoni sotamiz? "))
        except ValueError:
            print("Xato: Son kiriting!")
            continue
        ism = input("Mijoz ismi: ")
        tel = input("Telefoni: ")
        salon.sot(raqam, Mijoz(ism, tel))  # obyekt ichida obyekt!

    elif tanlov == "5":
        qimmat = salon.eng_qimmat()
        if qimmat is None:
            print("Sotuvda avto qolmadi!")
        else:
            print(f"👑 Eng qimmati: {qimmat}")

    elif tanlov == "6":
        salon.saqla()

    elif tanlov == "7":
        yukla()

    elif tanlov == "0":
        print("Xayr! Yaxshi savdolar 🚗")
        break

    else:
        print("Bunday bo'lim yo'q!")
