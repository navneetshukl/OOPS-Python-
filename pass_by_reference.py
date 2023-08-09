class Customer:
    def __init__(self, name):
        self.name=name
        
 
def greet(customer):
    print(id(customer))
    customer.name="Yatinjal"
    print(customer.name)
    print(id(customer))  
         
#! Address we get from both the code will be same
cust=Customer("Navneet")
print(id(cust))

greet(cust)

print(cust.name)

#* After changing the name will change from Navneet to Yatinjal and the address will remain the same in all case.
#* This shows that objects in python are mutable. 