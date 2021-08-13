a=[1,3,34,65,33,2,54]
largest=a[0]
i=0
while i<len(a):
    if a[i]>largest:
        largest=a[i]
    i=i+1
print(largest)