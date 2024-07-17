"""
    10. 대입식을 사용해 반복을 피하라
"""

fresh_fruit = {
    '사과': 10,
    '바나나': 8,
    '레몬': 5
}


def make_lemonade(count):
    pass


def out_of_stock():
    pass


def make_cider(count):
    pass


def slice_bananas(count):
    pass


class OutOfBananas(Exception):
    pass


def make_smoothies(count):
    pass

def pick_fruit():
    pass

def make_juice(fruit, count):
    pass

count = fresh_fruit.get('레몬', 0)
if count:
    make_lemonade(count)
else:
    out_of_stock()

# 왈라스 대입식 사용
if count := fresh_fruit.get('레몬', 0):
    make_lemonade(count)
else:
    out_of_stock()

count = fresh_fruit.get('사과', 0)
if count >= 4:
    make_cider(count)
else:
    out_of_stock()

if (count := fresh_fruit.get('사과', 0)) >= 4:
    make_cider(count)
else:
    out_of_stock()


# 바나나주스 > 애플주스 > 레모네이드
count = fresh_fruit.get('바나나', 0)
if count >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
else:
    count = fresh_fruit.get('사과', 0)
    if count >= 4:
        to_enjoy = make_cider(count)
    else:
        count = fresh_fruit.get('레몬', 0)
        if count:
            to_enjoy = make_lemonade(count)
        else:
            to_enjoy = '아무것도 없음'

# 아래와 같이 리팩토링 할 수 있다.
if (count := fresh_fruit.get('바나나', 0)) >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
elif (count:= fresh_fruit.get('사과',0)) >=4:
    to_enjoy = make_cider(count)
elif (count:= fresh_fruit.get('레몬',0)):
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = '아무것도 없음'

# 신선한 과일이 배달돼서 이 과일을 모두 주스로 만든 후 병에 담기로 한 경우
# 아래의 코드는 fresh_fruit = pick_fruit() 호출을 두번하기 때문에 반복적이다.
bottles = []
fresh_fruit = pick_fruit()
while fresh_fruit:
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
    fresh_fruit = pick_fruit()

# 아래와 같이 바꿀 수 있다.
# break 도 굳이 필요 없다.
bottles = []
while fresh_fruit := pick_fruit():
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)

