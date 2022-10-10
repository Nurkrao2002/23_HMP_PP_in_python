''' Duck typing means:
Calling a method on any object without knowing the type/class of the object '''

class Duck:
    def sound(self):
        print("It makes Quack sound")

class Rat:
    def sound(self):
        print("Rat makes ssss sound")

def Animal(obj):
    obj.sound()

# d=Duck()
# d.sound()
# r=Rat()
# r.sound()

# d=Duck()
# Animal(d) # Duck makes Quack sound
# r=Rat()
# Animal(r) # Rat makes sss sound
