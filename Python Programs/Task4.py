#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    user_input = input("Введите значение: ")
    return user_input

def test_input(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def str_to_int(value):
    return int(value)

def print_int(value):
    print(value)

if __name__ == '__main__':
    input_str = get_input()

    if test_input(input_str):
        int_value = str_to_int(input_str)
        print_int(int_value)
    else:
        print("Введенное значение не является целым числом.")