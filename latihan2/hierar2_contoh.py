class Employee:
    def _init_(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_salary(self):
        return self.salary
class Manager(Employee):
    def _init_(self, name, age, salary, department):
        super()._init_(name, age, salary)
        self.department = department
    def get_department(self):
        return self.department
class Programmer(Employee):
    def _init_(self, name, age, salary, language):
        super()._init_(name, age, salary)
        self.language = language
    def get_language(self):
        return self.language
# Hierarchical Inheritance
class SeniorProgrammer(Programmer):
    def _init_(self, name, age, salary, language, level):
        super()._init_(name, age, salary, language)
        self.level = level
    def get_level(self):
        return self.level