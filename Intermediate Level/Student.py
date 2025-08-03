students=[]
def add_students():
    name = input("Enter the name: ")
    rollno = int(input("Enter Roll No: "))
    marks = float(input("Enter marks: "))
    students.append([name,rollno,marks])
    print("Student added successfully")

def display_students():
    if not students:
        print("No student record available")
    else:
        print("Student Records: ")
        for student in students:
            print(f"Student: {student[0]}, Roll No: {student[1]}, Marks: {student[2]}" )
        print()

def search_students():
    rollno = int(input("Enter Roll No to search: "))
    found= False
    for student in students:
        if student[1] == rollno:
            print(f"Found: Student:  {student[0]}, Roll No: {student[1]}, Marks: {student[2]}" )
            found= True
            break
    if not found:
        print("Student not found")

while True:
    print("1. Add Students")
    print("2. Display Students")
    print("3. Search Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_students()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_students()
    elif choice == "4":
        print("Existing program...")
        break
    else:
        print("Invalid choice, please try again.\n")

