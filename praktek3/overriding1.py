class Matematika:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c=0):
        return a + b + c

mat = Matematika()
B = mat.add(20, 50, 29)
print(B)
mut = Matematika()
C = mut.add(32,23)
print(C)