
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
print("4. Update Student")

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

        duplicate = False
        try:
            with open("students.txt", "r") as file:
                for line in file:
                  line=line.strip()
                  if not line:
                     continue
                
                  parts =line.split(",")
                  if len(parts) !=3:
                    continue
                  existing_roll_no =int (parts[1])
                  if existing_roll_no == roll_no:
                    duplicate = True
                    break   
            
        except FileNotFoundError:
            pass

        if duplicate:
            print("Error ❌ Roll number already exists, choose a different number")
        else:
            break

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

# ---------------- UPDATE STUDENT ----------------
elif choice == "4":
    try:
        update_roll = int(input("Enter roll number to update: "))
    except ValueError:
        print("Invalid value  Please choose the numeric value")
        exit()

    found = False
    students = []

    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, roll_no, class_name = line.strip().split(",")
                if int(roll_no) == update_roll:
                    found = True
                    print(f"Current Name: {name}, Class: {class_name}")
                    
                
                    print("1. Name")
                    print("2. Class")
                    print("3. Both")
                    choice_update = input("Choose option (1/2/3): ")

                    if choice_update == "1":
                        new_name = input("Enter new name: ")
                        if new_name == "":
                            new_name = name
                        new_class = class_name

                    elif choice_update == "2":
                        new_class = input("Enter new class: ")
                        if new_class == "":
                            new_class = class_name
                        new_name = name

                    elif choice_update == "3":
                        new_name = input("Enter new name (leave blank to keep same): ")
                        if new_name == "":
                            new_name = name
                        new_class = input("Enter new class (leave blank to keep same): ")
                        if new_class == "":
                            new_class = class_name

                    else:
                        print("Invalid option, keeping old values")
                        new_name = name
                        new_class = class_name

                    students.append(f"{new_name},{roll_no},{new_class}\n")
                else:
                    students.append(line)

        with open("students.txt", "w") as file:
            file.writelines(students)

        if found:
            print("Student successfully updated ")
        else:
            print("Student not found ")

    except FileNotFoundError:
        print("No students file found")

else:
    print("Invalid option")


