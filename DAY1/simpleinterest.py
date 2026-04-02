p_amount= int(input("Enter the principal amount: "))#10000
roi = int(input("Enter the rate of interest: "))#10
time = int(input("Enter the time in years: "))#1

si = p_amount * roi * time / 100
print("Simple Interest = ", si )