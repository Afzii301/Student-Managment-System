import os
class Student:
    def __init__(self, name, roll_no, class_name):
        self.name = name
        self.roll_no = roll_no
        self.class_name = class_name

    def save_data(self):
        with open("students.txt", "a") as file:
            file.write(f"{self.name},{self.roll_no},{self.class_name}\n")


while True:
    print("\n=== School Management System ===")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Delete Student") 
    print("4. Update Student")
    print("5. Sort Students")
    print("6. Exit")
    choice = input("Choose the option: ")

    # ---------------- ADD STUDENT ----------------
    if choice == "1":
        # NAME
        while True:
            name = input("Student name: ").strip()
            if not name:
                print("Name cannot be empty")
                continue
            if not name.replace(" ", "").isalpha():
                print("Invalid name. Only alphabets allowed")
                continue
            break

        # ROLL NUMBER
        while True:
            try:
                roll_no = int(input("Student roll number: "))
            except ValueError:
                print("Invalid value. Enter numeric value")
                continue

            duplicate = False
            try:
                with open("students.txt", "r") as file:
                    for line in file:
                        parts = line.strip().split(",")
                        if len(parts) == 3 and int(parts[1]) == roll_no:
                            duplicate = True
                            break
            except FileNotFoundError:
                pass

            if duplicate:
                print("Roll number already exists. Choose a different number")
            else:
                break

        # CLASS NAME
        class_name = input("Student class: ").strip() or "N/A"

        # SAVE
        student = Student(name, roll_no, class_name)
        student.save_data()
        print("Student successfully added")

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
            print("Invalid value. Enter numeric value")
            continue

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
                print("Student successfully deleted")
            else:
                print("Student not found")
        except FileNotFoundError:
            print("No students file found")

    # ---------------- UPDATE STUDENT ----------------
    elif choice == "4":
        try:
            update_roll = int(input("Enter roll number to update: "))
        except ValueError:
            print("Invalid value. Enter numeric value")
            continue

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
                            new_name = input("Enter new name: ") or name
                            new_class = class_name
                        elif choice_update == "2":
                            new_class = input("Enter new class: ") or class_name
                            new_name = name
                        elif choice_update == "3":
                            new_name = input("Enter new name (leave blank to keep same): ") or name
                            new_class = input("Enter new class (leave blank to keep same): ") or class_name
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
                print("Student successfully updated")
            else:
                print("Student not found")
        except FileNotFoundError:
            print("No students file found")

    # ---------------- SORT STUDENTS ----------------
    elif choice == "5":
        print("\n--- Sort Students ---")
        print("1. Sort by Name")
        print("2. Sort by Roll Number")
        sort_choice = input("Choose sorting option: ")

        students = []

        try:
            with open("students.txt", "r") as file:
                for line in file:
                    name, roll_no, class_name = line.strip().split(",")
                    students.append([name, int(roll_no), class_name])

            if sort_choice == "1":
                students.sort(key=lambda x: x[0].lower())
                print("\n--- Sorted by Name ---")
            elif sort_choice == "2":
                students.sort(key=lambda x: x[1])
                print("\n--- Sorted by Roll Number ---")
            else:
                print("Invalid option")
                continue

            print("\nName\tRoll No\tClass")
            print("-" * 30)
            for s in students:
                print(f"{s[0]}\t{s[1]}\t{s[2]}")
        except FileNotFoundError:
            print("No students file found")

    # ---------------- EXIT ----------------
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid option")
