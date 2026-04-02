#WAP to accept value of A,B,C and find max value
a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))
c = int(input("Enter value of C: "))

if a>b:
    if a>c:
        print("A is the greatest number.")
    else:
        print("C is the greatest number.")
else:
    if b>c:
        print("B is the greatest number.")
    else:
        print("C is the greatest number.")