"""Завдання 1
 Створіть клас «Дріб». Збережіть у класі чисельник
та знаменник. Реалізуйте методи класу для введення і ведення даних.
Також створіть методи класу для
виконання арифметичних операцій (додавання,
віднімання, множення, ділення і т. д.). До вже
реалізованого класу «Дріб» додайте необхідні
перевантажені методи та оператори."""

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator #спільний знаменник
        return Fraction(new_numerator, new_denominator)

fraction1 = Fraction(4, 7)
fraction2 = Fraction(5, 8)
print(fraction1 + fraction2)