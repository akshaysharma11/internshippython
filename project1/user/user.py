import data.data as data
class User:
    def userLogin(s):
        name = input("enter user name")
        password=input("enter password")
        if name in data.user and password in data.password:
            pos=data.user.index(name)
            if(password==data.password[pos]):
                return True
            else:
                return False
        else:
            return False
        
    