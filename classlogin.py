product=["product1","product2","product3","product4"]
rate =[100,200,240,233]
qty=[20,32,20,40]
addproduct=[]
addqty=[]
addrate=[]
user  = ["user1","user2"]
password=[111,123]

username = input("enter name")
if username in user:
     print("user login")

p=''
r=False
for i in range(len(user)):
    if(username == user[i]):
        r=True
        p=i
        break
print(p)
log= False
if(r):
    password1 =int( input("Enter password"))
    if password1==password[p]:
        print("login")
        log=True
else:
    print("not login")
p_pos=-1
p_find=False
if(log):
    i=0
    while(i<len(product)):
        print(product[i],end="\t")
        print(rate[i],end="\t")
        print(qty[i],end="\n")
        i=i+1
    while True:
        exist=False
        ch = input("enter add product 'yes'")
        if(ch == 'yes'):
            pro=input("enter product name")
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
                      if(addqty[i]+q>qty[p_pos]):
                          print("exceed the quantity")
                      else:
                           addqty[i]+=q
                           qty[p_pos]-=q
                           print(qty)
            if p_find and not exist:
                q= int(input("enter qty"))
                print()
                if(q<=qty[p_pos]):
                    print(rate[p_pos])
                    addproduct.append(pro)
                    addqty.append(q)
                    qty[p_pos]-=q
                    print(qty)
                    addrate.append(rate[p_pos])
                else:
                    print("not") 
        else:
            break
    print("* add to cart **")
    for i in range(len(addproduct)):
        print(addproduct[i],end="\t")
        print(addqty[i],end="\t")
        print(addrate[i],end="\n")
    print("* add to cart **")
    rm=input(" product  remove 'yes'")
    if rm =='yes':
        p=input("enter product name")
        for i in range(len(addproduct)):
            if p==addproduct[i]:
                addproduct.pop(i)
                addqty.pop(i)
                addrate.pop(i)
                break
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
    
print("***")
