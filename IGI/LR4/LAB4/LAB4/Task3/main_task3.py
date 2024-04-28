# -*- coding: cp1251 -*-

import math
import numpy as np
from Task3.check_input_task3 import input_float, display_results
from Task3.functions_task3 import SequenceAnalyzer, ln_approximation
  
def main_task3():
    print("Программа для вычисления значения функции ln(1+x) через ряд Тейлора\n")
    x_values = np.linspace(-0.9, 0.9, 100)

    # Create an instance of SequenceAnalyzer class
    sequence_analyzer = SequenceAnalyzer(x_values)

    # Construct a graph comparing a series and a mathematical function
    series_values = [sequence_analyzer.calculate_series(x, 10) for x in x_values]
    math_values = [np.log1p(x) for x in x_values]
    sequence_analyzer.plot_series_comparison(x_values, series_values, math_values)

    # Analyze the sequence
    analysis_results = sequence_analyzer.analyze_sequence()

    # Output the analysis results to the console
    print("Mean:", analysis_results['mean'])
    print("Median:", analysis_results['median'])
    print("Mode:", analysis_results['mode'])
    print("Variance:", analysis_results['variance'])
    print("Standard Deviation:", analysis_results['standard_deviation'])
    
    while True:
        x = input_float("Введите значение x: ")
        eps = input_float("Введите точность вычислений (eps): ")

        # Calculating the approximate value of a function
        approx, n = ln_approximation(x, eps)

        # Calculating the value of a function using the module math
        math_val = math.log1p(x)

        # Results output
        display_results(x, approx, n, math_val, eps)

        choice = input("Хотите ввести новое значение x (да/нет)? ").lower()
        if choice != "да":
            break
