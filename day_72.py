class ParentClass:
    def parent_method(self):
        print("This is a method in the parent class.")
class ChildClass(ParentClass):
    def parent_method(self):
        print("anshu")
        super().parent_method()
    def child_method(self):
        print("This is a method in the child class.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()