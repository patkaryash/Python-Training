# def msg(): #called function
#     print("Hello World")

# msg() #calling function
# msg()

def arithmatic():
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add, sub, mul, div
# print(arithmatic()) #calling function
result = arithmatic() #calling function and storing the returned values in a variable
print("Arithmetic Results: ", result) #printing the addition result
