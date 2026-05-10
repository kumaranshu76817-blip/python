# count = 1
# while count <= 9999999999:
#     print("anshu kumar ----------" , count)
#     count+= 1

#print number from  1 to 100
i = 1
while i<=100:
    print(i)
    i+=1

#print numbner form 100 to 1
i = 100
while i>=1:
    print(i)
    i-=1

#print the multiplication table of a number n
i = 1
while i<= 10:
    print (5,"x",i,"=",5*i)
    i+=1

#print the element of the followin list using a lop

#traverse
nums = [1,4,9,16,3,34,3,45,65]
idx = 0
# while idx<len(nums):
#     print(nums[idx])
#     idx+=1
x=16
while idx< len(nums):
    if(nums[idx] == x):
        print(nums[idx])
    idx += 1

i = 1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("end of loop")