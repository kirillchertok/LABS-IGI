# -*- coding: cp1251 -*-

import os
from datetime import datetime
from uu import Error
from Task1.main_task1 import main_task1
from Task2.main_task2 import main_task2
from Task3.main_task3 import main_task3
from Task4.main_task4 import main_task4
from Task5.main_task5 import main_task5


# ������� �������� ����� ������ �������
def input_task(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 5:
                return value
            else:
                print("����� ������ ���� �� 1 �� 5.")
        except ValueError:
            print("����������, ������� ����� �������.")

# �������� ������� ���������
def main():
    while True:
        # ������� ������� �������
        os.system('cls' if os.name == 'nt' else 'clear')

        taskNumber = input_task("������� ����� ������� : ")
        
        # ������� ������� �������
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # ����� ������ �������
        if(taskNumber == 1):
            main_task1()
        elif taskNumber == 2:
            main_task2()
        elif taskNumber == 3:
            main_task3()
        elif taskNumber == 4:
            main_task4()
        elif taskNumber == 5:
            main_task5()
            
        choice = input("\n������ ������� ����� ������� (��/���)? ").lower()
        if choice != "��":
            break   

if __name__ == "__main__":
    main()
