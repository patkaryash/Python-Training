#WAP to check if a list is palindrome 
s = [1,2,3,2,1]
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")