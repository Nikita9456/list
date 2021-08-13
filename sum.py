numbers=[5,80,55,66,40,33,29]
print(numbers[0:4])
list_length=len(numbers)
i=0
sum=numbers[i]
while i<len(numbers):
    sum=sum+numbers[i]
    i=i+1
print(sum)
