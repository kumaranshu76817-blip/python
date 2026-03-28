class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])

string = "anshu-30000"

e = Employee.fromStr(string)

print(e.name)
print(e.salary)