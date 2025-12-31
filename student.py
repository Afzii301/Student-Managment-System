
class Student:
    def __init__(self, name, roll_no, class_name):
        self.name = name
        self.roll_no = roll_no
        self.class_name = class_name

    def save_data(self):
        with open("students.txt", "a") as file:
            file.write(f"{self.name},{self.roll_no},{self.class_name}\n")


print("=== School Management System ===")
print("1. Add Student")
print("2. Display Students")
print("3. Delete Student")

choice = input("choose the option: ")

# ---------------- ADD STUDENT ----------------
if choice == "1":
    name = input("Student name : ")

    # roll number validation + duplicate check
    while True:
        try:
            roll_no = int(input("student roll number: "))
        except ValueError:
            print("Invalid value  Please choose the numeric value")
            continue

        # duplicate check
        duplicate = False
        try:
            with open("students.txt", "r") as file:
                for line in file:
                    _, existing_roll, _ = line.strip().split(",")
                    if int(existing_roll) == roll_no:
                        duplicate = True
                        break
        except FileNotFoundError:
            pass  # file abhi nahi bani, ok

        if duplicate:
            print("Error: Roll number already exists, choose a different  roll number")
        else:
            break  # valid aur unique roll number

    class_name = input("student class: ")

    student = Student(name, roll_no, class_name)
    student.save_data()
    print("Student successfully add ")

# ---------------- DISPLAY STUDENTS ----------------
elif choice == "2":
    try:
        with open("students.txt", "r") as file:
            print("\n--- Students List ---")
            for line in file:
                name, roll_no, class_name = line.strip().split(",")
                print(f"Name: {name} | Roll No: {roll_no} | Class: {class_name}")
    except FileNotFoundError:
        print("No students found")

# ---------------- DELETE STUDENT ----------------
elif choice == "3":
    try:
        delete_roll = int(input("Enter roll number to delete: "))
    except ValueError:
        print("Invalid value  Please choose the numeric value")
        exit()

    found = False
    students = []

    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, roll_no, class_name = line.strip().split(",")
                if int(roll_no) != delete_roll:
                    students.append(line)
                else:
                    found = True

        with open("students.txt", "w") as file:
            file.writelines(students)

        if found:
            print("Student successfully deleted ")
        else:
            print("Student not found ")

    except FileNotFoundError:
        print("No students file found")

else:
    print("Invalid option")
