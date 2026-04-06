class Student:
    @staticmethod
    def get__personal_detail(firstname,lastname):
        print("your personal detail = ",firstname,lastname)
        
    
    @staticmethod
    def contact_detail(mobil_no, rollno):
        print("your contact detail = ",mobil_no,rollno)
        
Student.get__personal_detail("prashant","kumar")
Student.contact_detail(8787878787,101)