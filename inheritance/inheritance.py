class User:
    def login(self):
        print("Login")
        
    def register(self):
        print("Register")
        

class Student(User): #! Here 'Student' class is inheriting 'User' class
    def enroll(self):
        print("Enroll")
        
    def review(self):
        print("Review")
        
stu1=Student()
stu1.enroll()
stu1.review()
stu1.register()
stu1.login()

u=User()
u.login()
u.register()