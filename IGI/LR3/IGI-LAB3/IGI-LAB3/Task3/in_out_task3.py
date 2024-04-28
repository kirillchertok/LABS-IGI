# -*- coding: cp1251 -*-

# Функция отвечающая за начало программы и ввод/вывод данных
# Дата разработки : 29.03.2024

import random
import string
from Task3.functions_task3 import is_hexadecimal

# Функция генерации строки
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Основная функции
def main_task3():
    print("Программа для выявления является ли строка шестнацатеричным числом\n")
    while True:
        # Ввод строки
        input_string = input("Введите строку: ")
        
        # Вывод результата
        if is_hexadecimal(input_string):
            print("\nВведенная строка является шестнадцатеричным числом.")
        else:
            print("\nВведенная строка не является шестнадцатеричным числом.")
            
        choice = input("\nХотите продолжить (да/нет)? ").lower()
        if choice != "да":
            break