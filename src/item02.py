

"""
  2. PEP8 스타일의 가이드를 따르라
"""


class StaticMethod:
    # 스태틱메소드: 인스턴스 필요X
    @staticmethod
    def factorial(number):
        if number == 0:
            return 1
        else:
            return number * StaticMethod.factorial(number - 1)


factorial = StaticMethod.factorial(5)
print(factorial)


class ClassMethod:
    # 스태틱메소드: 인스턴스 필요X
    @classmethod
    def factorial(cls, number):
        if number == 0:
            return 1
        else:
            return number * ClassMethod.factorial(number - 1)


factorial = ClassMethod.factorial(5)
print(factorial)
