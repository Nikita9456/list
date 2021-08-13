magic_sqare=[[8,3,4],
            [1,5,9],
            [6,7,2]]
i=0
sum1=0
while i<len(magic_sqare):
    r=0
    while r<len(magic_sqare[i]):
        sum1=sum1+magic_sqare[i][r]
        r=r+1
        break
    i=i+1
print(sum1)
l=0          
sum2=0
while l<len(magic_sqare):
    k=0
    while k<len(magic_sqare[l]):
        sum2=sum2+magic_sqare[l][k]
        k=k+1
        break
    l=l+1
print(sum2)
h=0
sum3=0
while h<len(magic_sqare):
    p=0
    while p<len(magic_sqare[h]):
        if h==p:
            sum3=sum3+magic_sqare[p][p]
        p=p+1
    h=h+1
print(sum3)
if sum1==sum2==sum3:
    print("magic sqare")
else:
    print("it is not")