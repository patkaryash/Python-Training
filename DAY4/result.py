import csv
f= open("results1.csv", "a", newline="")
a = csv.writer(f)
# a.writerow(["rollno", "name", "mobileno", "math", "phy", "chem", "total", "percentage", "email", "result"])
rollno = int(input("Enter roll number: "))
name = input("Enter name: ")
mobileno = int(input("Enter mobile number: "))
math = int(input("Enter marks in math: "))
phy = int(input("Enter marks in physics: "))
chem = int(input("Enter marks in chemistry: "))
total = math + phy + chem
percentage = total / 3
email = input("Enter email: ")
if percentage >= 40:
    result = "Pass"
else:
    result = "Fail"
a.writerow([rollno, name, mobileno, math, phy, chem, total, percentage, email, result])
print("Data written to the file successfully.")


