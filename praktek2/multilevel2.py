class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} speaks")
class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan
    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wingspan}")
class Pelican(Bird):
    def __init__(self, name, wingspan, color):
        super().__init__(name, wingspan)
        self.color = color
    def speak(self):
        print(f"{self.name} is a {self.color} pelican that talks")
pelican = Pelican("Dia", 3, "white")
pelican.speak() 
pelican.fly() 