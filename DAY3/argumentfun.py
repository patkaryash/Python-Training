#positional argument
def login(username, password):
    if username == password:
        print("Login successful")
    else:
        print("Login failed")


username=input("Enter username:")
password=input("Enter password:")
login(username, password)