
from data import student_grads as  student_infos
# print("Student Graduation:", student_infos)

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

def print_highest_score_student() -> None:
    """
    This function finds the student with the highest score and prints their information.
    """
    highest_score = 0
    highest_scoring_student = None
    for student_info in student_infos:
        student_scores = student_info[3]
        total_score = sum(student_scores)
    if total_score > highest_score:
        highest_score = total_score
        highest_scoring_student = student_info

    if highest_scoring_student:
        print("Student with the highest score:")
        table_header()
        table_record(highest_scoring_student)
    else:
        print("No student data found.")
print_all_student()

def add_new_student() -> None:
  """
  This function prompts the user for new student information and adds it to the student data.
  """
  new_student_id = get_student_id()
  new_student_name = get_student_name()
  new_student_gender = get_student_gender()
  new_student_scores = get_student_scores()
  student_infos.append((new_student_id, new_student_name, new_student_gender, new_student_scores))
print("New student information added successfully!")

def get_student_id() -> int:
  pass
def get_student_name() -> str:
  pass
def get_student_gender() -> bool:
  pass
def get_student_scores() -> tuple:
  pass


def modify_student_score() -> None:
  """
  This function allows modifying an existing student's score.
  """
  student_id = get_student_id_to_modify()
  student_index = find_student_by_id(student_id)
  if student_index is not None:
    new_student_scores = get_student_scores()
    student_infos[student_index] = (student_infos[student_index][0], student_infos[student_index][1], student_infos[student_index][2], new_student_scores)
    print("Student score modified successfully!")
  else:
    print("Student with ID", student_id, "not found.")


def get_student_id_to_modify() -> int:
    pass
def find_student_by_id(student_id: int) -> int:
  """
  This function searches for a student with the given ID and returns the index in the student_infos list, or None if not found.
  """
  for index, student_info in enumerate(student_infos):
    if student_info[0] == student_id:
      return index
  return None
def get_student_scores() -> tuple:
    pass



def count_female_and_male_students() -> None:
  """
  This function counts the number of female and male students and displays the results.
  """
  female_count = 0
  male_count = 0
  for student_info in student_infos:
    is_male = student_info[2]  
    if is_male:
      male_count += 1
    else:
      female_count += 1

  print("Number of Female Students:", female_count)
  print("Number of Male Students:", male_count)







