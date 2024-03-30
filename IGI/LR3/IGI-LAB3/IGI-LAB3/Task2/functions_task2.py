# -*- coding: cp1251 -*-

# Дата разработки : 29.03.2024
# Функция для вычисления колличества чисел больше 23 в массивке

def count_numbers_above_23():
    vector = []
    count = 0
    while True:
        try:
            number = int(input("Введите целое число: "))
            if number == 15:
                print("Ввод прекращен")
                break  # Прекращаем ввод при достижении числа 15
            if number > 23:
                vector.append(number)
                count += 1
        except ValueError:
            print("Ошибка! Введите целое число.")
    return count,vector