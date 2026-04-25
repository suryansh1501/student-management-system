students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    students.append({"name": name, "roll": roll})
    print("Student added successfully!")

def show_students():
    if not students:
        print("No students found")
    else:
        for s in students:
            print(f"Name: {s['name']}, Roll: {s['roll']}")

def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s["roll"] == roll:
            print(f"Found: {s['name']}")
            return
    print("Student not found")

def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!")
            return
    print("Student not found")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again!")