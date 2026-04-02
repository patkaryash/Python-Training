#WAP to accept any character and check whether it is uppercase, lowercase, digit or special character using ascii characters.
a = ord(input("Enter any character: "))

if a >=65 and a <=91:
    print("The character is uppercase.")
elif a >=97 and a <=122:
    print("The character is lowercase.")
elif a >=48 and a <=57:
    print("The character is a digit.")
else:
    print("The character is a special character.")


