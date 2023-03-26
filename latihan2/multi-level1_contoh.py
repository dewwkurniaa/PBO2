class Animal:
    def _init_(self, name):
        self.name = name
    def speak(self):
        print("The animal speaks")
class Dog(Animal):
    def _init_(self, name, breed):
        super()._init_(name)
        self.breed = breed
    def speak(self):
        print("The dog barks")
class Bulldog(Dog):
    def _init_(self, name, breed, origin):
        super()._init_(name, breed)
        self.origin = origin
    def speak(self):
        print("The bulldog growls")