collection = {1,2,3,4, " helllo ", " world "}
print(collection)
print(type(collection))
print(len(collection))


#set methods
collection1 = set() #empty set syntax
collection1.add(1)
collection1.add(2)
collection1.add(3)
collection1.add(3)
collection1.add("anshu kumar")
collection1.add((1,2,3))

collection1.remove(2)
print(collection1)
print(len(collection1))
print(type(collection1))
print(collection1.pop())


set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2)) #{1,2,3,4}
print(set1.intersection(set2)) #{2,3}



#practice question
dict = {
    "cat" : " a smal animal",
    "table" : ["a piece of furniture", "l;ist of facts And figures"]
}
print(dict)


subjects = {
    "python", " java ", "c++", "python", "javascript", "java",
    "python","java","c++","c"

}
print(subjects)
print(len(subjects))


#wap to enter marks of 3 subject from the user and stor then in a dictionary. start with an empty dictionary and  one by one. use subject naem as key and marks as value.
# marks = {}
# x = int(input("enter phy: "))
# marks.update({"phy" : x})

# x = int(input("enter maths: "))
# marks.update({"maths" : x})

# x = int(input("enter chem:"))
# marks.update({"chem ": x})




Values = {9, "9.0", 8, 8.0}
print(Values)