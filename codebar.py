from ast import BinOp


class Member:
    def __init__(self, fullname):                           #Initializing the Class with __init__ (Always self first, then the attribute fullname)
        self.fullname = fullname                            #Use a dot method concept to create fullname 
        
    def member(self):
        print(f"Hello, my name is {self.fullname}")

Thomas = Member("Thomas")
Thomas.member()
Jen = Member("Jen")
Jen.member()
class Student(Member):                                     #New student class is accessing member class through parameter () with super().
    def __init__(self, fullname, reason):                  #Initializing class again new parameter of reason
        super().__init__(fullname)                         #Essentialy unlocks the self.fullname from Member class
        self.reason = reason                               #Dot method again to crease reason

class Instructor(Member):
    def __init__(self, fullname, bio, skills):
        super().__init__(fullname)
        self.bio = bio
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

class Workshop():
    def __init__(self, date, subject, instructor = [], students = []):
        self.date = date
        self.subject = subject
        self.instructor = instructor
        self.students = students
    
    def add_participant(self, member):
        if (type(member).__name__) == "Instructor":
            self.instructor.append(member)
        elif (type(member).__name__) == "Student":
            self.students.append(member)
            