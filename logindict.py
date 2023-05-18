#1.
#make a list of both password and username and
#prompt user for enter the username
#if correct ask for the password
#check if password correct or not


#sum max min len without function
#login using dictionary


credential={"user":["akshay","sharma"] ,"password":["123","456"]}
index=0
user=input("enter username")
for i in credential.values():
    for j in i:
        if(j==user):
            password=input("enter password")
            if(password==credential["password"][index]):
                print("login")
            else:
                print("failed login")
                break
        else:
            index+=1
