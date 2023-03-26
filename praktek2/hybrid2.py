class Seseorang:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def get_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)
# Single Inheritance
class Mahasiswa(Seseorang):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
    def get_info(self):
        super().get_info()
        print("Student ID:", self.student_id)
# Single Inheritance
class Employee(Seseorang):
    def __init__(self, name, age, address, salary):
        super().__init__(name, age, address)
        self.salary = salary
    def get_info(self):
        print("Salary:", self.salary)
# Multiple Inheritance
class Penulis(Employee, Mahasiswa):
    def __init__(self, name, age, address, salary, student_id, published_books):
        Employee.__init__(self, name, age, address, salary)
        Mahasiswa.__init__(self, name, age, address, student_id)
        self.published_books = published_books
    def get_info(self):
        super().get_info()
        print("Student ID:", self.student_id)
        print("Published Books:", self.published_books)
penulisA = Penulis("Dewi", "17", "Bumi", "20jt", "210511032", "Ada")
penulisA.get_info()