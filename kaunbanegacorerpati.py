question = [
    [
        "which language was used to create fb?","python","french","javaScript","php","none",4
    ],
    [
       "which language was used to create fb?","python","french","javaScript","php","none",4 
    ],
    [
        "which language was used to create fb?","python","french","javaScript","php","none",4
    ],[
        "which language was used to create fb?","python","french","javaScript","php","none",4
    ],
]
levels = [1000,2000,3000,4000,5000,10000,20000,40000,8000,160000,320000]
for i in range(0,len(question)):
    question = question[i]
    print(f"Question for rs.{levels[i]}")
    print(f"a. {question[1]}          b.{question[2]}")
    print(f"c.{question[3]}   d.{question[4]}")
    reply = int(input("enter your answer(1-4)"))
    if(reply == question[-1]):
        print(f"correct andwer, you have won Rs.{levels[i]}")
        if(i==4):
            money = 10000
        elif(i ==9):
            money = 320000
        elif(i==14):
            money = 10000000
    else:
        print("worng answer")
        break