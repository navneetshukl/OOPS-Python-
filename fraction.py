
#! In this class we are creating out own data type of name "Fraction"

class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d

#? All methods starting from "__func__()" is magic function

#! All are magic functions and are very useful to create there own datatype    
    def __str__(self):
        return f"{self.num}/{self.den}"
    
    
    def __add__(self,other):
        temp_num=self.num*other.den+other.num*self.den
        temp_den=self.den*other.den
        return f"{temp_num}/{temp_den}"
    
    def __sub__(self,other):
        temp_num=self.num*other.den-other.num*self.den
        temp_den=self.den*other.den
        return f"{temp_num}/{temp_den}"
    
    def __mul__(self,other):
        temp_num=self.num*other.num
        temp_den=other.den*self.den
        return f"{temp_num}/{temp_den}"
    
    def __truediv__(self,other):
        temp_num=self.num*other.den
        temp_den=other.num*self.den
        return f"{temp_num}/{temp_den}"
    
x=Fraction(3,4)
y=Fraction(5,6)

print(x)

print(y)

print(x+y)    
print(x-y)
print(x*y)
print(x/y)    