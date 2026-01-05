
import os

# ==================== STUDENT CLASS =====================
class Student:
    def __init__(self, name, roll_no, class_name, subjects):
        self.name = name
        self.roll_no = roll_no
        self.class_name = class_name
        self.subjects = subjects  # {subject: marks}

    def save_data(self):
        # tamam subjects ko 1 line me save karna
        subjects_str = ";".join([f"{sub}:{mark}" for sub, mark in self.subjects.items()])
        with open("students.txt", "a") as file:
            file.write(f"{self.name},{self.roll_no},{self.class_name},{subjects_str}\n")


# ===================== MAIN PROGRAM =====================
while True:
    print("\n=== School Management System ===")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Delete Student")
    print("4. Update Student")
    print("5. Sort Students")
    print("6. Exit")

    choice = input("Choose option: ")

    # ---------------- ADD STUDENT ----------------
    if choice == "1":

        # ---- NAME ----
        while True:
            name = input("Student name: ").strip()
            if name and name.replace(" ", "").isalpha():
                break
            print(" Invalid name")

        # ---- ROLL NO (unique) ----
        while True:
            try:
                roll_no = int(input("Roll number: "))
            except ValueError:
                print(" Invalid roll number")
                continue

            duplicate = False
            if os.path.exists("students.txt"):
                with open("students.txt", "r") as file:
                    for line in file:
                        if int(line.split(",")[1]) == roll_no:
                            duplicate = True
                            break

            if duplicate:
                print(" Roll number already exists")
            else:
                break

        # ---- CLASS ----
        class_name = input("Class name: ").strip() or "Unknown"

        # ---- SUBJECTS & MARKS ----
        subjects = {}

        while True:
            subject = input("Subject name (type 'done' to finish): ").strip()

            if subject.lower() == "done":
                break

            if not subject.replace(" ", "").isalpha():
                print(" Invalid subject name")
                continue

            while True:
                marks = input(f"Enter marks for {subject} (0-100): ")
                if marks.isdigit() and 0 <= int(marks) <= 100:
                    subjects[subject] = int(marks)
                    break
                print(" Invalid marks")

        if not subjects:
            print(" No subjects added. Student not saved.")
            continue

        student = Student(name, roll_no, class_name, subjects)
        student.save_data()
        print(" Student added successfully")

    # ---------------- DISPLAY STUDENTS ----------------
    elif choice == "2":
        if not os.path.exists("students.txt"):
            print("No data found")
            continue

       

        with open("students.txt", "r") as file:
            for line in file:
                name, roll, cls, subs = line.strip().split(",", 3)
            print("\n")
            print(f"Name :{name}")
            print(f"Roll :{roll}")
            print(f"Class :{cls}")
             
            total_marks=0
            subject_count=0
            for s in subs.split(";"):
                sub,marks=s.split(":")
                
                mark=int(marks)
                print(f"{sub}")
                print(f"Mark :{mark}")
                total_marks+=mark
                subject_count+=1

                total_marks+=mark
                subject_count+=1
                
            average=total_marks/subject_count if subject_count>0 else 0
            print(f"Average marks :{average:.2f}")
    # ---------------- DELETE STUDENT ----------------
    elif choice == "3":
        try:
            del_roll = int(input("Enter roll number to delete: "))
        except ValueError:
            print(" Invalid roll number")
            continue

        if not os.path.exists("students.txt"):
            print("No data found")
            continue

        new_lines = []
        found = False

        with open("students.txt", "r") as file:
            for line in file:
                if int(line.split(",")[1]) != del_roll:
                    new_lines.append(line)
                else:
                    found = True

        with open("students.txt", "w") as file:
            file.writelines(new_lines)

        print(" Student deleted" if found else " Student not found")

    # ---------------- UPDATE STUDENT ----------------
    elif choice == "4":
        try:
            up_roll = int(input("Enter roll number to update: "))
        except ValueError:
            print(" Invalid roll number")
            continue

        if not os.path.exists("students.txt"):
            print("No data found")
            continue

        updated = []
        found = False

        with open("students.txt", "r") as file:
            for line in file:
                name, roll, cls, subs = line.strip().split(",", 3)

                if int(roll) == up_roll:
                    found = True
                    print("Current subjects:", subs)

                    new_name = input("New name (Enter to keep same): ").strip() or name
                    new_class = input("New class (Enter to keep same): ").strip() or cls

                    new_subjects = {}
                    while True:
                        subject = input("New subject (type 'done'): ").strip()
                        if subject.lower() == "done":
                            break
                        marks = input("Marks (0-100): ")
                        if marks.isdigit() and 0 <= int(marks) <= 100:
                            new_subjects[subject] = int(marks)

                    if not new_subjects:
                        # agar new subjects na dein to purane rehne dein
                        updated.append(line)
                    else:
                        subjects_str = ";".join(
                            [f"{s}:{m}" for s, m in new_subjects.items()]
                        )
                        updated.append(f"{new_name},{roll},{new_class},{subjects_str}\n")
                else:
                    updated.append(line)

        with open("students.txt", "w") as file:
            file.writelines(updated)

        print(" Student updated" if found else " Student not found")

    # ---------------- SORT STUDENTS ----------------
    elif choice == "5":
        if not os.path.exists("students.txt"):
            print("No data found")
            continue

        print("1. Sort by Name")
        print("2. Sort by Roll")
        print("3. Sort by Average Marks")
        s_choice = input("Choose: ")

        students = []

        with open("students.txt", "r") as file:
            for line in file:
                name, roll, cls, subs = line.strip().split(",", 3)
                marks = [int(s.split(":")[1]) for s in subs.split(";")]
                avg = sum(marks) / len(marks)
                students.append([name, int(roll), cls, subs, avg])

        if s_choice == "1":
            students.sort(key=lambda x: x[0].lower())
        elif s_choice == "2":
            students.sort(key=lambda x: x[1])
        elif s_choice == "3":
            students.sort(key=lambda x: x[4], reverse=True)
        else:
            print(" Invalid option")
            continue

        print("\nName | Roll | Class | Average")
        print("-" * 40)
        for s in students:
            print(f"{s[0]} | {s[1]} | {s[2]} | {s[4]:.2f}")

    # ---------------- EXIT ----------------
    elif choice == "6":
        print("Goodbye")
        break

    else:
        print(" Invalid option")
