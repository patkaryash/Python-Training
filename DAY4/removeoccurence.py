#WAP to remove all occurences of a given element from a list
list = [1,2,2,3,4,2]
print(list)
newlist = []
element = int(input("Enter the element to remove: "))
for i in list:
    if i != element:
        newlist.append(i)
print(newlist)