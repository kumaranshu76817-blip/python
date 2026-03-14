class Employee:
    def __init__(self):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of employee:{self.id} is{self.name}")

class programmer(Employee):
    def showLanguage(self):
        print("the default language is python")

e1 = Employee("anshu",400)
e1.showDetails()
e2 = programmer("anshu", 4100)
e2.showDetails()
e2.showLanguage()
