class Human:
    height = 170
    progress = 20
    def info(self):
        print('I m human')
class Student(Human):
    progress = 15

    def info(self):
        print('I m student')


class Worker(Human):
    salary = 1000


'''class Grandparent:
    height = 170
    age = 60
    home = 'Будинок в селі'


class Parent(Grandparent):
    age = 40

class Child(Parent):
    height = 100

    def __init__(self):
        print(self.height)
        print(self.age)
        print(self.home)

stud = Student()
worker = Worker()


print(stud.height)
print(worker.height)

print(worker.salary)
print(stud.progress)

stud.info()

child = Child()


print(stud.progress)
print(worker.progress)'''

'''class SuperTest:

    def _test1(self):
        print("Test1")

    def test2(self):
        print('Test2')

    def __test3(self):
        print("Test3")

    def __init__(self):
        SuperTest.__test3()

class Test(SuperTest):

    def print(self):
        self._test1()

t = SuperTest()'''


'''class Student:
    def __init__(self, age):
        self.__age = age

    def getAge(self):
        return self.__age
    def setAge(self, age):
        if age < 0 or age > 100:
            return

        self.__age == age

st = Student(15)
print(st.getAge())
st.setAge(20)
print(st.getAge())'''


class Tvariny:
    alive = True
    breathe = True
    eat = True
    weight = True
    height = True
    slep = True



class Ptahy(Tvariny):
    fly = True
    legs = 2
    wings = 2


class Gorobchik(Ptahy):
    def __init__(self, height, weight, age, sitiy):
        self.weight = weight
        self.height = height
        self.age = age
        self.sitiy = sitiy

class Sinichka(Ptahy):
    def __init__(self, height, weight, age, sitiy):
        self.weight = weight
        self.height = height
        self.age = age
        self.sitiy = sitiy



class Savci(Tvariny):
    legs = 4
    ushi = 2
    def __init__(self):
        print("З'явилась нова тварина")


class Sobaka(Savci):
    def __init__(self, name, weight, height, age,deti=None, breed=None):
        self.weight = weight
        self.height = height
        self.name = name
        self.deti = deti
        self.breed = breed
        self.age = age

    bigTeeth = True

    def __str__(self):
        if self.breed != None:
            return f'Пса зовут - {self.name}, ему {self.age} лет, порода - {self.breed}'
        else:
            return f'Пса зовут - {self.name}, ему {self.age} лет'

class Kityk(Savci):
    def __init__(self, name, weight, height, deti=None, breed=None):
        self.weight = weight
        self.height = height
        self.name = name
        self.deti = deti
        self.breed = breed

    claws = True

'''bobik = Sobaka('bobik')
print(bobik.age)
bobik.age = 40
print(bobik.age)'''

bobik_boss = Sobaka(name = 'bobik', weight= 30, age = 6, height=100, breed='Avcharka')

print(bobik_boss)