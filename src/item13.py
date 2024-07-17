"""
    13. 슬라이싱보다는 나머지를 모두 잡아내는 언패킹을 사용하라
"""

# 예를 들어 중고차 매매상에서 판매하는 자동차들의 출고 이후 몇년 지났는지를 표현하는 리스트
car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)

# 아래처럼 언패킹하면 당연히 에러가 난다.
# oldest, second_oldest = car_ages_descending

# 다음과 같이 하면 좀 지저분하다.
# oldest = car_ages_descending[0]
# second_oldest = car_ages_descending[1]
# others = car_ages_descending[2:]
# print(oldest, second_oldest, others)


oldest, second_oldest, third_oldest, *others = car_ages_descending
print(oldest, second_oldest, third_oldest, others)

oldest, *_, youngest = car_ages_descending
print(oldest, youngest)

# 최댓값만 구하고 싶으면
oldest, *_ = car_ages_descending
print(oldest)


def generate_csv():
    yield ('날짜', '제조사', '모델', '연식', '가격')

# 이런식으로 해도 되지만.
all_csv_rows = list(generate_csv())
header = all_csv_rows[0]
rows = all_csv_rows[1:]

it = generate_csv()
header, *rows = it
print('CSV 헤더', header)
