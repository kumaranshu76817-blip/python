from functools import reduce
# def cube(x):
#     return x*x*x
# print(cube(2))

l = [1,2,4,5,6,4,3]
# newl = []
# for item in l:
#     newl.append(cube(item))
newl = list( map(lambda x: x*x*x,l))
print(newl)
def filter_function(a):
    return a>4
newnewl = list(filter(filter_function,l))
print(newnewl)

#calculate the sum of the number using the reduce function
number = [1,2,3,4,5]
def mysum(x,y):
    return x+y
sum = reduce(mysum,number)
print(sum)