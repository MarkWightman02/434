userName = input("Username: ")
userPassword = input("Password: ")

if(userName.lower() == "mark" and userPassword == "1234"):
    print("Welcome to facebook!")
else:
    print("Wrong credentials, try again!")