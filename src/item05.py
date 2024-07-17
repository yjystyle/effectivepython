"""
    5. 복잡한 식을 쓰는 대신 도우미 함수를 작성하라 
"""
from urllib.parse import parse_qs
my_values = parse_qs('빨강=5&빨강=6&파랑=0&초록=',
                     keep_blank_values=True)
print(repr(my_values))

#질의 문자열이 '빨강=5파랑=0&초록='인 경우
red = my_values.get('빨강', [''])[0] or 0
green = my_values.get('초록', [''])[0] or 0
opacity = my_values.get('투명도', [''])[0] or 0

print(f'빨강: {red!r}')
print(f'초록: {green!r}')
print(f'투명도: {opacity!r}')

red_str = my_values.get('빨강',[''])
red = int(red_str[0]) if red_str[0] else 0

# 도우미 함수 작성
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default

green = get_first_int(my_values, '초록')
