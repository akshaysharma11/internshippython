dict1={"name":"akshay","subject":["ml","python","ai"],"age":{}}

for x in dict1.values():
    if(type(x)==str):
        print(x,"is a string type")
    elif(type(x)==list):
        print(x,"is a list type")
    elif(type(x)==dict):
        print(x,"is a dictionary type")

    