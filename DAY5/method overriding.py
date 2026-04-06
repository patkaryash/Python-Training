#method overriding(parent and child relationship must be there)
class Rbi:
    def home_loan(self):
        print("Home loan interest rate is 7%")
    def car_loan(self):
        print("Car loan interest rate is 8%")
        
        
class Sbi(Rbi):
    def home_loan(self):
        print("Sbi Provide home loan at 6% interest rate")
    def car_loan(self):
        print("Car loan interest rate is 7%")
        super().home_loan()   #calling method of parent class using super() function
        
obj = Sbi()   #creating object of child class
obj.home_loan()   #calling method of child class using child
obj.car_loan()    #calling method of child class using child