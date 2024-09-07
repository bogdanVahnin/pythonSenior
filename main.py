class Student:
    count_of_student = 0
    def __init__(self, name, age=15):
        self.name = name
        self.age = age
        print("Hi!")
        Student.count_of_student += 1
    def __str__(self):
        return f"Я {self.name}, мені {self.age} років."


    '''def info(self):
        print(f"Я {self.name}, мені {self.age} років.")'''

    def __del__(self):
        print(f"Я {self.name}, і я пішов")
        Student.count_of_student -= 1

    def __len__(self):
        return self.age

    def grow(self,delta = 1):
        oldAge = self.age
        self.age += delta
        if self.age > 100:
            print("Error Age")
            self.age = oldAge

Anton = Student(name = 'Anton')
Anton.grow(23)
Kirill = Student(name = 'Kirill',age = 17)
print(Anton.age)
print(Kirill.age)

print(Student.count_of_student)

#Anton.info()
#Kirill.info()

print(Anton)
print(Kirill)


print(len(Anton))
print(len(Kirill))