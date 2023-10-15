def solution(n):
    result = 0
    for a in range(n+1):
        for b in range(a+1):
            if a >= b and a*b == n:
                result += 1
    return result*2 if (n ** .5) != int(n ** .5) else result*2-1 # 시간초과 뜸