class classname:
    counter =1
    def __init__(self):
        
#! We can access the static variable by using the class name.We can make the static variable unaccessible by using
#! "__" in front of static variable name like __static.variable. We can make getter and setter for accessing the value.
#! We will not pass "self" in getter and setter methods because the static variable will use classname.
        self.serial=classname.counter
        classname.counter=classname.counter+1
        
    def get_counter(self):
        print(self.serial)
        
        
s1=classname()
s1.get_counter()

s2=classname()
s2.get_counter()

s3=classname()
s3.get_counter()
