import math

def solution(n):
    for i in range(2, 12):
        if math.factorial(i) > n:
            return i-1

# 또 다른 풀이
def solution2(n):
    k = 10
    while n < math.factorial(k):
        k -= 1
    return k