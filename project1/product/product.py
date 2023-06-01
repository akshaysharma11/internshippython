import user.user as user
import data.data as predata
class Product:
    def showcart(self):
        print("********* Your cart **********")
        pdata = predata.productdata['addtocart']
        for i in range(len(pdata['pro_id'])):
                
                #taking the value of productid that has beed added to the cart
                pos=pdata['pro_id'][i]

                #printing the productname with help of above position
                print(predata.productdata["product"]["productname"][pos],end="\t")
                print(pdata["pqty"][i],end="\t")
                print()


    def prodcut_test(self,product):
        pos =-1
        pdata = predata.productdata['product'];
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
                if(qty<=predata.productdata["product"]["qty"][pos]):
                    if(pos in predata.productdata['addtocart']['pro_id']):
                        print("already existed product")
                        existindex=predata.productdata['addtocart']['pro_id'].index(pos)
                        predata.productdata['addtocart']['pqty'][existindex]+=qty
                    else:
                        cart = predata.productdata['addtocart']
                        l1 = predata.productdata['addtocart']['pro_id']
                        l2 = predata.productdata['addtocart']['pqty']
                        l1.append(pos)
                        l2.append(qty)

                    #deducting the qty that has been added to the cart
                    predata.productdata["product"]["qty"][pos]-=qty

                    ch=input("do you wish to add more product[yes/no] ")
                else:
                    print("exceed the quantity")
            else:
                print("product not  found")


    def removeproduct(self):
        prodname=input("enter product name you want to remove ")
        try:
            pos=predata.productdata["product"]["productname"].index(prodname)
            if(pos in predata.productdata["addtocart"]["pro_id"]):
                qty_pos=predata.productdata["addtocart"]["pro_id"].index(pos)
                predata.productdata["addtocart"]["pro_id"].remove(pos)
                val=predata.productdata["addtocart"]["pqty"].pop(qty_pos)

                #increment value to the stock that has been removed from cart
                predata.productdata["product"]["qty"][pos]+=val

        except:
            print("something went wrong")
        finally:
            print()
            print(user)

    def payment(self):
        pdata = predata.productdata['addtocart']
        amount=0
        for i in range(len(pdata['pro_id'])):
                pos=pdata['pro_id'][i]
                rate=predata.productdata["product"]["rate"][pos]
                amount+=rate*pdata["pqty"][i]

        print("total payable amount : ",amount)
        while(True):
            inamount=int(input("enter value "))
            if(inamount==amount):
                print("*****Thank you for the shopping****")
                break
            else:
                print("please correct the amount")

    def showproduct(s):
        print("show product")
        pdata = predata.productdata['product'];
        for j  in range(len(pdata['productid'])):
            if(j==0):
                for i in pdata.keys():
                    print(i,end="\t")
                print()
            for i in pdata.keys():
                    print(pdata[i][j],end="\t")
            print()
        s.addtocart()
        s.showcart()

        while(True):
            ch=input("do you want to remove any product ")
            if(ch=="yes"):
                s.removeproduct()
            else:
                break
        s.showcart()
        s.payment()    
    