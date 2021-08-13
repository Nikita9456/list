a=[1,2,3,4,5,6,7,5]
i=0
b=a[0]
c=a[0]
while i<len(a):
    if a[i]>b:
        b=a[i]
        if a[i]<c:
            c=a[i]
    i=i+1
print("maxminum number",b)
print("maximunm number",c)