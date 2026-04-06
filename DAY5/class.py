class Student:
    roll_no = 101
    def studentData(self):  #method/member function
        print("Student information")
        
obj = Student()  #object creation
print(obj.roll_no)  #accessing class variable
obj.studentData()  #calling method