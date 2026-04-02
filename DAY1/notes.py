#WAP for change calculation with respect to Total amount
Amount = int(input("Enter the total amount: "))
print("100 notes =", Amount//100)
print("50 notes =", (Amount % 100)//50)
print("20 notes =", (Amount % 50)//20)
print("10 notes =", (Amount % 20)//10)
print("5 notes =", (Amount % 10)//5)
print("2 notes =", (Amount % 5)//2)
print("1 notes =", (Amount % 2)//1)
