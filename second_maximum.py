num=[12,5,8,6,7,8,9,4,3]
i=0
c=num[0]
k=[]
while i<len(num):
    if num[i]<c:
        c=num[i]
    i=i+1
num.remove(c)
j=0
b=num[0]
while j<len(num):
    if num[j]<b:
        b=num[j]
    j=j+1
print(b)