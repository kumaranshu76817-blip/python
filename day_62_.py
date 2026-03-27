class Employee:
    def __init__(self):
        self.__name = "anshu"
a = Employee()
# print(a.__name) # cannot be accessed directily
print(a._Employee__name) # can be accessed indirectly
print(a.__dir__())