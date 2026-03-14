class Person:
    def __init__(self,name,occupaation):
        print("hey i am a person") 
        self.name = name
        self.occupaation = occupaation
        

    def info(self):
        print(f"{self.name} is a {self.occupaation}")


a = Person("rahul","backenddeveloper")
a.name="anshu"
a.occupaation = "hr"
# print(a.name)
a.info()