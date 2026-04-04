# a = {(1,2):1,(2,3):2,(4,5):3}
# print(a[(4,5)])

# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])

# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# sum = 0
# for i in arr:
#     sum += arr[i]
# print(sum)

# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0000] = 4 # This will overwrite the value of key 1 because
#                 #1 and 1.0 are considered the same key in Python dictionaries
# sum = 0
# for i in my_dict:
#     sum += my_dict[i]
# print(sum)

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for i in my_dict:
#     sum += my_dict[i]
# print(sum)
# print(my_dict)

# box={}
# jars = {}
# crates = {}
# box['biscuits'] = 1
# box['chocolates'] = 3
# jars['sugar'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))

# dict = {'c': 97, 'a': 96, 'b': 98}
# for _ in sorted(dict):
#     print(dict[_])

# rec = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# r = rec.copy() # creates a shallow copy of the dictionary
# print(id(r) == id(rec)) # prints False, as r is a different object in memory
# print(id(r)) # prints the memory address of r
# print(id(rec)) # prints the memory address of rec

# rec = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# id1 = id(rec) # stores the memory address of rec in id1
# del rec # deletes the reference to the dictionary object
# rec = {'name': 'Alice', 'age': 30, 'city': 'New York'} # creates a new dictionary object with the same content
# id2 = id(rec) # stores the memory address of the new dictionary object in id2
# print(id1 == id2) 
# print(id1) # prints the memory address of the first dictionary object
# print(id2) # prints the memory address of the second dictionary object
# print(id(id1))
# print(id(id2))

#Write a function to find the key with the minimum value in a dictionary
s = {"a": 5, "b": 2, "c": 8, "d": 1}
min_key = None
for i, j in s.items():
    if min_key is None or j < s[min_key]:
        min_key = i
print(min_key)