from collections import Counter

def solution(s):
    cnt = Counter(list(s))
    result = [k for k, v in cnt.items() if v == 1]
    return ''.join(sorted(result))

# 또 다른 풀이
def solution2(s):
    return ''.join(sorted([ch for ch in s if s.count(ch) == 1]))