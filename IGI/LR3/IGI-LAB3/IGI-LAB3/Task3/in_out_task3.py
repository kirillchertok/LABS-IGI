# -*- coding: cp1251 -*-

# ������� ���������� �� ������ ��������� � ����/����� ������
# ���� ���������� : 29.03.2024

import random
import string
from Task3.functions_task3 import is_hexadecimal

# ������� ��������� ������
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# �������� �������
def main_task3():
    print("��������� ��� ��������� �������� �� ������ ���������������� ������\n")
    while True:
        # ���� ������
        input_string = input("������� ������: ")
        
        # ����� ����������
        if is_hexadecimal(input_string):
            print("\n��������� ������ �������� ����������������� ������.")
        else:
            print("\n��������� ������ �� �������� ����������������� ������.")
            
        choice = input("\n������ ���������� (��/���)? ").lower()
        if choice != "��":
            break