nums = [1,2,9,16,25,36,49,64,]
x = 49
idx = 0
for el in nums:
    if(el == x):
        print("number fount at idx" , idx)
        idx+=1

#sum of first natural number
sum = 0
for i in range(5):
    sum += i
    i+=1
    
print(sum)

#wap to find the factorial of first n number.(using for)
n = 5
fact = 1
i = 1
while i<= n:
    fact *=i
    i += 1

print("factoral", fact)