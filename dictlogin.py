credential={"user":["akshay","sharma"] ,"password":["123","456"]}
product={
    "product1":{"name":"product1","price":100,"qty":40},
    "product2":{"name":"product2","price":200,"qty":20},
    "product3":{"name":"product3","price":300,"qty":30},
    "product4":{"name":"product4","price":50,"qty":50}
}

index=0
user=input("enter username")
for i in credential.values():
    for j in i:
        if(j==user):
            password=input("enter password")
            if(password==credential["password"][index]):
                print("login")
                for x in product.values():
                    print(x)
            else:
                print("failed login")
                break
        else: 
            index+=1
    else:
        print("wrong credntials")
        break        


'''
#copying the data into the one dict to another dictionary
data={"name":"ak","age":30}
data1={}
def usercopy(data):
    for i in data:
        data1[i]=data[i]

usercopy(data)
print(data1)
print(data)

#taking input from the user to the list into the dictionary

'''
#product and add to cart dictionary 