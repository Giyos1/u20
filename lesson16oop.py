a = 12
b = "salom"
c = "alik"

# print(type(a))  # -- int
# print(type(b))
# print(b)
# print(b.upper())
# print(c.isdigit())


class Person:
    def __init__(self, name, age, gender, phone_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone_number = phone_number

    def info(self):
        return f'shaxning malumotlari ismi - {self.name}, age - {self.age} gender - {self.gender}'


p1 = Person('Ali',25,'M','+998901234567')
# p2 = Person('vali',26,'M','+998901334567')

# print(p1.name)
# print(p1.age)
# print(p1.gender)
# print(p1.phone_number)
# print(f'p1 shaxning malumotlari ismi - {p1.name}, age - {p1.age} .....')
# print(f'p2 shaxning malumotlari ismi - {p2.name}, age - {p2.age} .....')
# print(p2)

# print(p1.info())
# print(p2.info())

