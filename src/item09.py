"""
    for나 while 루프 뒤에 else 블록을 사용하지 말라
"""

for i in range(3):
    print('Loop', i)
else:
    print('Else block!')


def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % 1 == 0 and b % 1 == 0:
            return False
    return True


# assert coprime(4, 9)
assert not coprime(4, 9)

