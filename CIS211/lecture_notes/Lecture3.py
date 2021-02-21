""" Classes and Subclasses"""


class Mammal(object):
    def hair_kind(self) -> str:
        return "Some kind of fur"

    def speak(self):
        return self.sound()

    def sound(self):
        raise NotImplementedError("Hey, sound was not defined")


class Dog(Mammal):
    def milk_kind(self) -> str:
        return "Dog Milk"

    def hair_kind(self) -> str:     # This is what we call overwriting
        return "Dog hair"           # This overrides the hair_kind method in Mammal class

    def sound(self) -> str:
        return "Arf"


class Poodle(Dog):
    def __init__(self):
        pass

    def hair_kind(self) -> str:
        return "Curly fur"


class Weasel(Mammal):

    def sound(self) -> str:
        return "squeal"


fido = Dog()
fifi = Poodle()
my_weasel = Weasel()
my_pets = [fido, fifi, my_weasel]
for pet in my_pets:
    print (f"My pet says {pet.speak()}")

# Here is where we begin to see a benefit for method overwriting
# With different classes. We want something different to print for
# Different classes while calling the same method for each class

# print(Dog.hair_kind(fifi))  # DONT DO THIS
# It will result in a different method call then what we want
# Cause fifi dont have dog hair he has curly fur

# Class Poodle will also know the class Mammal because they cascade
# so Mammal is passed into Dog which is passed into Poodle so Poodle knows Mammal

print(fifi)
# This doesnt do the right print statement compared to the for
# loop because in for loop it calls all the way to mammal
# which has class object which has the __str__ function
# or print function built in


