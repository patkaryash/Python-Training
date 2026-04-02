# val1 = int(input("Enter the value of val1: "))
# val2 = int(input("Enter the value of val2: "))
# print("Before swapping: val1 =", val1, "and val2 =", val2)
# temp = val1
# val1 = val2
# val2 = temp
# print("After swapping: val1 =", val1, "and val2 =", val2)

val1 = int(input("Enter the value of val1: ")) #100
val2 = int(input("Enter the value of val2: ")) #200
print("Before swapping: val1 =", val1, "and val2 =", val2)
val1 = val1 + val2 #100 + 200 = 300
val2 = val1 - val2 #300 - 200 = 100
val1 = val1 - val2 #300 - 100 = 200
print("After swapping: val1 =", val1, "and val2 =", val2)
