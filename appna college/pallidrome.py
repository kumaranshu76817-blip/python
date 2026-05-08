#check is if a list is pallidrom 
list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palldrome")
else:
    print("not palldrome")

#second way to pallidrome
num = 121
original = num
reverse = 0
while num>0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if(original == reverse):
    print("pallidrom")
else:
    print("not pallidrome")