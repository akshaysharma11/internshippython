user ={"username":["user1","user2","user3"],"password":[123,456,111],"product":{"productid":[1,2,3],"productname":["product1","product2","product3"],"qty":[10,20,34],"rate":[200,300,500]},"addtocart":{} }   

def prodcut_test(product):
    print("pro test")
    pdata = user['product'];
    if(product in pdata["productname"]):
        return True
    return False

def addtocart():
    print("**************   add to cart ******************")
    while(True):
        pro_name = input("enter product name")
        if(prodcut_test(pro_name)):
            print("product found")            
        else:
            print("product not  found")

def Product():
    #print("product")
    pdata = user['product'];
    #print(pdata);
    for j  in range(len(pdata['productid'])):
        if(j==0):
            for i in pdata.keys():
                print(i,end="\t")
            print()
        for i in pdata.keys():
                print(pdata[i][j],end="\t")
        print()
    addtocart()
        
def loginUser():
   
    print(user)
    name =input("enter user name")
    pos = -1
    find =False
    for i in range(len(user["username"])):
        print(i)
        if(name==user["username"][i]):
            
            print(user["username"][i])
            pos=i
            find =True
            break
    if(find):
        #print(pos)
        password1= int(input("Enter password" ))
        
        for p in user.keys():
            if(p=="password"):
                print(user[p][pos])
                if(password1 ==user[p][pos]):
                    print("login")
                    Product()
           
    
loginUser()


#first check the qty and update the qty
#remove the product
#payment 
#