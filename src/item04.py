"""
  4. C 스타일의 문자열을str.format과 쓰기보다는 f-문자열을 통한 인터폴레이션을 사용하라
"""

a = 0b10111011
b = 0xc5f
print('이진수: %d, 십육진수: %d' % (a, b))

# 1. tuple내 데이터값의 순서에 의존한다.
key = 'my_car'
value = 1.234
formatted = '%-10s = %.2f' % (key, value)
print(formatted)

# reordered_tuple = '%-10s = %.2f' % (value, key)
# print(reordered_tuple)
# Traceback (most recent call last):
#   File "/Users/junyeong/Study/Book/effectivepython/item4.py", line 16, in <module>
#     reordered_tuple = '%-10s = %.2f' % (value, key)
#                       ~~~~~~~~~~~~~~~^~~~~~~~~~~~~~
# TypeError: must be real number, not

# 2. 식을 읽기가 어려워질 수 있다.
pantry = [
    ('아보카도', 1.25),
    ('바나나', 2.5),
    ('체리', 15),
]
for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %.2f' % (i, item, count))
for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %.2f' % (i + 1, item.title(), round(count)))

# 3. 같은 값을 여러번 사용하고 싶으면 튜플에서 같은 값을 여러번 반복해야 된다.

# 가래서 내장함수 format과 str.format이 나옴
a = 1234.5678
formatted = format(a, ',.2f')
print(formatted)

key = 'my_var'
value = 1.234

formatted = '{} = {}'.format(key, value)
print(formatted)

formatted = '{:<10} = {:.2f}'.format(key, value)
print(formatted)

formatted = '{1} = {0}'.format(key, value)
print(formatted)

# 인터폴레이션을 통한 형식 문자열
key = 'my_var'
value = 1.234

formatted = f'{key} = {value}'
print(formatted)
formatted = f'{key!r:<10} = {value:.2f}'
print(formatted)