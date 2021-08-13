question_list=["1.how many continents are there?",
               "2.what is the capital of india?",
               "3.ng ki miss navgurukul kon hai?"]
option_list=[["1.four","2.nine","3.seven","4.eight"],
             ["1.chandigarh","2.bhopal","3chennai","4.delhi"],
             ["1.nikita","pooja","teena","rekha"]]
solution_list=[3,4,1]
answer_list=["3.seven","4.eight","3.chennai","4.delhi","1.nkita","2.teena"]
i=0
n=1
m=0
count=0
amount=10000
while i<len(question_list):
    print(question_list[i])
    j=0 
    while j<len(option_list[i]):
        print(option_list[i][j])
        j+=1
    lifeline=input("do you want 5050 lifeline")
    if lifeline=="yes":
        print(5050)
        if count==0:
            print(answer_list[m+i])
            print(answer_list[m+n])
            num=int(input("enter the answer"))
            if num==solution_list[i]:
                print("your answer is correct")
                print("you won",amount)
            else:
                print("your answer is wrong")
                print("you loose the game")
                break
            count+=1
        else:
            print("you already used lifeline")
            e=int(input("enter the answer"))
            if e==solution_list[i]:
                print("your answer is correct")
                print("you won",amount)
            else:
                print("your answer is wrong")
                print("you loose the game")
                break
    elif lifeline=="no":
        f=int(input("enter the answer"))
        if f==solution_list[i]:
            print("your answer is correct")
            print("you won",amount)
        else:
            print("your answer is wrong")
            print("you loose the game")
            break
    else:
        print("nothing")
    amount=amount+1000
    i=i+1
    n=n+1
    m=m+1




# question_list=["1.how many continent are there?","2.what is the capital of india","3.who is miss navgurukul"]
# answer_list=[["1.four","2.three","3.seven","4.ten"],
#             ["1.chandigarh","2.delhi","3.uttrakhad","4.pune"],
#             ["1.nikita","2.priyanka","3.ankita","4.pooja"]]
# solition_list=[3,2,1]
# answer_list=["3.seven","1.four","4.pune","2.delhi","1.nikita","2.priyanka"]
# i=0
# a=1
# b=0
# count=0
# amount=0
# while i<len(question_list):
#     print(question_list[i])
#     j=0
#     k=0
#     while j<len(answer_list[i]):
#         print(answer_list[i][j])
#         j=j+1
#     lifeline=input("do you want 5050 lifeline")
#     if lifeline=="yes":
#         print(5050)
#         if count==0:
#             print(answer_list[b+1])
#             print(answer_list[b+a]):