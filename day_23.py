l= [11,23,3,4,5,1]
print(l)
l.append(4)
l.sort(reverse = True)
print(l.index(4))
print(l)
print(l.count(1))
l.insert(1,534)
print(l)
m = [122,345,678,]
l.extend(m)
print(l)
k = l+ m
k.sort()
print(k)