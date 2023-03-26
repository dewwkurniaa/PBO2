class Animal:
    def _init_(self, name, color):
        self.name = name
        self.color = color
    def get_name(self):
        return self.name
    def get_color(self):
        return self.color
class Mammal(Animal):
    def _init_(self, name, color, fur):
        super()._init_(name, color)
        self.fur = fur
    def get_fur(self):
        return self.fur
class Bird(Animal):
    def _init_(self, name, color, wingspan):
        super()._init_(name, color)
        self.wingspan = wingspan
    def get_wingspan(self):
        return self.wingspan
# Hierarchical Inheritance
class Reptile(Mammal):
    def _init_(self, name, color, fur, scale):
        super()._init_(name, color, fur)
        self.scale = scale
    def get_scale(self):
        return self.scale