"""
    7. range보다는 enumerate를 사용하라
"""

favor_list = ['바닐라', '초콜릿', '피칸', '딸기']
it = enumerate(favor_list)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# 1 부터 셀 수 있다.
for i, flavor in enumerate(favor_list, 1):
    print(f'{i}: {flavor}')


