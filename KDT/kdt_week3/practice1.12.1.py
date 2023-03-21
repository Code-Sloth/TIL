# 명세서

class Calculator:
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2
    def plus(self):
        return self.number1 + self.number2
    def minus(self):
        return self.number1 - self.number2
    def multiply(self):
        return self.number1 * self.number2
    def division(self):
        return self.number1 // self.number2
    def print(self):
        print(f'number1 = {self.number1}, number2 = {self.number2}')
        print('합 :', self.number1 + self.number2)
        print('빼기 :', self.number1 - self.number2)
        print('곱 :', self.number1 * self.number2)
        print('몫 :', self.number1 // self.number2)

# plus

calculator = Calculator(10, 5)
print(calculator.plus())

calculator.number1 = -2
calculator.number2 = 2
print(calculator.plus())

# minus

calculator = Calculator(10, 5)
print(calculator.minus())

calculator.number1 = -2
calculator.number2 = 2
print(calculator.minus())

# multiply

calculator = Calculator(10, 5)
print(calculator.multiply())

calculator.number1 = -2
calculator.number2 = 2
print(calculator.multiply())

# division

calculator = Calculator(10, 5)
print(calculator.division())

calculator.number1 = -2
calculator.number2 = 2
print(calculator.division())

# print

calculator = Calculator(10, 5)
calculator.print()

calculator.number1 = -2
calculator.number2 = 2
calculator.print()