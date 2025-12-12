class Animal:
    def __init__(self, sound):
        self.sound = sound
    
    def make_sound(self):
        return f"Animal makes {self.sound}"

class Cat(Animal):
    def __init__(self):
        
        super().__init__("Meow")
    
    def make_sound(self):
        
        return "Meow!"


print("Animal class:")
ani1 = Animal("animal sound")
print(ani1.make_sound())

print("Cat class:")
cat1 = Cat()
print(cat1.make_sound())
