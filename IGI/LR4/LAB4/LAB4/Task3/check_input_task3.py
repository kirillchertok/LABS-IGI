# -*- coding: cp1251 -*-

def input_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if(abs(value) > 1):
                print("������� ����� |x|<1")
            else:    
                return value
        except ValueError:
            print("����������, ������� �����.")

def display_results(x, approx, n, math_val, eps):
    print("-" * 50)
    print("x\t  n\tF(x)\tMath(F(x))\teps")
    print(f"{x}\t {n}\t{approx:.3f}\t{math_val:.3f}\t        {eps}")
    print("-" * 50)
    print("������ �������� :")
    print(f"F(x) - {approx:.10f}\tMath(F(x)) - {math_val:.10f}\n")