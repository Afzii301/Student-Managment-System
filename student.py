class Student:
    def __init__(self, name, roll_no, class_name):
        self.name = name
        self.roll_no = roll_no
        self.class_name = class_name

    def save_data(self):
        # student ka data file me save hoga
        with open("students.txt", "a") as file:
            file.write(f"{self.name},{self.roll_no},{self.class_name}\n")


print("=== School Management System ===")
print("1. Add Student")

choice = input("choose the option: ")

if choice == "1":
    name = input("Student name : ")

    # roll number validation (loop ke sath)
    while True:
        try:
            roll_no = int(input("student roll number: "))
            break   # sahi value mil gayi
        except ValueError:
            print("Invalid value  Please choose the numeric value")

    class_name = input("student class: ")

    student = Student(name, roll_no, class_name)
    student.save_data()

    print("Student successfully add ")
else:
    print("Invalid option")
