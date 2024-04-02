def solution(before, after):
    before_list = list(before)
    after_list = list(after)
    return 1 if sorted(before_list) == sorted(after_list) else 0

# 또 다른 풀이
def solution2(before, after):
    return 1 if sorted(before) == sorted(after) else 0 # sorted()는 문자열 사용가능, 반환값은 리스트 형태