#WAP to check whether the given file exists or not.
#if it is available then print its content
import os,sys
fname = input("Enter the file name: ")
if os.path.isfile(fname):
    print("File exists:", fname)
    f = open(fname, "r")
else:
    print("File does not exist:", fname)
    sys.exit(0)
print("File content:", f.read())
data = f.read()
print(data)
