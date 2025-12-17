from abc import ABC, abstractmethod
class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(animal):
    def make_sound(self):
        return "Woof!"
class  Cat(animal):
    def make_sound(self):
        return "Meow!"
dog=Dog()
cat=Cat()   
animals=[dog,cat]
for animal in animals:
    print(animal.make_sound())           