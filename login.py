attempt=0
product=["product1","product2","product3","product4"]
rate =[100,200,240,233]
qty=[20,32,20,40]
addproduct=[]
addqty=[]
addrate=[]

def login(userlist,passlist):
    name=input("enter username")
    password=input("enter password")
    for i in range(len(userlist)):
        if(name==userlist[i] and password==passlist[i]):
            return True

def showproduct():
    i=0
    while(i<len(product)):
        print(product[i],end="\t")
        print(rate[i],end="\t")
        print(qty[i],end="\n")
        i=i+1

def addtocart(pro):
    exist=False
    p_find=False
    for i in range(len(product)):
        if(product[i]==pro):
            p_pos=i
            p_find=True
    for i in addproduct:
        if(i==pro):
            i=addproduct.index(pro)
            print("already added product")
            q= int(input("enter qty"))
            exist=True
            if(q>qty[p_pos]):
                print("exceed the quantity")
            else:
                addqty[i]+=q
                qty[p_pos]-=q
    
    if p_find and not exist:
                    q= int(input("enter qty"))
                    print()
                    if(q<=qty[p_pos]):
                        addproduct.append(pro)
                        addqty.append(q)
                        qty[p_pos]-=q
                        addrate.append(rate[p_pos])
                    else:
                        print("not") 
def showcart():
    for i in range(len(addproduct)):
        print(addproduct[i],end="\t")
        print(addqty[i],end="\t")
        print(addrate[i],end="\n")
     
def showpayment():
     totalpay=0
     for i in range(len(addproduct)):
        print(addproduct[i],end="\t")
        print(addqty[i],end="\t")
        print(addrate[i],end="\n")
        totalpay+=addqty[i]*addrate[i];
     print("Total pay",totalpay)
     pay =int(input("enter pay"))
     if(pay==totalpay):
        print("thx")

def removeproduct(rm):
    while(True):
        if(rm=="yes"):
            p=input("enter product name")
            for i in range(len(addproduct)):
                if p==addproduct[i]:
                    addproduct.pop(i)
                    addqty.pop(i)
                    addrate.pop(i)
                    break
            rm=input("do you want to remove any other product ")
        else:
            return


while(True):
    user=["user1","user2"]
    password=["123","234"]
    if(login(user,password)):
        print("login")
        showproduct()
        ch="yes"
        while(ch=="yes"):
            proname=input("Enter the product name : ")
            addtocart(proname)
            ch=input("do you want to continue : yes/no ")
        showcart()
        rm=input("do you want to remove any product ")
        removeproduct(rm)
        showpayment()

    else:
        print("not login")
        attempt+=1
    if(attempt==3):
        break;
