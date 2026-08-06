FILE_NAME = "records.txt"

try:
    with open(FILE_NAME, "r") as file:
        print("Student Records\n")

        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("File not found.")