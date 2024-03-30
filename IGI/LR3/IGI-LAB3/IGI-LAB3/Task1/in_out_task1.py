# -*- coding: cp1251 -*-

# Функции отвечающая за начало программы и ввод/вывод данных
# Дата разработки : 29.03.2024

import math
from Task1.functions_task1 import ln_approximation

# Функция для проверки ввода на число |x|<1
def input_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if(abs(value) > 1):
                print("Введите число |x|<1")
            else:    
                return value
        except ValueError:
            print("Пожалуйста, введите число.")

# Функция для демонстрации результатов
def display_results(x, approx, n, math_val, eps):
    print("-" * 50)
    print("x\t  n\tF(x)\tMath(F(x))\teps")
    print(f"{x}\t {n}\t{approx:.3f}\t{math_val:.3f}\t        {eps}")
    print("-" * 50)
    print("Полные значения :")
    print(f"F(x) - {approx:.10f}\tMath(F(x)) - {math_val:.10f}\n")

# Функция для старта задания    
def main_task1():
    print("Программа для вычисления значения функции ln(1+x) через ряд Тейлора\n")

    while True:
        x = input_float("Введите значение x: ")
        eps = input_float("Введите точность вычислений (eps): ")

        # Вычисление приближенного значения функции
        approx, n = ln_approximation(x, eps)

        # Вычисление значения функции с помощью модуля math
        math_val = math.log1p(x)

        # Вывод результатов
        display_results(x, approx, n, math_val, eps)

        choice = input("Хотите продолжить (да/нет)? ").lower()
        if choice != "да":
            break