n=[[1,2,3],[4,5,6],[6,7,8]]
j=n[0]+n[1]+n[2]
a=j
i=0
k=0
while i<len(a):
    k=k+a[i]
    i=i+1
print(k)

def n(a):
    j=a[0]+a[1]+a[2]
    # print(j)
    a=j
    i=0
    k=0
    while i<len(a):
        k=k+a[i]
        i=i+1
    print(k)
n([[1,2,3],[2,4,5],[7,6,5]])