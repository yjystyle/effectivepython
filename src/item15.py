"""
    15. 딕셔너리 삽입 순서에 의존할 때는 조시하라
"""

from typing import Dict, MutableMapping
from collections.abc import MutableMapping
votes = {
    'otter': 1281,
    'polar bear': 587,
    'fox': 863
}


def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i,  name in enumerate(names, 1):
        ranks[name] = i


def get_winner(ranks):
    return next(iter(ranks))


ranks = {}
populate_ranks(votes, ranks)
print(ranks)
winner = get_winner(ranks)
print(winner)

# 프로그램의 요구사항이 변경되어 ui 요소에서 겨로가를 보여줄 때 등수가 아니라 알파벳으로 표시


class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)


sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)            # {'otter': 1, 'fox': 2, 'polar bear': 3}
winner = get_winner(sorted_ranks)
print(winner)                       # fox


def populate_ranks(votes: Dict[str, int], ranks: Dict[str, int]) -> None:
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))


class SortedDict(MutableMapping[str, int]):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)


sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)