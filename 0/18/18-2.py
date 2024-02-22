def solution(n):
    return 1 if n ** 0.5 == int(n ** 0.5) else 2

# 또 다른 풀이
def solution2(n):
    return 1 if (n ** 0.5).is_integer() else 2