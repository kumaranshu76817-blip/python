#recursive function
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5)

def fact(n):
    if(n == 0 or n== 1):
        return 1
    else:
        return n * fact(n-1)
print(fact(5))


def sum(a):
    if(a == 0):
        return 
    else:
        return sum(n-1) + sum(n)

print(sum)
    