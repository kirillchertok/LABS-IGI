# -*- coding: cp1251 -*-

# ���� ���������� : 29.03.2024
# ������� ��� ���������� ����������� ����� ������ 23 � ��������

def count_numbers_above_23():
    vector = []
    count = 0
    while True:
        try:
            number = int(input("������� ����� �����: "))
            if number == 15:
                print("���� ���������")
                break  # ���������� ���� ��� ���������� ����� 15
            if number > 23:
                vector.append(number)
                count += 1
        except ValueError:
            print("������! ������� ����� �����.")
    return count,vector