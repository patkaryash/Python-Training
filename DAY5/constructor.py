# class Demo:
#     def __init__(self):
#         print("Constructor is called")
    
#     def msg(self):
#         print("Welcome to Python programming")

# obj1 = Demo()  #constructor is called
# # print(obj1)
# obj2 = Demo()  #constructor is called
# obj1.msg()  #Welcome to Python programming


class Hod:
    def __init__(self):
        self.name= "Yash Patkar" #2 byte
        self.age=19              #3 byte
        self.empid=101           #1 byte
    def info(self):
        print("My name is",self.name)
        print("My age is",self.age)
        print("My empid is",self.empid)
obj = Hod()
obj.info()
