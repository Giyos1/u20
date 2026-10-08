class Student:
    def __init__(self, name, step):
        self.name = name
        self.step = step

    # def __str__(self):
    #     return f'{self.name} - {self.step}'

    def __repr__(self):
        return f'{self.name} - {self.step}'


s1 = Student('Ali', 2)
s2 = Student('Vali', 2)
s3 = Student('Gani', 2)


# print(s1)


class Universitet:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, s):
        self.students.append(s)

    def __lt__(self, y):
        return len(self.students) < len(y.students)

    def __le__(self, y):
        return len(self.students) <= len(y.students)

    def __add__(self, other):
        u = Universitet(self.name + " " + other.name)
        u.students = self.students + other.students
        return u

    def __len__(self):
        return len(self.students)

    def __getitem__(self, item):
        return self.students[item]


u1 = Universitet('TATU')
u2 = Universitet('INHA')

u1.add_student(s1)
u1.add_student(s2)

u2.add_student(s3)
# print(u1 >= u2)
u3 = u1 + u2


# print(u3.name)
# print(u3.students)

# print(len(u3))
# print(u3[0])  # u3.stundets[0]


# a = 1
# b = 3

# print(a < b)

# print(dir(s1))


class Avto:
    __avto_count = 0

    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        Avto.__avto_count += 1

    @classmethod
    def get_avto_count(cls):
        return cls.__avto_count

    def __len__(self):
        pass


a1 = Avto('Cobalt', 'chevrolet', 2026)
a2 = Avto('Matiz', 'chevrolet', 2026)
a3 = Avto('Damas', 'chevrolet', 2026)

print(Avto.get_avto_count())
