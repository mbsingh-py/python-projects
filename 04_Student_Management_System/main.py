file = "data.txt"

# Extracting raw data from file and process to use
try:
    with open(file, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    lines = []

students = []

for line in lines:
    parts = line.strip().split(",")

    if len(parts) != 3:
        continue

    roll, name, marks = parts

    students.append({
        "roll": int(roll),
        "name": name,
        "marks": int(float(marks))
    })


# Functions
def num_validation(datatype, name):  # Number validation
    while True:
        try:
            value = datatype(input(f"Enter {name}: "))
            return value
        except ValueError:
            print("Enter only numbers allowed!")


def name_validation():  # Name validation
    while True:
        name = input("Enter name: ").strip()
        clean_name = name.replace(" ", "")
        if clean_name == "":
            print("Empty name is not allowed!")
        elif clean_name.isalpha():
            name = " ".join(name.split()).title()
            break
        else:
            print("Only alphabets and spaces are allowed!")
    return name


def show_data(data_list):
    if not data_list:
        print("No data available!\n")
        return

    print(f"{'Roll no.':<10} {'Name':<20} {'Marks':<5}")
    for i in data_list:
        print(f"{i['roll']:<10} {i['name']:<20} {i['marks']:<5}")
    print()


def search_by(type, value):
    data = []
    for i in students:
        if type == "marks":
            if i[type] == value:
                data.append(i)
        else:
            if str(i[type]).lower() == str(value).lower():
                data.append(i)
    return data


def save_to_file():
    with open(file, "w") as f:
        for s in students:
            f.write(f"{s['roll']},{s['name']},{s['marks']}\n")


def add_student():
    print("\n• Enter roll no. '0' to go back\n")

    while True:
        roll = num_validation(int, "roll no.")

        if roll == 0:
            break
        elif roll < 0:
            print("Negative input not allowed!")
            continue

        if search_by("roll", roll):
            print("Student already exists!")
            show_data(search_by("roll", roll))
            continue

        name = name_validation()

        while True:
            marks = num_validation(int, "marks")
            if marks < 0:
                print("Negative marks not allowed!")
            else:
                break

        students.append({
            "roll": roll,
            "name": name,
            "marks": marks
        })

        save_to_file()
        print("Student added successfully!\n")


def search_student():
    print("""
1. Search by Roll
2. Search by Name
3. Search by Marks
4. Back
""")

    while True:
        choice = num_validation(int, "choice")

        if choice == 1:
            roll = num_validation(int, "roll")
            data = search_by("roll", roll)

        elif choice == 2:
            name = name_validation()
            data = search_by("name", name)

        elif choice == 3:
            marks = num_validation(int, "marks")
            data = search_by("marks", marks)

        elif choice == 4:
            break

        else:
            print("Please enter a valid choice!")
            continue

        if data:
            show_data(data)
        else:
            print("Student not found!\n")


def update():
    while True:
        roll = num_validation(int, "roll")

        if roll == 0:
            return
        elif roll < 0:
            print("Enter valid roll no.")
        else:
            break

    while True:
        marks = num_validation(int, "marks")

        if marks < 0:
            print("Enter valid marks")
        else:
            break

    found = False

    for i in students:
        if i["roll"] == roll:
            i["marks"] = marks
            found = True
            break

    if found:
        save_to_file()
        print("Marks updated\n")
    else:
        print("Student not found\n")


def delete():
    while True:
        roll = num_validation(int, "roll")

        if roll == 0:
            return
        elif roll < 0:
            print("Enter valid roll no.")
        else:
            break

    found = False

    for idx, i in enumerate(students):
        if i["roll"] == roll:
            show_data([i])

            while True:
                confirm = input("Are you sure? (y/n): ").strip().lower()

                if confirm == "y":
                    break
                elif confirm == "n":
                    print("Delete cancelled\n")
                    return
                else:
                    print("Enter only 'y' or 'n'")

            del students[idx]
            found = True
            break

    if found:
        save_to_file()
        print("Deleted successfully\n")
    else:
        print("Student not found\n")


# Main Menu
while True:
    print("""
    1. Add Student
    2. View Students
    3. Search Student
    4. Update Student
    5. Delete Student
    6. Exit
    """)

    num = num_validation(int, "your choice")

    if num == 1:
        add_student()

    elif num == 2:
        show_data(students)

    elif num == 3:
        search_student()

    elif num == 4:
        update()

    elif num == 5:
        delete()

    elif num == 6:
        print("Program ends\nHave a nice day!")
        break

    else:
        print("Invalid choice\n")
