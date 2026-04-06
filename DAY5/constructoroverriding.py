#Constructor Overriding

class Father:
    def __init__(self):
        print("Father: I am constructor of Father class")
        
class Son(Father):
    def __init__(self):
        print("Son: I am constructor of Son class")
        super().__init__()   #calling constructor of parent class using super() function
        
obj = Son()   #Son: I am constructor of Son class
