# -*- coding: cp1251 -*-

from Task5.functions_task5 import MatrixOperations

def input_int(prompt):
    while True:
        try:
            value = int(input(prompt)) 
            return value
        except ValueError:
            print("Пожалуйста, введите число.")

def main_task5():
    print("Задание с матрицей")
    while True:
        n = input_int("Количество строк матрицы: ")
        m = input_int("Количество столбцов матрицы: ")
        matrix_ops = MatrixOperations(n, m)
        print("Original Matrix:")
        print(matrix_ops.matrix)

        sorted_matrix = matrix_ops.sort_matrix_by_last_column()
        print("\nСортировка матрицы по последнему столбцу (в порядке убывания):")
        print(sorted_matrix)

        mean = matrix_ops.calculate_mean_last_column()
        print("\nСреднее значение последнего столбца (с помощью NumPy):", round(mean, 2))

        mean_manual = matrix_ops.calculate_mean_last_column_manually()
        print("Среднее значение последнего столбца (рассчитано вручную):", round(mean_manual, 2))
        
        choice = input("\nХотите продолжить (да/нет)? ").lower()
        if choice != "да":
            break