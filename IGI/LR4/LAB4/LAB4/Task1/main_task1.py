# -*- coding: cp1251 -*-

from Task1.functions_task1 import School, Student, write_csv, write_pickle, get_student_inf
from Task1.check_input_task1 import input_datasave_type, input_filename, input_grades

def print_school_data(school):
    """
    Print information about school
    
    param school : school which information you want to see
    """
    pass_percentage, excellent_count = school.calculate_performance()
    print("������� �������� ������������ : ", pass_percentage)
    print("���������� ���������� : ", excellent_count)

    # Find underachievers and excellent students
    underachievers = school.find_underachievers()
    print("\n������������ : ")
    for student in underachievers:
        print(student.name)
            
    excellent_students = school.find_excellent_students()
    print("\n��������� : ")
    for student in excellent_students:
        print(student.name)


def main_task1():
    """
    The main function of task1.
    """
    print("������� 1: ��������� ������ � ����")
    
    school = School()
    
    """
    default_csv - default filename for csv format
    default_pickle - default filename for pickle format
    """
    default_csv = "school_data.csv"
    default_pickle = "school_data.pkl"
    
    """
    student(1-3) - default students data
    """
    student1 = Student("Pasha", [3, 5, 4, 4, 2])
    student2 = Student("Kirill", [9, 9, 8, 10, 8])
    student3 = Student("Arthur", [6, 7, 10, 9, 8])
    
    school.add_student(student1)
    school.add_student(student2)
    school.add_student(student3)

    while True:
        
        type = input_datasave_type("�������, ����� �������� �� ������ �������� � ���� CSV-1/pickle-2 ")
        filename = input_filename("�������, ��� ����� ��� ��������� '/', ����� ��� ����� ���� ��������� ")
        
        if (filename == 0):
            if (type == 1):
               filename = default_csv
            else:
                filename = default_pickle
                
        if (type == 1):
            write_csv(filename, school)
        else:
            write_pickle(filename, school)
        
        print_school_data(school)
            
        print("\n������� ������ ���������")
        name = input("������� ��� : ")
        grades = input_grades()
        
        newStudent = Student(name, grades)
        school.add_student(newStudent)
        
        (average, status) = get_student_inf(newStudent)
        print(f"\n������ {name}")
        print(f"������� ���� : {average}")
        print(f"������ : {status}\n")
        
        print_school_data(school)
        if (type == 1):
            write_csv(filename, school)
        else:
            write_pickle(filename, school)
                    
        choice = input("������ ���������� (��/���)? ").lower()
        if choice != "��":
            break


        