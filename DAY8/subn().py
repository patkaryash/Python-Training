import re
a=input("Enter the string:")
mtch = re.subn("[0-9]","*",a)
print(mtch)
print("The string is:",mtch[0])
print("The number of occurences:",mtch[1])