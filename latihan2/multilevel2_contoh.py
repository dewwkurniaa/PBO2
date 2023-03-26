class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Employee(Person):
    def _init_(self, name, age, id, salary):
        super()._init_(name, age)
        self.id = id
        self.salary = salary
    def get_details(self):
        super().get_details()
        print(f"ID: {self.id}, Salary: {self.salary}")
class Manager(Employee):
    def _init_(self, name, age, id, salary, department):
        super()._init_(name, age, id, salary)
        self.department = department
    def get_details(self):
        super().get_details()
        print(f"Department: {self.department}")