#WAP to reverse each word in a string

s = "Hello World"
a = s.split()
b = ""
for i in a:
    b += i[::-1] + " "
print(s)
print(b)