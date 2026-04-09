import re
count = 0
matcher = re.finditer("Hi", "Hi Hi Hi Hi")
for i in matcher:
    count += 1
    print(i.start(), "...", i.end(), "...", i.group())
print("The number of occurences:", count)