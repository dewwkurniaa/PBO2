class Shape:
    def _init_(self, name, color):
        self.name = name
        self.color = color
    def get_name(self):
        return self.name
    def get_color(self):
        return self.color
class TwoDimensional(Shape):
    def _init_(self, name, color, sides):
        super()._init_(name, color)
        self.sides = sides
    def get_sides(self):
        return self.sides
class ThreeDimensional(Shape):
    def _init_(self, name, color, faces):
        super()._init_(name, color)
        self.faces = faces
    def get_faces(self):
        return self.faces
# Hierarchical Inheritance
class Sphere(ThreeDimensional):
    def _init_(self, name, color, faces, radius):
        super()._init_(name, color, faces)
        self.radius = radius
    def get_radius(self):
        return self.radius