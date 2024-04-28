# -*- coding: cp1251 -*-

from Task4.functions_task4 import Rhombus
from Task4.check_input_task4 import check_input_angle, check_input_color, check_input_side

def main_task4():
    print("Программма по вычислению площади ромба и его отрисовки")
    while True:
        side = check_input_side()
        angle = check_input_angle()
        color = input("Введите цвет: ")

        rhombus = Rhombus(side, angle, color)
        print("Площадь ромба:", rhombus.calculate_area())
        print(rhombus)
        print("Фигура:\n")
        rhombus.draw()
        
        choice = input("\nХотите продолжить (да/нет)? ").lower()
        if choice != "да":
            break