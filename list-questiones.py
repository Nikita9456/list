num=30
n=[16,11,12,13,14,17,18,19]
i=0
a=[]
while i<len(n):
    j=4
    while j<len(n):
        if n[i]+n[j]==num:
            a.append((n[i],n[j]))
        j=j+1
    i=i+1
print(a)               


# list1=[23,14,56,12,19,9,15,25,31,42,43]
# even=[]
# odd=[]
# for number in list1:
#     if number%2==0:
#         even.append(number)
#     else:
#         odd.append(number)

# print("list=",list1)
# print("odd list=",odd)
# print("even list",even)
# print("sum of odds=",sum(odd))
# print("sum of evens=",sum(even))

# # num=[23,14,56,12,19,9,15,24,31,42,43]
# # i=0
# sum=0
# while i<len(num):
#     sum=sum+num[i]
#     i=i+1
# print(sum)
# even=[]
# odd=[]
# i=0
# while i<len(num):
#     m=num[i]
#     if m%2==0:
#         even.append(m)
#     else:
#         odd.append(m)                                                                          
#     i=i+1
# print("num=",num)
# print("even=",even)
# print("odd=",odd)

#report card

# markes=[
#     [78,34,56,45,34,63],
#     [45,43,63,53,23,24],
#     [23,43,65,56,75,34]
# ]
# i=0
# sum=0
# while i<len(markes):
#     j=0
#     while j<len(markes[i]):
#         sum=sum+markes[i][j]
#         j=j+1
#     i=i+1
#print(sum)

# # marks=[ 

# markes=[76,45,87,55,98,23,11],
#         [45,67,44,33,24,45],
#         [45,87,27,43,75]
# ]
# # i=0
# # sum=0
# while i<len(marks):
#     j=0
#     while j<len(marks[i]):
#         sum=sum+marks[i][j]
#         j=j=1
#     i=i+1
# print(sum)

# # marks=[
# #     [12,23,54,34,23,23,54],
# #     [32,54,22,12,22,22,54],
# #     [12,43,23,12,54,67,45]
# # ]
# # i=0
# # sum=0
# # while i<len(marks):
# #     j=0
# #     while j<len(marks[i]):
# #         sum=sum+marks[i][j]
# #         j=j+1
# #     i=i+1
# # print(sum)

#even-odd-sum

# num=[2,4,6,3,7,5,4,3,8,6,3]
# i=0
# even=[]
# odd=[]
# sum=0
# sum1=0
# while i<len(num):
#     m=num[i]
#     if m%2==0:
#         even.append(m)
#         sum=sum+num[i]
#     else:
#         odd.append(m)
#         sum1=sum+num[i]
#     i=i+1
# print(even,sum)
# print(odd,sum1)