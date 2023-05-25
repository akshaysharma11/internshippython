data={"user":[],"info":[]}

#taking input into the dictionary
while(True):
    key=input("Enter the key values for dictionary")
    value=input("enter the value of above key in the dictionary")
    data[key]=value
    con=input("do you wish to quit [yes/no] ")
    if(con=="yes"):
        break

#taking input in the list inside the dictionary
while(True):
    user=input("Enter username ")
    data["user"].append(user)
    info=input("add information about this user")
    data["info"].append(info)
    con=input("do you wish to quit [yes/no] ")
    if(con=="yes"):
        break

print(data)