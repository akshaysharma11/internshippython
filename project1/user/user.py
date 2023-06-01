import data.data as data
class User:
    usercart={"pro_id":[],"pqty":[]}

    def payment(self):
        pdata = self.usercart
        amount=0
        for i in range(len(pdata['pro_id'])):
                pos=pdata['pro_id'][i]
                rate=data.productdata["product"]["rate"][pos]
                amount+=rate*pdata["pqty"][i]

        print("total payable amount : ",amount)
        while(True):
            inamount=int(input("enter value "))
            if(inamount==amount):
                print("*****Thank you for the shopping****")
                break
            else:
                print("please correct the amount")


    def showcart(self):
        print("********* Your cart **********")
        pdata=self.usercart
        for i in range(len(pdata['pro_id'])):
                
                #taking the value of productid that has beed added to the cart
                pos=pdata['pro_id'][i]

                #printing the productname with help of above position
                print(data.productdata["product"]["productname"][pos],end="\t")
                print(pdata["pqty"][i],end="\t")
                print()

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
    
    