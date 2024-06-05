
from data import student_grads as  student_infos
print("Student Graduation:", student_infos)

def show_menu()-> None: 
    """
    This function is used to print the menu
    =====|Menu|=====
    1.Print all student
    2.Print student with highest score
    3.Add new student information
    4.Modify student score
    5.Count female and male student
    0.Exting
    """
    print("=====|Menu|=====")
    print("1.Print all student")
    print("2.Print student with highest score")
    print("3.Add new student information")
    print("4.Modify student score")
    print("5.Count female and male student")
    print("0.Exting")

def table_header()-> None:
    id = "ID"
    name = "Name"
    gender = "Gender"
    math = "Math"
    physic = "physic"
    chemistry = "chemistry"
    total = "total"
    avg = "avg"
    print(f"{id:<10} {name:<25} {gender:<15} {chemistry:<10} {total:<10} {avg:<10}")

def table_record(student_info: tuple)-> None:
    id = student_info[0]
    name = student_info[1]
    isMale = "M" if student_info[2]  else "F"
    student_scores = student_info[3]
    math = student_scores[0]
    physic = student_scores[1]
    chemistry = student_scores[2]
    total =sum(student_scores) 
    avg = total /len(student_scores) 
    print(f"{id:<10} {name:<25} {isMale:<15} {math:<10} {physic:<10} {chemistry:<10} {total:<10} {avg:<10.2f}")

def print_all_student() -> None:
    table_header()
    for student_info in student_infos:
        table_record(student_info)
print_all_student()

def find_max_score() -> None:
    max_score = 0
    max_student_info = None
    for student_info in student_infos:
        total_score = sum(student_info[3])
        if total_score > max_score:
            max_score = total_score
            max_student_info = student_info

    if max_student_info:
        print("Student with the highest score:")
        table_header()
        table_record(max_student_info)
    else:
        print("No student information found.")

def add_new_student_info() -> None:
  
  """
  This function allows the user to add new student information.
  """
  id = input("Enter student ID: ")
  name = input("Enter student name: ")
  gender = input("Enter student gender (M/F): ").upper()
  math = float(input("Enter math score: "))
  physic = float(input("Enter physic score: "))
  chemistry = float(input("Enter chemistry score: "))
  new_student_info = (len(student_infos) + 1, name, gender == "M", (math, physic, chemistry))
  student_infos.append(new_student_info)  
  print("Student information added successfully!")


def modify_student_score() -> None:
    """
    This function allows the user to modify a student's scores.
    """
    student_id = input("Enter student ID whose score you want to modify: ")
    for student_info in student_infos:
        if student_info[0] == student_id:
            math = float(input("Enter new math score: "))
            physic = float(input("Enter new physic score: "))
            chemistry = float(input("Enter new chemistry score: "))
            student_info[3] = (math, physic, chemistry)
            print("Student score modified successfully.")
            return
    print("Student ID not found.")


def count_female_male_students() -> None:
    """
    This function counts the number of female and male students.
    """
    female_count = sum(1 for student_info in student_infos if not student_info[2])
    male_count = len(student_infos) - female_count
    print(f"Number of female students: {female_count}")
    print(f"Number of male students: {male_count}")


def menu() -> None:
    """
    This function displays the menu and handles user input.
    """
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            print_all_student()
        elif choice == '2':
            find_max_score()
        elif choice == '3':
            add_new_student_info()
        elif choice == '4':
            modify_student_score()
        elif choice == '5':
            count_female_male_students()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


menu()







