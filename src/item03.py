"""
  3. bytes와 str의 차이를 알아두라
"""


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

print(repr(to_str(b'foo')))
print(repr(to_str('foo')))
print(repr(to_str(b'\xed\x95\x9c')))  # 한
