class Phone:
    def __init__(self, price,brand,camera):
        print("Inside the phone constructor")
        self.brand = brand
        self.price = price
        self.camera = camera
        
class Smartphone(Phone):
    pass

s=Smartphone(200000,"Apple",13)
print(f"{s.price} {s.brand} {s.camera}")

#? Here when we are creating the object of Smartphone class the Smartphone class has no constructor but it is 
#? inheriting the constructor of parent class that is 'Phone'.This is constructor inheritance.