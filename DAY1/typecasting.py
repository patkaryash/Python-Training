# int() used to convert in integer
print(int(3.14))
# print(int(10+5j))
print(int(True))#=1
print(int(False))#=0
# print(int("4.22"))
print(int("4"))
# print(int("yash"))
# we can not convert complex value to int
# we can not convert floating point value string to int 
# cant convert string name to int '''

#float() used to convert in float
print(float(3)) #3.0
# print(float(50+2j)) 
print(float(True))#1.0
print(float(False))#0.0
# print(float("3.14"))
print(float("4"))
# print(float("yash"))
# we can not convert complex value to float
# we can not convert string name to float

# complex() used to convert 
print(complex(3))#3+0j
print(complex(3.14))#3.14+0j
print(complex(True))#1+0j
print(complex(False))#0+0j
print(complex("5"))#5+0j
print(complex("3.14"))#3.14+0j
#print(complex("yash"))
print(complex(5,-3))#5-3j
print(complex(True,False))#1+0j
# we can not convert string name to complex

#bool() used to convert
print(bool(0))#False
print(bool(15))#True
print(bool(3.14))#True
print(bool(""))#False
print(bool(0.0))#False
print(bool(1+2j))#True
print(bool(0+0j))#False
print(bool(-1))#True
print(bool(False))#False
print(bool(True))#True
print(bool("yash"))#True

