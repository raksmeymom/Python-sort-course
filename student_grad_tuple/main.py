from utility.until import *
import os

def main():
    os.system("cls")
    while True:
        show_menu()
        choice = int(input("Enter Your choise:"))
        if choice == 1:
            print_all_student()
        elif choice == 2:
            find_max_score()
        elif choice == 3:
            add_new_student()
        elif choice == 4:
            modify_student_score()
        elif choice == 5:
            males,females = count_male_female_student()
            print("=====| Count Male and Female student |=====")
            # print(f"Total Male student: {total_student[0]}")
            # print(f"Total Female student: {total_student[1]} ")

            print(f"Total Male student: {males}")
            print(f"Total Female student: {females} ")
        elif choice == 0:
            print("Exit the program")
            break
          
        else:
            print("Invalid choice")
if __name__ == "__main__" :
    main()




