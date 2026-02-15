num = int(input("enter the number: "))
total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total = total + (digit ** 3)
    temp = temp // 10

if total == num:
    print("armstrong number")
else:
    print("not armstrong number")
