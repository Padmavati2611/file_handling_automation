students = []

while True:
    print("\nStudent Record System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter age: ")
        course = input("Enter course: ")

        student = {
            "Name": name,
            "Age": age,
            "Course": course
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No records found.")
        else:
            print("\nStudent Records")
            for student in students:
                print(student)

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")