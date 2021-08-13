# s=[12,67,9,8,4,3,5,2,8,9]
a=int(input("enter the number"))
b=str(a)
l=len(b)
t=l-1
i=0
while i<len(b):
    code=int(b[i])
    num=(code)*10**t
    print(num,end=" ")
    if i!=len(b)-1:
        print("+",end=" ")
    i=i+1
    t=t-1