class Person:

    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def display(self):
        print(self.name, self.id)


class Emp(Person):
    def Print(self):
        print("Emp class is called")

obj2 = Emp("Mayank", 104)

obj2.display()

obj2.Print()