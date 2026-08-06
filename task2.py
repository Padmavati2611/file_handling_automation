FILE_NAME = "records.txt"

while True:
    print("\nStudent Record System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        age = input("Age: ")
        course = input("Course: ")

        with open(FILE_NAME, "a") as file:
            file.write(f"{name},{age},{course}\n")

        print("Record saved successfully!")

    elif choice == "2":
        try:
            with open(FILE_NAME, "r") as file:
                records = file.readlines()

                if len(records) == 0:
                    print("No records found.")

                else:
                    print("\nStudent Records")
                    for record in records:
                        name, age, course = record.strip().split(",")
                        print(f"Name : {name}")
                        print(f"Age : {age}")
                        print(f"Course : {course}")
                        print("-----------------------")

        except FileNotFoundError:
            print("records.txt not found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")