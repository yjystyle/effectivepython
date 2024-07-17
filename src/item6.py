"""
    6. 인덱스를 사용하는 대신 대입을 사용해 데이터를 언패킹해라.
    --> 가능한 한 인덱스 사용을 피할 수 있고, 더 명확하고 파이썬다운 코드를 만들 수 있다.
"""


def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                a[i-1], a[i] = a[i], a[i-1]
    return a


a = ['프레즐', '당근', '쑥갓', '베이컨']
result = bubble_sort(a)
print(result)

snacks = [('베이컨', 350), ('도넛', 240), ('머핀', 190)]
for rank, (name, calories) in enumerate(snacks):
    print(f'#{rank}: {name} 은 {calories} 칼로리입니다.')