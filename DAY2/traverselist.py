# names=[4,2,5,6,7,8,9]
# for i in names:
#     print(i) #prints the whole list one by one

#move all the zeroes to the end of the list    
A = [4,0,2,5,0,1]
print(A) #prints the whole list before moving all the zeroes to the end of the list
for i in A:
    if i == 0:
        A.remove(i) #removing the zeroes from the list
        A.append(i) #adding the zeroes at the end of the list
print(A) #prints the whole list after moving all the zeroes to the end of the list
    
