def solution(n, numlist):
    return [i for i in numlist if i % n == 0]

# 또 다른 풀이
def solution2(n, numlist):
    return list(filter(lambda v: v%n == 0, numlist))