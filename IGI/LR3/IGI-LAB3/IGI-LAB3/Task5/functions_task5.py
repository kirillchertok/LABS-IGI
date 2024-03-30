# -*- coding: cp1251 -*-

# Дата разработки : 29.03.2024
# Функции для 
# 1)Вычисления количества нечетных отрицательных элементов
# 2)Вычисления суммы элементов списка, расположенных до последнего элемента, равного нулю

# Функция для проверки, является ли число нечетным и отрицательным.
def is_odd_negative(number):
    return number < 0 and number % 2 != 0

# Функция для вычисления количества нечетных отрицательных элементов.
def calculate_odd_negative_count(float_list):
    odd_negative_count = sum(1 for number in float_list if is_odd_negative(number))
    return odd_negative_count

# Функция для вычисления суммы элементов списка до последнего нуля.
def calculate_sum_before_last_zero(float_list):
    sum_before_last_zero = 0
    for number in float_list:
        if number == 0:
            break
        sum_before_last_zero += number
    return sum_before_last_zero