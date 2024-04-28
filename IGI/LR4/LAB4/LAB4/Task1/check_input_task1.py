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
                print("���������� ������� ������ 1 ��� 2")
            else:
                return value
        except ValueError:
            print("���������� ������� ������ 1 ��� 2")
            
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
                    print("������������ ��� �����")
                    continue
                if ' ' in value:
                    print("������������ ��� �����")
                    continue
                return value
        except Error:
            print("������� ���������� ��������")
            
def input_grades():
    while True:
        try:
            elements = input("������� �������� ������ ����� ������ : ").split()
            if len(elements) > 5:
                print("������� ������ 5 �������")
            else:
                grades_list = [int(element) for element in elements]
                return grades_list
        except ValueError:
            print("���������� ������� ������ ������������ �����")
            