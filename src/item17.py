"""
    17. 내부 상태에서 원소가 없는 경우를 처리할 때는 setdefault보다 defaultdict를 사용하라
"""

visits = {
    '미국' : {'뉴욕', '로스엔젤레스'},
    '일본' : {'하코네'}
}

# 아래처럼 만들 수도 있다.
class Visits_A:
    def __init__(self):
        self.data = {}

    def add(self, country, city):
        city_set = self.data.setdefault(country, set())     # 주어진 나라가 data 딕셔너리에 있든 없든 관계없이 호출할 때마다 새로 set 인스턴스를 만들어야 한다. 
        city_set.add(city)
    
visits = Visits_A()
visits.add('러시아', '예카테린부르크')
visits.add('탄자니아', '잔지바르')
print(visits.data)

from collections import defaultdict

class Visits:
    def __init__(self):
        self.data = defaultdict(set)
    
    def add(self, country, city):
        self.data[country].add(city)

visits = Visits()
visits.add('영국', '바스')
visits.add('영국', '런던')
print(visits.data)