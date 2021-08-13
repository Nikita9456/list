num=[5,8,7,9,4,3,2,1]
i=0
while i<len(num):
    j=0
    while j<i:
        if num[i]<num[j]:
            t=num[i]
            num[i]=num[j]
            num[j]=t
        j=j+1
    i=i+1
print(num)
