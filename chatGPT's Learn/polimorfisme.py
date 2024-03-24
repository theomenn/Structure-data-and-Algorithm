# Polimorfisme Compile-Time (Static)
#overrring metode:
# class Kalkulator:
#     def tambah(self, a, b):
#         return a + b

#     def tambah(self, a, b, c):
#         return a + b + c

# kalkulator = Kalkulator()
# print(kalkulator.tambah(2, 3))        # Error: Hanya metode tambah dengan 3 parameter yang tersedia
# print(kalkulator.tambah(2, 3, 4))     # Output: 9

# Polimorfisme Runtime (Dynamic)
# overriding metode:
class Animal:
    def voiced(self):
        return "Suara animal umum"

class Cat(Animal):
    def voiced(self):
        return "Meow"

class Dog(Animal):
    def voiced(self):
        return "Woof"

animal = Animal()
cat = Cat()
dog = Dog()

# Polimorfisme runtime
list_animal = [animal, cat, dog]
for i in list_animal:
    print(i.voiced())

