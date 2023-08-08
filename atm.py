class Atm:
    
    #! Constructor
    def __init__(self):
        self.pin=""
        self.balance=0
        
        self.menu()
        
        
    def menu(self):
        user_input=input("""
                         Hello, how would you like to proceed?
                         1.Enter 1 to create pin
                         2.Enter 2 to deposit
                         3.Enter 3 to withdraw
                         4.Enter 4 to check balance
                         5.Enter 5 to exit
                         """)
        if user_input=='1':
            self.create_pin()
            
        elif user_input=='2':
            self.deposit()
            
        elif user_input=='3':
            self.withdraw()
            
        elif user_input=='4':
            self.check_balance()
            
        else:
            print("Bye")
        
    
    def create_pin(self):
        self.pin=input("Enter your Pin")
        print("Pin created Successfully")
        
    def deposit(self):
        temp=input("Enter your pin")
        if temp==self.pin:
            amount=input(int("Enter the amount"))
            self.balance=self.balance+amount
            print("Deposit successful")
        else:
            print("Invalid pin")
            
    def withdraw(self):
        temp=input("Enter your pin")
        if temp==self.pin:
            amount=int(input("Enter the amount"))
            if amount<self.balance:
                self.balance=self.balance-amount
                print("Operation successful")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Pin")
            
    def check_balance(self):
        temp=input("Enter your pin")
        if temp==self.pin:
            print(self.balance)
        else:
            print("Invalid Pin")
            

SBI=Atm()