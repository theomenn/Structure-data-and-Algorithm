class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        pass # metode ini akan dioverride oleh class child
    

class Cat(Animal):
    def sound(self):
        return "Meow"
    
class Dog(Animal):
    def sound(self):
        animal_sound = super().sound()
        return f"{animal_sound} Woof"
    
class Bird(Animal):
    def __init__(self, name, bird_type):
        super().__init__(name)
        self.bird_type = bird_type

    def terbang(self):
        return "Flying"
    
cat = Cat("ucup")
dog = Dog("jein")
bird = Bird("joni", "bekicau")
print(cat.sound())
print(dog.sound())
print(bird.terbang())

