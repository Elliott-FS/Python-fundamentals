class Guitar:
    def __init__(self):
        self.n_strings = 6
        self.play()

    def play(self):
        print('Air guitar sounds lol')


# Parant class guitar is passed in with its methods
# and attributes to child class ElectricGuitar.
# pass statement says just give it everything parent has
# and add nothing else.

class ElectricGuitar(Guitar):
    #pass
    def playLouder(self):
        print('BWWEEEEEEEWWWWWWW!')
    def __init__(self):
        super().__init__()
        self.n_strings = 8
        # super function says hey access highest level
        # __init__ method. While def __init__(self): says
        # we want to define a new attribute for this child
        # class. 

my_guitar = ElectricGuitar()

print('child class strings', my_guitar.n_strings)
print('parent class strings', Guitar().n_strings)