def solution(n):
    if n%7:
        return (int(n/7) + 1)
    else:
        return int(n/7)

# int를 붙이지 않고 //로 바로 몫 구한 후 소수점 버리기

# 또 다른 풀이
def solution(n):
    return n//7 + (1 if n%7 else 0)