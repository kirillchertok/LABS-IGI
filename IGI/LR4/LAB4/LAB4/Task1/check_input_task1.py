# -*- coding: cp1251 -*-

from uu import Error
import re


def input_datasave_type(prompt):
    """
    Check is datasave type is correct
    
    param prompt: String to add before input
    return: value, if input is 1 or 2, else start again
    """
    while True:
        try:
            value = int(input(prompt))
            if (value != 1 and value != 2):
                print("Пожалуйста вводите только 1 или 2")
            else:
                return value
        except ValueError:
            print("Пожалуйста вводите только 1 или 2")
            
def input_filename(prompt):
    """
    Check is filename is correct
    
    param prompt: String to add before input
    return: 0, if value is '/' , value if value is not '/' and it is filename
    """
    while True:
        try:
            value = input(prompt)
            if (value == '/'):
                return 0
            else:
                if re.search(r'[\\/:"*?<>|]', value):
                    print("Неккоректное имя файла")
                    continue
                if ' ' in value:
                    print("Неккоректное имя файла")
                    continue
                return value
        except Error:
            print("Введите корректные значения")
            
def input_grades():
    while True:
        try:
            elements = input("Введите элементы списка через пробел : ").split()
            if len(elements) > 5:
                print("Введите только 5 отметок")
            else:
                grades_list = [int(element) for element in elements]
                return grades_list
        except ValueError:
            print("Пожалуйста вводите только вещественные числа")
            