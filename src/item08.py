"""
    8. 여러 이터레이터에 대해 나란히 루프를 수행하려면 zip을 사용하라
"""
names = ['Cecilia', '남궁민수', '234234']
counts = [len(n) for n in names]
print(counts)

longest_name = None
max_count = 0

for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count
print(longest_name)


# 이런 경우 zip이라는 내장 함수 사용
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

# list 길이가 다르면 짧은 리스트를 기준으로 동작
names.append('Rosalind')
for name, count in zip(names, counts):
    print(name)

# 위의 경우에는 itertools 내장모듈의 zip_longest 대신 사용
import itertools

for name, count in itertools.zip_longest(names, counts):
    print(f'{name}: {count}')

