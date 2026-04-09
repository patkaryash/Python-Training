import re
a =  input("Enter a string to perform fullmatch operation:")
mtch = re.fullmatch(a, "python is very important language")
print(mtch)
if mtch != None:
    print("Match found at beginning level")
    print(mtch.start(), " ", mtch.end() )
else:
    print("There is no matching at beginning level")
                    