import csv
f= open("students.csv", "a", newline="") # "a" is the mode for appending to a file. If the file does not exist, it will be created. If it already exists, the new data will be added to the end of the file. The newline="" argument is used to prevent adding extra blank lines between rows in the CSV file.
a = csv.writer(f)
# a.writerow(["studentID","rollno","name","age","grade"])

studentID = int(input("Enter student ID: "))
rollno = int(input("Enter roll number: "))
name = input("Enter name: ")
age = int(input("Enter age: "))
grade = int(input("Enter grade: "))
a.writerow([studentID, rollno, name, age, grade])
print("Data written to the file successfully.") 