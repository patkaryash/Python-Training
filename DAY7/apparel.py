# import math
# a = [79,77,54,81,48,34,25,16]
# count = 0
# for i in a:
#     if math.sqrt(i) == math.sqrt(i)//1:
#         count+=1
# print("The total square plots are:",count)
    

import math
n=int(input("Enter a size of list:"))
list=[]
count=0
for i in range(n):
    b=int(input("Enter a number:"))
    list.append(b)
print(list)
for i in list:
    if math.sqrt(i)%1==0:
        count+=1
print(count)