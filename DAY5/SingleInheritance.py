#Single level inheritance
class College:    #Parent class or Base class
    def college_name(self):   #method of parent class
       print("YBIT")          
        
class Student(College):     #Child class or Derived class
    def student_info(self):  #method of child class
        print("Student Name: Yash Patkar") 
        print("Roll No: 101")
        
obj = Student()    #creating object of child class
obj.college_name() #accessing method of parent class using child class object
obj.student_info() 


