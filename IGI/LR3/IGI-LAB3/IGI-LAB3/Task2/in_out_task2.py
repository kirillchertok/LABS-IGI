# -*- coding: cp1251 -*-

# ������� ���������� �� ������ ��������� � ����/����� ������
# ���� ���������� : 29.03.2024

from Task2.functions_task2 import count_numbers_above_23

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