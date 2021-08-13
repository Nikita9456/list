numbers=[50,23,36,70,56,12,5,10,7]
list_length=len(numbers)
index=0
# more_then20=0
less_then40=0
while index<list_length:
    if numbers[index]<=40 and numbers[index]>=20:
        less_then40=less_then40+1
    index=index+1
print(less_then40) 
