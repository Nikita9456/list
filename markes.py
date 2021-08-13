markes=[
    [78,34,56,45,34,63],
    [45,43,63,53,23,24],
    [23,43,65,56,75,34]
]
i=0
sum=0
while i<len(markes):
    j=0
    while j<len(markes[i]):
        sum=sum+markes[i][j]
        j=j+1
    i=i+1
print(sum)
