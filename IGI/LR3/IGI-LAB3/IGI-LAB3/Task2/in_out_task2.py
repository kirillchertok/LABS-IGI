# -*- coding: cp1251 -*-

# ������� ���������� �� ������ ��������� � ����/����� ������
# ���� ���������� : 29.03.2024

import random
from Task2.functions_task2 import count_numbers_above_23

# ������� ��������� �������
def generate(length, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(length)]

# ������� ��������� 2 ������
def generate_2(limit, min_value, max_value):
    count = 1
    while count <= limit:
        yield count
        count = random.randint(min_value, max_value)
    

# �������� �������
def main_task2():
    print("��������� ��� ���������� ����������� ����� ������ 23 � �������\n")
    while True:
        # ��������� ������
        (number, vector) = count_numbers_above_23()
        
        # ����� ������
        print(f"\n���������� ������ : {vector}")
        print(f"����������� ����� : {number}\n")
        
        choice = input("������ ���������� (��/���)? ").lower()
        if choice != "��":
            break