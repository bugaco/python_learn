class Employee():
    def __init__(self, name, family_name, salary):
        """雇员的初始化方法"""
        self.name = name
        self.family_name = family_name
        self.salary = salary

    def give_raise(self, money=5000):
        self.salary += money


