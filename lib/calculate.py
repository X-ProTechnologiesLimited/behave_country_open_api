# file:features/steps/calculate.py
# -----------------------------------------------------------------------------
# DOMAIN-MODEL:
# -----------------------------------------------------------------------------

import math
class Calculate(object):

    def __init__(self):
        self.answer = None
        self.first_integer = None
        self.second_integer = None

    def load_number(self, x, y):
        self.first_integer = x
        self.second_integer = y

    def add_number(self, x, y):
        result = int(x) + int(y)
        return result

    def subtract_number(self, x, y):
        result = int(y) - int(x)
        return result

    def multiply_number(self, x, y):
        result = int(x) * int(y)
        return result

    def divide_number(self, x, y):
        result = int(x) / int(y)
        return int(result)

    def get_result(self, operator, x, y):
        if operator == 'add':
            self.answer = self.add_number(x, y)
        elif operator == 'subtract':
            self.answer = self.subtract_number(x, y)
        elif operator == 'divide':
            self.answer = self.divide_number(x, y)
        elif operator == 'multiply':
            self.answer = self.multiply_number(x, y)

