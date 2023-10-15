# def solution(n):
#     result = 0
#     for a in range(n+1):
#         for b in range(a+1):
#             if a >= b and a*b == n:
#                 result += 1
#     return result*2 if (n ** .5) != int(n ** .5) else result*2-1 # 시간초과 뜸

# 정답
def solution(n):
    result = 0
    for i in range(1, n+1):
        if n % i == 0:
            result += 1
    return result

# 또 다른 풀이
def solution2(n):
    return len([number for number in range(1, n+1) if n % number == 0])