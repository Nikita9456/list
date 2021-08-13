num=[2,4,6,3,7,5,4,3,8,6,3]
i=0
even=[]
odd=[]
sum=0
sum1=0
while i<len(num):
    m=num[i]
    if m%2==0:
        even.append(m)
        sum=sum+num[i]
    else:
        odd.append(m)
        sum1=sum+num[i]
    i=i+1
print(even,sum)
print(odd,sum1)

list1=[23,14,56,12,19,9,15,25,31,42,43]
even=[]
odd=[]
for number in list1:
    if number%2==0:
        even.append(number)
    else:
        odd.append(number)

print("list=",list1)
print("odd list=",odd)
print("even list",even)
print("sum of odds=",sum(odd))
print("sum of evens=",sum(even))
