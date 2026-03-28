class Employee:
    company = "apple"
    def show(self):
        print(f"the name is a{self.name} and comepany is {self.company}")
    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "anshu"
e1.show()
e1.changeCompany("tesla")
e1.show()
print(Employee.company)