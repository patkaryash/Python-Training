#WAP to accept phy, chem, and maths subject marks calculate total and percentage and if percentage is greater then equal to 60 and gender is equal to male so he is eligible for placement else eligible for data entry job.
phy = int(input("Enter marks of physics: "))
chem = int(input("Enter marks of chemistry: "))
math = int(input("Enter marks of maths:"))

total = phy + chem + math
percentage = total/3.0
gender = input("Enter gender (male/female): ")

if percentage >= 60 and gender == "male":
    print("You are eligible for placement.")
else:
    print("You are eligible for data entry job.")