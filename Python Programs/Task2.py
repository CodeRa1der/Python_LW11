#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def circle(radius):
    return math.pi * radius ** 2

def cylinder():
    radius = float(input("Введите радиус цилиндра: "))
    height = float(input("Введите высоту цилиндра: "))
    option = input("Хотите получить площадь боковой поверхности (s) или полную площадь (f)? ")

    if option == "s":
        lateral_area = 2 * math.pi * radius * height
        print(f"Площадь боковой поверхности цилиндра: {lateral_area}")
    elif option == "f":
        lateral_area = 2 * math.pi * radius * height
        total_area = lateral_area + 2 * circle(radius)
        print(f"Полная площадь цилиндра: {total_area}")
    else:
        print("Некорректный вариант. Выберите 'side' или 'full'.")

if __name__ == '__main__':
    cylinder()
