#WAP to find common elements between 2 lists 
s = [1,2,3,4]
p = [3,4,5,6]
common = []
for i in s:
    if i in p:
        common.append(i)
print(common)
