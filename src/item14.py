"""
    14. 복잡한 기준을 사용해 정렬할 때는 key 파라미터를 사용하라
"""


class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'


tools = [
    Tool('수준계', 3.5),
    Tool('해머', 1.25),
    Tool('스크류드라이버', 0.5),
    Tool('끌', 0.25)
]

# tools.sort()
tools.sort(key=lambda x: x.name)
print(tools)
tools.sort(key=lambda x: x.weight)
print(tools)

places = ['home', 'work', 'New York', 'Paris']
places.sort()
print('대소문자 구분: ', places)
places.sort(key=lambda x: x.upper())
print('대소문자 무시: ', places)

power_tools = [
    Tool('드릴', 4),
    Tool('원형 톱', 5),
    Tool('착암기', 40),
    Tool('연마기', 4),
]
power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)

# weight 내림차순, name 오름차순
power_tools.sort(key=lambda x: (-x.weight, x.name))
print(power_tools)