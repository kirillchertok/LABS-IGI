# -*- coding: cp1251 -*-

import csv
import pickle

class Student:
    """
    Represents a student with a name and grades.
    """
    def __init__(self, name, grades):
        """
        Initialize a student with a name and a list of grades.

        :param name: The name of the student.
        :param grades: A list of grades for the student.
        """
        self.name = name
        self.grades = grades

class School:
    """
    Represents a school with a list of students.
    """
    def __init__(self):
        """
        Initialize an empty school.
        """
        self.students = []

    def add_student(self, student):
        """
        Add a student to the school.

        :param student: The student object to add.
        """
        self.students.append(student)

    def calculate_performance(self):
        """
        Calculate the pass percentage and the number of excellent students in the school.

        :return: A tuple containing the pass percentage and the number of excellent students.
        """
        total_students = len(self.students)
        pass_count = 0
        excellent_count = 0
        for student in self.students:
            average_grade = sum(student.grades) / len(student.grades)
            if average_grade >= 8.0:
                excellent_count += 1
            if average_grade >= 5.0:
                pass_count += 1
        pass_percentage = (pass_count / total_students) * 100
        return pass_percentage, excellent_count

    def find_underachievers(self):
        """
        Find the underachieving students in the school.

        :return: A list of underachieving students.
        """
        underachievers = []
        for student in self.students:
            average_grade = sum(student.grades) / len(student.grades)
            if average_grade < 5.0:
                underachievers.append(student)
        return underachievers

    def find_excellent_students(self):
        """
        Find the excellent students in the school.

        :return: A list of excellent students.
        """
        excellent_students = []
        for student in self.students:
            average_grade = sum(student.grades) / len(student.grades)
            if average_grade >= 8.0:
                excellent_students.append(student)
        return excellent_students    

def get_student_inf(student):
        """
        Check student information
        
        param student: student, to check
        return: (average_grade, Неуспевающий) if student is underachiever, (average_grade, Отличник) if student id excellent
        """
        average_grade = sum(student.grades) / len(student.grades)
        if average_grade < 5.0:
                return (average_grade, "Неуспевающий")
        if average_grade >= 8.0:
                return (average_grade, "Отличник")  

def write_csv(filename, school):
    """
    Write the student data to a CSV file.

    :param filename: The name of the CSV file.
    :param school: The school object containing the student data.
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Grades"])
        for student in school.students:
            writer.writerow([student.name, student.grades])

def write_pickle(filename, school):
    """
    Write the student data to a pickle file.

    :param filename: The name of the pickle file.
    :param school: The school object containing the student data.
    """
    with open(filename, 'wb') as file:
        pickle.dump(school.students, file)

def read_pickle(filename):
    """
    Read the student data from a pickle file.

    :param filename: The name of the pickle file.
    :return: A list of student objects.
    """
    with open(filename, 'rb') as file:
        return pickle.load(file)
    
def read_csv(filename):
    """
    Read the student data from a pickle file.

    :param filename: The name of the pickle file.
    :return: A list of student objects.
    """
    with open('data.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = []
        for row in reader:
            data.append(row)