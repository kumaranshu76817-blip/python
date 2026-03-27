class Employee:
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02
    def showDetails(self):
        print(f"the name of the employee is {self.name} and the reaise amount is {self.raise_amount}")

emp1 = Employee("anshu")
emp1.raise_amount = 0.3
emp1.showDetails()
Employee.showDetails(emp1)
emp2 = Employee("rohan")
emp2.showDetails()