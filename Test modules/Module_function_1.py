import inspect
from math import sqrt

message: str = 'Добро пожаловать в самую лучшую ' \
               'программу для вычисления '\
               'квадратного корня из заданного числа'


def CalculateSquareRoot(Number: int) -> float:
    """ Вычисляет квадратный корень"""
    return sqrt(Number)


def calc(your_number: float) -> float:
    if your_number <= 0:
        return ''

    print(f'Мы вычислили квадратный корень'
          f' из введённого вами числа.'
          f' Это будет: {CalculateSquareRoot(your_number)}')


print(inspect.cleandoc(message))
calc(25.5)
