def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)
    return answer

# 또 다른 풀이
def solution2(n):
    return [i for i in range(1, n+1) if n%1 == 0]