# -*- coding: cp1251 -*-

# ������� ���������� �� ������ ��������� � ����/����� ������, � ����� ��������
# ���� ���������� : 29.03.2024

import random
from Task5.functions_task5 import calculate_odd_negative_count,calculate_sum_before_last_zero

# ������� �������� �� ����
def input_float_list():
    while True:
        try:
            elements = input("������� �������� ������ ����� ������ : ").split()
            float_list = [float(element) for element in elements]
            return float_list
        except ValueError:
            print("���������� ������� ������ ������������ �����")
            
# ������� ��������� �������
def generate(length, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(length)]            

# �������� ������� ���������            
def main_task5():
    print("��������� ��� ��������� ������������ �������\n")
    while True:
        # ���� ������
        float_list = input_float_list()
        
        # ��������� ��������
        odd_negative_count = calculate_odd_negative_count(float_list)
        sum_before_last_zero = calculate_sum_before_last_zero(float_list)
        
        # ����� ���������� ��������
        print(f"\n���������� �������� ������������� ��������� : {odd_negative_count}")
        print(f"����� ��������� �� ���������� ���� : {sum_before_last_zero}")
        
        choice = input("\n������ ���������� (��/���)? ").lower()
        if choice != "��":
            break