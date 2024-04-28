# -*- coding: cp1251 -*-

# Функция отвечающая за начало программы и ввод/вывод данных
# Дата разработки : 29.03.2024

import random
from Task2.functions_task2 import count_numbers_above_23

# Функция генератор массива
def generate(length, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(length)]

# Функция генератор 2 версия
def generate_2(limit, min_value, max_value):
    count = 1
    while count <= limit:
        yield count
        count = random.randint(min_value, max_value)
    

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