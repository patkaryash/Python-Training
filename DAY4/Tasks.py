# s= {"name": "Yash", "age": 25}

# key = input("Enter the key to check: ")
# if key in s:
#     print(f"{key} is present in the dictionary.")
# else:
#     print(f"{key} is not present in the dictionary.")

#Write a function to count the frequency of elemenets in a list using a dictionary
# a = [1, 2, 3, 3, 5]
# b = {}
# for i in a:
#     if i in b:
#         b[i] += 1
#     else:
#         b[i] = 1
# print(a)
# print(b)


# count repetitive digits and find repetitive digits and give it as security key and if no repetitive digits are there then print -1
mylist = [5,7,8,3,7,8,9,2,3]
newlist = []

for i in range(len(mylist)):
    count = 0
    key= mylist[i]
    
    j = i + 1
    while j < len(mylist):
        if key == mylist[j]:
            count += 1
            newlist.append(key)
        j += 2
print(len(newlist))