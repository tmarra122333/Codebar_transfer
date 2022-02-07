from ast import BinOp


class Member:
    def __init__(self, fullname):                           #Initializing the Class with __init__ (Always self first, then the attribute fullname)
        self.fullname = fullname                            #Use a dot method concept to create fullname 
        
    def member(self):
        print(f"Hello, my name is {self.fullname}")

# Thomas = Member("Thomas")
# Thomas.member()
# Jen = Member("Jen")
# Jen.member()
class Student(Member):                                     #New student class is accessing member class through parameter () with super().
    def __init__(self, fullname, reason):                  #Initializing class again new parameter of reason
        super().__init__(fullname)                         #Essentialy unlocks the self.fullname from Member class
        self.reason = reason                               #Dot method again to crease reason

class Instructor(Member):
    def __init__(self, fullname, bio,):
        super().__init__(fullname)
        self.bio = bio
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

class Workshop():
    def __init__(self, date, subject,):
        self.date = date
        self.subject = subject
        self.instructor = []
        self.students = []
    def add_participant(self, member):
        if (type(member).__name__) == "Instructor":
            self.instructor.append(member)
        elif (type(member).__name__) == "Student":
            self.students.append(member)
        else:
            print('member does not exist')

    def print_details(self):
        print(f"Workshop details: {self.date}, {self.subject}")
        for i, student in enumerate(self.students):
            print(f"{i + 1}. {student.fullname} - {student.reason}")
        for i, instructor in enumerate(self.instructor):
            print(f"{i + 1}. {instructor.fullname} - {instructor.bio} - {instructor.skills}")

workshop = Workshop("12/03/2014", "Shutl")
jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")


workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()
