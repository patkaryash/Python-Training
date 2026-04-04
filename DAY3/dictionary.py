mydict = {
    101: "yash",
    102: "siddharth",
    "103": "prashant",
    "104": "satyarth",
    101:"ashish", #when we have duplicate keys in a dictionary then the last value will be assigned to that key and the previous value will be overwritten
    104:"ashish"
}
# print(mydict) #prints the whole dictionary
# print(type(mydict)) #dictionary is a collection of key-value pairs which are unordered, changeable and indexed. No duplicate members.

#with the help of key we have to print the values
# a = mydict[102] #prints the value of key 102 which is "siddharth"
# print(a) #prints the value of key 102 which is "siddharth"

# mydict[102] = "pranav" #adding a new key-value pair to the dictionary
# print(mydict) #prints the whole dictionary after adding a new key-value pair

# only print the keys of the dictionary
# for x in mydict:
#     print(x) #prints the keys of the dictionary

# only print the values of the dictionary
# for x in mydict.values(): #prints the values of the dictionary
#     print(x)

# print key and values both
# for x, y in mydict.items():
#     print(x,y) #prints the keys and values of the dictionary    

# If I have to add new key and value pair in my dictionary
mydict["mobile_no"] = "1234567890"
print(mydict) #prints the whole dictionary after adding a new key-value pair
