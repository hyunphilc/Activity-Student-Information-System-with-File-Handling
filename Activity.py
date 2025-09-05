import csv

students = {}

def load_from_file(filename="students.csv"):
    global students
    try:
        with open(filename, mode="r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                student_id, name, age, *grades = row
                students[student_id] = {
                    "name": name,
                    "age": int(age),
                    "grades": list(map(int, grades))
                }
        print("Data loaded from file.")
    except FileNotFoundError:
        print("No data file found. Starting with empty data.")

def save_to_file(filename="students.csv"):
    with open(filename, mode="w", newline='') as file:
        writer = csv.writer(file)
        for student_id, info in students.items():
            writer.writerow([student_id, info["name"], info["age"]] + info["grades"])
    print("Data saved to file.")

def add_student():
    student_id = input("Enter student ID: ")
    if student_id in students:
        print("Student ID already exists.")
        return
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    grades = []
    while True:
        grade = input("Enter grade (or type 'done' to finish): ")
        if grade.lower() == 'done':
            break
        else:
            grades.append(int(grade))
    students[student_id] = {"name": name, "age": age, "grades": grades}
    print("Student added successfully.")


def update_student():
    student_id = input("Enter student ID to update: ")
    if student_id not in students:
        print("Student not found.")
        return
    print("What would you like to update?")
    print("1. Name")
    print("2. Age")
    print("3. Grades")
    choice = input("Enter choice: ")
    if choice == '1':
        students[student_id]['name'] = input("Enter new name: ")
    elif choice == '2':
        students[student_id]['age'] = int(input("Enter new age: "))
    elif choice == '3':
        grades = []
        while True:
            grade = input("Enter grade (or type 'done' to finish): ")
            if grade.lower() == 'done':
                break
            else:
                grades.append(int(grade))
        students[student_id]['grades'] = grades
    else:
        print("Invalid choice.")
        return
    print("Student updated successfully.")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully.")
    else:
        print("Student not found.")

def display_students():
    if not students:
        print("No students found.")
        return
    for student_id, info in students.items():
        print(f"\nStudent ID: {student_id}")
        print(f"Name: {info['name']}")
        print(f"Age: {info['age']}")
        print("Grades: ", ", ".join(map(str, info["grades"])))


def main():
    load_from_file()
    while True:
        print("\n===== Student Information System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            save_to_file()
        elif choice == '6':
            load_from_file()
        elif choice == '7':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()