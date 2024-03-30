# -*- coding: cp1251 -*-

# ���� ���������� : 29.03.2024
# ������� ��� 
# 1)���������� ���������� �������� ������������� ���������
# 2)���������� ����� ��������� ������, ������������� �� ���������� ��������, ������� ����

# ������� ��� ��������, �������� �� ����� �������� � �������������.
def is_odd_negative(number):
    return number < 0 and number % 2 != 0

# ������� ��� ���������� ���������� �������� ������������� ���������.
def calculate_odd_negative_count(float_list):
    odd_negative_count = sum(1 for number in float_list if is_odd_negative(number))
    return odd_negative_count

# ������� ��� ���������� ����� ��������� ������ �� ���������� ����.
def calculate_sum_before_last_zero(float_list):
    sum_before_last_zero = 0
    for number in float_list:
        if number == 0:
            break
        sum_before_last_zero += number
    return sum_before_last_zero