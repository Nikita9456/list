a=[2,3,6,5,8]
i=0
k=[]
num=int(input("enter the num"))
while i<len(a):
    if i<num:
        k.append(a[i])
    else:
        k.append(a[-i])
    i=i+1
print(k)