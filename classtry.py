user ={"username":["user1","user2","user3"],"password":[123,456,111],"product":{"productid":[1,2,3],"productname":["product1","product2","product3"],"qty":[10,20,34],"rate":[200,300,500],"dis":[2,3,5]},"addtocart":{ "pro_id":[],"pqty":[]} }   

class shop:
        #show cart 
    def showcart(self):
        print("********* Your cart **********")
        pdata = user['addtocart']
        for i in range(len(pdata['pro_id'])):
                
                #taking the value of productid that has beed added to the cart
                pos=pdata['pro_id'][i]

                #printing the productname with help of above position
                print(user["product"]["productname"][pos],end="\t")
                print(pdata["pqty"][i],end="\t")
                print()



    #payment
    def payment(self):
        pdata = user['addtocart']
        amount=0
        for i in range(len(pdata['pro_id'])):
                pos=pdata['pro_id'][i]
                rate=user["product"]["rate"][pos]
                amount+=rate*pdata["pqty"][i]

        print("total payable amount : ",amount)
        while(True):
            inamount=int(input("enter value "))
            if(inamount==amount):
                print("*****Thank you for the shopping****")
                break
            else:
                print("please correct the amount")


    #remove product function
    def removeproduct(self):
        prodname=input("enter product name you want to remove ")
        try:
            pos=user["product"]["productname"].index(prodname)
            if(pos in user["addtocart"]["pro_id"]):
                qty_pos=user["addtocart"]["pro_id"].index(pos)
                user["addtocart"]["pro_id"].remove(pos)
                val=user["addtocart"]["pqty"].pop(qty_pos)

                #increment value to the stock that has been removed from cart
                user["product"]["qty"][pos]+=val

        except:
            print("something went wrong")
        finally:
            print()
            print(user)


    def prodcut_test(self,product):
        pos =-1
        pdata = user['product'];
        for j  in range(len(pdata['productid'])):
            if(product == pdata["productname"][j]):
                pos =j
                return pos
        return pos


    def addtocart(self):
        print("**************   add to cart ******************")
        ch="yes"
        while(ch=="yes"):
            pro_name = input("enter product name ")
            pos = self.prodcut_test(pro_name)
            if(pos!=-1):
                qty = int(input("enter qty "))

                #checking if entered quantity is within the limit
                if(qty<=user["product"]["qty"][pos]):
                    if(pos in user['addtocart']['pro_id']):
                        print("already existed product")
                        existindex=user['addtocart']['pro_id'].index(pos)
                        user['addtocart']['pqty'][existindex]+=qty
                    else:
                        cart = user['addtocart']
                        l1 = user['addtocart']['pro_id']
                        l2 = user['addtocart']['pqty']
                        l1.append(pos)
                        l2.append(qty)

                    #deducting the qty that has been added to the cart
                    user["product"]["qty"][pos]-=qty

                    ch=input("do you wish to add more product[yes/no] ")
                else:
                    print("exceed the quantity")
            else:
                print("product not  found")
            
    def Product(self):
        pdata = user['product'];
        for j  in range(len(pdata['productid'])):
            if(j==0):
                for i in pdata.keys():
                    print(i,end="\t")
                print()
            for i in pdata.keys():
                    print(pdata[i][j],end="\t")
            print()
        self.addtocart()
        self.showcart()

        while(True):
            ch=input("do you want to remove any product ")
            if(ch=="yes"):
                self.removeproduct()
            else:
                break
        self.showcart()
        self.payment()    

    def loginUser(self):
        name =input("enter username ")
        pos = -1
        find =False
        for i in range(len(user["username"])):
            if(name==user["username"][i]):
                pos=i
                find =True
                break
        if(find):
            password1= int(input("Enter password " ))
            
            for p in user.keys():
                if(p=="password"):
                    if(password1 ==user[p][pos]):
                        self.Product()
    
s=shop()
s.loginUser()