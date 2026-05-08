marks = [94.4, 87.5, 45.5, 23.3]
print(marks)
print(type(marks))
print(len(marks))
print(marks[1:4])
print(marks[1:])


student = ["anshu", 95, 17 , "bihar"]
print(student[0])
student[0] = "rahul"
print(student)


#list methods
list = [2,1,3]
list.append(4)  #add one element at the end
list.insert(1,5) # add middle element 
list.remove(1) # remove first occuresnc element
list.pop(2) # remove at index
print(list)
list.sort() #sorts in ascending order
list.sort(reverse= True) #sorts in descending order
list.reverse()  # reverese list
print(list)