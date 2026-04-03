# mytuple = ("yash", "Ashish", "Rahul", "Sandip","Komal", "Pratik", "Satyarth","23","3.15", "Siddharth")
# print(mytuple) #prints the whole tuple
# print(type(mytuple)) #tuple is a collection of items which are ordered and unchangeable. Allows duplicate members.  

# mytuple[2] = "Akshay" #changing the value of index 2
# print(mytuple) #prints the whole tuple after changing the value of index 2

# init_tuple =()
# print(init_tuple.__len__()) #prints the length of the tuple which is 0
# print(type(init_tuple)) #prints the type of the tuple which is <class 'tuple'>

# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a', 'b')
# print(init_tuple_a == init_tuple_b) #prints True because both tuples have the same elements

# init_tuple_a = '1', '2'
# init_tuple_b = ('3', '4')
# print(init_tuple_a + init_tuple_b) #prints the concatenation of both tuples which is ('1', '2', '3', '4')

# init_tuple = ('Python') *3
# print(type(init_tuple)) #prints the type of the tuple which is <class 'str'> because it is a string and not a tuple

# init_tuple = ('Python',) *3
# print(type(init_tuple)) #prints the type of the tuple which is <class 'tuple'> because it is a tuple

# init_tuple = (1,)*3
# init_tuple[0] = 2
# print(init_tuple) #prints the whole tuple after changing the value of index 0 which is not possible because tuples are unchangeable and will raise a TypeError

# init_tuple = ((1,2),)*7
# print(len(init_tuple[3:8])) #prints the length of the tuple from index 3 to 7 which is 4 because it is a tuple of tuples and each tuple has 2 elements


