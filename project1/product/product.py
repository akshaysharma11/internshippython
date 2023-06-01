import user.user as user
import data.data as predata
class Product:
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
                usercart=user.User.usercart
                qty = int(input("enter qty "))

                #checking if entered quantity is within the limit
                if(qty<=predata.productdata["product"]["qty"][pos]):
                    if(pos in usercart['pro_id']):
                        print("already existed product")
                        existindex=usercart['pro_id'].index(pos)
                        usercart['pqty'][existindex]+=qty
                    else:
                        cart = usercart
                        l1 = usercart['pro_id']
                        l2 = usercart['pqty']
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
        user1=user.User()
        try:
            pos=predata.productdata["product"]["productname"].index(prodname)
            if(pos in user1.usercart["pro_id"]):
                qty_pos=user1.usercart["pro_id"].index(pos)
                user1.usercart["pro_id"].remove(pos)
                val=user1.usercart["pqty"].pop(qty_pos)

                #increment value to the stock that has been removed from cart
                predata.productdata["product"]["qty"][pos]+=val

        except:
            print("something went wrong")
        finally:
            print()
            print(user)

    def showproduct(s):
        print("show product")
        pdata = predata.productdata['product'];
        user1=user.User()
        for j  in range(len(pdata['productid'])):
            if(j==0):
                for i in pdata.keys():
                    print(i,end="\t")
                print()
            for i in pdata.keys():
                    print(pdata[i][j],end="\t")
            print()
        s.addtocart()
        user1.showcart()

        while(True):
            ch=input("do you want to remove any product ")
            if(ch=="yes"):
                s.removeproduct()
            else:
                break
        user1.showcart()
        user1.payment()    
    