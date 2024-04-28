# -*- coding: cp1251 -*-

from Task5.functions_task5 import MatrixOperations

def input_int(prompt):
    while True:
        try:
            value = int(input(prompt)) 
            return value
        except ValueError:
            print("����������, ������� �����.")

def main_task5():
    print("������� � ��������")
    while True:
        n = input_int("���������� ����� �������: ")
        m = input_int("���������� �������� �������: ")
        matrix_ops = MatrixOperations(n, m)
        print("Original Matrix:")
        print(matrix_ops.matrix)

        sorted_matrix = matrix_ops.sort_matrix_by_last_column()
        print("\n���������� ������� �� ���������� ������� (� ������� ��������):")
        print(sorted_matrix)

        mean = matrix_ops.calculate_mean_last_column()
        print("\n������� �������� ���������� ������� (� ������� NumPy):", round(mean, 2))

        mean_manual = matrix_ops.calculate_mean_last_column_manually()
        print("������� �������� ���������� ������� (���������� �������):", round(mean_manual, 2))
        
        choice = input("\n������ ���������� (��/���)? ").lower()
        if choice != "��":
            break