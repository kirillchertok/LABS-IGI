# -*- coding: cp1251 -*-

# ������� ���������� �� ������ ��������� � ����/����� ������
# ���� ���������� : 29.03.2024

import math
from Task1.functions_task1 import ln_approximation

# ������� ��� �������� ����� �� ����� |x|<1
def input_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if(abs(value) > 1):
                print("������� ����� |x|<1")
            else:    
                return value
        except ValueError:
            print("����������, ������� �����.")

# ������� ��� ������������ �����������
def display_results(x, approx, n, math_val, eps):
    print("-" * 50)
    print("x\t  n\tF(x)\tMath(F(x))\teps")
    print(f"{x}\t {n}\t{approx:.3f}\t{math_val:.3f}\t        {eps}")
    print("-" * 50)
    print("������ �������� :")
    print(f"F(x) - {approx:.10f}\tMath(F(x)) - {math_val:.10f}\n")

# ������� ��� ������ �������    
def main_task1():
    print("��������� ��� ���������� �������� ������� ln(1+x) ����� ��� �������\n")

    while True:
        x = input_float("������� �������� x: ")
        eps = input_float("������� �������� ���������� (eps): ")

        # ���������� ������������� �������� �������
        approx, n = ln_approximation(x, eps)

        # ���������� �������� ������� � ������� ������ math
        math_val = math.log1p(x)

        # ����� �����������
        display_results(x, approx, n, math_val, eps)

        choice = input("������ ���������� (��/���)? ").lower()
        if choice != "��":
            break