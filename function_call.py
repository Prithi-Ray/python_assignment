# Student Management System

students = {}  # Dictionary to store student records

def add_student(student_id, name, age, grade, email):
    """Add a new student to the system"""
    if student_id in students:
        print("Student ID already exists!")
    else:
        students[student_id] = {"name": name, "age": age, "grade": grade, "email": email}
        print(f"Student '{name}' added successfully!")

def view_students():
    """Display all student records"""
    if not students:
        print("No students available.")
        return
    print("\nStudent Records:")
    print("-" * 60)
    for student_id, details in students.items():
        print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Grade: {details['grade']}, Email: {details['email']}")
    print("-" * 60)

def search_student(query):
    """Search student by ID or Name"""
    found_students = []
    for student_id, details in students.items():
        if query.lower() in details["name"].lower() or query == student_id:
            found_students.append((student_id, details))

    if found_students:
        print("\nSearch Results:")
        print("-" * 60)
        for student_id, details in found_students:
            print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Grade: {details['grade']}, Email: {details['email']}")
        print("-" * 60)
    else:
        print("No student found with that ID or Name.")

def update_student(student_id):
    """Update student details"""
    if student_id in students:
        print("\nEnter new details (leave blank to keep unchanged):")
        new_name = input("New Name: ") or students[student_id]["name"]
        new_age = input("New Age: ") or students[student_id]["age"]
        new_grade = input("New Grade: ") or students[student_id]["grade"]
        new_email = input("New Email: ") or students[student_id]["email"]
        
        students[student_id] = {"name": new_name, "age": new_age, "grade": new_grade, "email": new_email}
        print(f"Student '{new_name}' updated successfully!")
    else:
        print("Student ID not found.")

def delete_student(student_id):
    """Delete a student record"""
    if student_id in students:
        del students[student_id]
        print(f"Student ID {student_id} deleted successfully!")
    else:
        print("Student ID not found.")

def menu():
    """Display the menu and handle user input"""
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            age = input("Enter Age: ")
            grade = input("Enter Grade: ")
            email = input("Enter Email: ")
            add_student(student_id, name, age, grade, email)

        elif choice == "2":
            view_students()

        elif choice == "3":
            query = input("Enter Student ID or Name to search: ")
            search_student(query)

        elif choice == "4":
            student_id = input("Enter Student ID to update: ")
            update_student(student_id)

        elif choice == "5":
            student_id = input("Enter Student ID to delete: ")
            delete_student(student_id)

        elif choice == "6":
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

# Run the Student Management System
menu()