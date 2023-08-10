class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera
        
    def buy(self):
        print("Buying Phone")
        
class Product:
    
    def buy(self):
        print("Product buy method")
        
class SmartPhone(Phone,Product):
    pass

s=SmartPhone(20000,"Apple",12)

s.buy()

#! In the case of conflict of any methods or constructor the inherting class which is named first i.e. in this case
#! "Phone" class is named first.So the Phone class will get priority first
        