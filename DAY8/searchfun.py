# import re
# a = input("Enter a string to perform search operation:")
# mtch = re.search(a, "python is very important language")
# print(mtch)
# if mtch != None:
#     print(mtch.start(), " ", mtch.end(), " ", mtch.group())
# else:
#     print("There is no matching")
    
    
#Search from file
import re
f = open("DAY 8 notes.txt", "r")
for line in f:
    mtch = re.search("develop", line)
    if mtch != None:
        print(mtch.start(), " ", mtch.end(), " ", mtch.group())
f.close()


