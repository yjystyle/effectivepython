"""
    18. __missing__을 사용해 키에 따라 다른 디폴트 값을 생성하는 밭법을 알아두라
"""

# old way
pictures = {}
path = 'profile_1234.png'

# if (handle := pictures.get(path)) is None:
#     try:
#         handle = open(path, 'a+b')
#     except OSError:
#         print(f'경로를 열 수 없습니다: {path}')
#         raise
#     else:
#         pictures[path] = handle

# handle.seek(0)
# image_data = handle.read()

# # setdefault 활용
# try:
#     handle = pictures.setdefault(path, open(path, 'a+b'))
# except OSError:
#     print(f'경로를 열 수 없습니다: {path}')
#     raise
# else:
#     handle.seek(0)
#     image_data = handle.read()


# defaultdict
# 인자를 받을 수 없다.
# Traceback (most recent call last):
#   File "c:\dev\PYTHON\effectivepython\src\item18.py", line 44, in <module>
#     handle = pictures[path]
#              ~~~~~~~~^^^^^^
# TypeError: open_picture() missing 1 required positional argument: 'profile_path'

'''
from collections import defaultdict

def open_picture(profile_path):
    try:
        return open(profile_path, 'a+b')
    except OSError:
        print(f'경로를 열 수 없습니다: {profile_path}')
    raise

pictures = defaultdict(open_picture)
handle = pictures[path]
handle.seek(0)
image_data = handle.read()
'''

# 해법

def open_picture(profile_path):
    try:
        # 'a' -> append : 파일이 존재하지 않으면 새 파일 생성, 파일이 존재하면 파일 끝에 데이터 추가
        # 'b' -> Binary
        # '+' -> Read and Write
        return open(profile_path, 'a+b')
    except OSError:
        print(f'경로를 열 수 없습니다: {profile_path}')
    raise


# dictionary 타입을 상속받은 클래스
class Pictures(dict):
    def __missing__(self, key):
        # value = open_picture(key)
        value = open_picture('profile_123.png')
        self[key] = value
        return value
    
pictures = Pictures()

# path가 pictrues 딕셔너리에 없으면 __missing__ 호출
handle = pictures[path]
handle.seek(0)
image_data = handle.read()

# 있으면 사용, 없으면 클래스 __missing__ 호출하여 경로 읽어들이기
