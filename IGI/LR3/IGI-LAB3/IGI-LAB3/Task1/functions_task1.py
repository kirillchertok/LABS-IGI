# -*- coding: cp1251 -*-

# ���� ���������� : 29.03.2024
# ������� ��� ���������� �������� ������� ln(1+x) ����� ��� �������

import math

def ln_approximation(x, eps=1e-10, max_iterations=500):
    result = 0
    for n in range(1, max_iterations + 1):
        term = (math.pow(-1,n-1)) * (math.pow(x,n)) / n
        result += term
        if abs(term) < eps:
            break
    return result, n