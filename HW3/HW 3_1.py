"""Задание 1.Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль"""

"""Вариант 1"""
number1 = int(input("Insert number#1"))
number2 = int(input("Insert number#2"))

def division(*numbers):
    try:
        calc = float(number1 / number2)
        return round(calc,3)
    except ZeroDivisionError:
        return "you cant use 0"

print(f'result {division()}')


"""Вариант 2"""
def division(number1, number2):
    try:
        calc = float(number1 / number2)
        return round(calc,3)
    except ZeroDivisionError:
        return "You cant use 0"

print(division (int(input("Insert number#1 ")), int(input("Insert number#2"))))


"""Вариант 3"""
number1 = int(input("Insert number#1"))
number2 = int(input("Insert number#2"))

if number2 != 0:
    def division(number1: object, number2: object) -> object:
        calc = float(number1 / number2)
        return round(calc,3)
    print(division(number1, number2))

else:
    print("you can not use 0")
