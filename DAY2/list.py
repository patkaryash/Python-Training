mylist = ["Yash", "Atharv" , "Nilesh" , "pranav" ,77, "Paste",80.23,"siddharth"]
print(mylist) #prints the whole list
# print(type(mylist)) #list is a collection of items which are ordered and changeable. Allows duplicate members.
# print(mylist[0]) #indexing starts from 0
# print(mylist[1]) #indexing starts from 1
# print(mylist[2]) #indexing starts from 2
# print(mylist[-1]) #negative indexing starts from -1 which is the last element of the list
# print(mylist[2:5]) #slicing the list from index 2 to 4 (5 is not included)
# print(mylist[2:]) #from index 2 to end
# print(mylist[:5]) #from start to index 4
# print(mylist[1:8:2]) #from index 1 to 7 with step 2
# print(mylist[:]) #from start to end
# print(mylist[::-1]) #reverse the list

# mylist[2]="Akshay" #changing the value of index 2
# print(mylist) #prints the whole list after changing the value of index 2

# if "Yash" in mylist:
#     print("Yash is present in the list")
# else:
#     print("Yash is not present in the list")

# mylist.append("Satyarth") #adding an element at the end of the list
# print(mylist) #prints the whole list after adding an element at the end of the list

# mylist.insert(1,"Sanket") #adding an element at index 1
# print(mylist) #prints the whole list after adding an element at index 1

# mylist.remove("Sanket") #removing an element from the list  
# print(mylist) #prints the whole list after removing an element from the list    

newlist = mylist.copy() #copying the list to a new list
print(newlist) #prints the new list which is a copy of the original list