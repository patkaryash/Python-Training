#WAP to accept 5 numbers and find the greatest number among them.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
e = int(input("Enter fifth number: "))
if a > b and a > c and a > d and a > e:
    print("The greatest number is: ", a)
if b > a and b > c and b > d and b > e:
    print("The greatest number is: ", b)   
if c > a and c > b and c > d and c > e:
    print("The greatest number is: ", c)
if d > a and d > b and d > c and d > e:
    print("The greatest number is: ", d)
if e > a and e > b and e > c and e > d:
    print("The greatest number is: ", e)