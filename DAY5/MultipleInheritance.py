#Multilevel Inheritance
class College:                 #first level parent class
    def college_name(self):
        print("YBIT")
        
class Student(College):             #second level child class
    def student_info(self):
        print("Student Name: Yash Patkar")
        print("Roll No: 101")
        
        
class Exam(Student):
    def subject(self):
        print("Subject1: Python")
        print("Subject2: Java")
        print("Subject3: C++")
        
obj = Exam()    #creating object of child class
obj.college_name() #accessing method of first level parent class using child class object
obj.student_info() #accessing method of second level parent class using child class object
obj.subject() #accessing method of child class using child class object
