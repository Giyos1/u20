# # Meros
# # DRY
# # OOP 4 ta tamoyildan
#
# # 1 - inheritance(meros)
#
# class Person:  # Parent
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def get_info(self):
#         return f'{self.name} - {self.age} ({self.gender})'
#
#
# class Student(Person):  # Child
#     def __init__(self, name, age, gender, step):
#         super().__init__(name, age, gender)
#         self.step = step
#
#     def get_info(self):
#         return f'{self.name} - {self.age} ({self.gender}) step [{self.step}]'
#
#
# class Teacher(Person):
#     def __init__(self, name, age, gender, subject):
#         super().__init__(name, age, gender)
#         self.subject = subject
#
#
# class Employee(Person):
#     def __init__(self, name, age, gender, department):
#         super().__init__(name, age, gender)
#         self.department = department
#
#
# s1 = Student('Ali', 23, 'M', 2)
# print(s1.get_info())
#
#
# # multy inhertance
#
# class Scanner:
#     def scan(self):
#         return "Scanning..."
#
#
# class Faxer:
#     def fax(self):
#         return "Sending fax..."
#
#     def test(self):
#         print('test fax')
#
#
# # IKKI otadan meros:
# class MFP(Scanner, Faxer):
#     def print_doc(self):
#         return "Printing..."
#
#
# mfp = MFP()
# print(mfp.scan())  # Scanner'dan
# print(mfp.fax())  # Faxer'dan
# print(mfp.print_doc())  # o'ziniki
# mfp.test()

# class Car:
#     def __init__(self, model, colour, km):
#         self.model = model
#         self.colour = colour
#         self.__km = km
#
#     def get_km(self):
#         return self.__km
#
#     def set_km(self, yangi_km):
#         if yangi_km < 0:
#             print('manfiy son mumkin emas')
#         else:
#             self.__km += yangi_km


# matiz1 = Car('matiz', 'oq', 12000)
# # print(matiz1.km)
# # matiz1.km = 11800
# # print(matiz1.km)
# print(matiz1.get_km())
# matiz1.set_km(-8000)
# print(matiz1.get_km())


from abc import ABC, abstractmethod


# Abstrakt sinf: ATM interfeysi
class ATM(ABC):
    @abstractmethod
    def insert_card(self):
        pass

    @abstractmethod
    def enter_pin(self):
        pass

    @abstractmethod
    def withdraw_money(self, amount):
        pass


# Merosxo'r sinf: ATM funksiyalari
class BankATM(ATM):
    def insert_card(self):
        print("Kartangizni kiritdingiz.")

    def enter_pin(self):
        print("PIN-kodni muvaffaqiyatli kiritdingiz.")

    def withdraw_money(self, amount):
        # Pul olish jarayonini soddalashtirib ko'rsatamiz
        print(f"{amount} so'm muvaffaqiyatli yechildi.")


# ATM funksiyalaridan foydalanish
atm = BankATM()

# Foydalanuvchi amallari
atm.insert_card()          # Kartangizni kiritdingiz.
atm.enter_pin()            # PIN-kodni muvaffaqiyatli kiritdingiz.
atm.withdraw_money(100000) # 100000 so'm muvaffaqiyatli yechildi.