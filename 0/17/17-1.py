def solution(num, k):
    num = list(map(int, str(num)))
    return num.index(k)+1 if k in num else -1

# 또 다른 풀이
def solution2(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1