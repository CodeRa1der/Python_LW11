#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mult():
    result = 1
    while True:
        num = float(input("Введите число (введите 0 для завершения): "))
        if num == 0:
            break
        result *= num
    return result

if __name__ == '__main__':
    product = mult()
    print(f"Произведение введенных чисел: {product}")
