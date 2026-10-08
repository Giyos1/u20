# kutubxona project ->
# 1- nimani malumotni saqlaymiz ? <- > Kitob - shablon yasar ekanmiz
# 2- kitobni nima malumotlarni saqlaymiz? <-> name, author, dds_number, isb_number
# 3- kitob obyekti bilan bogliq nima ishlar qilamiz? <-> kitob objectlari bn get_info()

class Author:
    def __init__(self, name, age, book_count):
        self.name = name
        self.age = age
        self.book_count = book_count


class Book:
    def __init__(self, name, author, isb_number, dds_number=12):
        self.name = name
        self.author = author
        self.dds_number = dds_number
        self.isb_number = isb_number

    def get_info(self):
        return f'{self.name} [{self.author.name} yoshi {self.author.age}] || {self.isb_number}'


a1 = Author('O\'lmas Umarbekov', '94', 20)

b1 = Book('Odam bo\'lish qiyin', a1, 12312, 12345)
b2 = Book('«Tuhmat» ', a1, 14312, 52345)

b1.isb_number = '123554545'

print(b1.get_info())
# print(b1)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Book:
    def __init__(self, name, author, dds_number=None, ib_number=None):
        self.title = name
        self.author = author
        self.ddsn = dds_number
        self.isbn = ib_number

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author.name}, DDS Number: {self.ddsn}, ISBN: {self.isbn}"

p1 = Person("John Doe", 30)
b1 = Book("The Great Gatsby", p1,"F. Scott Fitzgerald", "813.52")
# b1.isbn = "978-0743273565"
# print(p1.get_info())
print(b1.get_info())
print(b1.isbn)