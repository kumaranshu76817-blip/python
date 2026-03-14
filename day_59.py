def greet(fx):
    def mfx(*args,  **kwargs):
        print("good morning")
        fx(*args, **kwargs)
        print("Thank for using function")
    return mfx
@greet
def hello():
    print("hello world")

@greet
def add(a,b):
    print(a+b)

# greet(hello)()
# greet(add)(1,2)
hello()
add(1,3)