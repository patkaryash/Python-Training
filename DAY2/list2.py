mylist = [['yash', 'patkar'], ['85.56'], [440022,"yyy"]]
# print(mylist) #prints the whole list
# # print(mylist[row][column]) #indexing starts from 0
# print(mylist[0][0]) #prints 'yash'
# print(mylist[0][1]) #prints 'patkar'
# print(mylist[1][0]) #prints '85.56'
# print(mylist[2][0]) #prints '440022'
# print(mylist[2][1]) #prints 'yyy'

# list1=["yash", "patkar"]
# print(list1*2) #prints the list1 two times

# list2 =[50,25.50, 'yash']
# del list2[2]
# print(list2) #prints the whole list after deleting the list

# list2 =[50,25.50, 'yash']
# list2.clear()
# print(list2) #prints the whole list after clearing the list

# name= "yash patkar"
# print(name)
# myname=list
# print(myname) #prints the whole list which is a copy of the original list

# mylist = [40, 30 , 20, 10]
# mylist.reverse()
# print(mylist) #prints the whole list after reversing the list

# mylist=[44,22,77,0,9,88]
# mylist.sort(reverse=True)
# print(mylist) #prints the whole list after sorting the list in descending order

#Alising of list
#alising is creating a new variable that points to the same list in memory. Any changes made to the list through either variable will affect the same list in memory.
# mylist=[44,22,77,0,9,88]
# newlist=mylist #assigning the address of mylist to newlist
# print(id(mylist)) #prints the memory address of mylist
# print(id(newlist)) #prints the memory address of newlist which is same as mylist
# mylist[0]="yash"
# print(mylist) #prints the whole list after changing the value of index 0
# print(newlist) #prints the whole list after changing the value of index 0 which is same as mylist

# arr = [[1,2,3,4,],
#       [4,5,6,7,],
#       [8,9,10,11,], 
#       [12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop())

# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i - 1] = arr[i]
# for i in range(0,6):
#     print(arr[i], end=" ")
      
      
# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)    

a=[1,2,3,4,5,6,7,8,9]
print(a[3:0:-1])

