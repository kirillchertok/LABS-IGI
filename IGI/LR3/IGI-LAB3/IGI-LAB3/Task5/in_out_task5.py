# -*- coding: cp1251 -*-

# Функции отвечающая за начало программы и ввод/вывод данных, а также проверку
# Дата разработки : 29.03.2024

import random
from Task5.functions_task5 import calculate_odd_negative_count,calculate_sum_before_last_zero

# Функция проверки на ввод
def input_float_list():
    while True:
        try:
            elements = input("Введите элементы списка через пробел : ").split()
            float_list = [float(element) for element in elements]
            return float_list
        except ValueError:
            print("Пожалуйста вводите только вещественные числа")
            
# Функция генератор массива
def generate(length, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(length)]            

# Основная функция программы            
def main_task5():
    print("Программа для обработки вещественных списков\n")
    while True:
        # Ввод данных
        float_list = input_float_list()
        
        # Получение значение
        odd_negative_count = calculate_odd_negative_count(float_list)
        sum_before_last_zero = calculate_sum_before_last_zero(float_list)
        
        # Вывод полученных значений
        print(f"\nКоличество нечетных отрицательных элементов : {odd_negative_count}")
        print(f"Сумма элементов до последнего нуля : {sum_before_last_zero}")
        
        choice = input("\nХотите продолжить (да/нет)? ").lower()
        if choice != "да":
            break