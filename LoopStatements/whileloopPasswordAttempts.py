attempt = 1

while attempt <= 5:

    password = input("Enter Password: ")

    if password == "Lakshman@123":
        print("Login Successful")
        break

    else:
        print("Wrong Password")
    attempt += 1
