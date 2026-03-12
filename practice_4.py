# f = open('myfile.txt','rt')
# # print(f)
# text = f.read()
# print(text)
# f.close()
# f = open('myfile.txt','a')
# f.write('hello, world')
# f.close()

with open ('myfile.txt','a'):
    f.write("hey i am inside with")
