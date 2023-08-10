class Phone:
    def __init__(self, price,brand,camera):
        self.__price = price
        self.brand= brand
        self.camera = camera
        
    def buy(self):
        print("Buying the Phone")
        
    def return_phone(self):
        print('Returning phone')
        

class SmartPhone(Phone):
    pass

SmartPhone(1000,"Apple","13px").buy()