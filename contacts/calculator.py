class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 == 0:
            return '두번째 숫자에 0이 들어갈 수 없습니다.'
        else:
            return self.num1 // self.num2

if __name__ == "__main__":
    calc = Calculator(6, 2)     # num1 = 4, num2 = 6
    sumResult = calc.sum()
    subResult = calc.subtract()
    multiResult = calc.multiplication()
    diviResult = calc.division()
    print(f'덧셈 결과 {sumResult}')
    print(f'뺄셈 결과 {subResult}')
    print(f'곱셈 결과 {multiResult}')
    print(f'나눗셈 결과 {diviResult}')




