infor = {
    "key" : "value",
    "name" : "Anshu",
    "subjects" :  ["python", "c", "java"],
    "learning" : "coding", 
    "age" : 35,
    "is_adult" : True,
    "marks" : 95.5
}
print(infor)
print(type(infor))
print(infor["subjects"])


infor["name"] = "anshu kumar" #overwrite
print(infor)


null_dict = {}
null_dict["name"] = "anshu"
print(null_dict)



#NESTED DICTIONARY
student = {
    "name" : "anshu kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 90,
        "math" : 45
    }
}

print(student["subjects"]["chem"])
print(list(student.keys()))
print(student.items())
new_dict = {"name": "neha ", "age" : 16}
student.update(new_dict)
print(student)


# print(student["name2"])   #erro
print(student.get("name2"))  # no error -> None

