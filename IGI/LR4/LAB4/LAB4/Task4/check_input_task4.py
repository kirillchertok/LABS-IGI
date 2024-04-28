# -*- coding: cp1251 -*-

def check_input_side():
    """
    Prompts the user to enter a number within the range from 3 to 15 (inclusive).

    :return: The input value as an integer if it is a number within the specified range.
    :rtype: int
    """
    while True:
        input_value = input("������� ������� �����: ")
        try:
            number = int(input_value)
            if 3 <= number <= 15:
                return number
            else:
                print("������� ����� �� 3 �� 15 ��� �����������")
        except ValueError:
            print("������� �����")

def check_input_angle():
    """
    Prompts the user to enter a number within the range from 100 to 170 (inclusive).

    :return: The input value as an integer if it is a number within the specified range.
    :rtype: int
    """
    while True:
        input_value = input("������� ����� ����: ")
        try:
            number = int(input_value)
            if 100 <= number <= 170:
                return number
            else:
                print("������� ����� �� 100 �� 170")
        except ValueError:
            print("������� �����")

def check_input_color():
    """
    Prompts the user to enter a number within the range from 0 to 255 (inclusive).

    :return: The input value as an integer if it is a number within the specified range.
    :rtype: int
    """
    while True:
        input_value = input("������� ���� � ������� ANSI escape(0 - 255): ")
        try:
            number = int(input_value)
            if 0 <= number <= 255:
                return number
            else:
                print("������� ����� �� 0 �� 255")
        except ValueError:
            print("������� �����")