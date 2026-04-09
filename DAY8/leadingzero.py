#WAP to remove only leading zeros from a list of integers using for loop
s = [0,0,1,2,0,3,0,0,4]
result = []
started = False

for num in s:
    if num != 0:
        started = True
    if started:
        result.append(num)

print(s)
print(result)

