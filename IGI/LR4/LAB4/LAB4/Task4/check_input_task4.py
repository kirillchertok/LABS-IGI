# -*- coding: cp1251 -*-

def check_input_side():
    """
    Prompts the user to enter a number within the range from 3 to 15 (inclusive).

    :return: The input value as an integer if it is a number within the specified range.
    :rtype: int
    """
    while True:
        input_value = input("Введите сторону ромба: ")
        try:
            number = int(input_value)
            if 3 <= number <= 15:
                return number
            else:
                print("Введите число от 3 до 15 для наглядности")
        except ValueError:
            print("Введите число")

def check_input_angle():
    """
    Prompts the user to enter a number within the range from 100 to 170 (inclusive).

    :return: The input value as an integer if it is a number within the specified range.
    :rtype: int
    """
    while True:
        input_value = input("Введите тупой угол: ")
        try:
            number = int(input_value)
            if 100 <= number <= 170:
                return number
            else:
                print("Введите число от 100 до 170")
        except ValueError:
            print("Введите число")

def check_input_color():
    """
    Prompts the user to enter a number within the range from 0 to 255 (inclusive).

    :return: The input value as an integer if it is a number within the specified range.
    :rtype: int
    """
    while True:
        input_value = input("Введите цвет в палитре ANSI escape(0 - 255): ")
        try:
            number = int(input_value)
            if 0 <= number <= 255:
                return number
            else:
                print("Введите число от 0 до 255")
        except ValueError:
            print("Введите число")