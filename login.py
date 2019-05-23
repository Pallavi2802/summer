from getpass import getpass
login={"pallavi":"pallavi2802","karan":"1999"}
name = input("enter the user name : ")
paswd = getpass("enter your password : ")
if name in login.keys() :
    if paswd == login.get(name) :
        print("you have successfully loged in")
    else :
        print("your password is incorrect")
else:
    print("your username is incorrect")
    



