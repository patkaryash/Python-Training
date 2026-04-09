# #WAP to check the valid mobile number
# import re 
# mo = input("Enter mobile number: ")
# obj = re.fullmatch("[7-9][0-9]{9}",str(mo))
# if obj != None:
#     print("Valid mobile number")
# else:
#     print("Invalid mobile number")
    
    
    
import re
s = input("Enter the email:")
obj=re.fullmatch("\w[a-zA-Z0-9_.]*@ybit[.]ac[.]in",s)
if obj!=None:
    print("valid Email ID")
else:
    print("Invalid Email ID")