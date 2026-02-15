s = {1,2,3,4}
print(s)
info = {"anshu", 23, False , 3.4, 34}
print(info)

anshu = set()
print(type(anshu))

for value in info:
    print(value)



s1 = {1,2,3,4}
s2 = {1,3,5,7}
print(s1.union(s2))
s1.update(s2)
print(s1)
s1.intersection(s2)
print(s1)

cities = {"india", "austrila", "usa"}
cities2 = {"india","madrid", "kabul"}
print(cities.issuperset(cities2))
print(cities.issubset(cities2)) 