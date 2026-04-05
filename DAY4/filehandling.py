# f = open("myfile.txt", "w") # "w" is the mode for writing to a file. If the file does not exist, it will be created. If it already exists, it will be overwritten.
# print("name of file: ", f.name) #prints the name of the file
# print("file mode: ", f.mode) # "r" is the mode for reading from a file. The file must exist, otherwise an error will occur.
# print("readable: ", f.readable()) #returns True if the file is readable, False otherwise
# print("writable: ", f.writable()) #returns True if the file is writable, False otherwise
# print("file closed: ", f.closed) #returns True if the file is closed, False otherwise
# f.close()                        #closes the file
# print("file closed: ", f.closed) #After closing the file, the closed attribute will return True

# f = open("myfile.txt", "w")
# f.write("Mumbai is a smart city.\n") #writes the string to the file.
# f.write("Mumbai is a smart city.\n")
# f.write("Mumbai is a smart city.\n")
# f.write("Mumbai is a smart city.\n")
# f.write("Mumbai is a smart city.\n")
# f.close()
# print("Data written to the file successfully.")

# f = open("myfile.txt", "w") 
# mylist = ["yash\n", "prashant\n", "patkar\n"]
# f.writelines(mylist) #writes a list of strings to the file. Each string in the list will be written as a separate line in the file. If you want to add a newline character after each string, you can modify the list as follows:
# f.close()
# print("Data written to the file successfully.")

# reading from a file
# f = open("myfile.txt", "r") # "r" is the mode for reading from a file. The file must exist, otherwise an error will occur.
# print(f.read()) #reads the entire contents of the file and returns it as a string. After reading, the file pointer will be at the end of the file.
# # f.close() #closes the file


# with open("myfile.txt","w") as f:
#     f.write("amit\n")
#     f.write("ashish\n")
#     f.write("Prashant\n")
#     print("file closed: ", f.closed) #After the with block, the file will be automatically closed, so this will print True
# print("file closed: ", f.closed) #After the with block, the file will be automatically closed, so this will print True

# with open("myfile.txt", "r") as f:
#     content = f.read()
#     print(content)

# f1 = open("cowboy.jpg", "rb") # "rb" is the mode for reading a file in binary mode. This is used for non-text files such as images, videos, etc.
# f2 = open("album poster.jpg", "wb") # "wb" is the mode for writing to a file in binary mode. This is used for non-text files such as images, videos, etc.
# data = f1.read() #reads the entire contents of the file and returns it as a bytes object. After reading, the file pointer will be at the end of the file.
# f2.write(data) #writes the bytes data to the file. If the file does not exist, it will be created. If it already exists, it will be overwritten.
# print("New image is available with the name: album poster.jpg.")


