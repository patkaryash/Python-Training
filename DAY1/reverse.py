num = 123 # num = 321
print("The original number is: ", num)
a = num % 10 # a = 3
# print(a)
num = num // 10 # num = 12
# print(num)
b = num % 10 # b = 2
# print(b)
c = num // 10 #c =1
# print(c)
rev = a*100 + b*10 + c*1 # rev = 321
print("The reverse of the number is: ", rev)


num = 123456 # num = 654321
print("The original number is: ", num)
a = num % 10 # a = 6
num = num // 10 # num = 12345
b = num % 10 # b = 5
num = num // 10 # num = 1234
c = num % 10 # c = 4
num = num // 10 # num = 123
d = num % 10 # d = 3
num = num // 10 # num = 12
e = num % 10 # e = 2
num = num // 10 # num = 1  
f = num % 10 # f = 1
rev = a*100000 + b*10000 + c*1000 + d*100 + e*10 + f*1 # rev = 654321
print("The reverse of the number is: ", rev)