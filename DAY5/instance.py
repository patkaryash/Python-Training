# class Student:
#     def __init__(self):
#         self.s_name="Prashant"
#         self.s_rollno=101  #declaring instance variable inside a constructor

#     def getdata(self):
#         self.s_mb = 8787878787 #

# obj=Student()
# obj.getdata()
# del obj.s_name
# obj.s_branch="CE" # pyright: ignore[reportAttributeAccessIssue]
# print(obj.__dict__)

class Student:
    def __init__(self, name , rollno, mob):
        self.name = name
        self.rollno = rollno
        self.mob = mob
        
    def display(self):
        print(self.name,"",self.rollno,"",self.mob)
        
stud = Student("Prashant", 101, 8787878787)
stud.display()