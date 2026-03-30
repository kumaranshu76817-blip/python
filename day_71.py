x = [1,2,3]
print(dir(x))
print(x.__add__)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
p = Employee("anshu", 30000)
print(p.__dict__)

print(help(Employee))