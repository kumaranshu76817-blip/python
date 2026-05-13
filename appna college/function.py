#fuction defintion
def calc_sum(a,b): #parameter
    sum = a+b
    print(sum)
    return sum

calc_sum(3,2) #fuction call; arguments

calc_sum(5.435,234.2)

#average of 3 number
def calc_avg(a,b,c):
    sum = a+b+c
    avg = sum /3
    print(avg)
    
calc_avg(45,34,23)


#practice questions
cities = ["delhi","gurgaon","nodia"]
def print_len(list):
    print(len(list))

print_len(cities)


def oddEven(n):
    if(n%2 == 0):
        print("even")
    else:
        print("odd")
oddEven(2)