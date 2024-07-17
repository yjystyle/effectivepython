"""
    12. 스트라이드와 슬라이스를 한 식에 함께 사용하지 말라
    스트라이드 - 리스트[시작:끝:증가값]
    프로그램이 시간과 메모리를 감당하기 어려우면 itertools 내장 모듈의 islice 메서드를 고려하라.
"""

x = ['빨강', '주황', '노랑', '초록', '파랑', '자주']
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)

x = 'mongoose'
y = x[::-1]
print(y)

x = '스시'
y = x[::-1]
print(y)

w = x.encode('utf-8')
print(w)
z = w[::-1]
# print(z)

# print(b'\xec'.decode('utf-8'))
# Traceback (most recent call last):
#   File "/Users/junyeong/Study/Book/effectivepython/item12.py", line 25, in <module>
#     print(b'\xec'.decode('utf-8'))
#           ^^^^^^^^^^^^^^^^^^^^^^^
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xec in position 0: unexpected end of data

x = ['빨강', '주황', '노랑', '초록', '파랑', '자주']
print(x[1:-1])