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
    age = 1
    weight = True
    height = True



class Ptahy(Tvariny):
    fly = True
    legs = 2
    wings = 2
    age = 3
    weight = 2
    height = 10

class Gorobchik(Ptahy):
    def __init__(self, height, weight, age, sitiy):
        self.weight = weight
        self.height = height
        self.age = age
        self.sitiy = sitiy


class Savci(Tvariny):
    legs = 4
    age = 5
    weight = 20
    height = 100

class Sobaka(Savci):
    def __init__(self, name, deti=None):

        self.name = name
        self.deti = deti

    bigTeeth = True

class Kityk(Savci):
    def __init__(self, name, deti=None):
        self.name = name
        self.deti = deti

    claws = True

bobik = Sobaka('bobik')
print(bobik.age)
bobik.age = 40
print(bobik.age)

