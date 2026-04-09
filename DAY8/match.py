#match operation always match the beginning of string 
import re
a = input("Enter a string to perform match operation:")
mtch = re.match(a, "python is very important language")
print(mtch)
if mtch != None:
    print("Match found at beinning level")
    print(mtch.start(), " ", mtch.end() )
else:
    print("There is no matching at beginning level")