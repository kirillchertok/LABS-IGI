# -*- coding: cp1251 -*-

# Функция отвечающая за начало программы и ввод/вывод данных
# Дата разработки : 29.03.2024

from Task2.functions_task2 import count_numbers_above_23

# Основная функции
def main_task2():
    print("Программа для вычисления колличества чисел больше 23 в массиве\n")
    while True:
        # Получение данных
        (number, vector) = count_numbers_above_23()
        
        # Вывод данных
        print(f"\nПолученный массив : {vector}")
        print(f"Колличество чисел : {number}\n")
        
        choice = input("Хотите продолжить (да/нет)? ").lower()
        if choice != "да":
            break