a = 330
b = 3303
print("A") if a>b else print("=") if a==b else print("B")

c = 9  if a>b else 0
print(c)
marks = [12,56,32,98,12,45,1,4]
#  
for index, marks in enumerate(marks):
    print(marks)
    if(index == 3):
        print("anshu, awesome")