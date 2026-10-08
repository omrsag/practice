password = input("enter your password (q to quit): ")

while password != "q":
    if(password == "hi123123"):
        print("hello again!")
        break
    else:
        password = input("wrong password\nenter your password again (q to quit): ")