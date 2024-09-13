class Pet:
    count_of_pet = 0
    def __init__(self, animal, name, age):
        self.animal = animal
        self.name = name
        self.age = age
        print(f'Привіт! Я {self.animal} {self.name}')
        Pet.count_of_pet += 1
    def __str__(self):
        return f"Я {self.animal}, мене звати {self.name}, мені {self.age} років"


    def __del__(self):
        print(f"Я {self.animal} {self.name}, мені пора")
        Pet.count_of_pet -= 1



    def birthday(self):
        age = int(self.age)
        self.age = age + 1
        return (f"У {self.animal} {self.name} день народження, йому виповнилось {self.age}")

Sobaka = Pet(animal='пес', name='Бобік',age='24')
Kot = Pet(animal='кіт', name='Рижик',age='33')
Popugay = Pet(animal='попугай', name='Степан',age='45')

print(Sobaka)
print(Sobaka.birthday())
print(Kot)
print(Popugay)


