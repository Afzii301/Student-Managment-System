class student:
    def __init__(self,name,age,rollno,grade,marks):
        self.name=name
        self.age=age
        self.rollno=rollno
        self.grade=grade
        self.marks=marks
        
student=[]
def add_students ():
    name=input("Enter your name")
    age=int("Enter your age")
    rollno=int("Enter you grade")
    grade=input("Enter your grade")
    marks=float("Enter your marks")
    s=student(name,age,rollno,grade,marks)
    student.append(s)
    print("student add")
    