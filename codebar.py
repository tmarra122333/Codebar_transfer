class Member:
    def __init__(self, fullname):                           #Initializing the Class with __init__ (Always self first, then the attribute fullname)
        self.fullname = fullname                            #Use a dot method concept to create fullname 
        
    def member(self):
        print(f"Hello, my name is {self.fullname}")
Thomas = Member("Thomas")
Thomas.member()

# class Student(Member):
#     def __init__()