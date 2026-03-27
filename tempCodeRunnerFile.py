class Employee:
    def __init__(self,name):
        self.name = name
    def showDetails(self):
        print(f"the name of the employee is {self.name}")

emp1 = Employee("anshu")
emp1.showDetails()