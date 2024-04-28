# -*- coding: cp1251 -*-

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats

class SomeClass:
    def some_function():
        print("Привет из примеси")

class SequenceAnalyzer(SomeClass):
    def __init__(self, sequence):
        """
        Initializes a SequenceAnalyzer object with a given sequence.

        :param sequence: The input sequence.
        """
        self.sequence = sequence

    def calculate_series(self, x, n):
        """
        Calculates the series expansion of ln(1+x) up to the nth term.

        :param x: The value of x.
        :param n: The number of terms in the series.
        :return: The sum of the series expansion.
        """
        series_sum = 0
        for i in range(1, n + 1):
            series_sum += ((-1) ** (i - 1)) * (x ** i) / i
        return series_sum

    def analyze_sequence(self):
        """
        Analyzes the input sequence and calculates its mean, median, mode, variance, and standard deviation.

        :return: A dictionary containing the analysis results.
        """
        mean = np.mean(self.sequence)
        median = np.median(self.sequence)
        mode = stats.mode(self.sequence).mode
        if isinstance(mode, np.ndarray):
            mode = mode[0]
        variance = np.var(self.sequence)
        std_deviation = np.std(self.sequence)
        return {
            'mean': mean,
            'median': median,
            'mode': mode,
            'variance': variance,
            'standard_deviation': std_deviation
        }

    def plot_series_comparison(self, x_values, series_values, math_values):
        """
        Plots a comparison between the series expansion and the math function.

        :param x_values: The values of x for the plot.
        :param series_values: The values of the series expansion.
        :param math_values: The values of the math function.
        """
        plt.plot(x_values, series_values, label='Series Expansion')
        plt.plot(x_values, math_values, label='Math Function')
        plt.xlabel('x')
        plt.ylabel('ln(1+x)')
        plt.title('Comparison of Series Expansion and Math Function')
        plt.legend()
        plt.grid(True)
        plt.savefig('plot.png')
        plt.show()

    def find_terms_for_accuracy(self, x, target_accuracy):
        """
        Finds the number of terms needed in the series expansion to achieve the specified accuracy.

        :param x: The value of x.
        :param target_accuracy: The target accuracy.
        :return: The number of terms needed.
        """
        series_sum = 0
        n = 0
        while abs(series_sum - math.log1p(x)) > target_accuracy:
            n += 1
            series_sum = self.calculate_series(x, n)
        return n
    
def ln_approximation(x, eps=1e-10, max_iterations=500):
    result = 0
    for n in range(1, max_iterations + 1):
        term = (math.pow(-1,n-1)) * (math.pow(x,n)) / n
        result += term
        if abs(term) < eps:
           break
    return result, n