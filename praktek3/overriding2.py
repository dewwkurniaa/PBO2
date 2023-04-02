class Animal:
    def make_sound(self):
        print("The animal makes a sound")
class Wolf(Animal):
    def make_sound(self):
        print("The wolf auuuuu")
class Chiken(Animal):
    def make_sound(self):
        print("The chiken kukkuk")
class Bernard(Wolf):
    def make_sound(self):
        print("The bernard roars")
class Jago(Chiken):
    def make_sound(self):
        print("The jago crows")
def animal_sound(animal):
    animal.make_sound()

# Instantiate objects of each class
animal = Animal()
wolf = Wolf()
chiken = Chiken()
bernard = Bernard()
jago = Jago()

# Call the animal_sound function for each object
animal_sound(animal) 
animal_sound(wolf) 
animal_sound(chiken)
animal_sound(bernard) 
animal_sound(jago) 