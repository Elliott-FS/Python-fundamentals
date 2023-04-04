class Fruit: 
    def __init__(self, name, clr):
        self.name = name
        self.colour = clr
    
    def details(self):
        print('my ' + self.name + ' is ' + self.colour)

apple = Fruit("apple", "red")
apple.details()

# __init__ method is where you initialize 
# the attributes for the class. __init__ is ran 
# for every new instance of the class that is created.
