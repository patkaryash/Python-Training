#WAP to compress a string by replacing consecutive characters with thir counts

s = "aaabbbcccc"
a = ""
for i in s:
    if i not in a:
        a += i
        a += str(s.count(i))
print(s)
print(a)    