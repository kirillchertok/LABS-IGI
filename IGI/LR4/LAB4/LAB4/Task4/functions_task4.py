# -*- coding: cp1251 -*-

from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt
import math

class GeometricalFigure(ABC):
    @abstractmethod
    def calculate_area(self):
        """
        Abstract method to calculate the area of the geometric figure.
        """
        pass

    @abstractmethod
    def draw(self):
        """
        Abstract method to draw the geometric figure.
        """
        pass

class Color:
    def __init__(self, color):
        """
        Initializes a Color object with a given color.
        
        :param color: A string representing the color.
        """
        self._color = color
    
    @property
    def color(self):
        """
        Gets the color of the Color object.
        
        :return: The color of the Color object.
        """
        return self._color
    
    @color.setter
    def color(self, value):
        """
        Sets the color of the Color object.
        
        :param value: A string representing the new color.
        """
        self._color = value

class Rhombus(GeometricalFigure):
    def __init__(self, side, angle, color):
        """
        Initializes a Rhombus object with a given side length, angle, and color.
        
        :param side: The length of the side of the rhombus.
        :param angle: The angle of the rhombus in degrees.
        :param color: A string representing the color of the rhombus.
        """
        self.side = side
        self.angle = math.radians(angle)  # Convert degrees to radians
        self.color = str(color)
    
    def calculate_area(self):
        """
        Calculates the area of the rhombus.
        
        :return: The area of the rhombus.
        """
        return self.side * self.side * math.sin(self.angle)

    @classmethod
    def figure_name(cls):
        """
        Returns the name of the geometric figure.
        
        :return: The name of the geometric figure.
        """
        return "Rhombus"

    def draw(self):
        """
        Draws the rhombus with the specified color.
        """
        # Конвертируем угол из градусов в радианы
        obtuse_angle_radians = self.angle
    
        # Находим координаты вершин ромба
        x_a, y_a = 0, 0
        # Вершина B
        x_b, y_b = self.side * np.cos(obtuse_angle_radians), self.side * np.sin(obtuse_angle_radians)
        # Вершина C
        x_c, y_c = x_b + self.side, y_b
        # Вершина D
        x_d, y_d = x_a + self.side, y_a
    
        # Нарисовать ромб
        plt.plot([x_a, x_b, x_c, x_d, x_a], [y_a, y_b, y_c, y_d, y_a])
        plt.fill([x_a, x_b, x_c, x_d, x_a], [y_a, y_b, y_c, y_d, y_a], color=self.color)

        # Добавить заголовок и метки осей
        plt.title(f"Ромб со стороной {self.side} и углом {self.angle} и цвет {self.color}")
        plt.xlabel('X')
        plt.ylabel('Y')

        # Отобразить ромб
        plt.grid(True)
        plt.axis('equal')
        plt.show()
            
        # self.save_results_to_file("OutputTask4.txt")
        
    def __str__(self):
        """
        Returns a string representation of the Rhombus object.
        
        :return: A string representation of the Rhombus object.
        """
        return "{} {} colored with side length {} and angle {} degrees".format(
            self.figure_name(), self.color, self.side, math.degrees(self.angle)
        )
    def save_results_to_file(self, filename):
        """
        Saves the analysis results to a file.

        :param filename: The name of the file to save results.
        :param results: The analysis results.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            for i in range(int(self.side)):
                file.write(" " * (int(self.side) - i) + "*" * (2 * i + 1) + "\n")
            for i in range(int(self.side)-2, -1, -1):
                file.write(" " * (int(self.side) - i) + "*" * (2 * i + 1) + "\n")
    
