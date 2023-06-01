import user.user as user
import product.product as pro
obj = user.User()
if(obj.userLogin()):
    print(" **** user login***")
    obj = pro.Product()
    obj.showproduct()
else:
    print("not login user")
    