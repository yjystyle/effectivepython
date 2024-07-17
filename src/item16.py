"""
    16. in을 사용하고 딕셔너리 키가 없을 때 KeyError를 처리하기보다는 get을 사용하라
"""

counters = {
    '폼퍼니켈' : 2,
    '사워도우' : 1
}

key = '밀'

if key in counters:
    count = counters[key]
else:
    count = 0
counters[key] = count + 1


try:
    count = counters[key]
except KeyError:
    count = 0
counters[key] = count + 1


# 위처럼 쓰지말고 아래처럼
count = counters.get(key, 0)
counters[key] = count + 1


votes= {
    '바게트' : ['철수', '순이'],
    '치아바타' : ['하니', '유리'],
}
key = '브리오슈'
who = '단이'

# 위의 경우에도
if (names := votes.get(key)) is None:
    votes[key] = names = []

names.append(who)
print(votes)

names = votes.setdefault(key, [])
names.append(who)


