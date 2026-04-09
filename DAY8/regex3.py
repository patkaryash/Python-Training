import re
obj = input("Enter any character:") #7
objmatch=re.finditer(obj,"a7b @k9z")
for match in objmatch:
    print(match.start(), "...", match.end(), "...", match.group())
    