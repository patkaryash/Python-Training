#WAP to check count of special characters an white space in given string
#I/P- "gasgg54@#vscsd!s"

# s = "gasgg54@#vscsd!s"
# count = 0
# b=ord(s)
# for i in s:
#     if i not in b:
#         count += 1
# print(count)
        
input = "gasgg54@#vscsdls* "
count = 0
for i in input:
    if not i.isalnum():
        count += 1
print(count)