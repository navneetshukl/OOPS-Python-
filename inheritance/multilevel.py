class Product:
    def review(self):
        print("Product customer review")
        
class Phone(Product):
    def __init__(self,price,brand,camera):
        print("Inside the Phone's Constructor")
        self.__price = price
        self.brand= brand 
        self.camera = camera  
        
    def buy(self):
        print('Phone is being bought')
        
class SmartPhone(Phone):
    pass


s=SmartPhone(20000,"Apple",12)
p=Phone(10000,"Samsung",1)
s.buy()
s.review()
p.review()