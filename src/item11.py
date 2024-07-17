"""
    11. 시퀀스를 슬라이싱하는 방법을 익혀라
"""

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('가운데 2개: ', a[3:5])
print('마지막을 제외한 나머지: ', a[1:7])


# 0은 생략하는게 좋다
assert a[:5] == a[0:5]

# 리스트의 끝가지 슬라이싱할 때는 쓸데없이 큰 인덱스를 적지 말라.
assert a[5:] == a[5:len(a)]

print(a[:])
print(a[:5])
print(a[:-1])
print(a[4:])
print(a[-3:])
print(a[2:5])
print(a[2:-1])
print(a[-3:-1])

b = a[3:]
print(b)
a[1] = 99
print(b)

print(a)
b = a
c = a[:]
print('이전 a:',a)
print('이전 b:',b)
a[:] = [101, 102, 103]
assert a is b
print('이후 a:',a)
print('이후 b:',b)
print('이후 c:',c)
